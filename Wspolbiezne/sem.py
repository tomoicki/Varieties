import threading
import time
import random

class ExampleThread(threading.Thread):
    def __init__(self, sem, m, nr):
        threading.Thread.__init__(self)
        self.m = m
        self.sem = sem
        self.nr = nr
    def run(self):
        for i in range(self.m):
            time.sleep(random.random())
            with self.sem:
                print('Thread', self.nr, ', start nr', i)
                time.sleep(random.random())
                print('Thread', self.nr, ', stop nr', i)

sem = threading.Semaphore(3)
threads = [ExampleThread(sem, 10, i) for i in range(10)]

for t in threads:
    t.start()

for t in threads:
    t.join()