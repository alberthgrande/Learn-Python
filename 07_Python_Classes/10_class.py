class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person = Person("Alice", 30)

print(getattr(person, "name"))
print(getattr(person, "age"))
print(getattr(person, "gender"))