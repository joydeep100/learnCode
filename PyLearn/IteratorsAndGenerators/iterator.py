# Iterable vs Iterator

'''
Usuablly objects which can be looped over are called Iterable, ex. Strings, List, Dict, Tuple, Set etc

Iterator is the object on which we can call next. 

So when we do a for loop over a iterable, say a list. what happens behind the scene is.

list = [1,2,3]
it = iter(list) # this produces a iterator object on which we can call next until "StopIteration" error is seen

so we can do
next(it) => 1
next(it) => 2
next(it) => 3
next(it) => StopIteration Error
'''

# writing our own for loop


def my_for(iterable):

    iterator = iter(iterable)
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            print("END OF LOOP")
            break


my_for("hello")

'''
h
e
l
l
o
END OF LOOP
'''

# custom iterator


class MyIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0

    def __iter__(self):  # imp step
        return self     # imp step, this means you are specifying that the instance of the class itself is an iterator.

    def __next__(self):
        if self.index < len(self.data):
            result = self.data[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration


# Create an instance of MyIterator
my_iter = MyIterator([1, 2, 3, 4, 5])

# Iterate through the iterator using a for loop
for item in my_iter:
    print(item)
