import json
import re

def lambda_handler(event, context):
    email_text = event.get('email_text', '').lower()
    phishing_keywords = ['urgent','verify your account','click here','password','account suspended','confirm your identity','bank details','login immediately']
    detected = [k for k in phishing_keywords if k in email_text]
    has_link = bool(re.search(r'https?://|www\.', email_text))
    risk_score = min(len(detected) * 15 + (20 if has_link else 0), 100)
    risk_level = 'HIGH' if risk_score >= 50 else 'MEDIUM' if risk_score >= 20 else 'LOW'
    return {'statusCode': 200, 'body': json.dumps({'project':'AI-Powered Phishing Detection & Awareness Platform','risk_score':risk_score,'risk_level':risk_level,'phishing_indicators':detected,'suspicious_link_detected':has_link})}
