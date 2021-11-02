# Platzigram

Django course on platzi.
This is the app developed with some changes made by me.

## Development environment

```bash
docker-compose up -d --build
```

## Production environment

```bash
docker-compose -f docker-compose.prod.yml up -d --build
docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput
docker-compose -f docker-compose.prod.yml exec web python manage.py collectstatic --no-input --clear
```

### Troubleshooting

```bash
docker-compose -f docker-compose.prod.yml logs -f
```
