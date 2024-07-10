class Animal:
    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Function that demonstrates polymorphism
def animal_sound(animal):
    print(animal.make_sound())

# Creating instances of the child classes
dog = Dog()
cat = Cat()

# Using the same function to call methods on different objects
animal_sound(dog)  # Output: Woof!
animal_sound(cat)  # Output: Meow!
