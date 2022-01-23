import threading
import time
import random

class MyQueue:
    def __init__(self):
        lock = threading.RLock()
        self.cond = threading.Condition(lock)
        self.buf = []
    def enqueue(self, x):
        with self.cond:
           print('Adding', x)
           self.buf.append(x)
           self.cond.notify()
    def dequeue(self, n):
        with self.cond:
            while self.buf == []:
                self.cond.wait()
            el = self.buf.pop(0)
            print('Thread', n, 'is removing', el)
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
        for i in range(10):
            time.sleep(random.random())
            self.queue.dequeue(self.n)

queue = MyQueue()
threads = [Producer(queue, n) for n in range(10)]
threads += [Consumer(queue, n) for n in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()