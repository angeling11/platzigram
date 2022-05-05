# Platzigram

Django project developed during django's course at platzi.
This is the app developed with some changes and improvements made by me. The most important was to dockerize the application:

- Development environment.
- Production environment with multi-stage builds.

## Development environment

*To start the project for development purposes:*

```bash
docker-compose up -d --build
```

*To stop the project for development purposes:*

```bash
docker-compose down -v
```

## Production environment

*To start the project on production:*

```bash
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

*To stop the project in production environment:*

```bash
docker-compose -f docker-compose.prod.yml down -v
```

### Reuse volumes

*To start the project:*

```bash
docker-compose -f docker-compose.prod.yml -p proj1 up -d --build
docker-compose -f docker-compose.prod.yml -p proj1 exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml -p proj1 exec web python manage.py collectstatic --no-input --clear
```

*To stop the project:*

```bash
docker-compose -f docker-compose.prod.yml -p proj1 down
```

### Troubleshooting

```bash
docker-compose [-f docker-compose.prod.yml] logs -f
```

## TODO

- Configure non-root users for the db and nginx server.
- Change default style for the sign up view.
- Verify the required fields for a user to see the feed.
- Implement a pipeline for automatic CI/CD after a change.

## Author

natryvat

## Gratitude

Thanks to Michael Herman for his [blog](https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/) to dockerize the django application with postgres, gunicorn and nginx. It help me a lot to understand and setup the applications in the right way.
