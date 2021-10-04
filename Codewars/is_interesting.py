def is_interesting(number, awesome_phrases):
    if len(str(number)) <= 2:
        return 0
    if number in awesome_phrases:
        return 2
    if number-1 in awesome_phrases or number-2 in awesome_phrases:
        return 1
    if len(str(number)) == str(number).count(str(number)[0]):
        return 2
    if len(str(number+2)) == str(number+2).count(str(number+2)[0]) or len(str(number+1)) == str(number+1).count(str(number+1)[0]):
        return 1
    if int(str(number)[1:]) == 0:
        return 2
    if int(str(number+1)[1:]) == 0 or int(str(number+2)[1:]) == 0:
        return 1
    for i in range(len(str(number))-1):
        if int(str(number)[i]) + 1 != int(str(number)[i + 1]):
            return 0
        else:
            print("kupa")
            return 2
    """for i in range(len(str(number+1))-1):
        if int(str(number)[i]) + 1 != int(str(number)[i + 1]):
            return 0
        else:
            return 1
    for i in range(len(str(number+2))-1):
        if int(str(number)[i]) + 1 != int(str(number)[i + 1]):
            return 0
        else:
            return 1"""
n = 1284
print(is_interesting(n,[1337, 256]))
