class Grandparent:
    def grandparent_method(self):
        print("Method from Grandparent")

class Parent(Grandparent):
    def parent_method(self):
        print("Method from Parent")

class Child(Parent):
    def child_method(self):
        print("Method from Child")

c = Child()
c.grandparent_method()
c.parent_method()
c.child_method()
