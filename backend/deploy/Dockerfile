FROM python:3.12

ARG POSTGRESQL_HOST
ARG POSTGRESQL_PORT
ARG POSTGRESQL_DB_NAME
ARG POSTGRESQL_USER
ARG POSTGRESQL_PASSWORD

WORKDIR /opt/dofus_market

COPY dofus_market/requirements.txt /opt/dofus_market/requirements.txt
RUN pip install --no-cache-dir -r /opt/dofus_market/requirements.txt

# Mounts the application code to the image
COPY dofus_market /opt/dofus_market/dofus_market


EXPOSE 8000

# runs the production server
ENTRYPOINT ["python", "dofus_market/manage.py"]
CMD ["runserver", "0.0.0.0:8000"]