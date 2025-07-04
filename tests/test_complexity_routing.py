# /root/zammad_automation/tests/test_complexity_routing.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzers.auto_ticket_analyzer import analyze_incoming_ticket
from analyzers.data_extractor import extract_ticket_entities
from analyzers.complexity_and_routing import assign_specialist, estimate_complexity

sample_tickets = [
    {
        "title": "Question générale",
        "content": "Bonjour, j'aimerais savoir comment accéder à mon compte. Merci."
    },
    {
        "title": "Erreur critique T24",
        "content": "Erreur ORA-600 sur T24 avec le contrat 123456789. Système bloqué depuis ce matin."
    },
    {
        "title": "URGENT - Incident MGL",
        "content": "Incident critique sur MGL, tous les utilisateurs sont bloqués. Intervention immédiate requise."
    },
    {
        "title": "Problème récurrent FIRES",
        "content": "Problème apparu le 15/11/2024, récurrence le 22/11/2024. FIRES lent depuis hier."
    },
    {
        "title": "Problème urgent non identifié",
        "content": "Urgent: système en panne, erreur inconnue, plusieurs clients impactés."
    },
    {
        "title": "Problème UTINA",
        "content": "UTINA génère des timeouts, client_4567 affecté, référence contrat 987654321."
    },
    {
        "title": "Erreur CIP",
        "content": "CIP retourne HTTP 500, NullPointerException dans les logs, ID: XYZ789"
    },
    {
        "title": "Question MGL",
        "content": "Comment configurer MGL pour un nouveau client ?"
    },
    {
        "title": "Incidents multiples T24",
        "content": "T24 présente Fatal error, Exception in thread, et Segmentation fault. Contrat 111222333, user_001 impacté."
    },
    {
        "title": "Maintenance FIRES",
        "content": "Maintenance FIRES prévue demain, 3 contrats à migrer: 444555666, 777888999, 123123123."
    },
    {
        "title": "Production arrêtée",
        "content": "Production complètement arrêtée, perte de données possible, escalade immédiate nécessaire."
    },
    {
        "title": "Information CIP",
        "content": "CIP fonctionne normalement, juste une question sur la documentation."
    }
]

print("\n===== TEST ATTRIBUTION & COMPLEXITÉ =====\n")

for i, ticket in enumerate(sample_tickets):
    product_result = analyze_incoming_ticket(ticket)
    product = product_result["product"] if isinstance(product_result, dict) else product_result
    entities = extract_ticket_entities(ticket)
    expert = assign_specialist(product)
    complexity = estimate_complexity({**ticket, **entities})

    print(f"Test {i+1}:")
    print(f"  🛠 Produit détecté : {product}")
    print(f"  👨‍💻 Expert assigné  : {expert}")
    print(f"  📊 Complexité      : {complexity}")
    print("-" * 50)



