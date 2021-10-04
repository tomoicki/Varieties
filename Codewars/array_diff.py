def array_diff(a, b):
    for b_element in b:
        a[:] = (value for value in a if value != b_element)
    return a

a = [1,2,2,2,3]
b = [2]
c = array_diff(a,b)
print(c)