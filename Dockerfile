FROM python:3.9-slim-bullseye

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

RUN apt update && apt install unzip wget -y

RUN wget -O hayabusa.zip https://github.com/Yamato-Security/hayabusa/releases/download/v2.12.0/hayabusa-2.12.0-linux.zip

RUN unzip hayabusa.zip -d hayabusa && chmod +x hayabusa/hayabusa*

RUN rm hayabusa.zip hayabusa/hayabusa-2.12.0-lin-aarch64-gnu hayabusa/hayabusa-2.12.0-lin-x64-gnu hayabusa/*.md hayabusa/*.txt 

EXPOSE 9000

CMD ["gunicorn","--bind","0.0.0.0:9000", "--access-logfile", "-", "app:app"]



