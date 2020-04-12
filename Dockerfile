FROM python:3

WORKDIR /usr/src/app

RUN apt-get update && apt-get install git

RUN git clone https://github.com/joosthoeks/jhTAlib.git

RUN cd jhTAlib/ && pip3 install -e .

