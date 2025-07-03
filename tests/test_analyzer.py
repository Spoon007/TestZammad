import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from analyzers.auto_ticket_analyzer import analyze_incoming_ticket


# test_analyzer.py

test_tickets = [
    {"title": "Problème sur système TÉMÉNOS !", "article": "Crash du ..."},                 # T24
    {"title": "Connexion impossible : app’ M.G.L", "article": "Mobile gestion lague."},                 # MGL
    {"title": "T-Print en panne,", "article": "L’imprimante ne repond plus..."},                        # TPRINT
    {"title": "Bug sur JURIDIQUE", "article": "La solution Juris est injoignable."},                    # JURIS
    {"title": "Scanià"},         # UTINA
]



# Run tests
print("=== Résultats de détection des tickets ===\n")
for i, ticket in enumerate(test_tickets):
    result = analyze_incoming_ticket(ticket)
    print(f"Ticket {i+1}: {result}")




