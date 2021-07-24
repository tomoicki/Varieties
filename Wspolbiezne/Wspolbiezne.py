import threading
import time
import random

def counting(nr, m_max = 10):
    print(f'Rozpoczynam wątek nr {nr}')
    for m in range(m_max):
        time.sleep(random.random())
        # print('x')
        print(f'Wątek {nr}, komunikat nr {m}')
        # print('Wątek ',nr, 'komunikat nr ',m)
    print(f'Kończę wątek nr {nr}')


class CountingThread(threading.Thread):
    def __init__(self, nr, m_max = 10):
        threading.Thread.__init__(self)
        self.nr = nr
        self.m_max = m_max
    def run(self):
        counting(self.nr, self.m_max)

random.seed()

threads = [CountingThread(n) for n in range(2)]

for t in threads:
    t.start()

for t in threads:
    t.join()

print('Koniec')