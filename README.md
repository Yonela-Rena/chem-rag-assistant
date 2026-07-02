# Chemistry RAG Assistant

An AI-powered Chemistry Question Answering system built using Retrieval-Augmented Generation (RAG), FastAPI, FAISS, Hugging Face Embeddings, and Google Gemini.

The application retrieves relevant information from chemistry notes using semantic search and generates accurate, context-aware answers with Google's Gemini Large Language Model.

---

## Project Overview

This project demonstrates how Retrieval-Augmented Generation (RAG) can be applied to chemistry education.

The application:

- Extracts text from chemistry PDF notes
- Splits the document into semantic chunks
- Converts the chunks into vector embeddings using Hugging Face
- Stores the embeddings in a FAISS vector database
- Retrieves the most relevant context for a user's question
- Generates a natural language answer using Google Gemini
- Exposes the functionality through a FastAPI REST API with interactive Swagger documentation

---

## Features

- Extracts text from chemistry PDF notes
- Splits documents into semantic chunks
- Generates vector embeddings using Hugging Face
- Stores embeddings in a FAISS vector database
- Performs semantic similarity search
- Generates context-aware answers using Google Gemini
- REST API built with FastAPI
- Interactive Swagger API documentation

---

## Technologies Used

- Python 3
- FastAPI
- LangChain
- Hugging Face Embeddings
- FAISS Vector Database
- Google Gemini API
- PyPDF
- Uvicorn

---

## System Architecture

```text
Chemistry PDF
      │
      ▼
 PyPDFLoader
      │
      ▼
Text Splitter
      │
      ▼
Embedding Model
(sentence-transformers/all-MiniLM-L6-v2)
      │
      ▼
 FAISS Vector Store
      │
      ▼
Similarity Search
      │
      ▼
Google Gemini
      │
      ▼
Generated Answer
```

---

## Project Structure

```text
chem-rag-assistant/
│
├── app/
│   ├── ingest.py
│   ├── llm.py
│   ├── main.py
│   ├── rag.py
│   ├── search.py
│   └── test_rag.py
│
├── data/
│   └── chemistry_notes.pdf
│
├── vectorstore/
│   ├── index.faiss
│   └── index.pkl
│
├── screenshots/
│   ├── swagger.png
│   └── response.png
│
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/Yonela-Rena/chem-rag-assistant.git
```

Navigate to the project folder.

```bash
cd chem-rag-assistant
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate the virtual environment (Windows).

```bash
venv\Scripts\activate
```

Install the required dependencies.

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the project root.

```env
GOOGLE_API_KEY=your_google_gemini_api_key
```

You can obtain a free API key from Google AI Studio.

---

## Prepare Your Chemistry Notes

Place your chemistry PDF inside the `data/` folder.

Example:

```text
data/
└── chemistry_notes.pdf
```

Then build the vector database.

```bash
python app/ingest.py
```

The ingestion script:

- Loads the PDF
- Splits it into chunks
- Generates embeddings
- Creates the FAISS vector database

---

## Running the API

Start the FastAPI server.

```bash
uvicorn app.main:app --reload
```

Open Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## API Endpoints

### GET /

Returns a welcome message.

---

### POST /chat

Request

```json
{
  "question": "What are alpha carbons?"
}
```

Response

```json
{
  "question": "What are alpha carbons?",
  "answer": "Alpha (α) carbons are the carbon atoms located directly next to a carbonyl group...",
  "status": "success"
}
```

---

## Example Workflow

1. Place a chemistry PDF inside the `data/` folder.
2. Run the ingestion script.
3. Start the FastAPI server.
4. Open Swagger documentation.
5. Submit chemistry questions.
6. Receive AI-generated answers grounded in your document.

---

## Screenshots

### Swagger Documentation

![Swagger API](screenshots/swagger.png)

### Example Response

![Example response](screenshots/response.png)

---

## Skills Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Databases (FAISS)
- Large Language Model Integration
- Prompt Engineering
- REST API Development
- FastAPI
- Document Processing
- Embedding Models
- Python

---

## Future Enhancements

- Support multiple chemistry textbooks
- Upload PDFs through the API
- Return citations and source page numbers
- Conversation memory
- Docker containerization
- Streamlit or React frontend
- Cloud deployment
- OCR support for scanned chemistry notes

---

## Author

**Yonela Mhloluvele**

Final-year BSc Chemistry and Computer Science student with interests in Artificial Intelligence, Machine Learning, Retrieval-Augmented Generation (RAG), and Scientific Software Development.

GitHub:
https://github.com/Yonela-Rena