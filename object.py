class MyClass:
    def __init__(self):
        self.public = "I am public"
        self._protected = "I am protected"
        self.__private = "I am private"

    def public_method(self):
        return "This is a public method."

    def _protected_method(self):
        return "This is a protected method."

    def __private_method(self):
        return "This is a private method."

    def access_private_method(self):
        return self.__private_method()

obj = MyClass()

print(obj.public)
print(obj._protected)


print(obj.public_method())
print(obj._protected_method())


print(obj._MyClass__private)
print(obj.access_private_method())
