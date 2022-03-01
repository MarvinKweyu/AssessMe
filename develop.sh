#!/bin/bash

# create local environment and install dependencies
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# migrate and add usecase data
python3 manage.py migrate --settings=assessme.settings.dev
python3 manage.py loaddata use_case_data.json --settings=assessme.settings.dev