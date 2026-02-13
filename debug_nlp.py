import torch
from transformers import pipeline

import torch
from transformers import pipeline
import sys

def test_pipeline(name, task, model):
    try:
        print(f"Testing {name} ({task}) with model {model}...")
        p = pipeline(task, model=model, device=-1)
        print(f"  {name} loaded successfully.")
        return p
    except Exception as e:
        print(f"  {name} FAILED: {e}")
        return None

if __name__ == "__main__":
    # Test a very standard model first
    test_pipeline("Sentiment", "sentiment-analysis", "distilbert-base-uncased-finetuned-sst-2-english")
    
    # Test Zero-Shot with a different model
    test_pipeline("Zero-Shot", "zero-shot-classification", "cross-encoder/nli-distilroberta-base")
    
    # Test NER with a different model
    test_pipeline("NER", "ner", "dbmdz/bert-base-cased-finetuned-conll03-english")
    
    # Test T5
    test_pipeline("T5", "text2text-generation", "google/flan-t5-small")

