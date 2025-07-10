import spacy
nlp = spacy.load("en_core_web_sm")

text = "Natural Language Processing enables machines to understand and generate language."
doc = nlp(text)

print("=== Neural Model PoS Tagging using spaCy ===")
print("{:<15} {:<10} {:<10}".format("Token", "PoS", "Tag"))
print("-" * 40)
for token in doc:
    print("{:<15} {:<10} {:<10}".format(token.text, token.pos_, token.tag_))
