import sympy as sp


# Function to calculate the y
def calculate_y(x):
    return x**2 + 6 * x + 9


# values of x
x_values = [-5, -3, 0, 2, 5]

# calculate y for each x
y_values = [calculate_y(x) for x in x_values]

# print y values for each x
print("x values:", x_values)
print("y values:", y_values)


# Find x values where y is 0
x = sp.symbols("x")
quadratic_eq = x**2 + 6 * x + 9
solutions = sp.solve(quadratic_eq, x)

# Print the solutions
print("Solutions for x when y = 0:", solutions)
