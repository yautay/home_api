FROM python:3.8.6-buster

ADD ./src /var/www/html/mock-rest
ADD ./init.sh /
ADD ./flask.sh /

RUN chmod +x /init.sh /flask.sh
RUN /flask.sh

RUN mkdir /var/log/uwsgi

ENTRYPOINT ["/init.sh"]
