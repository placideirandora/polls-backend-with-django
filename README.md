# POLLS (DJANGO & DJANGO REST)

A Back-End RESTFul API for polling with Django and Django REST Framework

[![CircleCI](https://circleci.com/gh/placiderapson/polls-backend-with-django.svg?style=svg&circle-token=accf70da428315e0f1a0c93f89ecec07d51dd872)](https://app.circleci.com/pipelines/github/placiderapson/polls-backend-with-django)

## GETTING STARTED

### Clone The Project

```
$ git clone https://github.com/placiderapson/polls-backend-with-django
```

### Download, Install, And Setup PostgreSQL

```
# https://www.postgresql.org/download/
```

```
$ Create Database
```

### Configure Environment Variables

```
# Rename the file '.env.sample' to '.env' and Provide your corresponding Credentials
```

### Make And Apply Migrations

```
$ python3 manage.py makemigrations
```

```
$ python3 manage.py migrate
```

### Create A Super User

```
$ python3 manage.py createsuperuser
```

### Start The Server

```
$ navigate to 'http://localhost:8000/' to visit the web app
```

```
$ navigate to 'http://localhost:8000/admin/' and login with the superuser credentials to view the database
```

```
$ use your favorite api testing platform
```

### RUN TESTS

```
$ python3 manage.py test
```
