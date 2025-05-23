web_tech = ["Thirty", "Days", "Of", "Python"]
result = " ".join(web_tech)
print(result)

print("\n")

web_tech = ["Coding", "For", "All"]
company = ["SDSolutions"]
# web_tech.extend(company)
result = " ".join(web_tech)
print(result)
result_with_company = result + " " + " ".join(company)
print(result_with_company)
print("\n")
print(len(company))
print("\n")
print(result_with_company.upper())
print("\n")
print(result_with_company.lower())
print("\n")
# capitalize
print(result.capitalize())
print("\n")
# title
print(result.title())
print("\n")
# swapcase
print(result.swapcase())
print("\n")
split_result = result.split(" ", 1)
if len(split_result) > 1:  # check if split result is greater than 1
    result_without_first_word = split_result[1]  # if greater than 1 output
else:
    result_without_first_word = ""  # if not output

print(result_without_first_word)

print("\n")
print(result.find("Coding"))
print("\n")
print(result.replace("Coding", "Python"))
print("\n")

# replace method
result_replace = "Python for Everyone"
print(result_replace.replace("Everyone", "All"))
print("\n")

# split method
split_coding = "Coding For All"
print(split_coding.split())
print("\n")

tech_campanies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
split_companies = tech_campanies.split(", ")
print(split_companies)
print("\n")

coding_for_all = "Coding For All"
coding_for_all_index = coding_for_all[0]
print(coding_for_all_index)
coding_for_all_last_index = coding_for_all[-1]
print(coding_for_all_last_index)
character_at_10 = coding_for_all[10]
print(character_at_10)
print("\n")

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python For Everyone"
words = phrase.split()
acronym = "".join(word[0].upper() for word in words)
print(acronym)
print("\n")

# Create an acronym or an abbreviation for the name 'Coding For All'.
phrase = "Coding For All"
words = phrase.split()
acronym = "".join(word[0].upper() for word in words)
print(acronym)
print("\n")
# Use index to determine the position of the first occurrence of C in Coding For All.
print(phrase.index("C"))
print("\n")
# Use index to determine the position of the first occurrence of F in Coding For All.
print(phrase.index("F"))

# Use rfind to determine the position of the last occurrence of l in Coding For All  .
phrase = "Coding For All People"
print(phrase.rfind("l"))
print("\n")

# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = "You cannot end a sentence with because because because is a conjunction"
first_occurrence = sentence.find("because")
print(first_occurrence)
print("\n")

# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

remove_sentence = "because because because"
replace_sentence = sentence.replace(remove_sentence, "")
print(replace_sentence)
print("\n")

# Does 'Coding For All' start with a substring Coding?
coding_for_all = "Coding For All"

if coding_for_all.startswith("Coding"):
    print(f"The string starts with Coding")
else:
    print(f"The string is not starting with Coding")
print("\n")

# Does 'Coding For All' end with a substring coding?
if coding_for_all.startswith("coding"):
    print(f"The string starts with Coding")
else:
    print(f"The string is not starting with Coding")
print("\n")

# '   Coding For All      '  , remove the left and right trailing spaces in the given string.
trailing_phrase = "   Coding For All      "
return_trailing_phrase = " ".join(trailing_phrase.split())
print(return_trailing_phrase)
print("\n")

"""
Which one of the following variables return True when we use the method isidentifier():
30DaysOfPython
thirty_days_of_python
"""

var1 = "30DaysOfPython"
var2 = "thirty_days_of_python"

print(var1.isidentifier())
print(var2.isidentifier())
print("\n")

"""
The following list contains the names of some of python libraries: ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']. Join the list with a hash with space string.
"""
python_libraries = ["Django", "Flask", "Bottle", "Pyramid", "Falcon"]
join_list = "# ".join(python_libraries)
print(join_list)
print("\n")

sentence = "I am enjoying this challenge.\nI just wonder what is next."
print(sentence)
print("\n")

header_list = "Name\tAge\tCountry\t\tCity"
info_list = "Alberth\t25\tPhilippines\tSariaya"

full_data = header_list + "\n" + info_list

print(full_data)

print("\n")

radius = 30
area = 3.14 * radius**2

str_formatting = "The area of a circle with radius {} is {} meters square.".format(
    radius, area
)

print(str_formatting)
print("\n")

num1 = 8
num2 = 6
add = num1 + num2
minus = num1 - num2
multiply = num1 * num2
divide = num1 / num2
modulus = num1 % num2
floor_divide = num1 // num2
exponentiation = num2**num2
print("{} + {} = {}".format(num1, num2, add))
print("{} - {} = {}".format(num1, num2, minus))
print("{} * {} = {}".format(num1, num2, multiply))
print("{} / {} = {}".format(num1, num2, divide))
print("{} % {} = {}".format(num1, num2, modulus))
print("{} // {} = {}".format(num1, num2, floor_divide))
print("{} ** {} = {}".format(num1, num2, exponentiation))
