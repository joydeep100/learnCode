class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        raise NotImplementedError("Subclass must implement this method")

    def describe(self):
        return f"{self.name} is a {self.species}"

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Dog") # see no self
        self.breed = breed

    def make_sound(self):
        return "Woof!"

    def describe(self):
        return f"{self.name} is a {self.breed} {self.species}"
