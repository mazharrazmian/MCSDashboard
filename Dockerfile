FROM python:3
MAINTAINER Mazhar Ali
ENV PYTHONUNBUFFERED 1
EXPOSE 8000
RUN mkdir /code
WORKDIR /code

COPY requirements.txt /code/
RUN pip install -r requirements.txt

COPY . /code/
