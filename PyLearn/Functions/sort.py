# basics
num = [1, 2, 3, -1]
num.sort()  # sorts in-place and alters the original list
print(num)

num2 = [1, 2, 3, -1]
sorted(num2)
print(num2)  # no change

# change the direction
print(sorted(num2, reverse=True))

people = [
    {"name": "Bob", "age": 34, "occupation": "Doctor"},
    {"name": "Diana", "age": 30, "occupation": "Artist"},
    {"name": "Alice", "age": 28, "occupation": "Engineer"},
    {"name": "Charlie", "age": 25, "occupation": "Teacher"},
    {"name": "Edward", "age": 40, "occupation": "Chef"}
]
# sort alphbetically based on key --> person's name
print(sorted(people, key=lambda person: person["name"]))
