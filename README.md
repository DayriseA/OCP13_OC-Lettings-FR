# Orange County Lettings

> ### ***Avertissement :***
> *Ce projet, y compris ce qui est dans ce README, est un projet scolaire répondant à un scenario 
> fictif et n'a pas d'autres objectifs.*

## Résumé

Refonte du site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- PostgreSQL
- Interpréteur Python, version 3.10 ou supérieure
- Poetry
- Un compte Sentry

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).


#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/DayriseA/OCP13_OC-Lettings-FR.git`

#### Dépendances et environnement virtuel

- `python -m venv .venv` (optionnel: si vous voulez que l'environnement virtuel soit dans le même dossier)
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- `poetry install`
- Activer l'environnement virtuel: `poetry shell`
- Confirmer que la version de l'interpréteur Python est la version 3.10 ou supérieure: `python --version`
- Pour quitter le shell poetry: `exit`

#### Base de données

Créer une base de donnée pour l'application et un utilisateur qui en aura les droits.  
Si vous souhaiter exécuter les tests, l'utilisateur devra aussi avoir le droit de créer des tables.

#### Variables d'environnement / .env

- Créer un fichier .env à la racine de votre projet (soit au même niveau que manage.py)
- Y ajouter les informations nécessaires pour la connexion à votre base PostgreSQL:
  * *DB_NAME*
  * *DB_USER*
  * *DB_PASSWORD*
  * *DB_HOST*
  * *DB_PORT*
- Y ajouter aussi votre DSN pour l'integration avec Sentry via la variable *OCL_SENTRY_DSN*
- La variable *DEBUG* (True ou False) permet de contrôler si Django se lancera en mode debug ou non.

#### Exécuter le site

- `poetry shell`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `poetry run flake8`

#### Tests and coverage

- `poetry run pytest` pour lancer les tests.
- `pytest --cov=.` pour voir la couverture de tests. Option `--cov-report html` pour générer un rapport html.

#### Logs

Les fichiers de logs générés par la configuration de logging seront placés dans un dossier *'logs'* 
à la racine du projet.

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

