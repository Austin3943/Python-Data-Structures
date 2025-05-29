import numpy as np
import matplotlib.pyplot as plt

# Define the vector w
w = np.array([1, 4])  #New Vector

# Define the scalar
scalar = 3  #New Scalar

# Perform scalar multiplication
result = scalar * w

# Print the result
print("Vector w:", w)
print("Scaler:", scalar)
print("Result of", scalar, "* w =", result)

# Plot the vectors
plt.figure(figsize=(6, 6))
plt.quiver(0, 0, w[0], w[1], angles='xy',
           scale_units='xy', scale=1, color='blue',
           label='w')
plt.quiver(0, 0, result[0], result[1],
           angles='xy', scale_units='xy', scale=1,
           color='red', label='3w',)
plt.xlim(-1, 15)
plt.ylim(-1, 15)
plt.grid(True)
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.legend()
plt.title("Vector w and 3w")
plt.show()
