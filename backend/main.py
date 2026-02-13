from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from .nlp_engine import NLPEngine
from .memory_manager import MemoryManager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
import uuid
import os

app = FastAPI(title="Context-Aware Conversational AI Chatbot")

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize Engine and Memory
nlp_engine = NLPEngine()
memory_manager = MemoryManager()

class ChatRequest(BaseModel):
    message: str
    session_id: Optional[str] = None

class ChatResponse(BaseModel):
    response: str
    session_id: str
    intent: str
    entities: List[dict]
    confidence: float

def generate_bot_response(intent, entities, history):
    # Simple rule-based response generation based on intent and entities
    if intent == "greeting":
        return "Hello! I'm your AI assistant. How can I help you today?"
    elif intent == "farewell":
        return "Goodbye! Have a great day!"
    elif intent == "order_status":
        product = next((e['word'] for e in entities if e['entity'] in ['ORG', 'MISC']), "your items")
        return f"I've found your order for {product}. It's currently being processed."
    elif intent == "product_inquiry":
        return "That's a great question about our products. Let me find the details for you."
    elif intent == "human_handoff":
        return "I'm connecting you with a human agent for further assistance. Please wait a moment."
    else:
        return "I'm not exactly sure how to help with that. Could you please rephrase or provide more details?"

@app.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    session_id = request.session_id or str(uuid.uuid4())
    user_message = request.message
    
    # Process with NLP Engine
    nlp_result = nlp_engine.process(user_message)
    
    # Store message and context
    memory_manager.add_message(session_id, "user", user_message)
    for entity in nlp_result["entities"]:
        memory_manager.update_context(session_id, entity["entity"], entity["word"])
    
    # Generate response
    bot_msg = generate_bot_response(
        nlp_result["intent"], 
        nlp_result["entities"], 
        memory_manager.get_history(session_id)
    )
    
    memory_manager.add_message(session_id, "bot", bot_msg)
    
    return ChatResponse(
        response=bot_msg,
        session_id=session_id,
        intent=nlp_result["intent"],
        entities=nlp_result["entities"],
        confidence=nlp_result["confidence"]
    )

@app.get("/health")
async def health():
    return {"status": "healthy"}

# Serve Frontend
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
app.mount("/", StaticFiles(directory=frontend_path, html=True), name="frontend")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
