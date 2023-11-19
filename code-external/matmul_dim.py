import random
import time

# Initialize the random number generator
random.seed(0)

# Generate two 800x800 matrices with random values
matrix_size = 500
matrix_a = [[random.uniform(0.0, 1.0) for _ in range(matrix_size)] for _ in range(matrix_size)]
matrix_b = [[random.uniform(0.0, 1.0) for _ in range(matrix_size)] for _ in range(matrix_size)]

# Measure the time it takes to perform the matrix multiplication
start = time.time()
result_matrix = [[0.0] * matrix_size for _ in range(matrix_size)]
for i in range(matrix_size):
    for j in range(matrix_size):
        for k in range(matrix_size):
            result_matrix[i][j] += matrix_a[i][k] * matrix_b[k][j]
duration = time.time() - start

# Print the time taken
print("Time taken: {:.6f} seconds".format(duration))

# Ensure the result is computed to avoid optimization removing the computation
print("Result (first element): {}".format(result_matrix[0][0]))
