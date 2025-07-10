import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "The quick brown fox jumps over the lazy dog."
doc = nlp(text)

print("=== Syntactic Parsing (Dependency Tree) ===")
for token in doc:
    print(f"{token.text:<12} --> {token.dep_:<10} (head: {token.head.text})")

# Optional for notebooks only
try:
    displacy.render(doc, style="dep", jupyter=True)
except:
    print("\nVisualization only works in notebook/Colab.")
