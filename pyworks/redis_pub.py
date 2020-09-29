# python3
# redis_pub.py - Redisを使ったパブサブシステムのパブリッシャ

import redis, random

conn = redis.Redis()
cats = ["siamese", "persian", "maine coon", "norwegian forest"]
hats = ["stovepipe", "bowler", "tam-o-shanter", "fedora"]
for msg in range(10):
    cat = random.choice(cats)
    hat = random.choice(hats)
    print(f"Piblish: {cat} wears a {hat}")
    conn.publish(cat,hat)