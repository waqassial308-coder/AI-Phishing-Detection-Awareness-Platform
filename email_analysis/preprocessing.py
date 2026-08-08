import re

def clean_email_text(text):
    text = text.lower().strip()
    text = re.sub(r'\s+', ' ', text)
    return text
