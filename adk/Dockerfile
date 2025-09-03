FROM python:3.10.18-slim

RUN apt-get update

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY travel_assistant /usr/src/app/travel_assistant
RUN pip install --upgrade pip
RUN pip install google-adk