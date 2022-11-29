FROM node:16-alpine

COPY package.json yarn.lock /app/
WORKDIR /app
RUN yarn

COPY . /app

RUN yarn build

ENV HOST 0.0.0.0

CMD yarn start
