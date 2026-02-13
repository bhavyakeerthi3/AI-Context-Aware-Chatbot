# Context-Aware Conversational AI Chatbot

A sophisticated, production-ready conversational AI agent demonstrating core NLP capabilities with a modern web interface.

## 🚀 Features

- **Multi-Turn Context Preservation**: Remembers user preferences and previous entities within a session.
- **Generative Conversational AI**: Produces natural responses using `google/flan-t5-small`.
- **Intent Classification**: Zero-shot classification using `distilbert-base-uncased-mnli`.
- **Named Entity Recognition (NER)**: Extracting products, locations, and organizations using BERT.
- **FastAPI Backend**: High-performance REST API with asynchronous handling.
- **Premium Glassmorphic UI**: Clean, modern chat interface with smooth micro-animations.

## 🛠 Tech Stack

- **Backend**: Python, FastAPI, Hugging Face Transformers, PyTorch.
- **Frontend**: Vanilla HTML5, CSS3 (Glassmorphism), JavaScript (Fetch API).
- **Models**: DistilBERT-based Zero-Shot and NER.

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Conversational-AI-Chatbot
   ```

2. Install dependencies:
   ```bash
   pip install fastapi uvicorn transformers torch pydantic
   ```

3. Run the application:
   ```bash
   python -m uvicorn backend.main:app --host 0.0.0.0 --port 8001
   ```

4. Open your browser:
   Navigate to `http://localhost:8001` to start chatting!

## 🧪 Testing

Run the included test script to verify API functionality:
```bash
python test_api.py
```
