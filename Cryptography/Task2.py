import numpy

cryptogram = 'HSEFKHDAWSRSCKBQMVMPLCRWLMTXTPFE'
#  jeśli długość ktryptogramu jest nieparzysta, dodajemy X na koniec
if len(cryptogram) % 2 != 0:
    cryptogram += 'X'
#  dzielimy łańcuch 'abcd...' na listę dwu-elementowych łańcuchów ['ab','cd',...]
cryptogram_in_parts = [cryptogram[i:i+2] for i in range(0, len(cryptogram), 2)]
print(cryptogram_in_parts)
key = 'RABATKA'
#  pozbywamy się duplikatów liter z zachowaniem kolejności
key = "".join([j for i, j in enumerate(key) if j not in key[:i]])

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'
for letter in key:
    #  z łańcucha alphabet usuwamy te litery, które wystepują w 'key'
    alphabet = alphabet.replace(letter, '')
#  łączymy key z alphabet
replaced_alphabet = key + alphabet
#  tworzymy listę pięcioznakowych list
five = []
for i in range(5):
    temp = []
    for j in range(5):
        temp.append(replaced_alphabet[i*5+j])
    five.append(temp)
#  tworzymy macierz
matrix = numpy.array(five)
#  krok ułatwiający późniejsze zlokalizowanie litery po współrzednych
index_elements = []
for i in numpy.ndindex(matrix.shape):
    index_elements.append((matrix[i], i))
index_elements = dict(index_elements)

revealed_text = ''
print(matrix, '\n')
for double_letter in cryptogram_in_parts:
    first = index_elements[double_letter[0]]
    second = index_elements[double_letter[1]]
    #  jeśli obie litery znajdują się w tym samym wierszu lub tej samej kolumnie
    if first[0] == second[0] or first[1] == second[1]:
        #  współrzędne (wiersz, kolumna) litery zastępującej
        #  równe są (wiersz_litery_zastepowanej, kolumna_litery_zastepowanej - 1)
        first_replacement = (first[0], first[1] - 1)
        second_replacement = (second[0], second[1] - 1)
        first_substitute = matrix[first_replacement[0], first_replacement[1]]
        second_substitute = matrix[second_replacement[0], second_replacement[1]]
    #  w przeciwnym razie
    else:
        #  współrzędne (wiersz, kolumna) litery zastępującej
        #  równe są (wiersz_litery_zastepowanej, kolumna_pary_litery_zastepowanej)
        first_replacement = (first[0], second[1])
        second_replacement = (second[0], first[1])
        first_substitute = matrix[first_replacement[0], first_replacement[1]]
        second_substitute = matrix[second_replacement[0], second_replacement[1]]
    print(double_letter + ' -> ' + first_substitute + second_substitute)
    revealed_text += first_substitute
    revealed_text += second_substitute
print()
print(revealed_text)

