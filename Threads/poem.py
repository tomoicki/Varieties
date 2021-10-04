import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, line, target):
        threading.Thread.__init__(self)
        self.line = line
        self.target = target
    def run(self):
        t = self.target
        for i, c in enumerate(self.line):
            time.sleep(random.random()/50)
            t[i] = c
            print(i, c)

random.seed()
with open('poem.txt', 'r') as f:
    lines = f.read().splitlines()
target = [' '] * max(len(line) for line in lines)
threads = [MyThread(line, target) for line in lines]
for t in threads:
    t.start()
for t in threads:
    t.join()
print(''.join(target))