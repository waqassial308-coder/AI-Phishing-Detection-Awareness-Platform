def calculate_risk_score(indicator_count, clicked_simulation=False):
    score = min(indicator_count * 15 + (30 if clicked_simulation else 0), 100)
    level = 'HIGH' if score >= 50 else 'MEDIUM' if score >= 20 else 'LOW'
    return {'score': score, 'level': level}
