release: python manage.py migrate
web: gunicorn djangovue.wsgi --log-file -
worker: python manage.py deleteorphanedmedia --noinput
