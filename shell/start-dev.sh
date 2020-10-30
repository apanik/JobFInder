#!/usr/bin/env bash
source venv/bin/activate
pip install -r requirements/req-dev.txt
export DJANGO_SETTINGS_MODULE="p7.settings_dev"
python manage.py migrate
cat <<EOF | python manage.py shell
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
   user = User.objects.create_superuser('admin','admin@example.com', '123')
   user.first_name = 'Admin'
   user.save()
EOF
echo ----------------------------------------------------
echo Run the following to run the worker
echo export DJANGO_SETTINGS_MODULE="p7.settings_dev"
echo python manage.py rqworker
echo ----------------------------------------------------
python manage.py runserver 0:8080
