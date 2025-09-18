class Greeter:
    def greet(self, name, formal=False):
        if formal:
            print(f"Good day, Mr./Ms. {name}.")
        else:
            print(f"Hello, {name}!")


person = Greeter()


person.greet("Alice")


person.greet("Bob", True)