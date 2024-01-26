FROM python:3.11-bullseye

WORKDIR /app

COPY . /app/

RUN pip3 install -r requirements.txt

RUN apt update && apt install unzip wget -y

RUN wget -O hayabusa.zip https://github.com/Yamato-Security/hayabusa/releases/download/v2.12.0/hayabusa-2.12.0-linux.zip

RUN unzip hayabusa.zip -d hayabusa && chmod +x hayabusa/hayabusa*

EXPOSE 5000

CMD ["python", "app.py"]



