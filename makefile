run:
	python manage.py runserver 0.0.0.0:80
start-postgres:
	docker run -d --rm --name postgres -e POSTGRES_USER=${DATABASE_USERNAME} -p 5432:5432 -e POSTGRES_PASSWORD=${DATABASE_PASSWORD}  -e POSTGRES_DB=${DATABASE_NAME} -e PGDATA=/var/lib/postgresql/data/pgdata -v caroption_django:/var/lib/postgresql/data postgres:17.11

stop-postgres:
	docker stop postgres
