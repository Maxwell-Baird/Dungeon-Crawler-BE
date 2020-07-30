## Summary

A RESTful API that is a part of the Untitled Dungeon Crawler project. This API has two endpoints which return either a single NPC(non-player character) or all the NPCs. The NPC model has full CRUD (Create, Read, Update, Delete) implemented.

link to the API production site: https://whispering-temple-46123.herokuapp.com/api/v1/npcs

link to the Front-end Repo: https://github.com/Maxwell-Baird/Dungeon-Crawler

Link to the game: http://untitled-dungeon-crawler.herokuapp.com/

## Contributors

Maxwell Baird, Ruby Rinken, Justin Corbin, Trond Makonese, DeMarcus Kirby

## Setup

To setup the project you will need to have python 3.8, get-pip, and postgresql installed. After installing those apps you will pull down this repo. Then you will need to create a database callled dungeoncrawler using the username postgres. You will then need to follow the following commands:

$python3 -m venv env

$source env/bin/activa

$python get-pip.py

$pip install django

$pip install djangorestframework

$pip install django-cors-headers

$pip install psycopg2-binary

$python manage.py makemigration

$python manage.py migrate

$python manage.py loaddata fixtures/npc.json

To run the server use the following command:

$python manage.py runserver 8000

This will open the app at localhost:8000 where you can test the endpoints


## Endpoints
GET /api/v1/npcs This endpoint will return all NPCs inside the database

POST /api/v1/npcs This endpoint allows the user to create a new NPC which will then be added to the database. The data will be sent through the body as a JSON object.

DELETE /api/v1/npcs This endpoint will remove all NPCs from the database.

GET /api/v1/npcs/{id} This endpoint will return a single NPC based off the id given in the header.

PUT /api/v1/npcs/{id} This endpoint will update a single NPC attributes. The data that will replace the attributes will be sent through the body as a JSON object. At the moment there is bug which requires the PUT to must have the dialogue and options also sent in order for the update to happen.

DELETE /api/v1/npcs/{id} This endpoint will delete a NPC based off the id that was sent through the header.

## Commands

Reset database: $python manage.py dumpdata dungeon.npc

Seed database: $python manage.py loaddata fixtures/npc.json

Start server: $python manage.py runserver 8000

Run test: $python manage.py test

## Create the DATABASE
$ psql -U postgresq

postgres=# CREATE DATABASE dungeoncrawler;

postgres=# \q
