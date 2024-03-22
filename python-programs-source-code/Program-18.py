import numpy as np

# Creating a single-dimensional array
array = np.array([1, 2, 3, 4, 5])

# 1. Type of array, dimension of array, shape of array, size of array
print("Type of array:", type(array))
print("Dimension of array:", array.ndim)
print("Shape of array:", array.shape)
print("Size of array:", array.size)
print("=========================================\n")

# 2. Reshape array
reshaped_array = np.reshape(array, (5, 1))
print("Reshaped array:")
print(reshaped_array)
print("=========================================\n")

# 3. Flatten and transpose
flattened_array = array.flatten()
transposed_array = array.transpose()
print("Flattened array:", flattened_array)
print("Transposed array:", transposed_array)
print("=========================================\n")

# 4. Zeros
zeros_array = np.zeros(5)
print("Zeros array:", zeros_array)
print("=========================================\n")

# 5. Ones
ones_array = np.ones(5)
print("Ones array:", ones_array)
print("=========================================\n")

# 6. Linspace
linspace_array = np.linspace(0, 10, 5)
print("Linspace array:", linspace_array)
print("=========================================\n")

# 7. Random
random_array = np.random.randint(0, 10, 5)
print("Random array:", random_array)
print("=========================================\n")

# 8. Sum of array
array_sum = np.sum(array)
print("Sum of array:", array_sum)
print("=========================================\n")