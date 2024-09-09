# set (also known as hash sets) have only unique values and they do not have order (index)
# they are mutable

# *** VVI *** - sets are represented using { }
s0 = set({1, 2, 3})  # or s = {1,2,3}
print(s0)  # 1,2,3

# Create a new hash set
s = set()  # or set({1, 2, 3, 3})


s.add(1)
s.add(2)
s.add(3)
s.add(3)
print(s)  # the second 3 is gone

print(1 in s)  # True

for num in s:
    print(num)

s.add(4)
s.remove(1)  # will raise KeyError if not found
s.clear() # to purge set

print(s)

# common in both
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1 & set2
print(intersection)  # Output: {3, 4}

# difference [1]
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference = set1 - set2
print(difference)  # Output: {1, 2} , [1] which is in set1 but not in set2

# unique
'''
unique_to_1 = set1 - set2
unique_to_2 = set2 - set1

return sorted(list(unique_to_1)), sorted(list(unique_to_2))

'''
# subset
set1 = {1, 2}
set2 = {1, 2, 3}
print(set1.issubset(set2))  # Output: True

# superset
set1 = {1, 2, 3}
set2 = {1, 2}
print(set1.issuperset(set2))  # Output: True


# to make the set immutable
frozen = frozenset({1, 2, 3, 4})
print(frozen)  # Output: frozenset({1, 2, 3, 4})

# Add / Lookup / Remove is O(1) in a set and space wise its O(n)
