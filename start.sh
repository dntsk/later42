#!/bin/sh

./manage.py migrate --noinput
exec gunicorn --bind :8000 --workers 4 later42.wsgi:application
