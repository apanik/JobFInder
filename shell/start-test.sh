#!/usr/bin/env bash
source venv/bin/activate
export DJANGO_SETTINGS_MODULE="p7.settings_test"
python manage.py migrate
python manage.py runserver 127.0.0.1:8000

