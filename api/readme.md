# LangChain API Server with FastAPI, LangServe & Gemini

A simple AI application that exposes **LangChain chains as APIs** using **FastAPI and LangServe**, with a **Streamlit client** for interacting with the APIs.

The project currently provides two AI endpoints:

- 📝 Essay Generator
- ✍️ Poem Generator

Both use **Google Gemini** as the LLM.

---

## 🏗️ Architecture

```text
                 Streamlit Client
                       │
                       │ HTTP POST
                       ▼
              FastAPI + Uvicorn
                 localhost:8000
                       │
                    LangServe
                       │
              ┌────────┴────────┐
              │                 │
          /essay/invoke     /poem/invoke
              │                 │
              ▼                 ▼
           Prompt 1           Prompt 2
              │                 │
              └────────┬────────┘
                       ▼
                  Gemini Model
                       │
                       ▼
                Generated Output
```

---

## 🛠️ Tech Stack

- **Python**
- **LangChain**
- **LangServe**
- **FastAPI**
- **Uvicorn**
- **Google Gemini**
- **Streamlit**
- **Requests**
- **python-dotenv**

---

## 📁 Project Structure

```text
api/
│
├── server.py       # FastAPI + LangServe server
├── client.py       # Streamlit frontend
├── .env            # API key
└── README.md
```

---

## 📦 Installation

Create and activate a virtual environment:

```bash
python -m venv venv
```

Windows:

```powershell
venv\Scripts\activate
```

Install dependencies:

```bash
pip install fastapi uvicorn langserve sse-starlette streamlit requests python-dotenv langchain-core langchain-google-genai
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GOOGLE_API_KEY=your_gemini_api_key
```

Keep your API key private and **never commit `.env` to GitHub**.

Add this to `.gitignore`:

```text
.env
venv/
__pycache__/
```

---

# 🚀 Running the Project

The project has two parts:

1. FastAPI/LangServe server
2. Streamlit client

### 1. Start the FastAPI server

Open Terminal 1:

```powershell
python server.py
```

The server will run on:

```text
http://localhost:8000
```

### 2. Start Streamlit

Open Terminal 2:

```powershell
python -m streamlit run client.py
```

Streamlit will normally run on:

```text
http://localhost:8501
```

Open the URL in your browser.

---

# 🔌 API Endpoints

LangServe uses:

```python
add_routes(app, chain, path="/essay")
```

The `/essay` path is the **base path**.

LangServe automatically provides operations such as:

```text
/essay/invoke
/essay/batch
/essay/stream
/essay/stream_log
```

For this project, we use `/invoke` to execute the chain.

### Essay API

```text
POST /essay/invoke
```

Example request:

```json
{
  "input": {
    "topic": "Artificial Intelligence"
  }
}
```

### Poem API

```text
POST /poem/invoke
```

Example request:

```json
{
  "input": {
    "topic": "Nature"
  }
}
```

---

# 🧠 LangChain Chain

The essay chain is:

```python
prompt1 | model
```

The poem chain is:

```python
prompt2 | model
```

This uses LangChain's **LCEL pipe syntax**.

Conceptually:

```text
User Input
    ↓
Prompt Template
    ↓
Gemini
    ↓
AI Response
```

For example:

```python
prompt1 = ChatPromptTemplate.from_template(
    "Write me an essay about {topic} with 100 words."
)

add_routes(
    app,
    prompt1 | model,
    path="/essay"
)
```

---

# 🌐 FastAPI Server

FastAPI creates the API application:

```python
app = FastAPI(
    title="LangChain Server",
    version="1.0",
    description="A Simple API Server"
)
```

Uvicorn runs the application:

```python
uvicorn.run(
    app,
    host="localhost",
    port=8000
)
```

Therefore