import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, line, target, lock):
        threading.Thread.__init__(self)
        self.line = line
        self.target = target
        self.lock = lock
    def run(self):
        t = self.target
        time.sleep(random.random())
        with lock:
            for i, c in enumerate(self.line):
                time.sleep(random.random()/50)
                t[i] = c
                print(i, c)
            for j in range(i+1, len(t)):
                t[j]=' '

with open('poem.txt', 'r') as f:
    lines = f.read().splitlines()
target = [' '] * max(len(line) for line in lines)
lock = threading.RLock()
threads = [MyThread(line, target, lock) for line in lines]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(''.join(target))