# python3
# redis_washer.py - redis_dryer,pyの後に実行することでRedisを使った並行処理ができる

import redis
conn = redis.Redis()
print("Washer is starting")
dishes = ["salad","bread","entree","dessert"]
for dish in dishes:
    msg = dish.encode("utf-8")
    conn.rpush("dishes", msg)
    print("Washed",dish)
conn.rpush("dishes","quit")
print("Washer is done")