def is_triangle(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    else:
        return False

a = 1
b =2
c =3
print(is_triangle(a,b,c))