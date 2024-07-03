import math

radius = 30

area_of_cirle = math.pi * (radius ** 2)
circum_of_circle = 2 * math.pi * radius

user_radius = float(input("Enter the radius of the circle:"))
user_area_of_cirle = math.pi * (user_radius ** 2)

print("Area of circle : ", area_of_cirle)
print("Circumference of circle : ", circum_of_circle)
print("User area of circle : ", user_area_of_cirle)
