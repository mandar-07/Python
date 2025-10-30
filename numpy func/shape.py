import numpy as np
print("\nShape Manipulation:\n")

arr = np.arange(1, 13)
print("Original array:", arr)

reshaped = arr.reshape((3, 4))
print("Reshaped to 3x4:\n", reshaped)

flattened = reshaped.flatten()
print("Flattened back to 1D:", flattened)

transposed = reshaped.T
print("Transposed array:\n", transposed)

vstacked = np.vstack([reshaped, reshaped])
print("Vertically stacked:\n", vstacked)

hstacked = np.hstack([reshaped, reshaped])
print("Horizontally stacked:\n", hstacked)
