#!/usr/bin/env bash
cd /var/p7/
source venv/bin/activate
export DJANGO_SETTINGS_MODULE="p7.settings_prod"
#python manage.py runserver 0:8080 > projectseven.log
python manage.py runserver 127.0.0.1:8000

