"""
A set of challenge functions.

"""
from collections import Counter, OrderedDict
from math import sqrt
from typing import Any, List, Union, Tuple


def array_diff(array_a: list, array_b: list) -> list:
    """Get those elements from the first array which are not in the second one."""
    return list(set(array_a) - set(array_b))


def binary_array_to_number(array: List[int]) -> int:
    """Convert an array of bits into an integer."""
    return int("".join(map(str, array)), base=2)


def is_array_squared(array_a: List[int], array_b: List[int]) -> bool:
    """Check whether the second array is equal to the first squared array."""
    return [i ** 2 for i in array_a] == array_b


def first_non_repeating_letter(string: str) -> str:
    """Get the first non repeating letter from the string."""
    try:
        return [i[0] for i in Counter(string.lower()).items() if i[1] == 1][0]
    except IndexError:
        return ""


def find_uneven_occurrences(array: List[int]) -> Union[int, None]:
    """Find the last one integer which occurs an odd number of times."""
    try:
        return [i[0] for i in Counter(array).items() if i[1] % 2 == 1][-1]
    except IndexError:
        return None


def count_vowels(string: str) -> int:
    """Count and return a number of vowels."""
    return sum([i[1] for i in Counter(string).items() if i[0] in ("a", "e", "i", "o", "u")])


def string_middle(string: str) -> str:
    """Get the middle part of a given string."""
    half = len(string) // 2
    return string[half : (half + 1)] if len(string) % 2 else string[(half - 1) : (half + 1)]


def find_substrings(array_a: List[str], array_b: List[str]) -> List[str]:
    """Find items in the first array which are substrings of elements of the second array."""
    return [a for a in array_a for b in array_b if a in b]


def is_square(number: Union[int, float]) -> bool:
    """Check whether a number is a square."""
    return sqrt(number).is_integer()


def is_triangle(sides: Tuple[Union[int, float], ...]) -> bool:
    """Check whether a triangle can be made using sides."""
    a, b, c = sorted(sides)
    return a + b > c


def move_zeros(array: List[Any]) -> List[Any]:
    """Move zeros at the end of a given array."""
    return sorted(array, key=lambda x: True if type(x) == int and x == 0 else False)


def bracket_validator(string: str) -> bool:
    """Check whether for each opening bracket an expression contains a counterpart of closing bracket."""
    string = "".join([i for i in string if i in "()"])
    while string.find("()") != -1:
        string = string.replace("()", "")
    return True if string == "" else False


def encrypt_message(string: str) -> str:
    """For a given message replace a single occurrence of letter with dot and multiple occurrence with star."""
    return "".join(["." if Counter(string)[i] == 1 else "*" for i in string])


def arabic_to_roman(number: int) -> str:
    """Convert a number in arabic to roman format."""
    roman_number = ""
    arabic = [i * j for i in (1, 10, 100) for j in range(1, 10)] + [1000]
    roman = "I II III IV V VI VII VIII IX X XX XXX XL L LX LXX LXXX XC C CC CCC CD D DC DCC DCCC CM M"
    arabic_roman = OrderedDict({a: r for a, r in zip(arabic, roman.split(" "))})
    thousands, number = divmod(number, 1000)

    while number:
        temp = list()
        for key, val in arabic_roman.items():
            quotient, remainder = divmod(number, key)
            if quotient == 1:
                temp.append((remainder, val))

        number, val = sorted(temp, key=lambda el: el[0])[0]
        roman_number += val

    return thousands * "M" + roman_number


def unique_in_order(string: str) -> str:
    """Remove duplicated consecutive signs from a given string."""
    result = "".join([i for i, j in zip(string, string[1:] + string[0]) if i != j])
    return result if string[0] != string[-1] else result + string[-1]
