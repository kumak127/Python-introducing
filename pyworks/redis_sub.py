# python3
# redis_sub.py - Redisを使ったパブサブシステムのサブスクライバ

import redis

conn = redis.Redis()
topics = ["maine coon", "persian"]
sub = conn.pubsub()
sub.subscribe(topics)
for msg in sub.listen():
    print(msg)
    if msg["type"] == "message":
        cat = msg["channel"]
        hat = msg["data"]
        print(f"Subscribe: {cat} wears a {hat}")