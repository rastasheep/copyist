FROM python:2-slim
MAINTAINER Aleksandar Diklic <rastasheep@gmail.com>

ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update &&  apt-get install -y git gcc libjpeg-dev zlib1g-dev libxml2-dev libxslt-dev
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 80

CMD [ "python", "./copyist.py" ]
