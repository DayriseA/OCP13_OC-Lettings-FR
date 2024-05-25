#!/bin/sh

echo "Applying migrations if any..."
python manage.py migrate

echo "Collecting static files..."
python manage.py collectstatic --no-input --clear

echo "web container ready"

exec "$@"