# any(iterable) - returns true if any one is True
# all(iterable) - returns true if all items are True

numbers = [-1, -2, -3, 4, -5]

# Check if there is any positive number in the list
print(any(num > 0 for num in numbers)) # True
print(all(num > 0 for num in numbers)) # False


