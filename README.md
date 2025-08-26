# 🤖 Medical Retrieval-Augmented Generation (RAG) Chatbot

A robust, production-ready AI chatbot that delivers accurate, context-aware medical assistance by combining trusted medical document retrieval with advanced language generation.

---

## 📚 Overview

This project implements a modular, end-to-end pipeline featuring:

- Medical PDF ingestion, validation & chunking
- Specialized medical text embeddings (MedEmbed-base-v0.1)
- Vector store creation & semantic search with FAISS
- Conversational LLM integration using Groq Chat API
- Custom prompt engineering ensuring safe, professional responses
- Interactive Flask web UI for seamless user interaction
- Logging, error handling, and session-persistent chat history
- Docker-based deployment & Jenkins-powered CI/CD pipeline for automation

---

## ⚙️ Project Structure
```
app/
│
├── components/ # Core modules: loaders, embeddings, vectorstore, LLM integration
├── common/ # Logger, exception handling utilities
├── config/ # Configuration and environment variables
├── templates/ # Flask HTML templates
├── data/ # Medical PDF documents and datasets
├── logs/ # Application logging files
├── Dockerfile # Container build script
├── Jenkinsfile # CI/CD pipeline configuration
├── requirements.txt # Python dependencies
└── app.py # Flask web application entry point
```
---

## 🏗️ Features

- **Multi-step Document Processing:** From PDF loading to chunking for effective retrieval
- **Medical Embedding Model:** HuggingFace’s MedEmbed-base specialized for healthcare texts
- **Efficient Retrieval:** FAISS vector store for semantic similarity based document search
- **Groq Conversational Model:** Gateway to powerful, safe, and accurate medical answer generation
- **Custom Question-Answering Chain:** Fine-tuned prompt templates to ensure reliable medical advice
- **User-Friendly Web UI:** Session-based chat interface built with Flask and styled frontend
- **Robust Deployment Pipeline:** Containerized with Docker and automated via Jenkins CI/CD

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Groq API key and model name (set in `.env`)
- Optional HuggingFace API token for embeddings
- Docker & Jenkins (for deployment and CI/CD)

### Installation
```
git clone https://github.com/RaghuVamsi5546/Medical-RAG-Chatbot
pip install -r requirements.txt
```

### Configuration

Set the following environment variables or update the config files accordingly:

- `GROQ_API_KEY`
- `GROQ_MODEL_NAME`
- `HF_TOKEN`
- Paths: `DATA_PATH`, `DB_FAISS_PATH`, etc.

### Running the App
```
python app/application.py
```

Open browser at: [http://localhost:5000](http://localhost:5000)

---

## 🔧 Usage

- Place medical PDF documents inside the `data` directory.
- Run the pipeline to create the vector store.
- Use the web interface to ask medical questions.
- Clear session chat history with the provided UI button.

---

## 🤝 Contributing

Contributions are welcome!  
Open issues or pull requests for feature requests, bug fixes, or improvements.

---

## 📄 License

[MIT License](LICENSE) © 2025 Raghu Vamsi

---

## 📫 Contact

For help or collaboration, reach out via GitHub issues or email:  
<raghuvamsibolem@gmail.com>

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com)  
- [Groq AI](https://groq.com)  
- [HuggingFace](https://huggingface.co)  
- [FAISS](https://github.com/facebookresearch/faiss)  
- [Flask](https://flask.palletsprojects.com)
