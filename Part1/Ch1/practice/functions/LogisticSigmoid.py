import numpy as np
import matplotlib.pyplot as plt

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate x values
x = np.linspace(-10, 10, 100)

# Compute sigmoid values
y = sigmoid(x)

print(type(y))  # <class 'numpy.ndarray'>

plt.plot(x, y, label="Sigmoid Function")
plt.xlabel("x")
plt.ylabel("Sigmoid(x)")
plt.title("Sigmoid Function Plot")
plt.legend()
plt.grid()
plt.show()