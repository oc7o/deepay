FROM python:3.8-slim

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput
RUN chmod +x /app/scripts/*
ENV PATH="/app/scripts:${PATH}"

ENTRYPOINT [ "entrypoint.sh" ]