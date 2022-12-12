## ProninTeamBackend
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)

This is the backend code for ProninTeam project. For more information about the project, please see [site](https://proninteam.ru/).

## <a name="repositories"></a>Repositories
- [Backend](https://github.com/Capwell/ProninTeamBack)
- [Frontend](https://github.com/Capwell/ProninTeamFront)

## <a name="local-deployment-scenarios"></a>Local deployment scenario
Clone repository:

```git@github.com:Capwell/ProninTeamBack.git```

Create .env file at `.environment/` directory:

```
SECRET_KEY=<secret_key>
DB_ENGINE=<django.db.backends.postgresql>
DB_NAME=<db_name>
POSTGRES_USER=<pg_username>
POSTGRES_PASSWORD=<pg_password>
DB_HOST=<localhost>
DB_PORT=<5432>
EMAIL_LOGIN=<email_login>
EMAIL_PASSWORD=<email_password>
TELEGRAM_TOKEN=<tg_token>
TELEGRAM_CHAT_ID=<tg_chatid>
EMAIL_TO=<email_to>
EMAIL_FROM=<email_from>
CAPTCHA_SECRET_KEY=<capthca_secret_key>
```
Run docker-compose:
```docker-compose up -d```
