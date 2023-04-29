import redis
from envReader import getValue as gv

r = None
def initRedis():
    global r
    r = redis.Redis(host=gv("REDIS_HOST"), port=gv("REDIS_PORT"), db=0)

def setValue(key, value):
    global r
    r.set(key, value)

def valueExists(key):
    global r
    return r.exists(key)

def getValue(key):
    global r
    if valueExists(key):
        return r.get(key)
    else:
        return None