'''
Generator function are just functions which instead of using "return" keyword it uses "yield".
That means it can return multiple times.
So it basically returns an iterator.
and when yeild is invoked, it returns and stops there unitl the "next()" keyword is invoked.

A generator object is a special type of iterator that is produced by a generator function or 
a generator expression. It allows you to iterate over a sequence of values lazily, 
meaning it generates items one at a time and only when required, 
instead of storing the entire sequence in memory at once.

Advantages 
- improved memory efficiency
- lesser processing overheads
'''

def count_up_to(n):
    count = 1
    while (count <= n):
        yield count
        count += 1

counts = count_up_to(5) # will return me
# print(counts)  # <generator object count_up_to at 0x0000024EDB229970>
# print(next(counts)) # prints 1
# print(next(counts)) # prints 2

while True:
    try:
        print(next(counts))
    except StopIteration:
        print("END OF LOOP")
        break



