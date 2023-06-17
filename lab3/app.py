import torch
from typing import Dict
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import AutoTokenizer, AutoModelForSequenceClassification

app = FastAPI()

model = AutoModelForSequenceClassification.from_pretrained('./model')
tokenizer = AutoTokenizer.from_pretrained('./tokenizer')


class Item(BaseModel):
    text: str


def text2toxicity(text: str) -> Dict[str, float]:
    with torch.no_grad():
        inputs = tokenizer(text, return_tensors='pt', truncation=True, padding=True).to(model.device)
        proba = torch.sigmoid(model(**inputs).logits).cpu().numpy()
    proba = {k: float(v) for k, v in zip(model.config.id2label.values(), proba[0])}
    return proba


@app.post('/predict')
def predict(item: Item):
    return {'prediction': text2toxicity(item.text)}
