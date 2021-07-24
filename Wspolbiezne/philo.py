import threading
import time
import random

class Phil(threading.Thread):
    def __init__(self, forks, n):
        threading.Thread.__init__(self)
        self.forks = forks
        self.n = n
    def fork(self, dir):
        if dir == 'left':
            return self.forks[self.n]
        else:
            return self.forks[(self.n + 1) % 5]
    def fork_ord(self):
        if random.random() < 0.5:
            take1, take2 = 'left', 'right'
        else:
            take1, take2 = 'right', 'left'
        if random.random() < 0.5:
            put1, put2 = 'left', 'right'
        else:
            put1, put2 = 'right', 'left'
        return (take1, take2, put1, put2)
    def run(self):
        for i in range(100):
            print('Philosopher', self.n, 'thinks', i, 'th iteration')
            #time.sleep(random.random())
            take1, take2, put1, put2 = self.fork_ord()
            print('Philosopher', self.n, 'takes', take1, 'fork', i, 'th iteration')
            self.fork(take1).acquire()
            #time.sleep(random.random())
            print('Philosopher', self.n, 'takes', take2, 'fork', i, 'th iteration')
            self.fork(take2).acquire()
            print('Philosopher', self.n, 'eats', i, 'th iteration')
            #time.sleep(random.random())
            print('Philosopher', self.n, 'puts down', put1, 'fork', i, 'th iteration')
            self.fork(put1).release()
            #time.sleep(random.random())
            print('Philosopher', self.n, 'puts down', put2, 'fork', i, 'th iteration')
            self.fork(put2).release()

forks = [threading.Semaphore(1) for i in range(5)]
phils = [Phil(forks, i) for i in range(5)]

for t in phils:
    t.start()

for t in phils:
    t.join()