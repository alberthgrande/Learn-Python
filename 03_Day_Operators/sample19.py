"""
Write a Python script that displays the following table
1 1 1 1 1
2 1 2 4 8
3 1 3 9 27
4 1 4 16 64
5 1 5 25 125
"""

for col in range(1, 6):
    print(col, end=" ")
    for row in range(4):  # Adjusted to print 4 columns after the first number
        print(col**row, end=" ")
    print()  # Move to the next line after each row
