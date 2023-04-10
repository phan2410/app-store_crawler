FROM mcr.microsoft.com/playwright:v1.30.0-focal

RUN apt-get update --fix-missing
RUN apt-get install -y software-properties-common \
    && add-apt-repository ppa:deadsnakes/ppa \
    && apt-get install -y python3.10 libgl1-mesa-dev python3-pip

RUN pip3 install poetry

WORKDIR /app-store_crawler
COPY ./pyproject.toml .
RUN poetry env use python3.10 && poetry install && pip3 install --upgrade requests
RUN poetry run playwright install
COPY . .

ENV PYTHONUNBUFFERED=1
