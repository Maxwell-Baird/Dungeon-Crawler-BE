## Commands

Reset database: python manage.py dumpdata dungeon.npc

seed database: python manage.py loaddata fixtures/npc.json

start server: python manage.py runserver 8000

## Setup
download python: https://www.python.org/downloads/

create a database in postgres called dungeoncrawler

python3 -m venv env

source env/bin/activate

curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py

python get-pip.py

pip install django

pip install djangorestframework

pip install django-cors-headers

pip install psycopg2-binary

python manage.py makemigration

python manage.py migrate

python manage.py loaddata fixtures/npc.json

python manage.py runserver 8000

## Routes
/api/v1/npcs for all npcs

/api/v1/npcs/1 for a single npc (change the number to get a different npc)

## Running the server commands if you restarted

python3 -m venv env

source env/bin/activate

python manage.py runserver 8000

## Resetting the database
$ python manage.py dumpdata

$ psql -U postgres

postgres=# drop database dungeoncrawler;

postgres=# create database dungeoncrawler;

postgres=# \q

$ python manage.py makemigration

$ python manage.py migrate

$ python manage.py loaddata fixtures/npc.json
