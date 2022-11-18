# Later42

[![Maintained](https://img.shields.io/badge/maintained%20by-dntsk.dev-blue.svg)](https://dntsk.dev/) ![License](https://img.shields.io/github/license/dntsk/later42) ![Build Status](https://ci.lyalyuev.info/api/badges/dntsk/later42/status.svg)

Selfhostable read it later service.

## Installation with Docker

### Run with prepared images

This is the recommended way to run Later42

* copy provided `docker-compose.yml` and customize for your needs
* pull prepared images from the Docker Hub and start - `docker-compose pull && docker-compose up -d`

### Build custom images from sources

* clone this repo
* customize provided `docker-compose.yml` for your needs
* build docker images from the sources - `docker-compose build && docker-compose up -d`

## Environment variables

| Variable            | Default                 | Description
|---------------------|-------------------------|------------
TZ                    | UTC                     | Time zone
DEBUG                 | False                   | Enable/disable debug mode
SECRET_KEY            |                         | The secret key to make hashes
DOMAIN                | localhost               | Domain name where the site is hosted
DB_TYPE               | SQLite                  | Type of DB (SQLite, Postgres)
DB_HOST               | None                    | Host for Postgres DB
DB_NAME               | None                    | Name for Postgres DB 
DB_USER               | None                    | User for Postgres DB
DB_PASS               | None                    | Password for Postgres DB
REDIS_URL             | redis://localhost:6379  | Connection string for Redis
READABILITY_HOST      | http://localhost:8080/  | Connection string for [UReadability](https://github.com/ukeeper/ukeeper-readability)
EMAIL_USE_TLS         | False                   | Enable TLS for SMTP
EMAIL_HOST            | smtp                    | SMTP host
EMAIL_HOST_USER       | None                    | SMTP user
EMAIL_HOST_PASSWORD   | None                    | SMTP password
EMAIL_PORT            | 25                      | SMTP port
EMAIL_FROM            | noreply@later42.com     | Email address for From header
AIRBRAKE_PROJECT_ID   | None                    | Airbrake project id
AIRBRAKE_PROJECT_KEY  | None                    | Airbrake project key
AIRBRAKE_ENVIRONMENT  | development             | Airbrake environment
SENTRY_DSN            | None                    | Sentry DSN to catch errors

## Contribute

If you want to report a bug or request a new feature. Free feel to open a new issue or pull request.

English proofreading is needed, because my grammar is not that great sadly. Feel free to correct my grammar in this Readme or source code.
