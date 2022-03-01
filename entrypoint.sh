#!/bin/sh

if ["$DATABASE" = "postgres"]; 
then
    echo "Waiting for Postgres..."
    while !nc -z $SQL_HOST $SQL_PORT; do
        sleep 0.1
    done

    echo "PostgreSQL started"
fi


python manage.py flush --no-input --settings=assessme.settings.dev

# User credentials for admin
user=admin
email=admin@example.com
password=pass

python3 manage.py migrate --settings=assessme.settings.dev
echo "from django.contrib.auth.models import User; User.objects.create_superuser('$user', '$email', '$password')" | python3 manage.py shell --settings=assessme.settings.dev



exec "$@"