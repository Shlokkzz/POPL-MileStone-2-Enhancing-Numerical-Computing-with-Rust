import random

def euclidean_distance(a, b):
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** 0.5

def kmeans(data, k, max_iters):
    # Initialize centroids randomly
    centroids = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(k)]

    # Assign each data point to the nearest centroid
    for _ in range(max_iters):
        assignments = [min(range(k), key=lambda j: euclidean_distance(point, centroids[j])) for point in data]

        # Update centroids based on the assigned points
        centroid_sums = [(0, 0) for _ in range(k)]
        counts = [0] * k

        for i, centroid_idx in enumerate(assignments):
            centroid_sums[centroid_idx] = (centroid_sums[centroid_idx][0] + data[i][0], centroid_sums[centroid_idx][1] + data[i][1])
            counts[centroid_idx] += 1

        centroids = [(centroid_sum[0] / count, centroid_sum[1] / count) if count > 0 else centroid for centroid, (centroid_sum, count) in zip(centroids, zip(centroid_sums, counts))]

    return assignments

def main():
    # Set the parameters for the dataset and clustering
    num_clusters = 3
    num_samples_train = 300
    num_samples_test = 100
    max_iters = 100

    # Generate random training dataset
    train_data = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_samples_train)]

    # Perform K-means clustering on the training dataset
    train_assignments = kmeans(train_data, num_clusters, max_iters)

    # Get centroids directly from the training phase
    centroids = [(sum(point[0] for point, cluster in zip(train_data, train_assignments) if cluster == i) / max(1, train_assignments.count(i)),
                  sum(point[1] for point, cluster in zip(train_data, train_assignments) if cluster == i) / max(1, train_assignments.count(i)))
                 for i in range(num_clusters)]

    # Generate random test dataset
    test_data = [(random.uniform(0, 10), random.uniform(0, 10)) for _ in range(num_samples_test)]

    # Assign test samples to clusters using the centroids from training
    test_assignments = [min(range(num_clusters), key=lambda j: euclidean_distance(point, centroids[j])) for point in test_data]

    # Print accuracy
    correct_assignments = sum(1 for i, cluster in enumerate(test_assignments) if cluster == train_assignments[i])
    accuracy = correct_assignments / num_samples_test
    print(f"Accuracy: {accuracy:.2f}")

if __name__ == "__main__":
    main()
