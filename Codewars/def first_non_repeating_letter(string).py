def first_non_repeating_letter(string):
    i = 0
    if len(string) == 0:
        return ""
    for letter in string:
        if string.lower().count(letter.lower()) == 1:
            return letter
        i += 1
        if i == len(string):
            return ""


s = "AabbDNneccddffgg"
print(first_non_repeating_letter(s))