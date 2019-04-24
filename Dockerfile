FROM python:3.6

RUN pip install requirements.txt

RUN apt-get update

CMD ["echo", "Hello world from my first docker image"]