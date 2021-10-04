def binary_array_to_number(arr):
    solution = 0
    max_pow = len(arr)
    print(len(arr))
    i = 1
    for element in arr:
        print(element)
        solution += element*(2**(max_pow-i))
        i+=1
    return solution
array = [1, 1, 1, 1]
print(binary_array_to_number(array))