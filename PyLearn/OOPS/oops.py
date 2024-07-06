class First:

    #this is a class variable [2]
    active_users = 0

    '''This is a dunger method which starts with __ , 
       We should override this only in case we need to alter the behaviour of existing functionality
    '''
    def __init__(self, arg1): 
        self.arg1 = arg1
        self.__secret = 'not a secret' # any variable declared like this would be mangled [1]
        First.active_users+=1 # we need to invoke this this for [2]

    def get_arg1(self):
        print(self.arg1)

    @classmethod
    def fun(cls, arg1, arg2): # SUPER IMP, pass **cls** instead of self
        print(arg1 + arg2)

first = First(1)
first.get_arg1()


'''
dir & help
The dir() function is used to list the attributes and methods of an object. 
It provides a way to see what operations and properties are available for any object in Python.
dir([object])
'''
print(dir(first)) # we can see out secret var looks like this now '_First__secret' , Top Secret!!

'''
The help() function is used to display the documentation of modules, functions, classes, keywords, etc. 
It is an interactive way to get more information about Python objects.
help([object])
'''
print(help(first))

print(First.active_users) # for [2]

print(First.fun('hi', 'bye'))
