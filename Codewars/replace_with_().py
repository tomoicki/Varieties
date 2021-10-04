def duplicate_encode(word):
    translation = ""
    word = word.lower()
    for letter in word:
        if word.count(letter) == 1:
            translation += "("
        else:
            translation += ")"
    return translation

word = input("Enter a word: ")
translation = duplicate_encode(word)
print(translation)