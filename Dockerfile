FROM circleci/python:3.10-browsers-legacy

WORKDIR /app-store_crawler
COPY ./pyproject.toml .
RUN poetry install
RUN poetry run playwright install
COPY . .

ENV PYTHONUNBUFFERED=1
