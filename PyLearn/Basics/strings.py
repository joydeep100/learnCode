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
