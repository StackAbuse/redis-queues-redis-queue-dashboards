import redis

r = redis.Redis(host='localhost', port=6379, db=0)


def visit():
    if r.get('count') is None:
        r.set('count', 1)
    else:
        r.incr('count')
