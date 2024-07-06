'''
Generator function are just functions which instead of using "return" keyword it uses "yield".

That means it can return multiple times.

So it basically returns an iterator.

and when yeild is invoked, it returns and stops there unitl the "next()" keyword is invoked.
'''


def count_up_to(n):
    count = 1
    while (count <= n):
        yield count
        count += 1


counts = count_up_to(5)

print(counts)  # <generator object count_up_to at 0x0000024EDB229970>

print(next(counts)) # prints 1
print(next(counts)) # prints 2

# prints 3,4,5
for num in counts:
    print(num)