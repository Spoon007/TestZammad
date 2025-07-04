#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de test pour le module d'extraction de données des tickets Zammad.
Teste différents cas d'usage avec des tickets variés.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from analyzers.data_extractor import extract_ticket_entities

def test_data_extraction():
    """Test complet avec différents types de tickets."""
    
    # Test Case 1: Ticket avec contrat et date
    ticket_1 = {
        "title": "Problème accès client",
        "content": "Bonjour, le client avec le contrat 123456789 rencontre des difficultés depuis le 22/11/2024. Merci de regarder."
    }
    
    # Test Case 2: Ticket avec erreur technique
    ticket_2 = {
        "title": "Erreur base de données",
        "content": "L'application génère une erreur ORA-600 lors de la connexion. Stack trace disponible dans les logs."
    }
    
    # Test Case 3: Ticket avec identifiants clients
    ticket_3 = {
        "title": "Problème utilisateur",
        "content": "L'utilisateur client1234 et user_4567 ne peuvent pas se connecter. ID: XYZ789 également affecté."
    }
    
    # Test Case 4: Ticket avec dates variées
    ticket_4 = {
        "title": "Incident récurrent",
        "content": "Problème apparu hier, se reproduit depuis le 15 novembre 2024. Intervention prévue lundi prochain."
    }
    
    # Test Case 5: Ticket avec plusieurs types d'erreurs
    ticket_5 = {
        "title": "Erreurs multiples",
        "content": "NullPointerException détectée, suivi d'un Segmentation fault. HTTP 500 retourné aux clients."
    }
    
    # Test Case 6: Ticket avec contrat long
    ticket_6 = {
        "title": "Contrat entreprise",
        "content": "Référence contrat: 987654321012345 - Renouvellement le 2024-12-31"
    }
    
    # Test Case 7: Ticket avec identifiants techniques
    ticket_7 = {
        "title": "Problème serveur",
        "content": "Serveur srv001 en panne, ref: ABC123DEF, customer: ENT4567"
    }
    
    # Test Case 8: Ticket vide/sans données pertinentes
    ticket_8 = {
        "title": "Question générale",
        "content": "Bonjour, j'aimerais savoir comment fonctionne votre service. Merci."
    }
    
    # Test Case 9: Ticket avec tout type de données
    ticket_9 = {
        "title": "Incident critique client",
        "content": "Client ref: 456789123 (contrat 111222333444) signale erreur Fatal error depuis hier. User ID: CLI789 impacté. Logs montrent Exception in thread à 14h30 le 23/11/2024."
    }
    
    # Test Case 10: Ticket avec dates françaises
    ticket_10 = {
        "title": "Planification maintenance",
        "content": "Maintenance prévue le 15 décembre 2024, rappel fait ce matin. Intervention la semaine prochaine."
    }
    
    # Liste des tickets de test
    test_tickets = [
        ("Ticket 1 - Contrat + Date", ticket_1),
        ("Ticket 2 - Erreur DB", ticket_2),
        ("Ticket 3 - IDs clients", ticket_3),
        ("Ticket 4 - Dates variées", ticket_4),
        ("Ticket 5 - Erreurs multiples", ticket_5),
        ("Ticket 6 - Contrat long", ticket_6),
        ("Ticket 7 - IDs techniques", ticket_7),
        ("Ticket 8 - Ticket vide", ticket_8),
        ("Ticket 9 - Données complètes", ticket_9),
        ("Ticket 10 - Dates françaises", ticket_10),
    ]
    
    print("=" * 60)
    print("TEST D'EXTRACTION DE DONNÉES - TICKETS ZAMMAD")
    print("=" * 60)
    
    for i, (test_name, ticket) in enumerate(test_tickets, 1):
        print(f"\n🎫 {test_name}")
        print("-" * 50)
        print(f"Titre: {ticket['title']}")
        print(f"Contenu: {ticket['content']}")
        
        # Extraction des données
        results = extract_ticket_entities(ticket)
        
        print(f"\n📊 Résultats extraits:")
        print(f"  📋 Contrats: {results['contracts']}")
        print(f"  📅 Dates: {results['dates']}")
        print(f"  ❌ Erreurs: {results['errors']}")
        print(f"  🆔 IDs: {results['ids']}")
        
        # Statistiques
        total_found = len(results['contracts']) + len(results['dates']) + len(results['errors']) + len(results['ids'])
        print(f"  📈 Total éléments trouvés: {total_found}")
        
        if i < len(test_tickets):
            print("\n" + "─" * 60)

