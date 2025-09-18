class Mother:
    def mother_method(self):
        print("Method from Mother")

class Father:
    def father_method(self):
        print("Method from Father")

class Child(Mother, Father):
    def child_method(self):
        print("Method from Child")

c = Child()
c.mother_method()
c.father_method()
c.child_method()



