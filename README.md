# password-dictionary-generator

**Générateur de dictionnaire de mots de passe personnalisés**  
Ce script Python crée un fichier `dictionnaire.txt` contenant une liste de mots de passe de longueur exacte, basés sur des données personnelles et des caractères aléatoires (chiffres, symboles, majuscules).

## 🚀 Fonctionnalités

- Collecte d’informations personnelles : prénom, nom, date de naissance, ville, mot-clé.
- Génération de mots de passe d’une **longueur exactement spécifiée**.
- Possibilité que chaque mot de passe ait (ou non) des majuscules aléatoires.
- Ajout de chiffres et de symboles pour renforcer la robustesse.
- Écriture automatique du résultat dans `dictionnaire.txt`.

## 🛠️ Prérequis

- Python 3.6+
- Module standard `random`
- (Optionnel) un environnement virtuel (venv, conda…)

## 💾 Installation

1. Clone ce repository :
    ```bash
    git clone https://github.com/kevindeffo/password-dictionary-generator.git
    cd password-dictionary-generator
    ```

2. (Optionnel) Crée et active un environnement virtuel :
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Pas de dépendances externes à installer, tout est dans la bibliothèque standard.

## ▶️ Utilisation

Lance le script et suis les instructions :

```bash
python3 generate-password-dict.py
