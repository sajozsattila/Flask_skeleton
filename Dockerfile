FROM python:3.8.2-slim

ARG DEBIAN_FRONTEND=noninteractive

# the user which run the application
RUN useradd -s /bin/bash zen
# user home dir
WORKDIR /home/zen

# update the packages
RUN apt-get update -y

# install the necesarry python packages
COPY requirements.txt requirements.txt
RUN pip install -U pip setuptools
RUN pip install -r requirements.txt

# install the application
COPY app ./app
COPY waitress_server.sh ./
RUN chmod +x waitress_server.sh
COPY config.py ./config.py
RUN mkdir /home/zen/logs && chown zen /home/zen/logs && chgrp zen /home/zen/logs

# start the application
CMD su zen -c "/home/zen/waitress_server.sh" -
