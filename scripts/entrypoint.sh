#!/bin/bash

set -e

echo "Collect static files"
python manage.py collectstatic --noinput

echo "Make database migrations"
python manage.py makemigrations --noinput

echo "Apply database migrations"
python manage.py migrate

#echo "Creating superuser"
#echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', '', 'admin')" | python manage.py shell

if [ $DEBUG = 1 ]
then
  echo "Running Development"
  python manage.py runserver 0.0.0.0:8000
else
  echo "Running Production"
  gunicorn octoincore.asgi:application -k uvicorn.workers.UvicornWorker -b 0.0.0.0:8000
fi
