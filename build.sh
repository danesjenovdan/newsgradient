#!/bin/bash

sudo docker login rg.fr-par.scw.cloud/djnd -u nologin -p $SCW_SECRET_TOKEN
GIT_HASH=$(git rev-parse HEAD)

# # BUILD AND PUBLISH PWA
sudo docker build -f pwa/Dockerfile -t newsgradient-pwa:latest ./pwa
sudo docker tag newsgradient-pwa:latest rg.fr-par.scw.cloud/djnd/newsgradient-pwa:latest
sudo docker tag newsgradient-pwa:latest rg.fr-par.scw.cloud/djnd/newsgradient-pwa:${GIT_HASH}
sudo docker push rg.fr-par.scw.cloud/djnd/newsgradient-pwa:latest
sudo docker push rg.fr-par.scw.cloud/djnd/newsgradient-pwa:${GIT_HASH}

# BUILD AND PUBLISH API
sudo docker build -f api/Dockerfile -t newsgradient-api:latest ./api
sudo docker tag newsgradient-api:latest rg.fr-par.scw.cloud/djnd/newsgradient-api:latest
sudo docker tag newsgradient-api:latest rg.fr-par.scw.cloud/djnd/newsgradient-api:${GIT_HASH}
sudo docker push rg.fr-par.scw.cloud/djnd/newsgradient-api:latest
sudo docker push rg.fr-par.scw.cloud/djnd/newsgradient-api:${GIT_HASH}
