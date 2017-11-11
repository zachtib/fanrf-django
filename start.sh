#!/usr/bin/env bash

pip3 install -r requirements.txt

export ALLOWED_HOSTS=orangepizero
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8000