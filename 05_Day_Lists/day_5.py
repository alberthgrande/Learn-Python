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
all_fruits = fruits[0:4]  # 0 is the starts and 4 is the ends
print(all_fruits)
# this is also give the same result as the above
all_fruits = fruits[0:]  # if we don't set where to stop it takes all the rest
print(all_fruits)
orange_and_mango = fruits[1:3]  # it does not include the end index
orange_mango_lemon = fruits[-3:]
print(orange_and_mango)
print(orange_mango_lemon)
print("\n")

fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
print(fruits)
fruits[1] = "apple"
print(fruits)
fruits = ["banana", "orange", "mango", "lemon"]
last_index = fruits[-4:]  # it returns all the fruits
# this is also give the same result as the above
orange_and_mango = fruits[-3:-1]  # it does not include the end index
orange_mango_lemon = fruits[-3:]
print(orange_and_mango)
print(orange_mango_lemon)

print("\n")
fruits = ["banana", "orange", "mango", "lemon"]
fruits[0] = "avocado"
fruits[1] = "apple"
last_index = len(fruits) - 1  # get the last index
fruits[last_index] = "lime"  # change the value of the last index
print(fruits)
print("\n")

# checking items
fruits = ["banana", "orange", "mango", "lemon"]
does_exist = "banana" in fruits
print(does_exist)
does_exist = "lime" in fruits
print(does_exist)
print("\n")

# Append
fruits = ["banana", "orange", "mango", "lemon"]
fruits.append("apple")  # append() builtin method add at the end of array list
print(fruits)
fruits.append("lime")
print(fruits)
print("\n")

# insert
fruits = ["banana", "orange", "mango", "lemon"]
fruits.insert(0, "strawberry")  # 0 is the position and strawberry is the value
print(fruits)
fruits.insert(1, "peach")
print(fruits)
print("\n")

# remove
fruits.remove("banana")
print(fruits)
fruits.remove("lemon")
print(fruits)
print("\n")

# pop
fruits = ["banana", "orange", "mango", "lemon"]
fruits.pop()  # pop() remove the item on the end of the array list
print(fruits)
fruits.pop(
    0
)  # by adding a value on the pop method you can removed the value on the array list on its position
print(fruits)
print("\n")


# del
fruits = ["banana", "orange", "mango", "lemon"]
del fruits[0]
print(fruits)

# del fruits
# print(fruits)  # This should give: NameError: name 'fruits' is not defined

print("\n")

# clear
fruits = ["banana", "orange", "mango", "lemon"]
fruits.clear()
print(fruits)  # []


# copying a lits
fruits = ["banana", "orange", "mango", "lemon"]
fruits_copy = fruits.copy()
print(fruits_copy)
print("\n")

# join
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]
negative_numbers = [-5, -4, -3, -2, -1]
integers = negative_numbers + zero + positive_numbers
print(integers)
print("\n")

# join with extend
num1 = [0, 1, 2, 3]
num2 = [4, 5, 6]
num1.extend(num2)
print("Numbers:", num1)
print("\n")

negative_numbers = [-5, -4, -3, -2, -1]
positive_numbers = [1, 2, 3, 4, 5]
zero = [0]

negative_numbers.extend(zero)
negative_numbers.extend(positive_numbers)
print("Integers:", negative_numbers)

fruits = ["banana", "orange", "mango", "lemon"]
vegetables = ["Tomato", "Potato", "Cabbage", "Onion", "Carrot"]
fruits_and_vegetables = fruits + vegetables
print(fruits_and_vegetables)
print("\n")

# count
fruits = ["banana", "orange", "mango", "lemon"]
print("Banana count:", fruits.count("banana"))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("Age count:", ages.count(24))
print("\n")

# index
fruits = ["banana", "orange", "mango", "lemon"]
print("Index of banana:", fruits.index("banana"))
ages = [22, 19, 24, 25, 26, 24, 25, 24]
print("Index of age 24: ", ages.index(24))
print("\n")

# Reverse
fruits = ["banana", "orange", "mango", "lemon"]
fruits.reverse()
print("Revers the fruits: ", fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.reverse()
print("Reverse ages:", ages)
print("\n")

# sort
fruits = ["banana", "orange", "mango", "lemon"]
fruits.sort()
print(fruits)
ages = [22, 19, 24, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
