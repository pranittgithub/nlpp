from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small")

text = """
Artificial Intelligence (AI) is transforming industries across the globe. It is being applied in healthcare, finance, transportation, education, and many other sectors to enhance productivity and decision-making. 
AI systems are now capable of analyzing vast amounts of data, recognizing patterns, and making predictions with impressive accuracy. 
Machine learning, a subfield of AI, enables systems to learn from data without being explicitly programmed. 
As AI technology continues to advance, it is also raising important ethical and social questions. 
Experts emphasize the need for responsible development and use of AI to ensure that its benefits are shared broadly and its risks are minimized.
"""

summary = summarizer(text, max_length=60, min_length=25, do_sample=False)

print("=== Summary ===")
print(summary[0]['summary_text'])
