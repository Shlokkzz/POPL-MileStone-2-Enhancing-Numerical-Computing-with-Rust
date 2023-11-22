import random
import time

# Set the seed for random number generation
random.seed(42)

# Generate two 600x600 matrices with random values
matrix_a = [[random.random() for _ in range(600)] for _ in range(600)]
matrix_b = [[random.random() for _ in range(600)] for _ in range(600)]

# Measure the time it takes to perform matrix addition
start_time = time.time()

# Matrix addition
result_matrix = [[matrix_a[i][j] + matrix_b[i][j] for j in range(600)] for i in range(600)]

duration = time.time() - start_time

# Print the time taken
print("Time taken for matrix addition: {:.6f} seconds".format(duration))

# Ensure the result is computed to avoid optimization removing the computation
print("Result (first element):", result_matrix[0][0])
