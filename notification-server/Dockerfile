FROM node
RUN mkdir -p /opt/app
WORKDIR /opt/app
COPY . /opt/app
RUN npm install
EXPOSE 3000
CMD [ "npm", "start" ]