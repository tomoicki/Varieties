def valid_parentheses(string):
    temp = []
    for letter in string:
        if letter == '(':
            temp.append(letter)
        elif letter == ')':
            try:
                temp.pop()
            except:
                return False
    if len(temp) == 0 :
        return True
    else:
        return False

print(valid_parentheses("(())((()())())"))