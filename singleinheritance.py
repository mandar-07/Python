class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

Name=input("Enter name of dog :")
d = Dog(Name)
d.info()      
d.sound()