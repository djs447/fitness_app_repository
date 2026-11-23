#!/usr/bin/env bash
set -o errexit

pip install poetry==2.4.1

poetry install --only main

poetry run python fitness-app/manage.py collectstatic --noinput

poetry run python fitness-app/manage.py migrate

if [ -n "$DJANGO_SUPERUSER_USERNAME" ]; then
  poetry run python fitness-app/manage.py createsuperuser --noinput || true
fi
