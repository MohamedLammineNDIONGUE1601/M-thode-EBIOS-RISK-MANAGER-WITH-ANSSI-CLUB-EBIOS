# Méthode EBIOS Risk Manager avec ANSSI Club EBIOS

Outil en ligne de commande pour gérer les analyses de risques selon la méthode EBIOS Risk Manager de l'ANSSI.

## Description

EBIOS Risk Manager est une méthode d'appréciation et de traitement des risques numériques publiée par l'ANSSI (Agence Nationale de la Sécurité des Systèmes d'Information). Cette méthode est composée de 5 ateliers :

1. **Atelier 1** : Cadrage et socle de sécurité
2. **Atelier 2** : Sources de risque
3. **Atelier 3** : Scénarios stratégiques
4. **Atelier 4** : Scénarios opérationnels
5. **Atelier 5** : Traitement des risques

## Installation

Cloner le dépôt :
```bash
git clone https://github.com/MohamedLammineNDIONGUE1601/M-thode-EBIOS-RISK-MANAGER-WITH-ANSSI-CLUB-EBIOS.git
cd M-thode-EBIOS-RISK-MANAGER-WITH-ANSSI-CLUB-EBIOS
```

## Utilisation

### Commandes disponibles

```bash
# Afficher l'aide
python3 ebios.py --help

# Initialiser un nouveau projet
python3 ebios.py init mon-projet

# Exécuter les ateliers
python3 ebios.py atelier1  # Cadrage et socle de sécurité
python3 ebios.py atelier2  # Sources de risque
python3 ebios.py atelier3  # Scénarios stratégiques
python3 ebios.py atelier4  # Scénarios opérationnels
python3 ebios.py atelier5  # Traitement des risques

# Afficher la liste des commandes
python3 ebios.py help
```

### Exemples

Initialiser un nouveau projet :
```bash
python3 ebios.py init mon-analyse-de-risques
```

Démarrer l'atelier 1 :
```bash
python3 ebios.py atelier1
```

## Les 5 Ateliers EBIOS Risk Manager

### Atelier 1 : Cadrage et socle de sécurité
- Définir le périmètre de l'étude
- Identifier les biens supports et les biens essentiels
- Établir le socle de sécurité

### Atelier 2 : Sources de risque
- Identifier les parties prenantes
- Identifier les sources de risque
- Cartographier l'écosystème

### Atelier 3 : Scénarios stratégiques
- Construire les scénarios stratégiques
- Évaluer la gravité
- Prioriser les scénarios

### Atelier 4 : Scénarios opérationnels
- Construire les scénarios opérationnels
- Évaluer la vraisemblance
- Calculer les risques

### Atelier 5 : Traitement des risques
- Définir la stratégie de traitement
- Identifier les mesures de sécurité
- Planifier la mise en œuvre

## Références

- [Guide EBIOS Risk Manager - ANSSI](https://www.ssi.gouv.fr/guide/ebios-risk-manager-the-method/)
- [Club EBIOS](https://www.ssi.gouv.fr/actualite/club-ebios-rejoignez-la-communaute-des-utilisateurs-de-la-methode/)

## Licence

Ce projet est un outil d'accompagnement pour la méthode EBIOS Risk Manager.