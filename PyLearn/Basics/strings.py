# f-string
a = 1
print(f"hi, the value of a is {a}")

# other approach (format)
print("hi my name is {}".format("joydeep"))

# Input
name = input("What is your name :")

print('hello'.upper())
print('HELLO!'.lower())

# sorted and reversed
print(''.join(list(reversed('hello'))))
print(''.join(list(sorted('hello'))))

# default delimited is ' ', so this is same as .split()
print('hello world'.split(' '))

list = [1, 2, 3]

print(eval('list[' + '0' + ']'))

# ternary
# return "Positive" if num > 0 else "Negative"