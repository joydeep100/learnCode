# *args (or any name) will collect all args as a tuple
def fun(num1, *args):
    total = num1
    for num in args:
        total += num
    return total

print(fun(1, 2, 3, 4))  # 10

# *args unpacking
def fun(num1, *args):
    total = num1
    for num in args:
        total += num
    return total

print(fun(*[1, 2, 3, 4]))  # 10

# **kwargs (or any name) will collect all args as named arguments or a dict
def fun2(**kwargs):

    for k,v in kwargs.items():
        print(k,v)

fun2(name='joy', age='10', number='100')

# **kwargs unpacking
def fun2(**kwargs):

    for k,v in kwargs.items():
        print(k,v)

fun2(**dict(name='joy', age='10', number='100'))