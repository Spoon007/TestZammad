# /root/zammad_automation/analyzers/t24_client_routing.py

def detect_t24_client(text):
    """
    Détecte le client T24 en se basant sur les mots-clés présents dans le ticket.
    Retourne le code du client (ex: BFI, BAY...) ou 'UNKNOWN'.
    """
    client_keywords = ["BFI", "BAY", "BMCE", "CHAABI", "VISTA", "BNIG", "UMNIA"]
    text_lower = text.lower()

    for keyword in client_keywords:
        if keyword.lower() in text_lower:
            return keyword
    return "UNKNOWN"


def get_experts_for_client(client_code):
    """
    Retourne la liste des experts affectés à un client T24 donné.
    """
    expert_matrix = {
        "BFI": ["OTHMAN", "SALAH", "WALID"],
        "BAY": ["SAAD", "SALAH", "OTHMAN"],
        "CHAABI": ["HICHAM", "WALID"],
        "VISTA": ["WALID", "OTHMAN"],
        "BNIG": ["WALID"],
        "UMNIA": ["SALAH", "SAAD"],
        "BMCE": ["OTHMAN", "SALAH", "WALID", "SAAD", "HICHAM"],  # Tous les experts
    }
    return expert_matrix.get(client_code, [])


def classify_t24_issue_type(text):
    """
    Classe le ticket en :
    - 'T24 Functional'
    - 'T24 Technical / IT'
    - 'Unknown'
    """
    functional_keywords = ["commission", "paramétrage", "t24", "core banking"]
    technical_keywords = ["connexion", "serveur", "crash", "timeout", "infra", "cpu", "réseau"]

    text_lower = text.lower()

    for word in technical_keywords:
        if word in text_lower:
            return "T24 Technical / IT"
    for word in functional_keywords:
        if word in text_lower:
            return "T24 Functional"
    return "Unknown"


def analyze_t24_ticket(ticket_data):
    """
    Analyse complète d’un ticket T24 :
    - Détecte le client
    - Associe les experts
    - Classe le type de problème
    """
    full_text = f"{ticket_data.get('title', '')} {ticket_data.get('content', '')}"
    client = detect_t24_client(full_text)
    experts = get_experts_for_client(client)
    issue_type = classify_t24_issue_type(full_text)

    return {
        "client": client,
        "experts": experts,
        "issue_type": issue_type
    }

