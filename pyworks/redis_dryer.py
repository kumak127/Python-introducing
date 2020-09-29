# python3
# redis_dryer2.py - redis_washer.pyと一緒に実行することでRedisを使った並行処理を実行できる

import redis
conn = redis.Redis()
print("Dryer is starting")
while True:
    msg = conn.blpop("dishes")
    if not msg:
        break
    val = msg[1].decode("utf-8")
    if val == "quit":
        break
    print("Dried", val)
print("Dishes are dried")