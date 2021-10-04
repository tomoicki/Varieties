def get_middle(s):
    if len(s)/2 != int(len(s)/2):
        return print(s[int(len(s)/2)])
    else:
        return print(s[int((len(s)/2))-1:(int(len(s)/2))+1])

st = "middle"
get_middle(st)