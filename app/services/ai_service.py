from transformers import pipeline

class AIService:
    def __init__(self):
        # small models: quicker downloads
        self.summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
        self.sentiment = pipeline("sentiment-analysis")

    def summarize(self, text: str) -> str:
        out = self.summarizer(text, max_length=60, min_length=10, do_sample=False)
        return out[0]["summary_text"]

    def analyze(self, text: str):
        return self.sentiment(text)[0]  # {'label': 'POSITIVE', 'score': ...}
