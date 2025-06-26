# import pandas
# pandas.read_csv()
#
# import math
# result = math.sqrt(9)
# print(result)

# from math import sqrt, pi
# result = sqrt(9) * pi
# print(result)

import math as m
# res = m.sqrt(9) * m.pi
# print(res)

# import math
# print(dir(math))
# print(math.nan, type(math.nan))

# import random
# res = random.randint(1, 10)
# print("Random number:", res)

#importing everything from module
# from math import *
# print(pi)
# print(factorial(6))

try:
    import mathematics
    print(mathematics.pi)
except ImportError:
    print("Module not found! Please check the module name or install it if necessary")