SHELL := /bin/bash
virtual = .venv/bin/activate

setup:
	clear
	python -m venv .venv
	source $(virtual) && \
	python -m pip install -r requirements.txt && \
	python manage.py makemigrations && \
	python manage.py migrate && \
	python manage.py createsuperuser && \
	python manage.py runserver

setup-docker:
	clear
	docker compose -f 'compose.yaml' up -d --build

dbbackup-create:
	python manage.py dbbackup

dbbackup-list:
	python manage.py listbackups

dbbackup-restore:
	python manage.py dbrestore

clean:
	clear
	rm -rf db.sqlite3
	rm -rf **/migrations
	rm -rf **/__pycache__
	clear

test:
	clear
	python manage.py check

run:
	clear
	python manage.py runserver

PHONY: clean setup test run dbbackup-create dbbackup-list dbbackup-restore