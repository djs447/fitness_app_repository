poetry install --only main
python manage.py collectstatic --noinput
python manage.py migrate
