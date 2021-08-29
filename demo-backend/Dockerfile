FROM python:3.9-slim

USER root

WORKDIR /App
COPY ./requirements.txt /App/
RUN pip3 install -r requirements.txt


RUN useradd python
RUN chown python:python /App/*
RUN chown python:python /App
USER python
RUN chmod 700 /App/*
CMD ["python3", "run.py" ]