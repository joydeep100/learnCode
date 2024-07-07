print(type(9))  # <class 'int'>
print(type(1.2))  # <class 'float'>

print(4/2)  # its 2.0 and not 2, we can use 4//2 if we need integer divistion

name = "joydeep"
print(f"My name is {name}")

''' important operators

** exponentiaition
// integer division

is vs ==

is checks if they are stored in same memory address.
== checks for equality of values

'''

# abs, sum and round

print(abs(-1))

print(sum((1,2,3)))

print(round(10/3)) # 3
print(round(10/3, 2)) # 3.33

# count++ is invalid in python

import random

random_integer = random.randint(1, 10) # 1 and 10 inclusive

# type case int() | str() | float()

# rounding
round(1.5) # 2
round(1.4) # 1
round(3.1423, 2) # 3.14

# floor and ceil
import math
math.ceil(3.7) # 4
math.ceil(3.1) # 4 this is also 4 !!!
