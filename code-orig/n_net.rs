use rand::Rng;
use std::f64;
use std::time::{Instant};

// Define the sigmoid activation function
fn sigmoid(x: f64) -> f64 {
    1.0 / (1.0 + (-x).exp())
}

fn main() {
    // Generate a synthetic dataset for training
    let mut rng = rand::thread_rng();
    let mut X_train: Vec<(f64, f64)> = Vec::new();
    let mut y_train: Vec<i32> = Vec::new();
    for _ in 0..1000 {
        let x1 = rng.gen::<f64>();
        let x2 = rng.gen::<f64>();
        X_train.push((x1, x2));
        y_train.push(if x1 + x2 > 1.0 { 1 } else { 0 });
    }

    // Generate a synthetic dataset for testing
    let mut X_test: Vec<(f64, f64)> = Vec::new();
    let mut y_test: Vec<i32> = Vec::new();
    for _ in 0..200 {
        let x1 = rng.gen::<f64>();
        let x2 = rng.gen::<f64>();
        X_test.push((x1, x2));
        y_test.push(if x1 + x2 > 1.0 { 1 } else { 0 });
    }

    // Initialize the weights and biases
    let input_size = 2;
    let hidden_size = 3;
    let output_size = 1;
    let learning_rate = 0.1;

    // Initialize weights and biases with random values
    let mut weights_input_hidden = vec![vec![rng.gen::<f64>(); hidden_size]; input_size];
    let mut biases_hidden = vec![rng.gen::<f64>(); hidden_size];
    let mut weights_hidden_output = vec![vec![rng.gen::<f64>()]; hidden_size];
    let mut bias_output = rng.gen::<f64>();

    // Measure the time it takes to train txhe network
    let start = Instant::now();

    // Training loop
    let epochs = 10000;
    for _ in 0..epochs {
        // Forward propagation (training data)
        let mut hidden_input = vec![vec![0.0; hidden_size]; X_train.len()];
        let mut hidden_output = vec![vec![0.0; hidden_size]; X_train.len()];
        let mut output = vec![0.0; X_train.len()];
        for i in 0..X_train.len() {
            for k in 0..hidden_size {
                hidden_input[i][k] = biases_hidden[k];
                for j in 0..input_size {
                    hidden_input[i][k] += X_train[i].0 * weights_input_hidden[j][k];
                }
                hidden_output[i][k] = sigmoid(hidden_input[i][k]);
            }

            output[i] = bias_output;
            for k in 0..hidden_size {
                output[i] += hidden_output[i][k] * weights_hidden_output[k][0];
            }
            output[i] = sigmoid(output[i]);
        }

        // Backpropagation (training data)
        for i in 0..X_train.len() {
            let error = y_train[i] as f64 - output[i];
            let d_output = error * output[i] * (1.0 - output[i]);
            let mut error_hidden = vec![0.0; hidden_size];
            for k in 0..hidden_size {
                error_hidden[k] = d_output * weights_hidden_output[k][0];
            }

            for k in 0..hidden_size {
                let d_hidden = error_hidden[k] * hidden_output[i][k] * (1.0 - hidden_output[i][k]);
                bias_output += d_output * learning_rate;
                weights_hidden_output[k][0] += hidden_output[i][k] * d_output * learning_rate;
                biases_hidden[k] += d_hidden * learning_rate;
                for j in 0..input_size {
                    weights_input_hidden[j][k] += X_train[i].1 * d_hidden * learning_rate;
                }
            }
        }
    }

    // Calculate the time taken for training
    let end = start.elapsed();
    let duration = end.as_secs() as f64 + f64::from(end.subsec_nanos()) / 1_000_000_000.0;

    // Testing the model
    let mut correct_predictions = 0;
    for i in 0..X_test.len() {
        let mut hidden_input = vec![0.0; hidden_size];
        let mut hidden_output = vec![0.0; hidden_size];
        let mut output = 0.0;
        for k in 0..hidden_size {
            hidden_input[k] = biases_hidden[k];
            for j in 0..input_size {
                hidden_input[k] += X_test[i].0 * weights_input_hidden[j][k];
            }
            hidden_output[k] = sigmoid(hidden_input[k]);
        }

        for k in 0..hidden_size {
            output += hidden_output[k] * weights_hidden_output[k][0];
        }
        output = sigmoid(output);
        let predicted = if output > 0.5 { 1 } else { 0 };
        if predicted == y_test[i] {
            correct_predictions += 1;
        }
    }

    // Calculate accuracy
    let accuracy = correct_predictions as f64 / X_test.len() as f64;

    // Print the time taken and accuracy
    println!("Time taken for training: {:.6} seconds", duration);
    println!("Accuracy: {:.2}%", accuracy * 100.0);
}