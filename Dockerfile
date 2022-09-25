FROM python:latest
RUN apt-get update
RUN apt-get install wget
WORKDIR /src/
RUN wget "https://raw.githubusercontent.com/mschermann/forensic_accounting/master/fb_sub.csv"


COPY test.py ./
RUN python test.py