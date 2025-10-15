#!/usr/bin/env python3
"""
EBIOS Risk Manager - Command Line Interface
Méthode EBIOS Risk Manager avec ANSSI Club EBIOS
"""

import argparse
import sys


def init_project(args):
    """Initialize a new EBIOS Risk Manager project"""
    print(f"Initialisation d'un nouveau projet EBIOS: {args.name}")
    print("Création de la structure de projet...")
    # TODO: Create project structure


def workshop1(args):
    """Workshop 1: Scoping and security baseline"""
    print("Atelier 1: Cadrage et socle de sécurité")
    print("- Définir le périmètre de l'étude")
    print("- Identifier les biens supports et les biens essentiels")
    print("- Établir le socle de sécurité")


def workshop2(args):
    """Workshop 2: Risk origins"""
    print("Atelier 2: Sources de risque")
    print("- Identifier les parties prenantes")
    print("- Identifier les sources de risque")
    print("- Cartographier l'écosystème")


def workshop3(args):
    """Workshop 3: Strategic scenarios"""
    print("Atelier 3: Scénarios stratégiques")
    print("- Construire les scénarios stratégiques")
    print("- Évaluer la gravité")
    print("- Prioriser les scénarios")


def workshop4(args):
    """Workshop 4: Operational scenarios"""
    print("Atelier 4: Scénarios opérationnels")
    print("- Construire les scénarios opérationnels")
    print("- Évaluer la vraisemblance")
    print("- Calculer les risques")


def workshop5(args):
    """Workshop 5: Risk treatment"""
    print("Atelier 5: Traitement des risques")
    print("- Définir la stratégie de traitement")
    print("- Identifier les mesures de sécurité")
    print("- Planifier la mise en œuvre")


def list_commands(args):
    """List all available commands"""
    print("Commandes disponibles:")
    print("  init        - Initialiser un nouveau projet EBIOS")
    print("  atelier1    - Atelier 1: Cadrage et socle de sécurité")
    print("  atelier2    - Atelier 2: Sources de risque")
    print("  atelier3    - Atelier 3: Scénarios stratégiques")
    print("  atelier4    - Atelier 4: Scénarios opérationnels")
    print("  atelier5    - Atelier 5: Traitement des risques")
    print("  help        - Afficher cette aide")


def main():
    """Main entry point for the EBIOS Risk Manager CLI"""
    parser = argparse.ArgumentParser(
        description="EBIOS Risk Manager - Méthode ANSSI Club EBIOS",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemples:
  ebios.py init mon-projet
  ebios.py atelier1
  ebios.py atelier2
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Commandes disponibles')
    
    # Init command
    parser_init = subparsers.add_parser('init', help='Initialiser un nouveau projet EBIOS')
    parser_init.add_argument('name', help='Nom du projet')
    parser_init.set_defaults(func=init_project)
    
    # Workshop 1
    parser_w1 = subparsers.add_parser('atelier1', help='Atelier 1: Cadrage et socle de sécurité')
    parser_w1.set_defaults(func=workshop1)
    
    # Workshop 2
    parser_w2 = subparsers.add_parser('atelier2', help='Atelier 2: Sources de risque')
    parser_w2.set_defaults(func=workshop2)
    
    # Workshop 3
    parser_w3 = subparsers.add_parser('atelier3', help='Atelier 3: Scénarios stratégiques')
    parser_w3.set_defaults(func=workshop3)
    
    # Workshop 4
    parser_w4 = subparsers.add_parser('atelier4', help='Atelier 4: Scénarios opérationnels')
    parser_w4.set_defaults(func=workshop4)
    
    # Workshop 5
    parser_w5 = subparsers.add_parser('atelier5', help='Atelier 5: Traitement des risques')
    parser_w5.set_defaults(func=workshop5)
    
    # Help command
    parser_help = subparsers.add_parser('help', help='Afficher l\'aide')
    parser_help.set_defaults(func=list_commands)
    
    args = parser.parse_args()
    
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
