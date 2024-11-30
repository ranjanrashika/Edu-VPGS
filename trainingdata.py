import pandas as pd

data = pd.read_csv("C:\Users\Rashika Ranjan\OneDrive\Desktop\DL-PROJECT\training_data.csv")

description = data['Description'].tolist()
keywords = data['Keywords'].tolist()

from transformers import AutoTokenizer, AutoModelForSequenceClassification
tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased')
model = AutoModelForSequenceClassification.from_prretrained('bert-base-uncased', num_labels=len(set(keywords)))

encodings = tokenizer(keywords, truncation=True, padding=True, max_length=128, return_tensors="pt")

