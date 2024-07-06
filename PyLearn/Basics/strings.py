# f-string
a = 1
print(f"hi, the value of a is {a}")

# better approach (format)
print("hi my name is {}".format("joydeep"))

# Input
name = input("What is your name :")

print("Name entered is {}".format(name))

print('hello'.upper())
print('HELLO!'.lower())

print(''.join(list(reversed('hello'))))

# default delimited is ' ', so this is same as .split()
print('hello world'.split(' '))

list = [1, 2, 3]

print(eval('list[' + '0' + ']'))

# ternary
# return "Positive" if num > 0 else "Negative" if num < 0 else "Zero"

word = "banana"
sorted_word = sorted(word)
print(sorted_word)  # Output: ['a', 'a', 'a', 'b', 'n', 'n']
print(''.join(sorted_word))  # this would output full word
