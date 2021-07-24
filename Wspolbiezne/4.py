import threading
import time
import random
X = 10.0
class Adder(threading.Thread):
    def __init__(self, can_add, can_substract):
        threading.Thread.__init__(self)
        self.can_add = can_add
        self.can_substract = can_substract
    def run(self):
        global X
        while True:
            with self.can_add:
                while X >= 20.0:
                    self.can_add.wait()
                time.sleep(0.05 * random.random())
                before = X
                X = X + random.random() * 15.0
                print(F' [+] from {before} to {X} ')
                if X > 0.0:
                    self.can_substract.notify()
class Substr(threading.Thread):
    def __init__(self, can_add, can_substract):
        threading.Thread.__init__(self)
        self.can_add = can_add
        self.can_substract = can_substract
    def run(self):
        global X
        while True:
            with self.can_substract:
                while X <= 0.0:
                    self.can_substract.wait()
                time.sleep(0.05 * random.random())
                before = X
                X = X - random.random() * 15.0
                if before < 0.0:
                    print("WTF")
                print(F' [-] from {before} to {X} ')
                if X < 20.0:
                    self.can_add.notify()

lock = threading.Lock()
can_add = threading.Condition(lock)
can_substract = threading.Condition(lock)
threads = [Adder(can_add, can_substract) if random.random() < 0.5 else Substr(can_add, can_substract) for _ in range(10)]
for t in threads:
    t.start()
for t in threads:
    t.join()