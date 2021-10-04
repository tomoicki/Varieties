import threading
import time
import random

class MyQueue:
    def __init__(self, max_size):
        self.count = 0
        self.rpos = 0
        self.wpos = 0
        self.max_size = max_size
        self.buf = [None] * max_size
        lock = threading.RLock()
        self.write_condition = threading.Condition(lock)
        self.read_condition = threading.Condition(lock)
    def enqueue(self, x):
        with self.write_condition:
            while self.count == self.max_size:
                self.write_condition.wait()
            print(F'Adding {x} at {self.wpos}')
            self.count += 1
            self.buf[self.wpos] = x
            self.wpos = (self.wpos + 1) % self.max_size
            self.read_condition.notify()

    def dequeue(self, n):
        with self.read_condition:
            while self.count == 0:
                self.read_condition.wait()
            el = self.buf[self.rpos]
            self.rpos = (self.rpos + 1) % self.max_size
            self.count -= 1
            print(F'Thread {n} is removing {el}')
            self.write_condition.notify()
            return el

class Producer(threading.Thread):
    def __init__(self, queue, n):
        threading.Thread.__init__(self)
        self.queue = queue
        self.n = n
    def run(self):
        for i in range(10):
            time.sleep(random.random())
            self.queue.enqueue((self.n, i))

class Consumer(threading.Thread):
    def __init__(self, queue, n):
        threading.Thread.__init__(self)
        self.queue = queue
        self.n = n
    def run(self):
        for _ in range(10):
            time.sleep(random.random())
            self.queue.dequeue(self.n)


queue = MyQueue(max_size=2)
threads = [Producer(queue, n) for n in range(10)]
threads += [Consumer(queue, n) for n in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()