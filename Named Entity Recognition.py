import spacy
from spacy import displacy

nlp = spacy.load("en_core_web_sm")

text = "Apple was founded by Steve Jobs in California in 1976. He was born in the United States."
doc = nlp(text)

print("=== Named Entities ===")
print("{:<25} {:<15} {:<10}".format("Entity", "Label", "Explanation"))
print("-" * 55)
for ent in doc.ents:
    print("{:<25} {:<15} {:<10}".format(ent.text, ent.label_, spacy.explain(ent.label_)))

# Optional for notebooks only
try:
    displacy.render(doc, style="ent", jupyter=True)
except:
    print("\nNamed Entity Visualization works only in notebooks.")
