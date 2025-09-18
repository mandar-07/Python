class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, sound):
        super().__init__(name)
        self.sound = sound

d = Dog("rock", "barking")
print(f"{d.name} is {d.sound}") 