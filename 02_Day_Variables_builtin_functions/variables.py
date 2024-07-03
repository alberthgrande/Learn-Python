first_name = "Alberth"
last_name = "Ruado"
country = "Philippines"
city = "Sariaya"
age = "25"
is_married = False
skills = ["HTML", "CSS", "JS", "PHP", "Python"] 
person_info = {
    "firstname" : "Alberth",
    "lastname" : "Ruado",
    "country" : "Philippines",
    "city" : "Sariaya"
} 

# Printing the values stored in the variables

print("First name : ", first_name)
print("First name length : ", len(first_name))
print("Last name : ", last_name)
print("Last name length : ", len(last_name))
print("Country : ", country)
print("City : ", city)
print("Age : ", age)
print("Married : ", is_married)
print("Skills : ", skills)
print("Personal Information : ", person_info)

# Declaring multiple variables in one line

first_name, last_name, country, age, is_married = "Alberth", "Ruado", "Philippines", 25, False
print(first_name, last_name, country, age, is_married)
print("First name : ", first_name)
print("Last name : ", last_name)
print("Country : ", country)
print("Age : ", age)
print("Married : ", is_married)
