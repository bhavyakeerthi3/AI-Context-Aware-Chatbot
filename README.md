# Context-Aware Conversational AI Chatbot (Aura AI)

A sophisticated, production-ready conversational AI agent demonstrating core NLP capabilities with a modern React-based web interface.

## 🚀 Features

- **Multi-Turn Context Preservation**: Remembers user subjects (e.g., "Dell laptop") across conversations to resolve follow-up questions using pronouns like "its" or "that".
- **Grounded Information Engine**: Uses a structured Knowledge Base to provide factual responses about product pricing, shipping, and technical support.
- **Intent Classification**: High-fidelity NLU for detecting user intent (Order Status, Inquiries, Technical Support).
- **Named Entity Recognition (NER)**: Robust extraction of products (MacBook, iPhone, Dell, HP) and their variants.
- **Modern React UI**: Rebuilt with React + Vite + Lucide-React for a premium, responsive, and stateful experience.
- **FastAPI Backend**: High-performance REST API with session-managed memory.

## 🛠 Tech Stack

- **Backend**: Python, FastAPI, Pydantic, Manual NLU/NER Logic.
- **Frontend**: React, Vite, Axios, Lucide-React, CSS3 (Glassmorphism).

## 📦 Installation & Setup

### 1. Backend Setup
1. Navigate to the project root:
   ```bash
   cd Conversational-AI-Chatbot
   ```
2. Install Python dependencies:
   ```bash
   pip install fastapi uvicorn pydantic requests
   ```
3. Run the backend server:
   ```bash
   python -m uvicorn backend.main:app --host 0.0.0.0 --port 8002
   ```

### 2. Frontend Setup
1. Navigate to the React directory:
   ```bash
   cd frontend-react
   ```
2. Install Node dependencies:
   ```bash
   npm install
   ```
3. Run the frontend development server:
   ```bash
   npm run dev -- --port 3001
   ```

## 🧪 Usage & Testing

### Accessing the App
- **UI**: Open `http://localhost:3001` in your browser.
- **API Docs**: View the Swagger UI at `http://localhost:8002/docs`.

### Test Scenario: Context Memory
Try the following flow to see the bot's intelligence:
1. **User**: "I ordered a Dell laptop"
2. **Bot**: "Your order for Dell Laptop is being processed..."
3. **User**: "What is its status?"
4. **Bot**: Aura resolves "its" to the **Dell Laptop** and confirms the status.

### Automated Testing
Run the context verification script:
```bash
python test_context.py
```

---
*Developed as a showcase for robust AI conversational systems.*
