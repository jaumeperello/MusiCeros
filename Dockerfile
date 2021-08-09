FROM debian:latest

RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg python3-dev default-libmysqlclient-dev  build-essential libssl-dev -y 
RUN pip3 install -U pip
RUN mkdir /app/
WORKDIR /app/
COPY . /app/
ENV URLDB="mysql-url"
RUN pip3 install -U -r requirements.txt
CMD python3 main.py
