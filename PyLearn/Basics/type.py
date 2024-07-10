print(type('') is str)  # All are True
print(type([]) is list)
print(type(()) is tuple)
print(type({}) is dict)
print(type(set()) is not set)  # false

# Check if x is an instance of int
print(isinstance(10, int))  # Output: True

# Check if x is an instance of float
print(isinstance(10, float))  # Output: False
