#!/bin/sh

sed -i "s/sqlalchemy\.url.*/sqlalchemy.url = postgresql:\/\/statistics:$DB_PASSWORD@$DB_HOST:5432\/statistics/" statistics/config/alembic.ini

echo Waiting for postgresql  $DB_HOST:5432 ...
elapsed=0

while ! nc -z $DB_HOST 5432 2>/dev/null
do
    elapsed=$(( elapsed + 1))
    if [ "$elapsed" -gt 90 ]
    then
        echo "TIMED OUT !"
        exit 1
    fi
    sleep 1;
done

echo "POSTGRES READY !"

cd statistics/config
alembic -c alembic.ini upgrade head
cd ../..
flask run --host=0.0.0.0 --port=80
