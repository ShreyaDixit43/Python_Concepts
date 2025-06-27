def double(x):
    return x*2

double = lambda x: x*2
cube = lambda x: x*x*x
avg = lambda x,y: (x + y) / 2
avg1 = lambda x,y,z:(x+y+z) / 2

print(double(5))
print(cube(5))
print(avg(3,5))
print(avg1(4, 6, 7))

#lambda function to calculate product of two numbers,
prod = lambda x, y: print(f'{x} * {y} = {x * y}')
print(prod(3, 4))

#lamda with list comprehension
li = [lambda arg=x: arg * 10 for x in range(1, 5)]
for i in li:
    print(i())

#lambda if-else
check = lambda x:"Even" if x%2 ==0 else "odd"
print(check(4))

#filter()
# Example: Filter even numbers from a list
n = [1, 2, 3, 4, 5, 6]
even = filter(lambda x: x % 2 == 0, n)
print(list(even))

#map()
# Example: Double each number in a list
a = [1, 2, 3, 4]
b = map(lambda x: x * 2, a)
print(list(b))

#reduce()
from functools import reduce
# Example: Find the product of all numbers in a list
a = [1, 2, 3, 4]
b = reduce(lambda x, y: x * y, a)
print(b)
