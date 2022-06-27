FROM node:alpine as build
WORKDIR /app
RUN npm install yarn
COPY package*.json yarn.lock ./
RUN yarn install
COPY . ./
RUN yarn run build

FROM nginx:alpine
RUN rm -rf /usr/share/nginx/html/*
COPY --from=build /app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf
EXPOSE 80