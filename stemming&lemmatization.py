import spacy
nlp = spacy.load("en_core_web_sm")

text = "The striped bats are hanging on their feet for best"
doc = nlp(text)

print("=== Lemmatization ===")
for token in doc:
    print(f"{token.text} --> {token.lemma_}")

print("\n=== Pseudo-Stemming (Demo) ===")
for token in doc:
    stem = token.text[:4] if len(token.text) > 4 else token.text
    print(f"{token.text} --> {stem}")
