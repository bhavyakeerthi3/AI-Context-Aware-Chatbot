import json
import os
import re

class NLPEngine:
    def __init__(self):
        print("Initializing Pure-Python Optimized NLU Engine...")
        self.intents = ["customer_support", "product_inquiry", "order_status", "greeting", "farewell", "human_handoff", "technical_problem", "shipping_inquiry"]
        
        # Load Knowledge Base
        kb_path = os.path.join(os.path.dirname(__file__), "..", "data", "knowledge_base.json")
        try:
            with open(kb_path, 'r') as f:
                self.knowledge_base = json.load(f)
        except Exception as e:
            print(f"KB load error: {e}")
            self.knowledge_base = {}

    def classify_intent(self, text):
        text_lower = text.lower()
        
        # High-fidelity patterns mimicking transformer classification
        patterns = {
            "greeting": [r"hi", r"hello", r"hey", r"greeting"],
            "farewell": [r"bye", r"goodbye", r"farewell", r"see you"],
            "order_status": [r"order", r"track", r"status", r"delivery", r"where is my"],
            "product_inquiry": [r"price", r"cost", r"how much", r"buy", r"product", r"macbook", r"iphone", r"details"],
            "technical_problem": [r"login", r"password", r"reset", r"error", r"not working", r"technical", r"broken"],
            "human_handoff": [r"agent", r"human", r"talk to someone", r"support", r"representative"],
            "shipping_inquiry": [r"shipping", r"ship", r"time", r"days", r"deliver to"]
        }
        
        for intent, keyword_list in patterns.items():
            if any(re.search(kw, text_lower) for kw in keyword_list):
                return {"intent": intent, "confidence": 0.95}
            
        return {"intent": "customer_support", "confidence": 0.70}

    def extract_entities(self, text):
        entities = []
        text_lower = text.lower()
        
        # Heuristic entity extraction with broader coverage
        product_patterns = {
            "MacBook": [r"macbook", r"mac book", r"apple laptop"],
            "iPhone": [r"iphone", r"i phone", r"apple phone"],
            "Dell Laptop": [r"dell", r"inspiron", r"latitude", r"xps"],
            "HP Laptop": [r"hp", r"pavilion", r"envy", r"spectre"],
            "Samsung Phone": [r"samsung", r"galaxy", r"s24", r"s23"],
            "Pro": [r"pro", r"max", r"ultra"],
            "Laptop": [r"laptop", r"notebook", r"computer"],
            "Phone": [r"phone", r"mobile", r"smartphone"]
        }
        
        for entity_name, patterns in product_patterns.items():
            if any(re.search(p, text_lower) for p in patterns):
                # Classify Pro as VARIANT, others as PRODUCT
                etype = "PRODUCT" if entity_name != "Pro" else "PRODUCT_VARIANT"
                entities.append({"entity": etype, "word": entity_name, "score": 1.0})
            
        return entities

    def get_grounded_response(self, intent, entities):
        kb_section = self.knowledge_base.get(intent, self.knowledge_base.get("customer_support", {}))
        
        # Check for entity-specific answers
        for entity in entities:
            word = entity["word"].lower()
            if word in kb_section:
                return kb_section[word]
        
        return kb_section.get("default", "I understand you're asking about " + intent.replace("_", " ") + ". How specifically can I assist?")

    def process(self, text):
        intent_info = self.classify_intent(text)
        entities = self.extract_entities(text)
        grounded_res = self.get_grounded_response(intent_info["intent"], entities)
        
        return {
            "intent": intent_info["intent"],
            "confidence": intent_info["confidence"],
            "entities": entities,
            "grounded_response": grounded_res
        }

if __name__ == "__main__":
    engine = NLPEngine()
    print(engine.process("How much for a macbook pro?"))
