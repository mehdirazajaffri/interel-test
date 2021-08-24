FROM node:16-alpine
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . /opt/app
RUN npm install --quite
EXPOSE 3000
CMD [ "npm", "start" ]