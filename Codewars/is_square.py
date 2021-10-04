def is_square(n):
    if n >= 0 and n**0.5 == int(n**0.5):
        return True
    else:
        return False

number = int(input("Enter a number: "))
print(is_square(number))