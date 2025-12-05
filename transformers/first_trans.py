from transformers import pipeline

generator = pipeline("text-generation", model="gpt2")

result = generator("Hello", max_length=30)
print(result)
