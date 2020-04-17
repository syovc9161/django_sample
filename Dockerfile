FROM python:3.6

RUN apt-get update && apt-get -y install \
    libpq-dev

WORKDIR /app
ADD    ./requirements.txt   /app/
RUN    python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r requirements.txt

ADD    ./djangosample   /app/djangosample/
ADD    ./manage.py      /app/

CMD ["python", "manage.py", "runserver", "0:8000"]
