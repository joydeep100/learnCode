# tuples are immutable, they have order (index)

tuple = (1,2,3,4)

for num in tuple:
    print(num)

print(tuple[0])

'''dict.items() gives a iterator of tuples (k,v)

    so applying the same on sortet we need to

    sorted(dict.items(), key=lambda item: item[1])
'''