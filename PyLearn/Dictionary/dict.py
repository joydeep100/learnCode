my_dict = {'hey': 'hi', 1: 2}

print(my_dict['hey'], my_dict[1])

# iterating
for k, v in my_dict.items():  # [keys(), values(), items()]
    print(k, v)

print('hey' in my_dict)  # True
print(my_dict.get('hey'))  # hi

# comprehension
print({k: v * 2 for k, v in my_dict.items()})  # the : is most important

my_dict2 = dict(name='joy', age='10', number='100')

print(my_dict2)