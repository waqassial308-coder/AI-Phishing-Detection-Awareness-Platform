def format_scan_history(scan):
    return f"{scan.get('scan_id', 'N/A')} | {scan.get('risk_level', 'UNKNOWN')} | {scan.get('risk_score', 0)}"
