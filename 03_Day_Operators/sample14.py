# Even numbers are divisible by 2 and the remainder is zero. How do you check if a number is even or not using python?

input_num = int(input("Enter a number: "))

if input_num % 2 == 0:
    print("Even")
else:
    print("Odd")
