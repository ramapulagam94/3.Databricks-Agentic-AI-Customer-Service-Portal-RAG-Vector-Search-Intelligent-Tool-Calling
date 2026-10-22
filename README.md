### Project Overview

Designed and deployed an **Agentic AI-powered Customer Service Portal** on Azure Databricks, integrating Retrieval-Augmented Generation (RAG), Large Language Models (LLMs), and intelligent tool calling to provide context-aware responses to customer queries.

The solution uses both structured data stored in CSV files and unstructured information from approximately **500 PDF documents**. The PDF documents were processed to generate vector embeddings, which were stored and indexed using Databricks Vector Search to enable semantic retrieval of relevant information in response to user questions.

When a user submits a question through the deployed Databricks App, the AI agent uses the `gpt-oss-120b` model service to understand the query, retrieve relevant information through Vector Search, and invoke Unity Catalog Functions when structured data is required. These functions provide access to customer service history and return policy details. The agent combines the retrieved document context and tool results to generate a relevant response for the user.

The solution is deployed as a Databricks App with a chat-based interface, enabling users to interact with the AI-powered customer service agent.

### Technology Stack & Environment Specifications
<img width="650" alt="image" src="https://github.com/user-attachments/assets/cfd48d2b-3805-4126-aaac-6c756da7aba7" />



### Architecture diagram
<img width="847" height="362" alt="image" src="https://github.com/user-attachments/assets/acd36fef-d606-4bed-8f19-bca82e96440b" />

### Key Features

- **RAG Architecture:** Grounds LLM responses using relevant information retrieved from PDF documentation.
- **Structured Data Integration:** Uses CSV-based data through Unity Catalog Functions to support customer service queries.
- **Unstructured Document Processing:** Works with approximately 500 PDF documents to generate vector embeddings for semantic retrieval.
- **Databricks Vector Search:** Retrieves relevant document content based on the semantic similarity between user questions and indexed embeddings.
- **Agentic AI and Tool Calling:** Orchestrates the LLM, Vector Search, and Unity Catalog Functions based on the user's query.
- **Unity Catalog Functions:** Retrieves customer service history and return policy details.
- **LLM Integration:** Uses the `gpt-oss-120b` model service to understand queries and generate context-aware responses.
- **Databricks App Deployment:** Provides a deployed, chat-based interface for end users.
- **Governance and Access Control:** Uses configured app identity and permissions to access the agent and its supporting resources.

### Customer service portal flow
<img width="1672" height="941" alt="3" src="https://github.com/user-attachments/assets/09e8f8e5-f421-4cc4-ae97-09ef594b1649" />


### Output - Chatbot is responding

<img width="800" alt="image" src="https://github.com/user-attachments/assets/d92af992-c50e-4e1e-afa2-1e1df81dd7c8" />


<img width="800" alt="image" src="https://github.com/user-attachments/assets/3592f527-56e1-42aa-810d-8534f42cc467" />


### Validation & Monitoring Strategy.

<img width="700" alt="image" src="https://github.com/user-attachments/assets/260ce93e-7556-4549-a5b5-caa4287bdfc9" />

<img width="700" alt="image" src="https://github.com/user-attachments/assets/8a5b313e-36b5-4f15-bad4-88ce5c1e497a" />






