# Orange County Lettings

> ### ***Avertissement :***
> *Ce projet, y compris ce qui est dans ce README, est un projet scolaire répondant à un scenario 
> fictif et n'a pas d'autres objectifs.*

## Résumé

Refonte du site web d'Orange County Lettings

## Développement local

### Prérequis

- Git CLI
- PostgreSQL installé (et démarré)
- Interpréteur Python, version 3.10 ou supérieure
- Poetry (Doc [here](https://python-poetry.org/docs/) if needed)
- [Optionnel] Un compte Sentry (si besoin en local...).


#### Cloner le repository

Se positionner dans un dossier à votre convenance où cloner le repo puis faire:  
`git clone https://github.com/DayriseA/OCP13_OC-Lettings-FR.git`

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
```psql
CREATE USER <username> WITH PASSWORD '<password>' CREATEDB;
CREATE DATABASE <dbname> OWNER <username>;
```

#### Variables d'environnement / .env

- Créer un fichier .env à la racine de votre projet (soit au même niveau que manage.py)
- Y ajouter les informations nécessaires pour la connexion à votre base PostgreSQL:
  * **DB_NAME**
  * **DB_USER**
  * **DB_PASSWORD**
  * **DB_HOST**
  * **DB_PORT** (Si non défini: 5432 par défaut)
- Si voulu, pour l'integration avec Sentry, la variable **SENTRY_DSN**
- Définir la variable **DEBUG** à True

#### Faire les migrations

Lancer les migrations avec `poetry run python manage.py migrate`

#### Create a superuser

La base est actuellement vide et dans l'état actuel on ne peut rajouter du contenu que via l'interface admin.
Créer donc votre superuser django avec `poetry run python manage.py createsuperuser`

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


## Démarrage rapide (local)