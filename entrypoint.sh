#!/bin/sh

echo "Applying migrations if any..."
python manage.py migrate

echo "web container ready"

exec "$@"