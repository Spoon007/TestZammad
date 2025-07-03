import unicodedata
import re
from .keyword_mapping import keyword_map

# --- Utilitaires de normalisation ---
def normalize_text(text):
    text = text.lower()
    text = unicodedata.normalize('NFD', text).encode('ascii', 'ignore').decode("utf-8")
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()

# --- Analyse de ticket enrichie avec score de confiance ---
def analyze_incoming_ticket(ticket_data):
    subject_raw = ticket_data.get("title", "")
    body_raw = ticket_data.get("article", "")

    subject = normalize_text(subject_raw)
    body = normalize_text(body_raw)
    text = subject + " " + body

    matched_keywords = []
    product_scores = {}
    keyword_hits = {}
    detected_errors = re.findall(r"ora-\d{5}|exception|erreur|error", text, re.IGNORECASE)
    contract_ids = re.findall(r"\b\d{10,20}\b", text)

    for product, keywords in keyword_map.items():
        score = 0
        hits = []
        for kw in keywords:
            kw_norm = normalize_text(kw)
            if kw_norm in subject:
                score += 3  # mot-clé dans le titre = +3
                hits.append(kw)
            elif kw_norm in body:
                score += 2  # mot-clé dans le body = +2
                hits.append(kw)

        if hits:
            product_scores[product] = score
            keyword_hits[product] = hits

    # Vérifier ambiguïté (plus d’un produit trouvé)
    if len(product_scores) > 1:
        for p in product_scores:
            product_scores[p] -= 2

    # Déterminer le meilleur produit
    if product_scores:
        product = max(product_scores, key=product_scores.get)
        score = product_scores[product]
        matched_keywords = keyword_hits[product]
    else:
        product = "UNKNOWN"
        score = 0

    # Bonus points
    if detected_errors:
        score += 2
    if contract_ids:
        score += 1

    # Déterminer le niveau de confiance
    if score >= 8:
        confidence = "ÉLEVÉ"
    elif score >= 4:
        confidence = "MOYEN"
    else:
        confidence = "FAIBLE"

    return {
        "product": product,
        "confidence": confidence,
        "score": score,
        "matched_keywords": matched_keywords,
        "contract_ids": contract_ids,
        "errors": detected_errors,
        "dates": []  # optionnel
    }

