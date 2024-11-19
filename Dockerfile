FROM python:3.10.12-slim-bullseye

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1


ENTRYPOINT [ "python3", "/app/src/main.py" ]
