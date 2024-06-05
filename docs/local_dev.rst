###############
LOCAL DEV SETUP
###############

Installation (local dev)
========================

This section describes what you need to run the application locally as a developer.
If you just want to run the application and try it you can rather go to the 
:doc:`Quickstart <quickstart>` section.


Prerequisites
-------------

- Git CLI
- Python 3.10 or higher
- PostgreSQL installed and running
- Poetry (pipx installation recommended to keep it isolated). 
  Poetry doc `here <https://python-poetry.org/docs/#installation>`_ if needed
- A Sentry account (optional) if you want to use Sentry in your local setup


Install dependencies
--------------------

1. Clone the repository:
``git clone https://github.com/DayriseA/OCP13_OC-Lettings-FR.git``

2. Go to the project directory

3. [Optional] If you want your virtual environment to be in the project directory, you can either:
    - Tell Poetry to do so (see `here <https://python-poetry.org/docs/configuration/#virtualenvsin-project>`_)
    - Use ``python -m venv .venv`` beforehand and Poetry will automatically recognize and use it.

4. Install the dependencies with ``poetry install``


Database setup
--------------

Considering you have PostgreSQL installed and running, we will now create a database and a user 
for the application. We will use *psql* here because it is universal, but feel free to use any other tool 
like the bash *createuser* utility or *pgAdmin* if you prefer.

As an admin user, run the following commands:

.. code-block:: sql

    CREATE USER <username> WITH PASSWORD '<password>' CREATEDB;
    CREATE DATABASE <dbname> OWNER <username>;

*(The CREATEDB option here is necessary if you want to run the tests.)*


Set necessary environment variables
-----------------------------------

Create a `.env` file in the project root directory (same level as *manage.py*) and fill it like in 
the example below, replacing the values with yours:

- DEBUG=True
- DJANGO_SECRET_KEY=your_secret_key
- DB_NAME=your_db_name
- DB_USER=your_db_user
- DB_PASSWORD=your_db_password
- DB_HOST=localhost
- DB_PORT=5432 (default port, not needed if you use this one)
- SENTRY_DSN=your_sentry_dsn (optional)


Run the migrations
------------------

.. note::
    In the following sections of this *local dev setup* documentation, we assume all commands are run with 
    your virtual environment activated. So if you are not in it, activate it with ``poetry shell`` or you 
    can also prefix the commands with ``poetry run``.
    
Run the migrations with ``python manage.py migrate``

Create a superuser (if needed)
------------------------------

To create a superuser, just run ``python manage.py createsuperuser`` and follow the instructions.

*The database is currently empty and for now content can only be added through the admin interface.
So you need a superuser if you want to add content and see how the application works.
But I don't know, if you just want to run the tests, you don't need it.*


Run the application
-------------------

Run the application with ``python manage.py runserver``. 
In your browser you should now be able to see it on http://localhost:8000/


Linting and testing
-------------------

* To run the linter, just use ``flake8`` command.
* To run the tests, use ``pytest`` command.
* | To see the coverage, use ``pytest --cov=.`` command. 
  | Option ``--cov-report=html`` will generate an html report in an *htmlcov* directory.


Logs and errors
---------------

| Logs are stored in the *logs* directory at the root of the project.
| In addition to standard logs, if you have set up Sentry, you will see errors there as well.