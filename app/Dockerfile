FROM node:22.4-alpine3.19

WORKDIR /app

COPY package.json .

COPY . .

RUN yarn
RUN yarn global add serve
RUN yarn build
EXPOSE 3000
CMD [ "yarn", "preview" ]