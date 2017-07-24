FROM ubuntu:16.04

RUN apt-get update && apt-get -y install sudo vim curl git bash
RUN useradd -m docker && echo "docker:docker" | chpasswd && adduser docker sudo

RUN apt-get update && apt-get install -y \
            build-essential \
            openssl \
            libxml2-dev \
            libxslt-dev \
            libffi-dev \
            libssl-dev \
            libxslt1-dev \
            python-dev \
            python-numpy \
            python-openssl \
            python-pip \
            python-software-properties

RUN apt-get update && apt-get -y install rabbitmq-server
RUN service rabbitmq-server restart

USER docker
WORKDIR /app
ADD . /app

RUN pip install -r requirements.txt

CMD celery -A tasks beat --loglevel=INFO
