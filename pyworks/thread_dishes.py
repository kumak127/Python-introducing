# python3
# thread_dishes.py - threaingモジュールのテスト

import threading, queue, time

def washer(dishes, dish_queue):
    for dish in dishes:
        time.sleep(5)
        print("Washing", dish)
        dish_queue.put(dish)

def dryer(dish_queue):
    while True:
        dish = dish_queue.get()
        time.sleep(8)
        print("Dring", dish)
        dish_queue.task_done()

if __name__ == "__main__":
    dish_queue = queue.Queue()
    for n in range(2):
        dryer_thread = threading.Thread(target=dryer, args=(dish_queue,))
        dryer_thread.start()

    dishes  = ["salad", "bread", "entree", "desert"]
    washer(dishes, dish_queue)
    dish_queue.join()