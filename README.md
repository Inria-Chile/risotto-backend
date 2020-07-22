# RISOTTO's backend server

This repository hosts the code that runs RISOTTO's backend server.
RISOTTO stands for Research Intelligent Support and Organization TOol against COVID-19 and aims to support COVID-19 research.
More information is available at RISOTTO's homepage: https://inria-chile.github.io/risotto/.

## How to run locally

We provide a dockerized local development environment.
In order to launch it, run the following commands:

```bash
$ docker-compose -f docker/docker-compose-dev.yml up
```

## How to test

The unit test suite is executed by the following command:

```bash
$ docker-compose -f docker/docker-compose-dev.yml run --rm risotto-backend pytest
```

## Backend architecture

The backend is built on Python using the following libraries:

- Flask: https://flask.palletsprojects.com/en/1.1.x/
- Flask-SQLAlchemy: https://flask-sqlalchemy.palletsprojects.com/en/2.x/
- Flask-Migrate: https://flask-migrate.readthedocs.io/en/latest/

Even though currently the database and migrations libraries aren't being used, they are ready to be integrated uncommenting a few lines in `risotto/__init__.py`.