''' Takes cls are first parameter, applies to all instance of the class. '''
class MyClass:
    class_variable = 0

    def __init__(self):
        MyClass.class_variable += 1

    @classmethod
    def get_class_variable(cls):
        return cls.class_variable

    @classmethod
    def set_class_variable(cls, value):
        cls.class_variable = value

# Create instances
obj1 = MyClass()
obj2 = MyClass()


# Call class method
print(MyClass.get_class_variable())  # Output: 2
print(obj1.get_class_variable())     # Output: 2
obj1.set_class_variable(20)   
print(obj1.get_class_variable())     # Output: 20

# Static Method -------------------------------------------------------
'''  It behaves like a regular function but belongs to the class's namespace. '''

class MyClass:
    @staticmethod
    def add(x, y):
        return x + y

# Call static method
print(MyClass.add(5, 3))  # Output: 8
obj = MyClass()
print(obj.add(5, 3))      # Output: 8
