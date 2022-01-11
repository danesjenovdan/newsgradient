# we have to use python 3.8 since Lemmagen does not support 3.9
FROM python:3.8
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install -r requirements.txt

# install twint
# this is done with pip, because the --system
# flag in pipenv can't be used on single dependencies
# RUN pip install git+https://github.com/twintproject/twint.git#egg=twint

# install a fork of twint, since the original is broken after twitter made changes
RUN pip install git+https://github.com/rupert-jha/twint.git@158f40fd799471dc205a7929fc0aaaaaf76645f7#egg=twint

COPY . /app

EXPOSE 8000

ENV DJANGO_SETTINGS_MODULE=newsgradient.settings

CMD python manage.py runserver 0.0.0.0:8000


# FROM python:3.8
# RUN apt-get update && apt-get install --yes postgresql-client
# RUN mkdir /app
# WORKDIR /app
# COPY . /app
# RUN pip install -r requirements.txt
# EXPOSE 8000
