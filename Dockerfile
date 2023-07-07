# base image
FROM python:2.7

# Download latest listing of available packages:
RUN apt-get -y update

# Upgrade already installed packages:
RUN apt-get -y upgrade

# Install package required for sound steam
RUN apt-get -y install \ 
	libportaudio2 \
	libasound-dev

# set workdir for container
WORKDIR /App

# add naoqi OS
ADD https://community-static.aldebaran.com/resources/2.5.10/Python%20SDK/pynaoqi-python2.7-2.5.7.1-linux64.tar.gz .
RUN tar -xf pynaoqi-python2.7-2.5.7.1-linux64.tar.gz

# set environment variables for python to find naoqi api
ENV PYTHONPATH=/App/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages
ENV DYLD_LIBRARY_PATH=/App/pynaoqi-python2.7-2.5.7.1-linux64/lib

# add requirements to container
COPY requirements.txt .

# install requirements in container
RUN pip install -r requirements.txt

CMD python index.py