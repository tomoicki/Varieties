def move_zeros(array):
    for i in range(len(array)):
        if type(array[i]) == int and array[i] == 0:
            array.remove(array[i])
            array.append(array[i])
    return array
array = [False,1,0,1,2,0,1,3,"a"]
print(move_zeros(array))
