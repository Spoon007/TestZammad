import sys
import os

# Ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'analyzers')))



# /root/zammad_automation/resolvers/auto_resolver.py
from analyzers.auto_ticket_analyzer import analyze_incoming_ticket
from analyzers.data_extractor import extract_ticket_entities
from analyzers.t24_client_routing import detect_t24_client, get_experts_for_client, classify_t24_issue_type
from analyzers.keyword_mapping import detect_client, detect_client_product, classify_issue_type

def resolve_ticket(ticket_data):
    product_info = analyze_incoming_ticket(ticket_data)
    product = product_info.get('product') if isinstance(product_info, dict) else product_info

    entities = extract_ticket_entities(ticket_data)
    text = (ticket_data.get("title", "") + " " + ticket_data.get("article", "")).strip()

    result = {
        "product": product if product else "UNKNOWN",
        "contracts": entities.get("contracts", []),
        "dates": entities.get("dates", []),
        "errors": entities.get("errors", []),
        "client": None,
        "experts": [],
        "issue_type": None
    }

    if product == "T24":
        client = detect_t24_client(text)
        result["client"] = client if client else "UNKNOWN"
        result["experts"] = get_experts_for_client(client) if client else []
        result["issue_type"] = classify_t24_issue_type(text) if client else None

    elif product in ["SCANIA", "PAOMA", "UTINA", "KOBBY", "FIRES", "MGL", "CIP", "TPRINT", "TDC", "JURIS"]:
        client = detect_client(text)
        if client:
            result["client"] = client
            detected_product = detect_client_product(text)
            result["product"] = detected_product if detected_product else product
            result["issue_type"] = classify_issue_type(text)
            result["experts"] = [f"expert_{result['product'].lower()}"]
        else:
            result["client"] = "UNKNOWN"
            result["experts"] = []
            result["issue_type"] = None

    else:
        result["client"] = "UNKNOWN"
        result["experts"] = []
        result["issue_type"] = None

    return result
