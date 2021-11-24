# builder for installing python packages
FROM python:3.9.7-buster as builder

# install mlflow and mysqlclient
RUN pip install \
    mlflow \
    mysqlclient \
    boto3

# main image
FROM python:3.9.7-slim-buster

# copy python packages
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
# copy mlflow package
COPY --from=builder /usr/local/bin/mlflow /usr/local/bin/mlflow
# copy linux packages for mysql
COPY --from=builder /usr/lib/aarch64-linux-gnu /usr/lib/aarch64-linux-gnu
# copy gunicorn package
COPY --from=builder /usr/local/bin/gunicorn /usr/local/bin/gunicorn

# open port 5000
EXPOSE 5000

# set environment variables
ARG MYSQL_USER
ARG MYSQL_PASSWORD
ARG DB_HOST
ARG DB_NAME
ARG DEFAULT_ARTIFACT_ROOT
ENV MYSQL_USER=${MYSQL_USER}
ENV MYSQL_PASSWORD=${MYSQL_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_NAME=${DB_NAME}
ENV DEFAULT_ARTIFACT_ROOT=${DEFAULT_ARTIFACT_ROOT}

# Start mlflow server
CMD mlflow server \
    --host 0.0.0.0 \
    --port 5000 \
    --backend-store-uri mysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${DB_HOST}:3306/${DB_NAME} \
    --default-artifact-root ${DEFAULT_ARTIFACT_ROOT}