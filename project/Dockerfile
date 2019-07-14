FROM python:3.7

WORKDIR /project

RUN pip install uwsgi supervisor

RUN if [ "$PROJECT_ENV" = "productionn" ]; \
  then pip install -r requirements/production.txt;\
  else pip install -r requirements/development.txt;\
  fi
