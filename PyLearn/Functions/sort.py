# basics
num = [1, 2, 3, -1]
num.sort()  # sorts in-place and alters the original list
print(num)

# SORTED

num2 = [1, 2, 3, -1]
sorted(num2)
print(num2)  # no change

# change the direction
print(sorted(num2, reverse=True))

print('-'*20)

people = [
    {"name": "Bob", "age": 34, "occupation": "Doctor"},
    {"name": "Diana", "age": 30, "occupation": "Artist"},
    {"name": "Alice", "age": 28, "occupation": "Engineer"},
    {"name": "Charlie", "age": 25, "occupation": "Teacher"},
    {"name": "Edward", "age": 40, "occupation": "Chef"}
]

# sort alphbetically based on key --> person's name
print(sorted(people, key=lambda line: line["name"]))

print(sorted(people, key=lambda line: line["name"], reverse=True))

''' Applying sorted on a dict
dict.items() gives a iterator of tuples (k,v)
so applying the same on sortet we need to
sorted(dict.items(), key=lambda item: item[1])
'''
