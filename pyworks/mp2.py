# python3
# mp2.py - multiprocess.terminate関数のテスト用

import multiprocessing, time, os

def whoami(name):
    print(f"i'm {name}, in process {os.getpid()}")
    
def loopy(name):
    whoami(name)
    start = 1
    stop= 100
    for num in range(start, stop):
        print(f"\tNumber {num} of {stop}. Honk!")
        time.sleep(1)

if __name__ == "__main__":
    whoami("main")
    p = multiprocessing.Process(target=loopy, args=("loopy",))
    p.start()
    time.sleep(5)
    p.terminate()