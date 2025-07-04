# /root/zammad_automation/analyzers/complexity_and_routing.py

def assign_specialist(product):
    mapping = {
        "T24": "expert_t24",
        "MGL": "expert_mgl",
        "FIRES": "expert_fires",
        "UTINA": "expert_utina",
        "CIP": "expert_cip",
        "TPRINT": "expert_tprint",
        "TDC": "expert_tdc",
        "JURIS": "expert_juris"
    }
    return mapping.get(product.upper(), "à trier")

def estimate_complexity(ticket_data):
    text = (ticket_data.get("title", "") + " " + ticket_data.get("content", "")).lower()
    contracts = ticket_data.get("contracts", [])
    dates = ticket_data.get("dates", [])
    errors = ticket_data.get("errors", [])

    score = 0

    # Règles de complexité
    if any(word in text for word in ["urgent", "incident", "bloqué", "critique"]):
        score += 3
    if errors:
        score += 2
    if len(contracts) >= 1:
        score += 1
    if len(dates) >= 2:
        score += 2
    elif len(dates) == 1:
        score += 1
    if len(text.split()) < 8:
        score -= 1

    # Niveau de complexité
    if score >= 5:
        return "élevée"
    elif score >= 2:
        return "moyenne"
    else:
        return "faible"

