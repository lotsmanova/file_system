FROM python:3.10

RUN mkdir /app_fs

WORKDIR /app_fs

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app_fs/src/"

EXPOSE 5000