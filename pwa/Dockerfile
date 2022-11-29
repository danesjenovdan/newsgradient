FROM node:lts-alpine

ADD package.json /app/
WORKDIR /app
RUN yarn

COPY . /app

RUN yarn build

ENV HOST 0.0.0.0

CMD yarn start
