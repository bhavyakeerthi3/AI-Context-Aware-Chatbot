import requests
import json

BASE_URL = "http://localhost:8000"

def test_health():
    response = requests.get(f"{BASE_URL}/health")
    print(f"Health Check: {response.status_code} - {response.json()}")

def test_chat(message, session_id=None):
    payload = {"message": message}
    if session_id:
        payload["session_id"] = session_id
    
    response = requests.post(f"{BASE_URL}/chat", json=payload)
    data = response.json()
    print(f"\nUser: {message}")
    print(f"Bot: {data['response']}")
    print(f"Intent: {data['intent']} (Conf: {data['confidence']:.2f})")
    print(f"Entities: {data['entities']}")
    return data['session_id']

if __name__ == "__main__":
    try:
        test_health()
        sid = test_chat("Hello!")
        test_chat("Tell me about the MacBook Pro.", session_id=sid)
        test_chat("I'm having trouble with my login.", session_id=sid)
        test_chat("How long does shipping take?", session_id=sid)
        test_chat("Check my order status.", session_id=sid)
    except Exception as e:
        print(f"Error: {e}")
