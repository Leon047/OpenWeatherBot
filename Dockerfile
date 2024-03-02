FROM python:3.11
WORKDIR /bot 
COPY . /bot
RUN apt-get update -y &&\
    	pip install --upgrade pip &&\
    	pip install --no-cache -r requirements.txt 
ARG BOT_TOKEN
ARG OPEN_WEATHER_KEY
ENV BOT_TOKEN=${BOT_TOKEN}
ENV OPEN_WEATHER_KEY=${OPEN_WEATHER_KEY}
CMD ['python', 'run.py']
