FROM python:3.11-slim

RUN apt update && \
    apt install -y ffmpeg && \
    mkdir /server

WORKDIR /server

#ADD ./requirements.txt /server/requirements.txt

ADD . /server

RUN pip install -r requirements.txt

CMD ['python', 'test.py']