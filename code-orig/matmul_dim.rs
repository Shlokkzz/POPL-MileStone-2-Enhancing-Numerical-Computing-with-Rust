extern crate ndarray;
use ndarray::prelude::*;
use rand::Rng;
use rand::distributions::Uniform; // Import Uniform from rand::distributions
use std::time::Instant;

fn main() {
    // Initialize the random number generator
    let mut rng = rand::thread_rng();

    // Generate two 800x800 matrices with random values
    let matrix_a: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
    let matrix_b: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));

    // Measure the time it takes to perform the matrix multiplication
    let start = Instant::now();
    let result_matrix: Array2<f64> = matrix_a.dot(&matrix_b);
    let duration = start.elapsed();

    // Print the time taken
    println!("Time taken: {:?}", duration);

    // Ensure the result is computed to avoid optimization removing the computation
    println!("Result (first element): {}", result_matrix[(0, 0)]);
}
