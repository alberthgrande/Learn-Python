import matplotlib.pyplot as plt
import numpy as np

# Define the function y = 2x - 2
def linear_function(x):
    return 2 * x - 2

# Generate x values
x = np.linspace(-5, 5, 400)
y = linear_function(x)

# Create the plot
plt.figure(figsize=(8, 6))
plt.plot(x, y, label='y = 2x - 2')
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)

# Mark the x-intercept and y-intercept
plt.scatter([1], [0], color='red')  # x-intercept
plt.scatter([0], [-2], color='blue')  # y-intercept
plt.text(1, 0.5, 'x-intercept (1, 0)', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(-0.5, -2, 'y-intercept (0, -2)', fontsize=12, verticalalignment='top', horizontalalignment='right')

# Set the limits of the plot
plt.xlim(-5, 5)
plt.ylim(-10, 10)

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Graph of y = 2x - 2')
plt.legend()
plt.show()
