import requests
import json

BASE_URL = "http://localhost:8002"

def test_multi_turn():
    print("Testing Multi-turn Context Memory...")
    
    # 1. First Turn: Mention Entity
    payload1 = {"message": "I ordered a Dell laptop"}
    response1 = requests.post(f"{BASE_URL}/chat", json=payload1)
    data1 = response1.json()
    session_id = data1['session_id']
    
    print(f"\nUser: {payload1['message']}")
    print(f"Bot: {data1['response']}")
    print(f"Intent: {data1['intent']}")
    print(f"Entities: {data1['entities']}")

    # 2. Second Turn: Follow-up using anaphora
    payload2 = {"message": "What is its status?", "session_id": session_id}
    response2 = requests.post(f"{BASE_URL}/chat", json=payload2)
    data2 = response2.json()
    
    print(f"\nUser: {payload2['message']}")
    print(f"Bot: {data2['response']}")
    print(f"Intent: {data2['intent']}")
    print(f"Entities: {data2['entities']}")

    # 3. Third Turn: Mention Another Entity
    payload3 = {"message": "I also want to buy a MacBook", "session_id": session_id}
    response3 = requests.post(f"{BASE_URL}/chat", json=payload3)
    data3 = response3.json()
    
    print(f"\nUser: {payload3['message']}")
    print(f"Bot: {data3['response']}")
    print(f"Intent: {data3['intent']}")
    print(f"Entities: {data3['entities']}")

    # 4. Fourth Turn: Follow-up for the new entity
    payload4 = {"message": "How much does it cost?", "session_id": session_id}
    response4 = requests.post(f"{BASE_URL}/chat", json=payload4)
    data4 = response4.json()
    
    print(f"\nUser: {payload4['message']}")
    print(f"Bot: {data4['response']}")
    print(f"Intent: {data4['intent']}")
    print(f"Entities: {data4['entities']}")

if __name__ == "__main__":
    try:
        test_multi_turn()
    except Exception as e:
        print(f"Error: {e}")
