FROM node:14-alpine

WORKDIR /app

COPY ./frontend/package.json .
COPY ./frontend/package-lock.json .
RUN npm install

COPY ./frontend .