# RAG with Python Cookbook

Welcome 👋  

This repository contains all code examples from my O’Reilly book **_RAG with Python Cookbook_**.

The book is structured as a collection of modular, hands-on recipes that tackle specific parts of a Retrieval-Augmented Generation system — from data loading and embeddings to agentic workflows, Graph RAG, evaluation, and deployment.

Each recipe focuses on one well-defined problem and shows you how to solve it in practice. You can use them independently or combine them into larger systems.

<a href="https://learning.oreilly.com/library/view/rag-with-python/9798341600553/">
  <img src="https://raw.githubusercontent.com/polzerdo55862/RAG-with-Python-Cookbook/main/rag_cookbook.png" width="350" />
</a>

If you build LLM-powered applications in Python and want concrete, reusable patterns instead of abstract theory, this repository is for you.

---

## 🎯 Who This Repository Is For

This codebase is ideal if you:

- Build LLM applications in Python  
- Want practical, reusable RAG components  
- Care about architecture and system design  
- Explore Agentic RAG or Graph RAG  
- Prefer working examples over theoretical discussions  

---

## 🧠 What Makes This Different

- Modular, standalone recipes  
- Clear focus on one problem at a time  
- Covers classical RAG, Agentic RAG, and Graph RAG  
- Emphasizes architectural thinking without locking you into a single framework  

Rather than presenting one monolithic reference architecture, the book equips you with production-relevant building blocks that you can adapt to your own environment.

---

## 📚 What's Inside