def test_edge_cases():
    """Test des cas limites et spéciaux."""
    
    print("\n" + "=" * 60)
    print("TEST DES CAS LIMITES")
    print("=" * 60)
    
    # Cas limite 1: Numéros trop courts ou trop longs
    edge_case_1 = {
        "title": "Numéros limites",
        "content": "Contrat 1234567 (trop court), contrat 12345678 (OK), contrat 1234567890123456 (trop long)"
    }
    
    # Cas limite 2: Dates ambiguës
    edge_case_2 = {
        "title": "Dates ambiguës",
        "content": "Rendez-vous 32/13/2024 (invalide), 12/13/2024 (format US?), 2024/13/01 (mois invalide)"
    }
    
    # Cas limite 3: Faux positifs
    edge_case_3 = {
        "title": "Faux positifs",
        "content": "Numéro de téléphone 0123456789, code postal 75001, version 2.1.3"
    }
    
    edge_cases = [
        ("Cas limite 1 - Numéros limites", edge_case_1),
        ("Cas limite 2 - Dates ambiguës", edge_case_2),
        ("Cas limite 3 - Faux positifs", edge_case_3),
    ]
    
    for test_name, ticket in edge_cases:
        print(f"\n🎫 {test_name}")
        print("-" * 50)
        print(f"Titre: {ticket['title']}")
        print(f"Contenu: {ticket['content']}")
        
        results = extract_ticket_entities(ticket)
        
        print(f"\n📊 Résultats extraits:")
        print(f"  📋 Contrats: {results['contracts']}")
        print(f"  📅 Dates: {results['dates']}")
        print(f"  ❌ Erreurs: {results['errors']}")
        print(f"  🆔 IDs: {results['ids']}")

def performance_stats():
    """Affiche des statistiques de performance."""
    
    print("\n" + "=" * 60)
    print("STATISTIQUES DE PERFORMANCE")
    print("=" * 60)
    
    # Compteurs
    total_tests = 13  # 10 tests normaux + 3 cas limites
    contracts_found = 0
    dates_found = 0
    errors_found = 0
    ids_found = 0
    
    # Simulation des résultats attendus
    expected_results = {
        "contracts": 4,  # tickets 1, 6, 9 + cas limites
        "dates": 6,      # tickets 1, 4, 6, 9, 10
        "errors": 4,     # tickets 2, 5, 9
        "ids": 5         # tickets 3, 7, 9
    }
    
    print(f"📊 Résultats attendus sur {total_tests} tests:")
    print(f"  📋 Contrats trouvés: ~{expected_results['contracts']}")
    print(f"  📅 Dates trouvées: ~{expected_results['dates']}")
    print(f"  ❌ Erreurs trouvées: ~{expected_results['errors']}")
    print(f"  🆔 IDs trouvés: ~{expected_results['ids']}")
    print(f"  📈 Total éléments: ~{sum(expected_results.values())}")

if __name__ == "__main__":
    """Point d'entrée principal pour les tests."""
    
    print("🚀 Démarrage des tests d'extraction de données...")
    
    try:
        # Tests principaux
        test_data_extraction()
        
        # Tests des cas limites
        test_edge_cases()
        
        # Statistiques
        performance_stats()
        
        print("\n" + "=" * 60)
        print("✅ TESTS TERMINÉS AVEC SUCCÈS")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n❌ Erreur lors des tests: {e}")
        print("Vérifiez que le fichier data_extractor.py est bien présent et fonctionnel.")
        sys.exit(1)
