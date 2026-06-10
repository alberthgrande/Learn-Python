class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name.upper()} says woof woof! I'm {self.age} years old!")

dog_1 = Dog('Buddy', 3)
dog_2 = Dog('Max', 5)

dog_1.bark()
dog_2.bark()

print(dog_1.name)
