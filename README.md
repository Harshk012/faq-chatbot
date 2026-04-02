# 🤖 FAQ Chatbot — ICICI Prudential Life Insurance
### Powered by Neuro-SAN Agentic AI · FastAPI · React · MongoDB

[![CI/CD](https://github.com/YOUR_USERNAME/faq-chatbot/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/YOUR_USERNAME/faq-chatbot/actions)
[![Docker](https://img.shields.io/badge/Docker-Hub-blue?logo=docker)](https://hub.docker.com/u/YOUR_DOCKERHUB_USERNAME)

A production-grade FAQ chatbot for ICICI Prudential Life Insurance, featuring a **Neuro-SAN agentic network** for intelligent, multi-turn conversation handling.

---

## 🏗 Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    User Browser                         │
│         React + PrimeReact UI  (port 3000)              │
└─────────────────────┬───────────────────────────────────┘
                      │ REST API (POST /api/chat)
┌─────────────────────▼───────────────────────────────────┐
│              FastAPI Backend  (port 8000)                │
│                                                         │
│  ┌──────────────┐    ┌──────────────────────────────┐   │
│  │  POST /chat  │───▶│   Neuro-SAN Agent Service    │   │
│  │ GET /history │    │  DirectAgentSessionFactory   │   │
│  │  DELETE /..  │    │  faq_chatbot.hocon           │   │
│  └──────────────┘    └──────────────┬───────────────┘   │
│                                     │ LLM API           │
│  ┌──────────────┐    ┌──────────────▼───────────────┐   │
│  │   MongoDB    │    │     OpenAI GPT-4o / Ollama   │   │
│  │  (Motor)     │    │     (or any neuro-san LLM)   │   │
│  └──────────────┘    └──────────────────────────────┘   │
└─────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
faq-chatbot/
├── .github/
│   └── workflows/
│       └── ci-cd.yml              # GitHub Actions: test → build → push DockerHub
├── backend/
│   ├── app/
│   │   ├── main.py                # FastAPI app entry point
│   │   ├── api/
│   │   │   ├── chat.py            # POST /api/chat endpoint
│   │   │   └── history.py         # GET/DELETE /api/history/{session_id}
│   │   ├── models/chat.py         # Pydantic models (ChatRequest, ChatResponse)
│   │   ├── services/
│   │   │   ├── neuro_san_service.py  # Neuro-SAN agent invocation + fallback
│   │   │   └── faq_data.py           # ICICI Pru FAQ knowledge base
│   │   └── db/mongo.py            # Async MongoDB (Motor) connection
│   ├── registries/
│   │   ├── faq_chatbot.hocon      # Neuro-SAN agent definition
│   │   └── manifest.hocon         # Neuro-SAN agent registry manifest
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/
│   ├── src/
│   │   ├── App.js                 # Root component (PrimeReactProvider, layout)
│   │   ├── components/
│   │   │   ├── ChatWindow.jsx     # Orchestrates header, messages, input
│   │   │   ├── ChatHeader.jsx     # Brand header with clear button
│   │   │   ├── MessageBubble.jsx  # User/bot message with markdown
│   │   │   ├── TypingIndicator.jsx # Animated typing dots
│   │   │   ├── ChatInput.jsx      # PrimeReact InputTextarea + send Button
│   │   │   └── SuggestedQuestions.jsx # Quick-start question chips
│   │   ├── hooks/
│   │   │   └── useChat.js         # State management, session ID, API calls
│   │   ├── services/
│   │   │   └── api.js             # Axios client for FastAPI
│   │   └── styles/
│   │       └── global.css         # Full design system + ICICI brand theme
│   ├── public/index.html
│   ├── package.json
│   └── Dockerfile                 # Multi-stage: Node build → Nginx serve
└── docker-compose.yml             # MongoDB + Backend + Frontend
```

---

## 🧠 How Neuro-SAN Works in This Project

### What is Neuro-SAN?
[Neuro-SAN](https://github.com/cognizant-ai-lab/neuro-san) is a framework for building **agentic networks** — systems where multiple AI agents collaborate using a graph of tools and instructions, enabling richer, more contextual conversations than a single LLM call.

### Agent Definition (`faq_chatbot.hocon`)
The agent is defined in HOCON format and specifies:
- **`llm_config`** — which LLM model to use (e.g., `gpt-4o`)
- **`tools`** — the agent's name, description (used as initial prompt), and detailed instructions including the full FAQ knowledge base

```hocon
{
  "llm_config": { "model_name": "gpt-4o" },
  "tools": [{
    "name": "FAQChatbotAgent",
    "function": { "description": "FAQ assistant for ICICI Prudential" },
    "instructions": "You are a professional FAQ assistant... [full FAQ data embedded here]"
  }]
}
```

### Invocation Flow
```
POST /api/chat
     │
     ▼
neuro_san_service.py
     │
     ├─ Build context: FAQ data + last 6 messages from DB
     │
     ├─ DirectAgentSessionFactory.create_session("faq_chatbot")
     │
     ├─ session.streaming_chat({ user_message, sly_data })
     │         │
     │         ▼
     │    Neuro-SAN loads faq_chatbot.hocon
     │    → Calls LLM with instructions + user message
     │    → Streams response chunks
     │
     └─ Collect stream → return final text response
```

### Multi-turn Conversation
- Each chat session has a unique `session_id` (UUID stored in `sessionStorage`)
- Every message pair is persisted in MongoDB
- On each new message, the **last 6 messages** are fetched from DB and injected into the agent's context, enabling coherent multi-turn conversations like:
  - User: *"How do I change my bank account?"*
  - Bot: *"Submit a request with a cancelled cheque..."*
  - User: *"Is there any charge?"* ← Agent understands this refers to bank account change

### Fallback Mode
If Neuro-SAN / OpenAI is unavailable, the service falls back to **keyword-based FAQ lookup** so the chatbot remains functional during development without API keys.

---

## 🚀 Quick Start

### Prerequisites
- Docker & Docker Compose
- OpenAI API key (or another LLM supported by Neuro-SAN)

### 1. Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/faq-chatbot.git
cd faq-chatbot
```

### 2. Set your LLM API key
```bash
export OPENAI_API_KEY=sk-your-key-here
```

### 3. Run with Docker Compose
```bash
docker-compose up --build
```

**Services:**
| Service | URL |
|---------|-----|
| Frontend | http://localhost:3000 |
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| MongoDB | mongodb://localhost:27017 |

---

## 🛠 Local Development (without Docker)

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt

export OPENAI_API_KEY=sk-your-key
export MONGO_URL=mongodb://localhost:27017
export AGENT_MANIFEST_FILE=./registries/manifest.hocon

uvicorn app.main:app --reload --port 8000
```

### Frontend
```bash
cd frontend
cp .env.example .env
npm install --legacy-peer-deps
npm start                       # Opens http://localhost:3000
```

---

## 🔌 API Reference

### `POST /api/chat`
Send a message and receive a bot response.

**Request:**
```json
{
  "session_id": "uuid-string",
  "message": "How do I change my bank account?",
  "conversation_history": []
}
```

**Response:**
```json
{
  "session_id": "uuid-string",
  "reply": "To change your registered bank account, log in to iciciprulife.com...",
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### `GET /api/history/{session_id}`
Retrieve conversation history for a session.

### `DELETE /api/history/{session_id}`
Clear conversation history for a session.

### `GET /health`
Health check endpoint.

---

## 🐳 Docker Images (DockerHub)

| Image | Link |
|-------|------|
| Backend | `docker pull YOUR_DOCKERHUB_USERNAME/faq-chatbot-backend:latest` |
| Frontend | `docker pull YOUR_DOCKERHUB_USERNAME/faq-chatbot-frontend:latest` |

---

## ⚙️ GitHub Actions Setup

Add these secrets to your GitHub repository (`Settings → Secrets → Actions`):

| Secret | Description |
|--------|-------------|
| `DOCKERHUB_USERNAME` | Your DockerHub username |
| `DOCKERHUB_TOKEN` | DockerHub access token (not password) |

The pipeline runs on every push to `main`:
1. ✅ **Test backend** — install deps, lint, run pytest
2. ✅ **Test frontend** — install deps, build React app
3. 🐳 **Build & Push** — multi-arch Docker images pushed to DockerHub with `latest` + `sha-*` tags

---

## 📊 Evaluation Checklist

| Criterion | Implementation |
|-----------|---------------|
| **Backend API design** | RESTful FastAPI with Pydantic validation, async MongoDB, proper error codes |
| **Neuro-SAN conversation handling** | `DirectAgentSessionFactory`, HOCON agent config, multi-turn context injection |
| **Code readability** | Clean separation: api / models / services / db layers |
| **Functional chat UI** | React + PrimeReact components, session management, markdown rendering |
| **Correct API usage** | Axios service layer, error handling, loading states |
| **Error handling** | Toast notifications, fallback mode, typed error responses |
| **Valid Docker builds** | Multi-stage frontend, slim backend, healthchecks |
| **GitHub Actions pipeline** | Test → Build → Push on main branch |
| **DockerHub images** | Tagged with `latest` and `sha-*` |
| **README** | Architecture diagram, setup guide, Neuro-SAN explanation |
