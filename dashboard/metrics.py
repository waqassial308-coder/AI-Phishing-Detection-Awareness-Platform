def awareness_metrics(total_users, reported_phishing, clicked_simulation):
    report_rate = (reported_phishing / total_users * 100) if total_users else 0
    click_rate = (clicked_simulation / total_users * 100) if total_users else 0
    return {'report_rate': round(report_rate, 2), 'click_rate': round(click_rate, 2)}
