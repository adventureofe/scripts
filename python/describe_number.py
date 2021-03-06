#describer
from math import sqrt

def is_fibonacci(x):
    c = 0
    a = 1
    b = 1
    if x == 0 or x == 1:
        return True

    while c < x:
        c = a + b
        b = a
        a = c
    if c == x:
        return True
    else:
        return False

def is_pentagonal(n):
    k = (sqrt(24*n+1)+1)/6
    return k.is_integer()

def is_hexagonal(x):
    x = ((sqrt(8 * x + 1) +1) / 4)
    return x.is_integer()

def odd_or_even(x):
    if(x % 2 == 0):
        return True;
    return False;

is_triangular = lambda x: (0.5 * ((8 * x + 1) ** 0.5 - 1)).is_integer()

def is_square(n):
    if n<1:
        return False
    else:
        for i in range(int(n/2)+1):
            if (i*i)==n:
                return True
        return False

def describe(x):
    print("Describing", x)
    print(x, f"in binary = {x :b}")
    print(x, f"in octal = {x :o}")
    print(x, f"in hexadecimal = {x :X}")

    if(odd_or_even(x)):
        print(x, "is even")
    else:
        print(x, "is odd")

    print()

    if(is_triangular(x)):
        print(x, "is triangular")

    if(is_square(x)):
        print(x, "is square")

    if(is_pentagonal(x)):
        print(x, "is pentagonal")

    if(is_hexagonal(x)):
        print(x, "is hexagonal")

    if(is_fibonacci(x)):
        print(x, "is a fibonacci number")

    print()

    def descr()



describe(34)
describe(55)
