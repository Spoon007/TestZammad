# /analyzers/client_product_classifier.py

import re

# Listes ou dictionnaires d'exemples pour clients et produits
CLIENTS = {
    "SCANIA": ["scania", "scania trucks", "scania client"],
    "UTINA": ["utina", "utina leasing"],
    "KOBBY": ["kobby", "kobby solutions"],
    "PAOMA": ["paoma", "paoma services"],
    "FIRES": ["fires", "fires system"],
    "T24": ["t24", "temenos t24"],
}

PRODUCTS = {
    "T24": ["core banking", "temenos", "t24 system"],
    "FIRES": ["fire alarm", "fires system", "fire detection"],
    "UTINA": ["leasing", "vehicle leasing"],
    "KOBBY": ["software", "kobby app"],
    "SCANIA": ["truck", "logistics", "scania truck"],
    "PAOMA": ["maintenance", "paoma service"],
}

ISSUE_TYPES = {
    "technical": ["error", "failure", "crash", "bug", "exception", "fail"],
    "functional": ["feature", "request", "enhancement", "improvement"],
    "performance": ["slow", "latency", "performance", "delay"],
    "security": ["unauthorized", "vulnerability", "breach", "attack"],
}

def detect_client(text):
    """
    Detecte le client dans le texte à partir des mots-clés.
    Retourne le nom du client ou None si non détecté.
    """
    text_lower = text.lower()
    for client, keywords in CLIENTS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                return client
    return None

def detect_client_product(text):
    """
    Detecte le produit lié dans le texte à partir des mots-clés.
    Retourne le nom du produit ou None si non détecté.
    """
    text_lower = text.lower()
    for product, keywords in PRODUCTS.items():
        for kw in keywords:
            if kw.lower() in text_lower:
                return product
    return None

def classify_issue_type(text):
    """
    Classifie le type de problème à partir du texte.
    Retourne la catégorie la plus probable parmi ISSUE_TYPES ou None.
    """
    text_lower = text.lower()
    scores = {key: 0 for key in ISSUE_TYPES.keys()}
    for issue_type, keywords in ISSUE_TYPES.items():
        for kw in keywords:
            if kw in text_lower:
                scores[issue_type] += 1
    # Retourne la catégorie avec le plus grand score, ou None si aucun mot-clé trouvé
    max_score = max(scores.values())
    if max_score == 0:
        return None
    for issue_type, score in scores.items():
        if score == max_score:
            return issue_type

# Exemple d’utilisation rapide
if __name__ == "__main__":
    example_text = "We have a critical error on the Scania truck system, causing failures during startup."
    print("Client détecté:", detect_client(example_text))
    print("Produit détecté:", detect_client_product(example_text))
    print("Type d'incident:", classify_issue_type(example_text))
