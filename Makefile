setup:
	clear
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver

setup-docker:
	clear
	docker compose -f 'compose.yaml' up -d --build

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

PHONY: clean setup test run