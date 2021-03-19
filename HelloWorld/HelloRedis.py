import redis
conn = redis.Redis()
conn.set('hello', 'world')
msg = conn.get('hello')
print(msg)