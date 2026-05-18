backend-ai/

│
├── app/
│   │
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logging.py
│   │   └── constants.py
│   │
│   ├── api/
│   │   ├── routes/
│   │   │   ├── health.py
│   │   │   ├── research.py
│   │   │   ├── chat.py
│   │   │   └── upload.py
│   │   │
│   │   └── router.py
│   │
│   ├── agents/
│   │   ├── search_agent.py
│   │   ├── reader_agent.py
│   │   ├── writer_agent.py
│   │   ├── critic_agent.py
│   │   └── orchestrator.py
│   │
│   ├── chains/
│   │   ├── writer_chain.py
│   │   └── critic_chain.py
│   │
│   ├── tools/
│   │   ├── web_search.py
│   │   ├── scraper.py
│   │   └── pdf_reader.py
│   │
│   ├── services/
│   │   ├── research_service.py
│   │   ├── llm_service.py
│   │   └── rag_service.py
│   │
│   ├── models/
│   │   ├── request_models.py
│   │   └── response_models.py
│   │
│   ├── prompts/
│   │   ├── writer_prompt.py
│   │   └── critic_prompt.py
│   │
│   ├── utils/
│   │   ├── helpers.py
│   │   ├── parsers.py
│   │   └── validators.py
│   │
│   └── db/
│       ├── vector_store.py
│       └── memory_store.py
│
├── tests/
│
├── .env
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
