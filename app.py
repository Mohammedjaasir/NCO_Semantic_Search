import streamlit as st
import pandas as pd
from utils.embeddings import build_faiss_index, semantic_search

# Load your dataset
df = pd.read_csv(r"E:\Downloads\nco-semantic-search\data\cleaned_occupations.csv")

st.set_page_config(page_title="NCO Semantic Search", layout="wide")

st.title("🔍 NCO Semantic search ")
st.write("Search occupations from **NCO 2015** using **local embeddings + FAISS**.")

# Buildic Searc FAISS index once
if "index" not in st.session_state:
    with st.spinner("Building FAISS index with local embeddings... (This might take a moment)"):
        index, texts = build_faiss_index(df, text_column="Name")
        st.session_state.index = index
        st.session_state.texts = texts

# User input
query = st.text_input("Enter a job/occupation:", placeholder="e.g., app-based cab driver")

if query:
    st.subheader("🔎 Search Results")
    # The 'model' parameter is no longer needed
    results = semantic_search(query, st.session_state.index, st.session_state.texts, top_k=5)

    for res, dist in results:
        row = df[df["Name"] == res].iloc[0]
        st.markdown(f"""
        **Code:** {row['Code']}
        **Title:** {row['Name']}
        """)
        if "Description" in df.columns:
            st.markdown(f"**Description:** {row['Description']}")
        # Clarify that the score is distance (lower is better)
        st.write(f"*(Distance Score: {dist:.4f})*")
        st.write("---")