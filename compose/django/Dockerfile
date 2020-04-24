FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN apt update && apt -y install libpq-dev

RUN apt install -y nginx

WORKDIR /app
ADD    ./requirements.txt    /app/
RUN    python -m pip install \
    --trusted-host pypi.python.org \
    --trusted-host files.pythonhosted.org \
    --trusted-host pypi.org \
    -r requirements.txt
