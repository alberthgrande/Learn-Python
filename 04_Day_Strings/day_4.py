# Single line comment
letter = "A"  # A string could be a single character or a bunch of text
print(letter)  # P
print(len(letter))  # 1
greeting = "Hello, World!"  # A string couble a single or double qoute, "Hello, World!"
print(greeting)  # Hello, World!
print(len(greeting))  # 13
sentence = "I hope you are enjoying 30 days of python challenge"
print(sentence)

# Multiline String
multiline_string = """I am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)
# Another way of doing the same thing
multiline_string = """\nI am a teacher and enjoy teaching.
I didn't find anything as rewarding as empowering people.
That is why I created 30 days of python."""
print(multiline_string)

# String concatenation
first_name = "Alberth"
last_name = "Ruado"
space = " "
full_name = first_name + space + last_name
print("\n")
print(full_name)
# Checking length of string using len() built in function
print(len(first_name))
print(len(last_name))
print(len(first_name) > len(last_name))
print(len(full_name))

#### Unpacking characters
language = "Python"
a, b, c, d, e, f = language
print("\n")
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print("\n")

# Accessing characters in string by index
first_letter = language[0]
print(first_letter)
second_letter = language[1]
print(second_letter)
last_index = len(language) - 1
last_letter = language[last_index]
print(last_letter)
print("\n")

# If we want to start from right end we can use negative indexing. -1 is the last index
last_letter = language[-1]
print(last_letter)
second_last = language[-2]
print(second_last)
print("\n")

# Slicing
first_three = language[0:3]
print(first_three)
last_three = language[3:6]
print(last_three)
print("\n")

# Another way
last_three = language[-3:]
print(last_three)
last_three = language[3:]
print(last_three)
print("\n")

# Skipping character while splitting Python strings
pto = language[0:6:2]  # 0 is start, 6 is stop, 2 is step
print(pto)
print("\n")

# Escape sequence
print("I hope every one enjoying the python challenge.\nDo you?")
print("Days\tTopics\tExercise")
print("Day 1\t3\t5")
print("Day 2\t3\t5")
print("Day 3\t3\t5")
print("Day 4\t3\t5")
print("This is a back slash  symbol (\\)")  # To write a back slash
print('In every programming language it starts with "Hello, World!"')
print("\n")

## String Methods
# capitalize(): Converts the first character the string to Capital Letter

challenge = "thirty day of python"
print(challenge.capitalize())
print("\n")

# count(): returns occurrences of substring in string, count(substring, start=.., end=..)
print(challenge.count("y"))
print(challenge.count("y", 7, 14))
print(challenge.count("th"))
print("\n")

# endswith(): Checks if a string ends with a specified ending
print(challenge.endswith("on"))
print(challenge.endswith("tion"))
print("\n")

# expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
challenge = "thirty\tdays\tof\tpython"
print(challenge.expandtabs())
print(challenge.expandtabs(10))
print("\n")


# find(): Returns the index of first occurrence of substring
print(challenge.find("y"))
print(challenge.find("th"))
print("\n")

# format()	formats string into nicer output
first_name = "Alberth"
last_name = "Ruado"
job = "PHP Developer"
country = "Philippines"
sentence = "I am {} {}. I am a {}. I live in {}.".format(
    first_name, last_name, job, country
)
print(sentence)
print("\n")

radius = 30
pi = 3.14
area = pi * radius**2
result = "The area of circle with {} is {}.".format(str(radius), str(area))
print(result)
print("\n")

# isalnum(): Checks alphanumeric character

challenge = "ThirtyDaysPython"
print(challenge.isalnum())  # True

challenge = "30DaysPython"
print(challenge.isalnum())  # True

challenge = "thirty days of python"
print(challenge.isalnum())  # False

challenge = "thirty days of python 2019"
print(challenge.isalnum())  # False
print("\n")

# isalpha(): Checks if all characters are alphabets

challenge = "thirty days of python"
print(challenge.isalpha())  # True
num = "123"
print(num.isalpha())  # False
print("\n")

# isdecimal(): Checks Decimal Characters

challenge = "thirty days of python"
print(challenge.find("y"))  # 5
print(challenge.find("th"))  # 0
print("\n")

# isdigit(): Checks Digit Characters

challenge = "Thirty"
print(challenge.isdigit())  # False
challenge = "30"
print(challenge.isdigit())  # True
print("\n")

# isdecimal():Checks decimal characters

num = "10"
print(num.isdecimal())  # True
num = "10.5"
print(num.isdecimal())  # False
print("\n")

# isidentifier():Checks for valid identifier means it check if a string is a valid variable name

challenge = "30DaysOfPython"
print(challenge.isidentifier())  # False, because it starts with a number
challenge = "thirty_days_of_python"
print(challenge.isidentifier())  # True
print("\n")

# islower():Checks if all alphabets in a string are lowercase

challenge = "thirty days of python"
print(challenge.islower())  # True
challenge = "Thirty days of python"
print(challenge.islower())  # False
print("\n")

# isupper(): returns if all characters are uppercase characters

challenge = "thirty days of python"
print(challenge.isupper())  #  False
challenge = "THIRTY DAYS OF PYTHON"
print(challenge.isupper())  # True
print("\n")

# isnumeric():Checks numeric characters

num = "10"
print(num.isnumeric())  # True
print("ten".isnumeric())  # False
print("\n")

# join(): Returns a concatenated string

web_tech = ["HTML", "CSS", "JavaScript", "React"]
result = " , ".join(web_tech)
print(result)  # 'HTML# CSS# JavaScript# React'
print("\n")

# strip(): Removes both leading and trailing characters

challenge = " thirty days of python "
print(challenge.strip())  # 5
print("\n")


# replace(): Replaces substring inside

challenge = "thirty days of python"
print(challenge.replace("python", "coding"))  # 'thirty days of coding'
print("\n")

# split():Splits String from Left

challenge = "thirty days of python"
print(challenge.split())  # ['thirty', 'days', 'of', 'python']
print("\n")

# title(): Returns a Title Cased String

challenge = "thirty days of python"
print(challenge.title())  # Thirty Days Of Python
print("\n")

# swapcase(): Checks if String Starts with the Specified String

challenge = "thirty days of python"
print(challenge.swapcase())  # THIRTY DAYS OF PYTHON
challenge = "Thirty Days Of Python"
print(challenge.swapcase())  # tHIRTY dAYS oF pYTHON
print("\n")

# startswith(): Checks if String Starts with the Specified String

challenge = "thirty days of python"
print(challenge.startswith("thirty"))  # True
challenge = "30 days of python"
print(challenge.startswith("thirty"))  # False
