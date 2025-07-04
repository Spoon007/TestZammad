# /root/zammad_automation/tests/test_t24_routing.py

import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzers.t24_client_routing import analyze_t24_ticket

# Liste des tickets à tester
test_tickets = [
    {
        "title": "BFI - Erreur T24 sur commission client",
        "content": "Problème de calcul de commission sur T24 pour le client BFI. Paramétrage incorrect."
    },
    {
        "title": "Problème de connexion sur Vista",
        "content": "Impossible de se connecter au serveur T24 de Vista. Timeout répété."
    },
    {
        "title": "Incident réseau BNIG",
        "content": "Problème de réseau sur l'infrastructure BNIG. Perte de connexion intermittente."
    },
    {
        "title": "Système T24 Scania indisponible",
        "content": "Le système T24 pour Scania est complètement indisponible depuis ce matin."
    },
    {
        "title": "Urgent: crash sur MGL",
        "content": "Crash système sur MGL, intervention urgente requise."
    },
    {
        "title": "BMCE – Problème de paramétrage",
        "content": "Problème de paramétrage sur T24 pour BMCE. Configuration des comptes incorrecte."
    },
    {
        "title": "BAY - Crash serveur",
        "content": "Crash du serveur T24 pour BAY. CPU surchargé, redémarrage nécessaire."
    },
    {
        "title": "CHAABI - Core banking",
        "content": "Problème sur le core banking de CHAABI. Paramétrage des produits bancaires."
    },
    {
        "title": "UMNIA - Problème réseau",
        "content": "Problème de réseau sur UMNIA. Connexion instable avec timeout fréquents."
    },
    {
        "title": "Problème T24 général",
        "content": "Problème général sur T24. Fonctionnalité de commission ne fonctionne pas."
    },
]

# Exécution des tests
print("\n===== TEST ROUTAGE T24 =====\n")
for i, ticket in enumerate(test_tickets):
    result = analyze_t24_ticket(ticket)
    print(f"Test {i+1}:")
    print(f"  🏢 Client      : {result['client']}")
    print(f"  👨‍💼 Experts     : {', '.join(result['experts']) if result['experts'] else 'Aucun'}")
    print(f"  🧠 Issue Type  : {result['issue_type']}")
    print("-" * 50)

