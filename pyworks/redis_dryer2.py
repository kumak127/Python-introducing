# pytohn3
# redis_dryer2.py - Redisを使った並行処理のテスト

def dryer():
    import redis, os, time
    conn = redis.Redis()
    pid = os.getpid()
    timeout = 20
    print(f"Dryer process {pid} is starting")
    while True:
        msg = conn.blpop("dishes",timeout)
        if not msg:
            break
        val = msg[1].decode("utf-8")
        if val == "quit":
            break
        print(f"{pid}: dried {val}")
        time.sleep(0.1)
    print(f"Dryer process {pid} is done")

import multiprocessing
DRYERS=3
for num in range(DRYERS):
    if __name__ == "__main__":
        p = multiprocessing.Process(target=dryer)
        p.start()