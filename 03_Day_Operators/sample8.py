import math

# Task 8
# Equation: y = 2x - 2
slope_task_8 = 2
y_intercept_task_8 = -2
x_intercept_task_8 = -y_intercept_task_8 / slope_task_8

# Task 9
# Points: (2, 2) and (6, 10)
x1, y1 = 2, 2
x2, y2 = 6, 10
slope_task_9 = (y2 - y1) / (x2 - x1)
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Task 10: Compare slopes
slope_comparison = slope_task_8 == slope_task_9

# Output the results
result_8 = (slope_task_8, x_intercept_task_8, y_intercept_task_8)
result_9 = (slope_task_9, distance)
result_10 = slope_comparison

print("Task 8 Results: Slope, X-intercept, Y-intercept")
print(result_8)
print("\nTask 9 Results: Slope, Euclidean Distance")
print(result_9)
print("\nTask 10 Results: Are the slopes equal?")
print(result_10)