| Chapter | Title                                         | Colab Notebook / Source Link                                                                                                                                                                                                                                     |
| ------: | --------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|       1 | RAG Setup                                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch01_RAG_intro/rag_basics.ipynb)                                                          |
|       2 | Generation and Prompt Engineering             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch02_generation/generation.ipynb)                                                         |
|       3 | Loading Data                                  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch03_loading_data/loading_data_to_RAG.ipynb)                                              |
|       4 | Data Preparation                              | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch04_data_preparation_chunking_data/chunking_data.ipynb)                                  |
|       5 | Embeddings                                    | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch05_text_embedding/text_embeddings.ipynb)                                                |
|       6 | Similarity Search                             | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch06_similarity_search_vector_databases/vector_databases.ipynb)                           |
|       7 | Retrieval                                     | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch07_retrieval/retrieval_techniques.ipynb)                                                |
|   **8** | **Agentic RAG**                               |                                                                                                                                                                                                                                                                  |
|     8.4 | ↳ Building an Agentic System Using Function Calling | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch08_agentic_rag/8.4_building_agentic_system_function_calling/building_agents_without_framework.ipynb) |
|     8.5 | ↳ Accelerating Agents Using AsyncIO                 | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch08_agentic_rag/8.5_accelerating_agents_asyncio/book_snippet_asynchio.py)                                      |
|     8.6 | ↳ Building a Sales Negotiation Agent with OpenAI's Agents SDK | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch08_agentic_rag/8.6_sales_negotiation_agent_openai_sdk/building_agents_with_openai_sdk.ipynb)                     |
|     8.7 | ↳ Enriching Your Agent's Capabilities with MCP Tools | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch08_agentic_rag/8.7_mcp_tools/01_connect_to_playwright.py)                                                   |
|     8.8 | ↳ Building an Agentic System Using LangGraph       | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch08_agentic_rag/8.8_agentic_system_langgraph/building_agents_using_langgraph.ipynb)               |
|   **9** | **Graph RAG**                                 |                                                                                                                                                                                                                                                                  |
|     9.1 | ↳ Creating Your First Neo4j Knowledge Graph  | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch09_graph_rag/9.1_basic_sla_graph.ipynb)                                            |
|     9.2 | ↳ Extending the Knowledge Graph with Structured Data | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch09_graph_rag/9.2_enrich_company_data.ipynb)                                        |
|     9.3 | ↳ Building Your First Cypher Query            | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch09_graph_rag/9.3_cypher_queries.ipynb)                                             |
|     9.4 | ↳ Enabling Semantic Search on a Neo4j Knowledge Graph | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch09_graph_rag/9.4_embeddings_vector_search.ipynb)                                   |
|     9.5 | ↳ Optimize the Knowledge Graph for RAG Systems | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch09_graph_rag/9.5_useful_extensions.ipynb)                                          |
|      10 | RAG Evaluation                                | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch10_rag_evaluation/rag_evaluation_techniques.ipynb)                                      |
|  **11** | **RAG Chatbot (Streamlit)**                   |                                                                                                                                                                                                                                                                  |
|    11.1 | ↳ Building Your First Streamlit App          | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch11_rag_chatbot_streamlit/11.1_and_11.2_streamlit_chatbot_apps/03_simple_rag_app_2.py)                              |
|    11.2 | ↳ Building a Chatbot App Using Streamlit     | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch11_rag_chatbot_streamlit/11.1_and_11.2_streamlit_chatbot_apps/04_simple_rag_app_3.py)                              |
|    11.3 | ↳ Adding PDF Analyzer Functionality to Your Chatbot | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch11_rag_chatbot_streamlit/11.3_pdf_analyzer_functionality/entity_extraction_web_app.py)                  |
|    11.4 | ↳ Connect Your RAG App to a SQL Database     | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch11_rag_chatbot_streamlit/11.4_sql_database_connection/vanna_chat.py)                                              |
|    11.5 | ↳ Deploying Your Streamlit App Using Docker and AWS | [![View on GitHub](https://img.shields.io/badge/View%20on-GitHub-181717?logo=github)](https://github.com/polzerdo55862/RAG-with-Python-Cookbook/blob/main/ch11_rag_chatbot_streamlit/11.5_deploy_docker_aws/README.md)                                              |

> **💡 Tip:** Most notebooks can be run directly in Google Colab (no local setup required!). For local execution, each chapter folder contains its own `requirements.txt` file with the specific dependencies needed for that chapter.

---

## 🚀 What You'll Learn

The book walks you through the entire journey of building RAG systems:

- **Chapters 1-2**: Set up your environment, work with prompts, and choose the right foundation models
- **Chapters 3-4**: Load data from documents, databases, images, audio, and video, then prep it through cleaning and chunking
- **Chapters 5-6**: Understand embeddings, choose the right models, and pick vector databases that fit your needs
- **Chapter 7**: Level up with advanced retrieval techniques like metadata filtering, reranking, and query decomposition
- **Chapters 8-9**: Build intelligent agentic workflows and use knowledge graphs to preserve relationships
- **Chapters 10-11**: Evaluate your RAG systems properly and deploy production-ready apps with Streamlit, Docker, and AWS

Each chapter includes practical recipes with working code that you can adapt for your own projects. Just explore the folders in this repository to dive into the notebooks and examples!

---

## 🚀 Getting Started

### Prerequisites

Before running the examples, make sure you have:

- Python 3.9+  
- An OpenAI API key  
- Optional API keys depending on the chapter  
  - Anthropic for Claude models  
  - Google for Gemini models  
  - Neo4j credentials for Graph RAG  


## 🚀 Getting Started

### Prerequisites

Before running the examples, make sure you have:

-   Python 3.9+\
-   An OpenAI API key\
-   Optional API keys depending on the chapter
    -   Anthropic for Claude models\
    -   Google for Gemini models\
    -   Neo4j credentials for Graph RAG

------------------------------------------------------------------------

### Option 1: Run in Google Colab

Most notebooks can be executed directly in Colab. No local setup
required --- just click the Colab link in the table above.

------------------------------------------------------------------------

### Option 2: Run Locally

Clone the repository:

``` bash
git clone https://github.com/polzerdo55862/RAG-with-Python-Cookbook.git
cd RAG-with-Python-Cookbook
```

Create a virtual environment:

``` bash
python -m venv .venv
source .venv/bin/activate   # macOS / Linux
.venv\Scripts\activate      # Windows
```

Install dependencies for the chapter you want to explore:

``` bash
pip install -r ch02_generation/requirements_ch02_generation.txt
```

Create a `.env` file in the relevant chapter directory:

``` bash
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
```

------------------------------------------------------------------------

## 📁 Datasets

The `datasets/` folder contains sample data used across the book:

-   PDFs, Word, and Markdown files\
-   CSV files for structured data examples\
-   Images, audio, and video files\
-   Example datasets for Agentic RAG and Graph RAG

------------------------------------------------------------------------

## 🤝 Contributions

Contributions are welcome.

-   Open an issue to report bugs\
-   Submit a pull request for improvements\
-   Share how you are using the recipes

Feedback helps improve the material for the entire RAG community.

------------------------------------------------------------------------

## 📄 License

This repository contains code examples from the O'Reilly book *RAG with
Python Cookbook*. The code is provided for educational purposes to
accompany the book. Please refer to O'Reilly's terms for commercial use.

------------------------------------------------------------------------

Happy building 🚀
