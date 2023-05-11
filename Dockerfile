FROM python:3.10

ENV POETRY_VIRTUALENVS_CREATE=false \
    POETRY_HOME='/usr/local' \
    PYTHONUNBUFFERED=1

RUN curl -sSL 'https://install.python-poetry.org' | python - \
  && poetry --version

WORKDIR /app

COPY pyproject.toml poetry.lock /app/

RUN poetry install --no-interaction --no-ansi

COPY ./app /app/
