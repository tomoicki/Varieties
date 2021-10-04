def unique_in_order(iterable):
    result = []
    for i in range(len(iterable)-1):
        if iterable[i] != iterable[i+1]:
            result.append(iterable[i])
    if len(iterable) != 0:
        result.append(iterable[-1])
    return result
s = 'ABBCcAD'
print(unique_in_order(s))
