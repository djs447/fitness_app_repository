#!/usr/bin/env bash
set -o errexit

poetry install --only main

poetry run python fitness-app/manage.py collectstatic --noinput
