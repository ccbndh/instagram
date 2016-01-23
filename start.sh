#!/bin/bash

# Connect DB
psql -h $DB_HOST -U postgres --command "CREATE USER $DB_USER WITH SUPERUSER PASSWORD '$DB_PWD';"
psql -h $DB_HOST -U postgres --command "ALTER USER $DB_USER CREATEDB;"
output=`psql -h $DB_HOST -U postgres --command "CREATE DATABASE $DB_NAME OWNER=$DB_USER;"`

python manage.py migrate


python manage.py runserver 0.0.0.0:8000