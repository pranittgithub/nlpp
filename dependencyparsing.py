import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "Artificial Intelligence is transforming the way we interact with machines."
doc = nlp(text)

print("=== Dependency Parsing ===")
print("{:<15} {:<10} {:<15} {:<15}".format("Token", "Dep", "Head", "POS"))
print("-" * 60)
for token in doc:
    print("{:<15} {:<10} {:<15} {:<15}".format(
        token.text, token.dep_, token.head.text, token.pos_))

# Optional for notebooks only
try:
    displacy.render(doc, style="dep", jupyter=True)
except:
    print("\nVisualization only works in notebook/Colab.")
