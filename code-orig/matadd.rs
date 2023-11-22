extern crate ndarray;
use ndarray::prelude::*;
use rand::Rng;
use rand::distributions::Uniform;
use std::time::Instant;

fn main() {
    // Initialize the random number generator
    let mut rng = rand::thread_rng();

    // Generate two 600x600 matrices with random values
    let matrix_a: Array2<f64> = Array2::from_shape_fn((600, 600), |_| rng.sample(Uniform::new(0.0, 1.0)));
    let matrix_b: Array2<f64> = Array2::from_shape_fn((600, 600), |_| rng.sample(Uniform::new(0.0, 1.0)));

    // Measure the time it takes to perform matrix addition
    let start = Instant::now();
    let result_matrix: Array2<f64> = &matrix_a + &matrix_b; // Matrix addition
    let duration = start.elapsed();

    // Print the time taken
    println!("Time taken for matrix addition: {:?}", duration);

    // Ensure the result is computed to avoid optimization removing the computation
    println!("Result (first element): {}", result_matrix[(0, 0)]);
}
