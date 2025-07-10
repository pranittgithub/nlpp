import spacy
nlp = spacy.load("en_core_web_sm")

text = """
Artificial Intelligence is transforming the world.
It helps in automation, data analysis, and more.
Let's learn sentence segmentation and word tokenization!
"""

print("=== Sentence Segmentation ===")
doc = nlp(text)
for i, sent in enumerate(doc.sents, 1):
    print(f"{i}. {sent.text}")

print("\n=== Word Tokenization ===")
for i, sent in enumerate(doc.sents, 1):
    tokens = [token.text for token in sent]
    print(f"Sentence {i} tokens: {tokens}")
