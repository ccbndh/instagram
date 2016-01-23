FROM python:2.7
MAINTAINER ccbndh "thanhtinpk092007@gmail.com"
ENV REFRESHED_AT 2016-01-16

# Postgres client psql
RUN apt-get update
RUN apt-get install -y postgresql-client

WORKDIR /srv/instagram
ADD requirements.txt ./
RUN pip install -r requirements.txt

ADD start.sh ./
RUN chmod 775 start.sh
ENTRYPOINT ["/srv/instagram/start.sh"]

CMD []
