const WebSocket = require("ws");
const redis = require("redis");

const REDIS_SERVER = "redis://redis:6379";
const WEB_SOCKET_PORT = 3000;

var redisClient = redis.createClient(REDIS_SERVER);
redisClient.subscribe("devices");

const server = new WebSocket.Server({ port: WEB_SOCKET_PORT });

server.on("connection", function connection(ws) {
  redisClient.on("message", function (channel, message) {
    console.log(message);
    ws.send(message);
  });
});

console.log("WebSocket server started at ws://locahost:" + WEB_SOCKET_PORT);

