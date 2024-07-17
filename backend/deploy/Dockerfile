FROM python:3.12-slim

ARG POSTGRESQL_HOST
ARG POSTGRESQL_PORT
ARG POSTGRESQL_DB_NAME
ARG POSTGRESQL_USER
ARG POSTGRESQL_PASSWORD

WORKDIR /opt/dofus_market

COPY poetry.lock pyproject.toml /opt/dofus_market/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install poetry && \
    python -m venv .venv && \
    poetry install --without dev,tests

# Mounts the application code to the image
COPY manage.py /opt/dofus_market/manage.py
COPY django_project /opt/dofus_market/django_project
COPY market /opt/dofus_market/market
COPY api /opt/dofus_market/api
COPY grpc_market /opt/dofus_market/grpc_market


EXPOSE 8000

# runs the production server
ENTRYPOINT ["poetry", "run", "python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]
