FROM python:3


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ENV POETRY_HOME=/bin/poetry
ENV PATH="${POETRY_HOME}/bin/:${PATH}"

WORKDIR /app

EXPOSE 8007

RUN apt-get -y update && apt-get -y upgrade && \
    apt-get -y install bash python3 python3-dev postgresql-client  && \
    rm -vrf /var/cache/apk/* && \
    curl -sSL https://install.python-poetry.org  | python - && \
    poetry config virtualenvs.create false --local
COPY poetry.lock .
COPY pyproject.toml .

RUN poetry install
# RUN pip install redis

COPY . .