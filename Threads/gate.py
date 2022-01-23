import threading
import time
import random

class MyThread(threading.Thread):
    def __init__(self, m):
        threading.Thread.__init__(self)
        self.m = m
    def run(self):
        time.sleep(random.random())
        print('Thread', self.m, 'executed A')
        time.sleep(random.random())
        counter.count()
        gate.tryPass()
        print('Thread', self.m, 'executed B')
        time.sleep(random.random())

class Gate:
    def __init__(self, is_open = False):
        self.cond = threading.Condition()
        self.is_open = is_open
    def open(self):
        with self.cond:
            self.is_open = True
            self.cond.notify_all()
    def close(self):
        with self.cond:
            self.is_open = False
    def tryPass(self):
        with self.cond:
            while not self.is_open:
                self.cond.wait()

class Counter:
    def __init__(self, gate, n):
        self.lock = threading.RLock()
        self.gate = gate
        self.m = n
    def count(self):
        with self.lock:
            self.m -= 1
            if self.m == 0:
                self.gate.open()

gate = Gate()
counter = Counter(gate, 10)
threads = [MyThread(m) for m in range(10)]
for t in threads:
  t.start()
for t in threads:
  t.join()