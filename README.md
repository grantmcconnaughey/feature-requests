# Feature Requests

[![Build Status](https://travis-ci.org/grantmcconnaughey/feature-requests.svg?branch=master)](https://travis-ci.org/grantmcconnaughey/feature-requests)

[![Coverage Status](https://coveralls.io/repos/github/grantmcconnaughey/feature-requests/badge.svg?branch=master)](https://coveralls.io/github/grantmcconnaughey/feature-requests?branch=master)

## Running the App

### Installing Dependencies

It's a pretty good idea to create a virtual environment (although that isn't
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

## Running the tests

To run the tests, first ensure that you are in the outer feature_request
directory (the one that contains the files `manage.py` and `README.md`). Then
run the following command:

    coverage run manage.py test

To view the test coverage statistics, next run:

    coverage report
