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
    res = [[0 for j in range(n)] for i in range(m)]
    for i in range(m):
        for j in range(n):
            res[i][j] = sum(a[i][p] * b[p][j] for p in range(k))
    return res

def print_matrix(mat):
    for row in mat:
        nstrs = ['{0:8.6}'.format(x) for x in row]
        print(' '.join(nstrs))

with open('input.txt', 'r') as f:
    txt = f.read()

print_matrix(multiply(parseFile(txt)))