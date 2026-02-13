import torch
from transformers import pipeline

class NLPEngine:
    def __init__(self):
        # Using zero-shot classification for Intent Detection
        # BART is powerful but might be slow, so we use a smaller one if possible
        # However, for a demo, accuracy is key.
        self.intent_classifier = pipeline("zero-shot-classification", 
                                          model="typeform/distilbert-base-uncased-mnli",
                                          device=0 if torch.cuda.is_available() else -1)
        
        # NER pipeline
        self.ner_engine = pipeline("ner", 
                                   model="dbmdz/bert-base-cased-finetuned-conll03-english",
                                   aggregation_strategy="simple",
                                   device=0 if torch.cuda.is_available() else -1)
        
        self.intents = ["customer_support", "product_inquiry", "order_status", "greeting", "farewell", "human_handoff"]

    def classify_intent(self, text):
        result = self.intent_classifier(text, candidate_labels=self.intents)
        return {
            "intent": result['labels'][0],
            "confidence": result['scores'][0]
        }

    def extract_entities(self, text):
        entities = self.ner_engine(text)
        return [{
            "entity": ent["entity_group"],
            "word": ent["word"],
            "score": float(ent["score"])
        } for ent in entities]

    def process(self, text):
        intent_info = self.classify_intent(text)
        entities = self.extract_entities(text)
        return {
            "intent": intent_info["intent"],
            "confidence": intent_info["confidence"],
            "entities": entities
        }

if __name__ == "__main__":
    engine = NLPEngine()
    test_text = "I want to check my order status for the Macbook I ordered last week."
    print(engine.process(test_text))
