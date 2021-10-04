def comp(array1, array2):
    if type(array1) != list or type(array2) != list or len(array1) != len(array2):
        return False
    else:
        while len(array1) > 0:
            try:
                for i in range(len(array2) + 1):
                    if array1[0] ** 2 == array2[i]:
                        array1.pop(0)
                        array2.pop(i)
                        break
                    else:
                        i += 1
            except IndexError:
                return False
        return True
"""
def comp(array1, array2):
    try:
        return sorted([i ** 2 for i in array1]) == sorted(array2)
    except:
        return False
"""
a = [121, 144, 19, 161, 19, 144, 19, 11]
b = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp(a,b))