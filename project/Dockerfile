FROM python:3.7

ARG BUILD_ENVIRONMENT

WORKDIR /project

RUN pip install uwsgi supervisor

COPY ./requirements /product/tmp/requirements

RUN if [ "$BUILD_ENVIRONMENT" = "productionn" ]; \
  then pip install -r /product/tmp/requirements/production.txt;\
  else pip install -r /product/tmp/requirements/development.txt;\
  fi
