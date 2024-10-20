#!/bin/bash

# EDIT DATABASE NAME TO CHOOSE WHICH ONE YOU WANT
DATABASE_NAME="newsgradient"
K8S_NAMESPACE="newsgradient"

# DATABASE PASSWORD IS DYNAMICALLY RETRIEVED FROM THE CLUSTER
DATABASE_USER=$(kubectl get secret newsgradient-api-credentials -n $K8S_NAMESPACE -o jsonpath="{.data.DJANGO_DATABASE_USERNAME}" | base64 --decode)
DATABASE_PASSWORD=$(kubectl get secret newsgradient-api-credentials -n $K8S_NAMESPACE -o jsonpath="{.data.DJANGO_DATABASE_PASSWORD}" | base64 --decode)

echo
echo "PORT FORWARDING"
nohup kubectl port-forward pod/postgresql-11-postgresql-0 54321:5432 --namespace=shared &>/dev/null &

# store the kubectl pid for later
KUBECTL_PID=$!

# wait for port forwarding to initialise
sleep 5

echo
echo "DUMPING DATABASE TO db.dump"
PGPASSWORD=$DATABASE_PASSWORD \
    pg_dump -U $DATABASE_USER \
        -f db.dump \
        -d "$DATABASE_NAME" \
        -p 54321 \
        -h localhost

echo "DATABASE DUMP SAVED to db.dump"

# echo
# echo "DROPPING THE DB VOLUME"
# sudo docker-compose down -v db
# sudo docker-compose up -d

# sleep 5

# echo
# echo "LOADING DB INTO CONTAINER"
# sudo docker container exec -i $(sudo docker-compose ps -q db) psql -U postgres newsgradient < db.dump

# sudo docker-compose down

# echo "STOPPING PORT FORWARDING"
# kill $KUBECTL_PID

# echo
# echo "ALL DONE, YOU CAN RUN docker-compose up AND/OR DELETE db.dump"
