# python3
# mp.py - multiprocessingモジュールのテスト用

import multiprocessing, os

def do_this(what):
    whaomi(what)

def whaomi(what):
    print(f"Process {os.getpid()} says: {what}")

if __name__ == "__main__":
    whaomi("I'm the main program")
    for n in range(4):
        p = multiprocessing.Process(target=do_this, args=(f"I'm function {n}",))
        p.start()