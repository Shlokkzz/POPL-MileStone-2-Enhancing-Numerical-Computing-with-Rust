import random
import math
import time

# Define the sigmoid activation function
def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))

# Generate a synthetic dataset for training
X_train = [(random.random(), random.random()) for _ in range(1000)]
y_train = [1 if x[0] + x[1] > 1.0 else 0 for x in X_train]

# Generate a synthetic dataset for testing
X_test = [(random.random(), random.random()) for _ in range(200)]
y_test = [1 if x[0] + x[1] > 1.0 else 0 for x in X_test]

# Initialize the weights and biases
input_size = 2
hidden_size = 3
output_size = 1
learning_rate = 0.1

# Initialize weights and biases with random values
weights_input_hidden = [[random.random() for _ in range(hidden_size)] for _ in range(input_size)]
biases_hidden = [random.random() for _ in range(hidden_size)]
weights_hidden_output = [[random.random()] for _ in range(hidden_size)]
bias_output = random.random()

# Measure the time it takes to train the network
start = time.time()

# Training loop
epochs = 10000
for _ in range(epochs):
    # Forward propagation (training data)
    hidden_input = [[0.0 for _ in range(hidden_size)] for _ in range(len(X_train))]
    hidden_output = [[0.0 for _ in range(hidden_size)] for _ in range(len(X_train))]
    output = [0.0 for _ in range(len(X_train))]
    for i in range(len(X_train)):
        for k in range(hidden_size):
            hidden_input[i][k] = biases_hidden[k]
            for j in range(input_size):
                hidden_input[i][k] += X_train[i][j] * weights_input_hidden[j][k]
            hidden_output[i][k] = sigmoid(hidden_input[i][k])

        output[i] = bias_output
        for k in range(hidden_size):
            output[i] += hidden_output[i][k] * weights_hidden_output[k][0]
        output[i] = sigmoid(output[i])

    # Backpropagation (training data)
    for i in range(len(X_train)):
        error = y_train[i] - output[i]
        d_output = error * output[i] * (1.0 - output[i])
        error_hidden = [0.0 for _ in range(hidden_size)]
        for k in range(hidden_size):
            error_hidden[k] = d_output * weights_hidden_output[k][0]

        for k in range(hidden_size):
            d_hidden = error_hidden[k] * hidden_output[i][k] * (1.0 - hidden_output[i][k])
            bias_output += d_output * learning_rate
            weights_hidden_output[k][0] += hidden_output[i][k] * d_output * learning_rate
            biases_hidden[k] += d_hidden * learning_rate
            for j in range(input_size):
                weights_input_hidden[j][k] += X_train[i][j] * d_hidden * learning_rate

# Calculate the time taken for training
end = time.time()
duration = end - start

# Testing the model
correct_predictions = 0
for i in range(len(X_test)):
    hidden_input = [0.0 for _ in range(hidden_size)]
    hidden_output = [0.0 for _ in range(hidden_size)]
    output = 0.0
    for k in range(hidden_size):
        hidden_input[k] = biases_hidden[k]
        for j in range(input_size):
            hidden_input[k] += X_test[i][j] * weights_input_hidden[j][k]
        hidden_output[k] = sigmoid(hidden_input[k])

    for k in range(hidden_size):
        output += hidden_output[k] * weights_hidden_output[k][0]
    output = sigmoid(output)
    predicted = 1 if output > 0.5 else 0
    if predicted == y_test[i]:
        correct_predictions += 1

# Calculate accuracy
accuracy = correct_predictions / len(X_test)

# Print the time taken and accuracy
print("Time taken for training: {:.6} seconds".format(duration))
print("Accuracy: {:.2}%".format(accuracy * 100))

# import pandas as pd
# import random
# import math
# import time

# # Load the Iris dataset
# data = pd.read_csv('Iris.csv')

# # Assuming that the 'Species' column contains string labels
# # Map the string labels to integer labels
# species_mapping = {'Iris-setosa': 0, 'Iris-versicolor': 1, 'Iris-virginica': 2}
# data['species'] = data['Species'].map(species_mapping)

