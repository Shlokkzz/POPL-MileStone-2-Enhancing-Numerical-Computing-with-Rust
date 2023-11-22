use rand::Rng;

// Euclidean distance function for K-means
fn euclidean_distance(a: &(f64, f64), b: &(f64, f64)) -> f64 {
    ((a.0 - b.0).powi(2) + (a.1 - b.1).powi(2)).sqrt()
}

// Perform K-means clustering
fn kmeans(data: &[(f64, f64)], k: usize, max_iters: usize) -> Vec<usize> {
    let mut rng = rand::thread_rng();

    // Initialize centroids randomly
    let mut centroids: Vec<(f64, f64)> = (0..k)
        .map(|_| (rng.gen_range(0.0..10.0), rng.gen_range(0.0..10.0)))
        .collect();

    let mut assignments: Vec<usize> = vec![0; data.len()];

    for _ in 0..max_iters {
        // Assign each data point to the nearest centroid
        for (i, point) in data.iter().enumerate() {
            let mut min_distance = f64::INFINITY;
            let mut closest_centroid = 0;

            for (j, centroid) in centroids.iter().enumerate() {
                let distance = euclidean_distance(point, centroid);

                if distance < min_distance {
                    min_distance = distance;
                    closest_centroid = j;
                }
            }

            assignments[i] = closest_centroid;
        }

        // Update centroids based on the assigned points
        let mut centroid_sums: Vec<(f64, f64)> = vec![(0.0, 0.0); k];
        let mut counts: Vec<usize> = vec![0; k];

        for (i, &centroid_idx) in assignments.iter().enumerate() {
            centroid_sums[centroid_idx].0 += data[i].0;
            centroid_sums[centroid_idx].1 += data[i].1;
            counts[centroid_idx] += 1;
        }

        for (i, count) in counts.iter().enumerate() {
            if *count > 0 {
                centroids[i].0 = centroid_sums[i].0 / *count as f64;
                centroids[i].1 = centroid_sums[i].1 / *count as f64;
            }
        }
    }

    assignments
}

fn main() {
    // Set the parameters for the dataset and clustering
    let num_clusters = 3;
    let num_samples_train = 300;
    let num_samples_test = 100;
    let max_iters = 100;

    // Generate random training dataset
    let mut rng = rand::thread_rng();
    let train_data: Vec<_> = (0..num_samples_train)
        .map(|_| (rng.gen_range(0.0..10.0), rng.gen_range(0.0..10.0)))
        .collect();

    // Perform K-means clustering on the training dataset
    let train_assignments = kmeans(&train_data, num_clusters, max_iters);

    // Get centroids directly from the training phase
    let centroids: Vec<_> = (0..num_clusters)
        .map(|cluster| {
            let cluster_points: Vec<_> = train_data
                .iter()
                .zip(train_assignments.iter())
                .filter(|(_, &c)| c == cluster)
                .map(|(point, _)| point)
                .collect();

            let sum: (f64, f64) = cluster_points.iter().cloned().fold((0.0, 0.0), |acc, p| {
                (acc.0 + p.0, acc.1 + p.1)
            });

            let count = cluster_points.len() as f64;
            (sum.0 / count, sum.1 / count)
        })
        .collect();

    // Generate random test dataset
    let test_data: Vec<_> = (0..num_samples_test)
        .map(|_| (rng.gen_range(0.0..10.0), rng.gen_range(0.0..10.0)))
        .collect();

    // Assign test samples to clusters using the centroids from training
    let test_assignments: Vec<usize> = test_data
        .iter()
        .map(|point| {
            let mut min_distance = f64::INFINITY;
            let mut closest_centroid = 0;

            for (j, centroid) in centroids.iter().enumerate() {
                let distance = euclidean_distance(point, centroid);

                if distance < min_distance {
                    min_distance = distance;
                    closest_centroid = j;
                }
            }

            closest_centroid
        })
        .collect();

    // Print accuracy
    let correct_assignments: usize = test_assignments
        .iter()
        .enumerate()
        .filter(|&(i, &cluster)| cluster == train_assignments[i])
        .count();

    let accuracy = correct_assignments as f64 / num_samples_test as f64;
    println!("Accuracy: {:.2}", accuracy);
}
