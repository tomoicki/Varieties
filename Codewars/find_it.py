def find_it(seq):
    for item in seq:
        if seq.count(item)/2 != int(seq.count(item)/2):
            found = item
    return found

arr = [20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]
find_it(arr)