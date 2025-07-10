import spacy
from collections import Counter
from itertools import islice

nlp = spacy.load("en_core_web_sm")

text = """
Natural Language Processing enables machines to understand and generate human language.
It includes tasks such as text classification, machine translation, and more.
"""

doc = nlp(text.lower())
tokens = [token.text for token in doc if not token.is_punct and not token.is_space]

def generate_ngrams(tokens, n):
    return zip(*(islice(tokens, i, None) for i in range(n)))

trigrams = list(generate_ngrams(tokens, 3))
trigram_freq = Counter(trigrams)

print("=== Trigram Frequencies ===")
for trigram, freq in trigram_freq.items():
    print(f"{trigram} : {freq}")
