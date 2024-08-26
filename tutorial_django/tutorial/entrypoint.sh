#!/bin/sh

python manage.py collectstatic --noinput
python manage.py migrate --noinput

# # !NOT TO BE USED IN PRODUCTION: Create example Super User to test
# echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'admin')" | python manage.py shell

gunicorn tutorial.wsgi:application --bind 0.0.0.0:8000