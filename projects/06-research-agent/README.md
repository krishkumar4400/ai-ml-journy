# Architecture

```
                ┌──────────────────┐
                │    Next.js UI    │
                │  Chat / Dashboard│
                └────────┬─────────┘
                         │
          ┌──────────────┴──────────────┐
          │                             │
          ▼                             ▼

┌──────────────────┐        ┌──────────────────┐
│   Express.js     │        │     FastAPI      │
│ Main App Backend │        │    AI Backend    │
│ Auth / DB / API  │        │ Agents / RAG     │
└────────┬─────────┘        └────────┬─────────┘
         │                            │
         ▼                            ▼

 ┌──────────────┐           ┌────────────────┐
 │ PostgreSQL   │           │ Ollama / LLM   │
 └──────────────┘           └────────────────┘
```

# Folder Structure

```
ai-research-platform/

│
├── frontend/          → Next.js
│
├── backend-node/      → Express.js
│
├── backend-ai/        → FastAPI + LangChain
│
├── docker-compose.yml
│
└── README.md
```

# Best Long-Term Upgrade Path

| Upgrade    | Why             |
| ---------- | --------------- |
| LangGraph  | advanced agents |
| Qdrant     | vector DB       |
| Redis      | caching         |
| PostgreSQL | production DB   |
| Docker     | deployment      |
| Celery/RQ  | background jobs |
| WebSockets | live streaming  |
| Kubernetes | scaling         |

