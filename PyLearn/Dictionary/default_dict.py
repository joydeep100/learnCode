'''
defaultdict is a subclass of dict that provides default values for non-existent keys. 
This can be particularly useful when dealing with dictionaries where you expect missing keys.
'''
from collections import defaultdict

# Example usage
default_dict = defaultdict(int)
default_dict['a'] += 1
print(default_dict)  # Output: defaultdict(<class 'int'>, {'a': 1})
