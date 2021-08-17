import redis

r = redis.Redis(host='redis', port=6379, db=1)


def publish(channel="devices", data=""):
    r.publish(channel, data)
