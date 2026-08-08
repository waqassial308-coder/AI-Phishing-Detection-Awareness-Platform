import re

def extract_urls(text):
    return re.findall(r'https?://[^\s]+|www\.[^\s]+', text)

def has_suspicious_url(text):
    return len(extract_urls(text)) > 0
