#!/usr/bin/env bash

cd src
python manage.py test --settings=nubocore.settings
pytest --ds=nubocore.settings --durations=0 -p no:warnings