FROM python:3.9
RUN mkdir app
COPY . /app
WORKDIR /app 
RUN apt-get update -y &&\
    	pip install --upgrade pip &&\
    	pip install --no-cache -r requirements.txt
RUN . ./setenv.sh
ARG BOT_TOKEN=$BOT_TOKEN
ARG OPEN_WEATHER_KEY=$OPEN_WEATHER_KEY
EXPOSE 80/tcp
CMD ["python3.9", "server.py"]
