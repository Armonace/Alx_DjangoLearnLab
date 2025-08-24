# Deploying social_media_api

## Prereqs
- Python 3.12+
- Postgres (managed or local)
- Nginx + systemd (Ubuntu) or Heroku account

## Steps
1) Set env vars (see .env example)
2) Install reqs and prod settings module
3) Run migrations & collectstatic
4) Start Gunicorn (systemd) and Nginx or push to Heroku
5) Verify /health/ and main endpoints
6) Enable HTTPS, logging, and backups
