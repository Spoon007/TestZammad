
import sys
import os

# Ajoute le dossier racine du projet au PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from resolvers.auto_resolver import resolve_ticket

def test_resolve_tickets():
    tickets = [
        {
            "title": "Erreur ORA-600 sur T24",
            "article": "Client BFI avec contrat 12345678, date 22/11/2024."
        },
        {
            "title": "Panne moteur utina",
            "article": "Le camion Utina ne démarre plus, urgent."
        },
        {
            "title": "Maintenance PAOMA lente",
            "article": "Demande de maintenance sur équipement KOBBY."
        },
        {
            "title": "Problème réseau interne",
            "article": "Connexion lente sur toute la société."
        },
        {
            "title": "Ticket inconnu",
            "article": "Informations insuffisantes."
        },
    ]

    for i, ticket in enumerate(tickets, 1):
        print(f"\n--- Ticket #{i} ---")
        res = resolve_ticket(ticket)
        for k, v in res.items():
            print(f"{k}: {v}")

if __name__ == "__main__":
    test_resolve_tickets()
