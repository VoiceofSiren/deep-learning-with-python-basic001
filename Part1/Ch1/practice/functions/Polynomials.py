# f(x) = x^3 - 2x + 1
def my_func(x):
    return x**3 - 2*x + 1

'''
x_values = []
y_values = []
for i in range(-10, 11):
    x = float(i)
    x_values.append(x)
    y_values.append(my_func(x))
'''

# List Comprehension
x_values = [float(i) for i in range(-10, 11)]
y_values = [my_func(x) for x in x_values]

print(x_values)
print(y_values)

import matplotlib.pyplot as plt
import numpy as np

x_list = np.linspace(-2, 2, 21)
y_list = my_func(x_list)

plt.plot(x_list, y_list, label="y = x³ - 2x + 1")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Graph of y = x³ - 2x + 1")
plt.legend()

plt.grid(True)
plt.show()