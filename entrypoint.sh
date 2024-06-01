#!/bin/sh

echo "Applying migrations if any..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --no-input

gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000

exec "$@"