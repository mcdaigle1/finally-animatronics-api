FROM python:3.12-slim AS builder

WORKDIR /app

ENV POETRY_VERSION=2.3.4 POETRY_NO_INTERACTION=1 POETRY_VIRTUALENVS_CREATE=false

RUN pip install --no-cache-dir "poetry==$POETRY_VERSION"

COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --without dev

FROM python:3.12-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN adduser --disabled-password --gecos "" appuser

COPY --from=builder /usr/local/lib/python3.12/site-packages /usr/local/lib/python3.12/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

COPY finally_animatronics_api ./finally_animatronics_api

USER appuser

EXPOSE 8000

CMD ["uvicorn", "finally_animatronics_api.main:app", "--host", "0.0.0.0", "--port", "8000"]