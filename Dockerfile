FROM python:3.9-slim

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY ./scripts/ /scripts/
RUN chmod +x /scripts/*
ENV PATH="/scripts:${PATH}"

CMD [ "entrypoint.sh" ]