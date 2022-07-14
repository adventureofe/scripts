# required for reduce
from functools import reduce

# functions are arguments
add= lambda a, b : a + b
mult= lambda a, b : a * b
minus= lambda a, b: a - b
divide= lambda a, b : a / b
calculate = lambda a, b, func: func(a, b)

print(calculate(5, 6, mult))
print(calculate(7, 8, add))

# returning a function
def divisor(x):
    def dividend(y):
        return y / x

    return dividend

divide_this = divisor(2)
print(divide_this(10))


#map an array

areas = [123, 12, 161, 767, 1324]

doubled_areas = list(map(lambda area : area * 2, areas))
print(doubled_areas)

even_areas = list(filter(lambda area: area % 2 == 0, areas))
print(even_areas)

# NONE triggers off "", 0, 0.0, [], (), False, None
string_list = ["", "Argentina", "Brazil", "", "Chile", "Columbia", "", "Ecuador"]
filtered_list = list(filter(None, string_list))
print(filtered_list)

# applies function to first 2 terms
# applied to output and term 3
# applied to output and term 4

primes = [2,3,5,7,11,13,17,19,23,29]
added_primes = reduce(add, primes)
multiplied_primes = reduce(mult, primes)
print(added_primes)
print(multiplied_primes)
