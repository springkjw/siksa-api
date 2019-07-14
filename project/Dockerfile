FROM python:3.7

ARG PROJECT_ENV

WORKDIR /project

RUN pip install uwsgi

COPY ./requirements/base.txt /project/tmp/base.txt
COPY ./requirements/${PROJECT_ENV}.txt /project/tmp/${PROJECT_ENV}.txt
RUN pip install -r /project/tmp/${PROJECT_ENV}.txt
RUN rm -rf /project/tmp