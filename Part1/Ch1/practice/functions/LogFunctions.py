import numpy as np
import matplotlib.pyplot as plt

# Generate x values (avoiding zero since log(0) is undefined)
x = np.linspace(0.1, 10, 100)

# Compute log values
y = np.log(x)

# Plot the function
plt.plot(x, y, label="Natural Log Function")
plt.xlabel("x")
plt.ylabel("ln(x)")
plt.title("Logarithm Function Plot")
plt.legend()
plt.grid()
plt.show()