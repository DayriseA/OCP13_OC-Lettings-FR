##########
Quickstart
##########

Dockerized application
======================

In this section, we will see how to leverage docker-compose to quickly start and try out the application.


Prerequisites
-------------

- Git CLI
- A Sentry account if you want to use it.
- | Docker and Docker Compose installed on your machine.
  | Check the doc `here <https://docs.docker.com/get-docker/>`_ if needed.


Clone the repository
---------------------

| First, clone the repository on your machine:
| ``git clone https://github.com/DayriseA/OCP13_OC-Lettings-FR.git``


Set up environment variables
----------------------------

Create a `.env` file in the project root directory (same level as *manage.py*) and fill it like in 
the example below, replacing the values with yours:

- DJANGO_SECRET_KEY=your_secret_key
- ALLOWED_HOSTS='localhost 127.0.0.1'
- CSRF_TRUSTED_ORIGINS='http://localhost http://127.0.0.1'
- DB_NAME=your_db_name
- DB_USER=your_db_user
- DB_PASSWORD=your_db_password
- SENTRY_DSN=your_sentry_dsn (optional)


Start the application
---------------------

| From the project root directory, run the following command:
| ``docker-compose up -d``

This command will pull the images and start the containers in detached mode.
In your browser you should now be able to access it on http://localhost:8000/


Create a superuser
------------------

The first time you will need to create a superuser to access the admin interface and start creating content.
To do so, run the following command:

``docker-compose exec web python manage.py createsuperuser``

Then follow the instructions. Once done, you can access the admin interface on http://localhost:8000/admin/