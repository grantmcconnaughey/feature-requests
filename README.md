# Feature Requests

[![Build Status](https://travis-ci.org/grantmcconnaughey/feature-requests.svg?branch=master)](https://travis-ci.org/grantmcconnaughey/feature-requests)
[![Coverage Status](https://coveralls.io/repos/github/grantmcconnaughey/feature-requests/badge.svg?branch=master)](https://coveralls.io/github/grantmcconnaughey/feature-requests?branch=master)

A CRUD application for managing feature requests. Uses Django 1.9 and runs on Python 2.7 or Python 3.4+.

## Features

* A full CRUD application for managing and viewing reature requests.
* Uses Django 1.9.2 and Bootstrap 3
* 100% test coverage

## Open Source

This application uses open source software to run.

* **Django 1.9**
* **Bootstrap 3**
* **django-bootstrap3** — Django utilities for working with Bootstrap 3
* **django-ordered-model** — Django package for rearranging Feature Request's client priority
* **factory-boy** — Used to create model instances for tests
* **coverage** — Adds test coverage tracking

## Running the App

### Installing Dependencies

It's a good idea to create a virtual environment (although that isn't
required). If you're using virtualenvwrapper then run:

    mkvirtualenv feature_requests

Next, install the dependencies from requirements.txt:

    pip install -r requirements.txt

### Migrate the Database

Running migrations will create the SQLite database.

    python manage.py migrate

### Load Fixtures

Next, load the sample data into the database.

    python manage.py loaddata clients product_areas feature_requests

### Run the Server

Finally, run the server and navigate to http://127.0.0.1:8000/ in your browser.

    python manage.py runserver

## Running the Tests

To run the tests, first ensure that you are in the outer feature_request
directory (the one that contains the files `manage.py` and `README.md`). Then
run the following command:

    coverage run manage.py test

To view the test coverage statistics, next run:

    coverage report

## Screenshots

![Feature Requests list](screenshots/list.png)

![Feature Requests detail](screenshots/detail.png)

![Feature Requests create](screenshots/create.png)
