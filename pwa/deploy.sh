#!/usr/bin/env bash

git pull
docker-compose stop
docker-compose build
docker-compose up -d
