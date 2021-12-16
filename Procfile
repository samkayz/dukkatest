release: python manage.py makemigrations
release: python manage.py migrate
web: gunicorn dukka.wsgi --log-file -