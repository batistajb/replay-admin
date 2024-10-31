#!/usr/bin/env bash

tail -f /dev/null

pipenv install
pipenv shell
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000