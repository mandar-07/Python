class Student:
    def __init__(self, name):
        self.name = name
        print(f"Student {self.name} has been created.")

    def __del__(self):
        print(f"Student {self.name} has been deleted.")

s1 = Student("mandar")

del s1
