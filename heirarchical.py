class Parent:
    def parent_method(self):
        print("Method from Parent")

class Child1(Parent):
    def child1_method(self):
        print("Method from Child1")

class Child2(Parent):
    def child2_method(self):
        print("Method from Child2")

c1 = Child1()
c2 = Child2()
c1.parent_method()
c1.child1_method()
c2.parent_method()
c2.child2_method()
