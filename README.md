## NCO Semantic Knowledge Platform

---

<img width="1920" height="1080" alt="Screenshot 2025-09-07 183857" src="https://github.com/user-attachments/assets/e4a7fef8-b0a6-4a26-9bd1-ed51fca27d29" />



A platform for building and querying a semantic knowledge graph of Non-Commissioned Officer (NCO) data from unstructured text sources. This project uses Natural Language Processing (NLP) and ontology-driven data modeling to transform documents like performance reports, doctrinal manuals, and personnel records into actionable, interconnected knowledge.

Table of Contents
About The Project

Core Features

System Architecture

The NCO Ontology

Technology Stack

Getting Started

Prerequisites

Installation

Usage

Data Ingestion

Querying the Knowledge Graph

API Endpoints

Contributing

License

Contact

Acknowledgments

About The Project
The careers, skills, and experiences of Non-Commissioned Officers (NCOs) are often documented in vast amounts of unstructured text. This makes it difficult to perform large-scale analysis, identify skill gaps, find suitable candidates for a specific role, or understand career progression trends.

This project tackles that challenge by:

Defining a formal ontology to represent NCO-related concepts (e.g., ranks, skills, units, duties, performance metrics).

Using NLP pipelines to extract these concepts and their relationships from raw text documents.

Populating a knowledge graph (an RDF Triplestore) with the extracted data.

Providing an API to query this graph, allowing for complex, semantic-based questions that are impossible with traditional keyword searches.

For example, instead of searching for "leadership," you can ask:

"Find all Sergeant First Class NCOs who have demonstrated 'strategic planning' skills and have served in an infantry unit for more than 3 years."

Core Features
Ontology-Driven Data Model: Uses a formal OWL/RDF ontology to ensure data consistency and enable semantic reasoning.

NLP Extraction Pipeline: Leverages state-of-the-art NLP models (e.g., spaCy) for Named Entity Recognition (NER) and Relation Extraction tailored for the military domain.

Knowledge Graph Backend: Stores interconnected data in a robust RDF Triplestore (e.g., Apache Jena).

SPARQL Query Endpoint: A standardized endpoint for posing complex queries against the knowledge graph.

RESTful API: A simple API layer for easy integration with other applications and front-end interfaces.

Dockerized Environment: Ensures easy, reproducible setup for development and deployment.

System Architecture
The system follows a standard data processing pipeline:

[Unstructured Data] -> [Ingestion Service] -> [NLP Pipeline (NER, Relation Extraction)] -> [RDF Triplestore] <-> [SPARQL Endpoint] <-> [API Server] <-> [Client Application]
(e.g., PDFs, DOCX)                        (spaCy, Transformers)                    (Apache Jena)                        (FastAPI)
The NCO Ontology
The heart of the project is the NCO ontology (nco.owl), which formally defines the classes, properties, and relationships.

Key Classes (rdf:type):

nco:NCO: An individual Non-Commissioned Officer.

nco:Unit: A military unit or organization.

nco:Rank: An official rank (e.g., Sergeant, Staff Sergeant).

nco:Skill: A specific skill or competency (e.g., Marksmanship, Logistics).

nco:PerformanceReport: A document evaluating an NCO's performance.

nco:DutyPosition: A specific role or job an NCO holds.

Key Properties (owl:ObjectProperty):

nco:hasRank: Links an nco:NCO to their nco:Rank.

nco:isAssignedTo: Links an nco:NCO to a nco:Unit.

nco:holdsPosition: Links an nco:NCO to a nco:DutyPosition.

nco:possessesSkill: Links an nco:NCO to an nco:Skill.

nco:isEvaluatedBy: Links an nco:NCO to an nco:PerformanceReport.

Technology Stack
Backend: Python 3.9+, FastAPI

NLP: spaCy, Hugging Face Transformers

Ontology/RDF: RDFLib, OWLRL

Database (Triplestore): Apache Jena Fuseki

Containerization: Docker, Docker Compose

Ontology Editor (Recommended): Protégé

Getting Started
Follow these steps to get a local copy up and running.

Prerequisites
Docker and Docker Compose: Install Docker

Git

Python 3.9+ (for local development outside Docker)

Installation
Clone the repository:

Bash

git clone https://github.com/Mohammedjaasir/nco-semantic-Search.git
cd nco-semantic-project
Configure Environment Variables:
Create a .env file from the example template.

Bash

cp .env.example .env
Modify the .env file as needed (e.g., to set ports or database paths).

Build and Run with Docker Compose:
This is the recommended method. It will build the containers for the API, the NLP processor, and the Apache Jena triplestore.

Bash

docker-compose up --build
The services should now be running:

API Server: http://localhost:8000

API Docs (Swagger UI): http://localhost:8000/docs

Apache Jena Fuseki UI: http://localhost:3030

Usage
Data Ingestion
Place your unstructured documents (e.g., .txt, .pdf) into the /data/raw directory. Then, trigger the ingestion process via the API.

Bash

curl -X POST "http://localhost:8000/v1/ingest" -H "accept: application/json"
This will run the NLP pipeline on the documents in the specified folder and populate the triplestore.

Querying the Knowledge Graph
You can query the data directly using SPARQL through the Apache Jena UI or via the API.

Example SPARQL Query: Find all NCOs who possess the "Leadership" skill.

Code snippet

PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX nco: <http://example.org/ontology/nco#>

SELECT ?nco_name ?rank_label
WHERE {
  ?nco a nco:NCO ;
       nco:hasName ?nco_name ;
       nco:hasRank ?rank ;
       nco:possessesSkill ?skill .

  ?skill nco:skillName "Leadership" .
  ?rank rdfs:label ?rank_label .
}
API Endpoints
The API provides several endpoints for interacting with the knowledge graph. Visit http://localhost:8000/docs for a full interactive specification.

POST /v1/ingest: Start the data ingestion and processing pipeline.

POST /v1/query: Submit a SPARQL query in the request body and receive JSON results.

GET /v1/nco/{nco_id}: Retrieve all information about a specific NCO.

Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Please refer to CONTRIBUTING.md for our contribution guidelines and development process.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

License
Distributed under the MIT License. See LICENSE for more information.
