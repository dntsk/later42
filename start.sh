#!/bin/sh

./manage.py migrate --noinput
./manage.py collectstatic --noinput
exec gunicorn --bind :8000 --workers 8 --threads 4 later42.wsgi:application
