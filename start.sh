#!/usr/bin/env bash

echo "Install requirements"
pipenv install

echo "Activate virtual environment"
source $(pipenv --venv)/bin/activate

echo "Make migrations and migrate"
python manage.py makemigrations
python manage.py migrate

echo "Run server"
python manage.py runserver 0.0.0.0:8000