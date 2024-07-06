my_dict = {'hey': 'hi', 1: 2}

print(my_dict['hey'], my_dict[1])

# iterating
for k, v in my_dict.items():  # [keys(), values(), items()]
    print(k, v)

print('hey' in my_dict)  # True
print(my_dict.get('hey'))  # hi , get a value using .get()

# removing
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_dict.pop('c')
del my_dict['a']  # both pop or del can be used
print(my_dict)  # Output: {'a': 1, 'b': 2}


# comprehension
print({k: v * 2 for k, v in my_dict.items()})  # the : is most important

my_dict2 = dict(name='joy', age='10', number='100')

print(my_dict2)

new_dict = {}

# new_dict['2'] = (new_dict['2']  or 0) + 1 This approach as JS wont work, we need the below syntax
new_dict['1'] = new_dict.get('1', 0) + 1

print(new_dict)