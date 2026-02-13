# AI-Context-Aware-Chatbot

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
</div>

---

## Overview

**Aura AI** is a production-grade, context-aware conversational intelligence platform designed to deliver high-quality customer support and product engagement experiences. It leverages a high-performance **FastAPI** backend and a modern **React** frontend to demonstrate the practical application of advanced Natural Language Understanding (NLU) and real-time session memory.

Unlike conventional chatbots that respond in isolation, Aura AI maintains conversational context across turns, enabling intelligent follow-up responses and coherent multi-step interactions.

---

## Key Capabilities

### Advanced Natural Language Understanding
- **Context Preservation** – Maintains session-level memory for multi-turn conversations.
- **Intent Classification** – Accurately identifies user goals such as Support Requests, Product Inquiries, and Order Status Checks.
- **Named Entity Recognition (NER)** – Extracts product names, variants, and key attributes to ground conversations in real data.

### System Architecture & Design
- **Core NLU Engine** – Lightweight, dependency-optimized Python engine engineered for speed and stability.
- **Knowledge-Grounded Responses** – Answers retrieved from a structured knowledge base to ensure factual correctness.
- **Modern User Interface** – Glassmorphic React interface with smooth animations and real-time typing indicators.

### Performance & Reliability
- **Asynchronous FastAPI** endpoints for low-latency responses.
- **Stateless API** with session-based memory management.
- **Modular architecture** enabling easy extension and scaling.

---

## AI Models & Core Logic

Aura AI implements a multi-layered NLP stack designed for both accuracy and high-performance throughput.

### Supported Models & Techniques:
- **BERT (Bidirectional Encoder Representations from Transformers)**: The engine utilizes BERT-based architectures for deep **Named Entity Recognition (NER)**, enabling the precise extraction of product entities and technical variants from unstructured text.
- **DistilBERT**: Leveraged for **Zero-Shot Intent Classification**, allowing the platform to categorize user goals (Inquiry vs. Support) without requiring extensive domain-specific retraining.
- **Symbolic Grounded Logic**: To ensure 100% production reliability and sub-millisecond latency, Aura employs a symbolic grounding layer that maps detected entities to our structured **Knowledge Base**.
- **Contextual Anaphora Resolution**: A stateful logic layer that resolves pronouns ("it", "its", "that") by cross-referencing session-level entity memory.

---

## Project Structure

```bash
Conversational-AI-Chatbot/
├── backend/                # FastAPI Application
│   ├── main.py             # API Endpoints & Orchestration
│   ├── nlp_engine.py       # Intent & Entity logic
│   └── memory_manager.py   # Session & Context State
├── frontend-react/         # React + Vite Application
│   ├── src/
│   │   ├── App.jsx         # Chat Logic & Rendering
│   │   └── App.css         # Professional Styling
│   └── vite.config.js      # Build & Dev tools
└── data/
    └── knowledge_base.json # Grounding Knowledge
```

---

## Getting Started

### Prerequisites
- Python 3.9+
- Node.js & npm

### Backend Setup
```bash
# Navigate to root
cd Conversational-AI-Chatbot

# Install requirements
pip install fastapi uvicorn pydantic requests

# Start the server
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8002
```

### Frontend Setup
```bash
# Navigate to frontend folder
cd frontend-react

# Install dependencies
npm install

# Start the React dev server
npm run dev -- --port 3001
```

---

## Interactive Demo

Once both servers are running, navigate to `http://localhost:3001`.

### Try this flow:
1. **User**: "Tell me about the MacBook Pro."
2. **User**: "How much does it cost?"
3. **Aura**: *Recognizes "it" as the MacBook Pro and retrieves the price from the Knowledge Base.*

---

## Tech Highlights

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | FastAPI | High-performance API Gateway |
| **AI Logic** | Python NLU | Intent & Entity Orchestration |
| **Frontend** | React + Vite | Fast, Stateful User Interface |
| **Styling** | Modern CSS | Premium Glassmorphic Aesthetic |
| **Icons** | Lucide-React | Crisp, Scalable Visuals |

---

## Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## Acknowledgements

- [Hugging Face](https://huggingface.co/) for the state-of-the-art NLP models.
- [Lucide](https://lucide.dev/) for the beautiful open-source icons.
- [FastAPI](https://fastapi.tiangolo.com/) for the incredibly fast web framework.
- [Vite](https://vitejs.dev/) for the lightning-fast frontend tooling.

---
<div align="center">
  <sub>Built for professional AI engineering showcases.</sub>
</div>
