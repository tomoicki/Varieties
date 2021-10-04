string_numbers = {key: value for value, key in enumerate('zero one two three four five six seven eight nine ten '
                                                         'eleven twelve thirteen fourteen fifteen sixteen seventeen '
                                                         'eighteen nineteen'.split())}
string_numbers.update({key: 10 * value for value, key in enumerate('twenty thirty forty fifty sixty seventy eighty '
                                                                   'ninety hundred'.split(), 2)})
string_llions = {key: 1000 ** value for value, key in enumerate('thousand million'.split(), 1)}

def parse_int(string):
    llions = hundreds = number = 0
    for word in string.replace('-', ' ').replace(' and ', ' ').split():
        if word == 'hundred':
            hundreds = number * string_numbers[word]
            number = 0
        elif word in string_numbers:
            number += string_numbers[word]
        else:
            llions = (number + hundreds) * string_llions[word]
            number = hundreds = 0
    return llions + hundreds + number

print(parse_int('six hundred forty-four thousand eight hundred eighty-seven'))
