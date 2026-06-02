setup:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py createsuperuser
	python manage.py runserver

clean:
	rm -rf db.sqlite3
	rm -rf **/migrations
	rm -rf **/__pycache__
	clear

test:
	python manage.py check

run:
	python manage.py runserver

PHONY: clean setup test run