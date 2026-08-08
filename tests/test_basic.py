from risk_scoring.risk_score import calculate_risk_score

def test_high_risk_score():
    result = calculate_risk_score(4, True)
    assert result['level'] == 'HIGH'
