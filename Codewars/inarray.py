def in_array(array1, array2):
    r = []
    array1 = sorted(list(dict.fromkeys(array1)))
    for item1 in array1:
        for item2 in array2:
            if item1 in item2:
                r.append(item1)
                break
    return print(r)
a1 = ["live", "arp", "strong"]
a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
in_array(a1,a2)