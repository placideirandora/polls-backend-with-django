web: gunicorn polls.wsgi --log-file -
release: python3 manage.py makemigrations --no-input
release: python3 manage.py migrate --no-input