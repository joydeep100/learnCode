# set have only unique values and they do not have order (index)
# they are mutable

s = set({1, 2, 3, 3})

print(s)  # the second 3 is gone

print(1 in s)  # True

for num in s:
    print(num)

s.add(4)
s.remove(1)

print(s)

# common
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

intersection = set1 & set2
print(intersection)  # Output: {3, 4}

# difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

difference = set1 - set2
print(difference)  # Output: {1, 2}

# to make the set immutable
frozen = frozenset([1, 2, 3, 4])
print(frozen)  # Output: frozenset({1, 2, 3, 4})