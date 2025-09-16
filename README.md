# Clone repo

- `git clone git@github.com:JoshuaEastman/QuotesAPI.git'

## Setup

- Initial Setup
  - python manage.py migrate
  - python manage.py tailwind install
  - python manage.py tailwind build

- Admin Setup
  - python manage.py createsuperuser

## Post-setup

- Navigate to `localhost:8000/admin` and create some example quotes
- urls for quotes will be:
  - localhost:8000/quotes/v1/random (get a random quote)
  - localhost:8000/quotes/docs (swagger docs)
  - localhost:8000/quotes/demo (demo ui)