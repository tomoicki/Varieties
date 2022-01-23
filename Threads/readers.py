import threading
import time
import random

class RWLock:
    def __init__(self):
        self.rmut = threading.Lock()
        self.wmut = threading.Lock()
        self.readers = 0
    def rLock(self):
        with self.rmut:
            self.readers += 1
            if self.readers == 1:
                self.wmut.acquire()
    def rUnLock(self):
        with self.rmut:
            self.readers -= 1
            if self.readers == 0:
                self.wmut.release()
    def wLock(self):
        self.wmut.acquire()
    def wUnLock(self):
        self.wmut.release()

rw = RWLock()

class Reader(threading.Thread):
    def __init__(self, m):
        threading.Thread.__init__(self)
        self.m = m
    def run(self):
        for i in range(5):
            time.sleep(random.random())
            rw.rLock()
            print('Reader', self.m, 'starts reading,', i)
            time.sleep(random.random())
            print('Reader', self.m, 'stops reading,', i)
            rw.rUnLock()

class Writer(threading.Thread):
    def __init__(self, m):
        threading.Thread.__init__(self)
        self.m = m
    def run(self):
        for i in range(5):
            time.sleep(random.random())
            rw.wLock()
            print('Writer', self.m, 'starts writing,', i)
            time.sleep(random.random())
            print('Writer', self.m, 'stops writing,', i)
            rw.wUnLock()

def factory(m):
    if random.random() < 0.6:
        return Reader(m)
    else:
        return Writer(m)

threads = [factory(m) for m in range(3)]

for t in threads:
    t.start()

for t in threads:
    t.join()