FROM ubuntu:latest

WORKDIR /app

RUN apt update && apt install unzip wget -y

RUN wget -O hayabusa.zip https://github.com/Yamato-Security/hayabusa/releases/download/v2.12.0/hayabusa-2.12.0-linux.zip

RUN unzip hayabusa.zip

RUN chmod +x hayabusa*

ENTRYPOINT ["./hayabusa-2.12.0-lin-x64-gnu"]
