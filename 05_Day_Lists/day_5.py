empty_list = list()
print(len(empty_list))

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
animal_products = ["milk", "meat", "butter", "yoghurt"]
web_techs = [
    "HTML",
    "CSS",
    "JS",
    "React",
    "Redux",
    "Node",
    "MongDB",
]
countries = ["Finland", "Estonia", "Denmark", "Sweden", "Norway"]

print("Fruits: ", fruits)
print("Number of fruits:", len(fruits))
print("\n")

print("Vegetables:", vegetables)
print("Number of vegetables:", len(vegetables))
print("\n")

print("Animal products:", animal_products)
print("Number of animal products:", len(animal_products))
print("\n")

print("Web technologies:", web_techs)
print("Number of web technologies:", len(web_techs))
print("\n")

print("Countries: ", countries)
print("Number of countries:", len(countries))
print("\n")

fruits = ["banana", "orange", "mango", "lemon"]
first_fruits = fruits[0]
print(first_fruits)
second_fruits = fruits[1]
print(second_fruits)
last_fruits = fruits[3]
print(last_fruits)
last_index = len(fruits) - 1
print("last_index", last_index)
last_fruits = fruits[last_index]
print(last_fruits)
print("\n")

fruits = ["banana", "orange", "mango", "lemon"]
last_fruits = fruits[-1]
second_last = fruits[-2]
print(last_fruits)
print(second_last)
print("\n")

# Slicing items
fruits = ["banana", "orange", "mango", "lemon"]
all_fruits = fruits[0:4]
print(all_fruits)
