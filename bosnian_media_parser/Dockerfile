# we have to use python 3.8 since Lemmagen does not support 3.9
FROM rg.fr-par.scw.cloud/djnd/newsgradient-api:latest
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get -y install locales locales-all

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN mkdir /parser
WORKDIR /parser

COPY requirements.txt /parser/
RUN pip install -r requirements.txt

COPY . /parser

CMD bash runner.sh
