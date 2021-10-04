from collections import Counter


#  read 3000 most common english words
with open('3000_most_common_english_words.txt', 'r') as file:
    most_common_words = file.read().split('\n')
#  remove all 1-letter words such as 'a'
most_common_words = [item for item in most_common_words if len(item) >= 2]

with open('mono1.txt', 'r') as file:
    cryptogram = file.read()

english_letters_frequency = {'a': 0.082, 'b': 0.015, 'c': 0.028, 'd': 0.043, 'e': 0.13,
                             'f': 0.022, 'g': 0.02, 'h': 0.061, 'i': 0.07, 'j': 0.0015,
                             'k': 0.0077, 'l': 0.04, 'm': 0.024, 'n': 0.067, 'o': 0.075,
                             'p': 0.019, 'q': 0.00095, 'r': 0.06, 's': 0.063, 't': 0.091,
                             'u': 0.028, 'v': 0.0098, 'w': 0.024, 'x': 0.0015, 'y': 0.02,
                             'z': 0.00074}
english_letters_frequency = dict(sorted(english_letters_frequency.items(), key=lambda item: item[1], reverse=True))
english_letters_frequency = {key.upper(): value for key, value in english_letters_frequency.items()}

cryptogram_letters_count = dict(Counter(cryptogram))
cryptogram_letters_frequency = {key: round(value/len(cryptogram), 4) for key, value in cryptogram_letters_count.items()}
cryptogram_letters_frequency = dict(sorted(cryptogram_letters_frequency.items(), key=lambda item: item[1], reverse=True))

replacements_list = []
all_found_words = []
while True:
    print(f'Cryptogram:\n{cryptogram}')
    print(f'\nCryptogram letters frequency:\n{cryptogram_letters_frequency}')
    print(f'English language letters frequency:\n{english_letters_frequency}')
    letter_to_replace = input('\nLetter to replace: ')
    del cryptogram_letters_frequency[letter_to_replace]
    replacement_letter = input('Replacement letter: ').upper()
    del english_letters_frequency[replacement_letter]
    cryptogram = cryptogram.replace(letter_to_replace, replacement_letter)
    replacements_list.append(letter_to_replace + ' -> ' + replacement_letter)
    newly_found_words = set()
    newly_found_words.clear()
    found = False
    for word in most_common_words:
        if word.upper() in cryptogram:
            most_common_words.remove(word)
            all_found_words.append(word)
    print(f"\nAll words found so far {all_found_words}")
    print(f'You have replaced {replacements_list}')
    yesno = input("\nWant to change another letter? [y/n]:")
    if yesno == 'n':
        break
