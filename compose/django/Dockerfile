FROM python:3.6

ENV PYTHONUNBUFFERED 0

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app
ADD    ./requirements.txt    /app/
RUN    python -m pip install  --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt
