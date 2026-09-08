# AI Customer Intelligence & Support Analytics Assistant

An AI-powered customer analytics assistant that allows users to upload a SQLite database and ask questions about customer data using natural language.

The system combines SQL-based retrieval, semantic vector search, Reciprocal Rank Fusion (RRF), Cross-Encoder reranking, and an LLM to provide relevant and data-grounded answers.

## 🚀 Features

- Upload a SQLite database through a Streamlit interface
- Automatically index customer data for semantic search
- Ask questions using natural language
- Automatically classify questions into:
  - SQL
  - Vector
  - Hybrid
- Generate and execute SQL queries for analytical questions
- Perform semantic retrieval using vector embeddings
- Combine retrieval results using Reciprocal Rank Fusion (RRF)
- Rerank retrieved results using a Cross-Encoder
- Generate natural-language answers using an LLM
- Use SQLite as the authoritative source for structured data

## 🧠 System Architecture

```text
                 User
                   │
                   ▼
          Upload SQLite Database
                   │
                   ▼
             Streamlit UI
                   │
                   ▼
          Natural Language Query
                   │
                   ▼
          Question Classification
             /       |       \
            /        |        \
          SQL      Vector    Hybrid
           │          │         │
           ▼          ▼         ▼
       SQL Query   Vector     SQL + Vector
       Generation  Search      Retrieval
           │          │         │
           └──────────┼─────────┘
                      ▼
               RRF Fusion
                      │
                      ▼
           Cross-Encoder Reranking
                      │
                      ▼
              Final LLM Answer
```

## 🛠️ Technologies Used

- **Python** – Core programming language
- **SQLite** – Structured customer database
- **SQLAlchemy** – Database connection and SQL execution
- **LangChain** – LLM and retrieval orchestration
- **Ollama** – Local LLM and embedding models
- **Llama 3.2** – Natural language understanding and answer generation
- **Nomic Embed Text** – Text embeddings for semantic search
- **ChromaDB** – Vector database for storing embeddings
- **Sentence Transformers** – Cross-Encoder reranking
- **Streamlit** – Web application interface
- **uv** – Python dependency and project management

## 🔍 How It Works

1. **Upload Database**  
   The user uploads a SQLite database through the Streamlit interface.

2. **Database Indexing**  
   Customer records are read from SQLite and converted into documents for semantic indexing.

3. **Question Classification**  
   The system classifies the question as SQL, Vector, or Hybrid.

4. **SQL Retrieval**  
   Analytical questions are converted into SQL queries and executed against the database.

5. **Vector Retrieval**  
   Semantic questions are processed using embedding-based similarity search.

6. **Fusion and Reranking**  
   Retrieved candidates are combined and ranked using Reciprocal Rank Fusion and a Cross-Encoder.

7. **Final Answer**  
   The LLM generates a natural-language answer using the retrieved information.

   ## 💬 Example Questions

### SQL / Analytical Questions

- How many customers are there?
- What is the total order value?

### Vector / Semantic Questions

- What did customers complain about?
- What problems did customers experience with their products?

### Hybrid Questions

- Which Bangalore customers had delivery issues?

## ⚙️ Installation

Clone the repository:

```bash
git clone <your-github-repository-url>
cd sqlite_proj
uv sync
ollama pull llama3.2
ollama pull nomic-embed-text
```
## ▶️ Running the Application

Start the Streamlit application:

```bash
uv run streamlit run app.py

```
## 📁 Project Structure

```text
sqlite_proj/
│
├── app.py
├── sqlrag.py
├── company.db
├── pyproject.toml
├── uv.lock
├── chroma_sql_rag/
└── README.md
```
## Screenshots