# # Shuffle the dataset
# data = data.sample(frac=1, random_state=42).reset_index(drop=True)

# # Split the dataset into features and labels
# X = data[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']].values
# y = data['species'].values

# # Normalize features (optional but recommended)
# X = (X - X.mean(axis=0)) / X.std(axis=0)

# # Define the sigmoid activation function
# def sigmoid(x):
#     return 1.0 / (1.0 + math.exp(-x))

# # Initialize the weights and biases
# input_size = 4
# hidden_size = 3
# output_size = 3
# learning_rate = 0.1

# random.seed(42)  # For reproducibility
# weights_input_hidden = [[random.random() for _ in range(hidden_size)] for _ in range(input_size)]
# biases_hidden = [random.random() for _ in range(hidden_size)]
# weights_hidden_output = [[random.random() for _ in range(output_size)] for _ in range(hidden_size)]
# biases_output = [random.random() for _ in range(output_size)]

# # Measure the time it takes to train the network
# start_time = time.time()

# # Training loop
# epochs = 10000
# for _ in range(epochs):
#     for i in range(len(X)):
#         # Forward propagation
#         hidden_input = [0.0] * hidden_size
#         hidden_output = [0.0] * hidden_size
#         output = [0.0] * output_size

#         for k in range(hidden_size):
#             hidden_input[k] = biases_hidden[k]
#             for j in range(input_size):
#                 hidden_input[k] += X[i][j] * weights_input_hidden[j][k]
#             hidden_output[k] = sigmoid(hidden_input[k])

#         for k in range(output_size):
#             output[k] = biases_output[k]
#             for j in range(hidden_size):
#                 output[k] += hidden_output[j] * weights_hidden_output[j][k]
#             output[k] = sigmoid(output[k])

#         # Backpropagation
#         error_output = [y_i - output_i for y_i, output_i in zip(y, output)]
#         d_output = [error * output_i * (1.0 - output_i) for error, output_i in zip(error_output, output)]
#         error_hidden = [0.0] * hidden_size

#         for j in range(hidden_size):
#             for k in range(output_size):
#                 error_hidden[j] += d_output[k] * weights_hidden_output[j][k]

#         d_hidden = [error * hidden_output_i * (1.0 - hidden_output_i) for error, hidden_output_i in zip(error_hidden, hidden_output)]

#         for j in range(hidden_size):
#             biases_output[j] += d_output[j] * learning_rate
#             for k in range(output_size):
#                 weights_hidden_output[j][k] += hidden_output[j] * d_output[k] * learning_rate
#             biases_hidden[j] += d_hidden[j] * learning_rate
#             for k in range(input_size):
#                 weights_input_hidden[k][j] += X[i][k] * d_hidden[j] * learning_rate

# # Calculate the time taken for training
# end_time = time.time()
# duration = end_time - start_time

# # Print the time taken
# print(f"Time taken for training: {duration:.6} seconds")

# # Testing the model (accuracy calculation)
# correct_predictions = 0
# for i in range(len(X)):
#     hidden_input = [0.0] * hidden_size
#     hidden_output = [0.0] * hidden_size
#     output = [0.0] * output_size

#     for k in range(hidden_size):
#         hidden_input[k] = biases_hidden[k]
#         for j in range(input_size):
#             hidden_input[k] += X[i][j] * weights_input_hidden[j][k]
#         hidden_output[k] = sigmoid(hidden_input[k])

#     for k in range(output_size):
#         output[k] = biases_output[k]
#         for j in range(hidden_size):
#             output[k] += hidden_output[j] * weights_hidden_output[j][k]
#         output[k] = sigmoid(output[k])

#     predicted_class = output.index(max(output))
#     if predicted_class == y[i]:
#         correct_predictions += 1

# # Calculate accuracy
# accuracy = correct_predictions / len(X)
# print(f"Accuracy: {accuracy * 100:.2f}%")