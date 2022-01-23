import threading
import time
import random

class RWLock:
    def __init__(self):
        self.cond = threading.Condition()
        self.readers = 0
        self.waiting_writers = 0
        self.writer_active = False
    def rLock(self):
        with self.cond:
            while self.waiting_writers > 0 or self.writer_active:
                self.cond.wait()
            self.readers += 1
    def rUnLock(self):
        with self.cond:
            self.readers -= 1
            if self.readers == 0:
                self.cond.notify_all()
    def wLock(self):
        with self.cond:
            self.waiting_writers += 1
            while self.readers > 0 or self.writer_active:
                self.cond.wait()
            self.waiting_writers -= 1
            self.writer_active = True
    def wUnLock(self):
        with self.cond:
            self.writer_active = False
            self.cond.notify_all()

rw = RWLock()

class Reader(threading.Thread):
    def __init__(self, m):
        threading.Thread.__init__(self)
        self.m = m
    def run(self):
        global rw
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
        global rw
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
