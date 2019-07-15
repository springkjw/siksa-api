FROM python:3.7

WORKDIR /project

RUN pip install uwsgi supervisor

COPY ./requirements.txt /project/tmp/requirements.txt
RUN pip install -r /project/tmp/requirements.txt
RUN rm -rf /project/tmp