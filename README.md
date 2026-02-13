# 🤖 Aura AI: Context-Aware Conversational Chatbot

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB" />
  <img src="https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white" />
  <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=for-the-badge&logo=tailwind-css&logoColor=white" />
</div>

---

## 🌟 Overview

**Aura AI** is a cutting-edge, context-aware conversational agent designed to provide seamless customer support and product engagement. Built with a high-performance **FastAPI** backend and a sleek **React** frontend, Aura demonstrates the power of state-of-the-art NLU (Natural Language Understanding) combined with real-time session management.

> [!IMPORTANT]
> Aura doesn't just answer questions; she remembers the conversation history to provide intelligent follow-up responses, a feature often missing in standard chatbots.

---

## ✨ Key Features

### 🧠 Advanced NLU & Memory
- **Context Preservation**: Seamlessly resolves pronouns (it, that, its) by maintaining a stateful session memory.
- **Intent Classification**: High-accuracy detection of user goals (Support, Inquiry, Order Status).
- **Named Entity Recognition (NER)**: Automatically extracts product names and variants to ground conversations in reality.

### 🏢 Architecture & Design
- **Core Engine**: A dependency-optimized Python NLU engine designed for maximum stability and speed.
- **Grounded Responses**: Factual answers retrieved from a structured Knowledge Base, ensuring reliability.
- **Modern UI**: A premium glassmorphic interface built with React, featuring smooth animations and real-time typing indicators.

---

## 🏗 Project Structure

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

## � Getting Started

### Prerequisites
- Python 3.9+ 🐍
- Node.js & npm 📦

### 1️⃣ Backend Setup
```bash
# Navigate to root
cd Conversational-AI-Chatbot

# Install requirements
pip install fastapi uvicorn pydantic requests

# Start the server
python -m uvicorn backend.main:app --host 0.0.0.0 --port 8002
```

### 2️⃣ Frontend Setup
```bash
# Navigate to frontend folder
cd frontend-react

# Install dependencies
npm install

# Start the React dev server
npm run dev -- --port 3001
```

---

## 🧪 Interactive Demo

Once both servers are running, navigate to `http://localhost:3001`.

### Try this flow:
1. **User**: "Tell me about the MacBook Pro."
2. **User**: "How much does it cost?"
3. **Aura**: *Recognizes "it" as the MacBook Pro and retrieves the price from the Knowledge Base.*

---

## 🛠 Tech Highlights

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Backend** | FastAPI | High-performance API Gateway |
| **AI Logic** | Python NLU | Intent & Entity Orchestration |
| **Frontend** | React + Vite | Fast, Stateful User Interface |
| **Styling** | Modern CSS | Premium Glassmorphic Aesthetic |
| **Icons** | Lucide-React | Crisp, Scalable Visuals |

---

## 🤝 Contributing

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 🙏 Acknowledgements

- [Hugging Face](https://huggingface.co/) for the state-of-the-art NLP models.
- [Lucide](https://lucide.dev/) for the beautiful open-source icons.
- [FastAPI](https://fastapi.tiangolo.com/) for the incredibly fast web framework.
- [Vite](https://vitejs.dev/) for the lightning-fast frontend tooling.

---

## 📝 License
This project is open-source and available under the MIT License.

---
<div align="center">
  <sub>Built with ❤️ for professional AI engineering showcases.</sub>
</div>
