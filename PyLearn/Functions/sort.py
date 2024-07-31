# basics
num = [1, 2, 3, -1]
num.sort()  # sorts in-place and alters the original list but wont return sorted array
print(num)

# SORTED
num2 = [1, 2, 3, -1]
sorted(num2)
print(num2)  # no change

# change the direction
print(sorted(num2, reverse=True))

print('-'*20)

#sort based on length
print(sorted(['aa', 'bbba', 'dnsakjdhsa', 's'], key=len))   # ['s', 'aa', 'bbba', 'dnsakjdhsa']

people = [
    {"name": "Bob", "age": 34, "occupation": "Doctor"},
    {"name": "Diana", "age": 30, "occupation": "Artist"},
    {"name": "Alice", "age": 28, "occupation": "Engineer"},
    {"name": "Charlie", "age": 25, "occupation": "Teacher"},
    {"name": "Edward", "age": 40, "occupation": "Chef"}
]

# sort alphbetically based on key --> person's name
print(sorted(people, key=lambda line: line["name"], reverse=False))

#sorting a hash map
accounts = {'accountA': {'timestamp': '10', 'balance': 1000, 'transactions': 1400}, 
            'accountC': {'timestamp': '12', 'balance': 900, 'transactions': 1300}, 
            'accountB': {'timestamp': '8', 'balance': 800, 'transactions': 1200}
}

print(sorted(accounts.items(), key=lambda account: account[1]["transactions"], reverse=True))  
''' if we do not give .items() by default the keys would be considered and keys would be sorted
    now we get an iterator with each item as ('accountA','{'timestamp': '10', 'balance': 1000, 'transactions': 1400}') and so on
    so to sort based on transactions, we need to do account[1]["transactions"]
'''

''' Applying sorted on a dict
dict.items() gives a iterator of tuples (k,v)
so applying the same on sortet we need to
sorted(dict.items(), key=lambda item: item[1])
'''
