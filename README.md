# DeePay: Brief Documentation

🐙💻

## Vercel & AWS Setup

(Only For non-shady biz Xd)

## GitHub Actions Setup

Currently broke

## Local Setup

### Development

1. Setup .env file
2. `docker-compose build`
3. `docker-compose up db api -d`
4. `cd ./octoinui/`
5. `npm install`
6. `npm run dev`

### Production

Not production ready yet

## Enivornment Variables

TODO: move .env && .env.example to this repository and integrate through docker

- DEBUG
-

## Useful Commands

- Freeze the requirements:\
  `pip list --format=freeze > requirements.txt`
- Create a superuser:\
  `docker-compose run --rm api python manage.py createsuperuser`
- Make migrations:\
  `docker-compose run --rm api python manage.py makemigrations`
- Load all fixtures:\
  `docker-compose run --rm api python manage.py load-fixtures`

## Example Data

- Default Test User Password: `1234Password`

## TODO

- Fullfill Order life-cycle
  - Orders Overview
  - Order payout after 2 weeks if no objection (celery needed)
- escrow system
  - payins / payouts for account
  - sloow fees (1.5% suggested)
  - view balance
- messaging
  - between users
- Celery Tasks

### Generate Class Overview

1. `pip install django-extensions`
2. Add `django_extensions` to `INSTALLED_APPS` in `settings.py`
3. (Mac OS): `brew install graphviz`
4. `python manage.py graph_models -a --dot -o myapp_models.dot`
5. `dot -Tpng myapp_models.dot -omyapp_models.png`

### Dev

`npm run tailwind-watch`
