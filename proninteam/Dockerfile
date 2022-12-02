FROM python:3.11-slim

WORKDIR /app
COPY . /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir

RUN echo yes | python manage.py collectstatic --noinput
CMD ["gunicorn", "proninteam.wsgi:application", "--bind", "0:8000" ]
