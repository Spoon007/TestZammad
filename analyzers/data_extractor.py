# /root/zammad_automation/analyzers/data_extractor.py

import re
import dateparser
from .auto_ticket_analyzer import analyze_incoming_ticket


def extract_ticket_entities(ticket_data):
    """
    Extrait les données importantes d'un ticket Zammad :
    - Numéros de contrat (8 à 15 chiffres consécutifs)
    - Dates (formats multiples)
    - Messages d'erreur (ORA-600, NullPointerException, etc.)
    - Identifiants techniques ou clients (ex : client1234, user_4567, id:XYZ45)
    """
    title = ticket_data.get("title", "")
    article = ticket_data.get("article", "")
    text = f"{title} {article}"

    # Numéros de contrat : 8 à 15 chiffres consécutifs
    contract_ids = re.findall(r"\b\d{8,15}\b", text)

    # Dates : on capture les motifs explicites (JJ/MM/AAAA, AAAA-MM-JJ, etc.)
    raw_dates = re.findall(r"\b\d{1,2}/\d{1,2}/\d{4}\b|\b\d{4}-\d{2}-\d{2}\b|\b\d{1,2} [a-zA-Zé]+ \d{4}\b|\bhier\b|\baujourd'hui\b", text, re.IGNORECASE)

    # Normaliser les dates avec dateparser
    dates = []
    for d in raw_dates:
        parsed = dateparser.parse(d)
        if parsed:
            dates.append(d.strip())

    # Erreurs courantes (base simple)
    error_patterns = r"ORA-\d{3,5}|NullPointerException|Segmentation fault|Exception|erreur|error"
    errors = re.findall(error_patterns, text, re.IGNORECASE)

    # Identifiants techniques ou client (client1234, user_4567, id:XYZ45, usr_001, etc.)
    ids = re.findall(r"\b(?:client|user|id|usr|utilisateur|client)[_:\-]?[a-zA-Z0-9]+\b", text, re.IGNORECASE)

    return {
        "contracts": contract_ids,
        "dates": dates,
        "errors": errors,
        "ids": ids
    }


def full_ticket_analysis(ticket_data):
    """
    Combine l'analyse du produit et l'extraction des entités d'un ticket.
    Retourne un résultat complet.
    """
    product_result = analyze_incoming_ticket(ticket_data)
    entities = extract_ticket_entities(ticket_data)

    return {
        "product": product_result.get("product", "UNKNOWN"),
        "confidence": product_result.get("confidence", "FAIBLE"),
        "score": product_result.get("score", 0),
        "matched_keywords": product_result.get("matched_keywords", []),
        "contracts": entities["contracts"],
        "dates": entities["dates"],
        "errors": entities["errors"],
        "ids": entities["ids"]
    }

