FROM python:3.9.7-buster

# install mlflow and psycopg2
RUN pip install \
    mlflow \
    psycopg2
    
RUN mkdir -p mlflow/artifacts
# open port 5000
EXPOSE 5000

# set environment variables
ARG POSTGRES_USER
ARG POSTGRES_PASSWORD
ARG DB_HOST
ARG DB_NAME
ENV POSTGRES_USER=${POSTGRES_USER}
ENV POSTGRES_PASSWORD=${POSTGRES_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_NAME=${DB_NAME}

# Start mlflow server
CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --backend-store-uri postgresql+psycopg2://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${DB_HOST}:5432/${DB_NAME} \
    --default-artifact-root /mlflow/artifacts