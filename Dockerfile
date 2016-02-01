FROM alpine
MAINTAINER Aleksandar Diklic <rastasheep@gmail.com>

RUN apk update && apk upgrade
RUN apk add gcc git python py-pip py-lxml py-pillow libjpeg python-dev musl-dev
RUN rm -rf /var/cache/apk/*

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ADD requirements.txt /usr/src/app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 80

CMD [ "python", "./copyist.py" ]
