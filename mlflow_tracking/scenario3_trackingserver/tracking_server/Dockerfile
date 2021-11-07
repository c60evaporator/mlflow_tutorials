FROM python:3.9.7-slim-buster

# install mlflow and psycopg2
RUN pip install \
    mlflow \
    psycopg2 \
    mkdir /mlflow/
# open port 5000
EXPOSE 5000

## Start mlflow server
CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --backend-store-uri postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@postgresql:5432/mlflow-db