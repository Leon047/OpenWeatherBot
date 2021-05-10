FROM python:3.9
RUN mkdir /app
WORKDIR /app 
COPY . /app
RUN apt-get update -y &&\
    	pip install --upgrade pip &&\
    	pip install --no-cache -r requirements.txt
