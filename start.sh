#!/usr/bin/env bash

echo "Install requirements"
pipenv install

echo "Activate virtual environment"
source $(pipenv --venv)/bin/activate

pip install python-dotenv

#pip install boto3 django-storages

echo "Make migrations and migrate"
python manage.py makemigrations
python manage.py migrate

echo "Run server"
python manage.py runserver 0.0.0.0:8000