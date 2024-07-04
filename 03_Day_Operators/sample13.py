# Find the length of the text python and convert the value to float and convert it to string
import inflect

inf = inflect.engine()

str_python = len("python")


# convert the float number into a string
convert_str = inf.number_to_words(str_python)

print(convert_str)
