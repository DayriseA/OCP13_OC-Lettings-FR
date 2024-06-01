#!/bin/sh

echo "Applying migrations if any..."
python manage.py migrate

# Create superuser if no users exist (first run). This is added as a workaround as render free tier does 
# not allow ssh or shell access. Password is retrieved from environment variable to be set in render.
python manage.py initadmin

echo "Collecting static files..."
python manage.py collectstatic --no-input

gunicorn oc_lettings_site.wsgi:application --bind 0.0.0.0:8000

exec "$@"