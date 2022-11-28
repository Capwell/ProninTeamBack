FROM python:3.7-slim
WORKDIR /app
COPY ../proninteam/requirements.txt /app
RUN pip3 install -r /app/requirements.txt --no-cache-dir
COPY . /app
WORKDIR proninteam
RUN echo yes | python manage.py collectstatic --noinput
CMD ["gunicorn", "proninteam.wsgi:application", "--bind", "0:8000" ]