import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzers.auto_ticket_analyzer import analyze_incoming_ticket

test_tickets = [
    {
        "title": "Erreur ORA-00600 dans Temenos",
        "article": "Le système core banking T24 ne répond plus depuis ce matin. Contrat : 010011001234567"
    },
    {
        "title": "Demande info",
        "article": "Le client parle d’un problème général avec le système de paiement"
    },
    {
        "title": "",
        "article": "Merci de vérifier"
    },
    {
        "title": "Crash dans la caisse principale",
        "article": "Bug détecté dans tdc et impression bloquée sur tprint. Contrat: 12345678901234567890"
    },
    {
        "title": "FIRESYS down",
        "article": "incident sur fire system. erreur ORA-00001 détectée dans Fires."
    }
]

print("=== TESTS AVEC SCORE DE CONFIANCE ===\n")
for i, ticket in enumerate(test_tickets):
    result = analyze_incoming_ticket(ticket)
    print(f"🎫 Ticket {i+1}")
    print(f"Produit détecté     : {result['product']}")
    print(f"Score               : {result['score']}")
    print(f"Niveau de confiance : {result['confidence']}")
    print(f"Mots-clés détectés  : {result['matched_keywords']}")
    print(f"Erreurs trouvées    : {result['errors']}")
    print(f"Contrats détectés   : {result['contract_ids']}")
    print("-" * 60)

