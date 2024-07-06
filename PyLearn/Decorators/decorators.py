def wrapper_parent_func(fun):
    ''' we have to define a wrapper function'''
    def wrapper(): 
        fun()
        print('Now I have extended the functionality\n')
    return wrapper # vvi, notice the return position here

def greet():
    print("Hi my name is joy")

@wrapper_parent_func
def greet_sugar():
    print("Hi my name is joy, I am also having super power")

# now there are two ways to call this 1. using old school way

wrapped_greet = wrapper_parent_func(greet)
wrapped_greet()

# or lets try using the syntactic sugar @wrapper_func
greet_sugar()
