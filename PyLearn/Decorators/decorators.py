'''Decorators in Python are a powerful and flexible tool that allows you to modify 
or enhance the behavior of functions or methods. They are essentially functions that 
wrap another function, modifying its behavior without permanently changing it. 
Decorators are commonly used for tasks like logging, access control, memoization, 
and enforcing types.'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the decorated function is called")
        func()
        print("Something is happening after the decorated function is called")
    return wrapper  # vvi, to return the wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
