import threading

class MyThread(threading.Thread):
    def __init__(self, inp, res, i, j):
        threading.Thread.__init__(self)
        self.inp = inp
        self.res = res
        self.ij = (i,j)
    def run(self):
        i, j = self.ij
        dim, a, b = self.inp
        m,k,n = dim
        res = self.res
        res[i][j] = sum(a[i][p] * b[p][j] for p in range(k))
        print(f'Thread {i}, {j} computing')

def parseFile(txt):
    nums = txt.split()
    m,k,n = (int(x) for x in nums[:3])
    dims = (m, k, n)
    nums = nums[3:]
    a = [[float(nums[i * k + j]) for j in range(k)] for i in range(m)]
    nums = nums[(m * k):]
    b = [[float(nums[i * n + j]) for j in range(n)] for i in range(k)]
    return (dims, a, b)

def multiply(mats):
    dims, a, b = mats
    m,k,n = dims
    res = [[0.0 for i in range(n)] for j in range(m)]
    threads = [MyThread(mats, res, i, j) for i in range(n) for j in range(m)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return res

def print_matrix(mat):
    for row in mat:
        nstrs = ['{0:8.6}'.format(x) for x in row]
        print(' '.join(nstrs))

with open('input.txt', 'r') as f:
    txt = f.read()

print_matrix(multiply(parseFile(txt)))