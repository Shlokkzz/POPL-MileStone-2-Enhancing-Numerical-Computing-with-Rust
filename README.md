# Enhancing Numerical Computing with Rust

## Problem Statement
* The goal of this project is to optimize numerical and `scientific computing`.  
* Currently, Numpy is widely used for numerical and scientific computing, while Rust is known for its performance, safety, and system-level programming capabilities.   
* This project brings the advantages of Rust to the data science and scientific computing community while maintaining compatibility with existing Python-based workflows.

## Software architecture

<img width="765" alt="Screenshot 2023-11-20 at 1 52 08 AM" src="https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/106c6915-c6a2-4d74-803e-26f53e8399e7">


* Unit Tests: Writing tests for individual components to ensure their functionality.
* Integration and End-to-End Tests: Verifying the interactions and behaviors between components and the system as a whole.

* Testing component is placed locally and there is no databased invloved.  



## POPL Aspects
  ### Memory Management
   * `n_net.rs`
        ```RUST
        let mut X_train: Vec<(f64, f64)> = Vec::new();
        let mut y_train: Vec<i32> = Vec::new();
        // ... (similar declarations for other variables)
        ```
        Rust's ownership model ensures that memory is managed efficiently and safely by tracking ownership and enforcing strict rules about borrowing and mutability, thereby preventing issues like memory leaks or data races.
   * `dot_product.rs`
        ```RUST
        for i in 0..v1.len() {
            result += v1[i] * v2[i];
        }
        ```
        The loop in the dot_product function accesses elements of v1 and v2 without bounds checking, relying on Rust's memory safety guarantees through slice references.
  ### Ownership 
   * `n_net.rs` 
       ```RUST
       fn sigmoid(x: f64) -> f64 {
       // ...
       }
       ```
       Functions like sigmoid take ownership of their arguments. For instance, sigmoid takes ownership of a f64 value when called.
      ```RUST
      let mut X_train: Vec<(f64, f64)> = Vec::new();
      let mut y_train: Vec<i32> = Vec::new();
      ```
      The mut keyword signifies mutable ownership. Variables like X_train, y_train, X_test, y_test, etc., are declared as mutable (mut), allowing changes to the data they hold.

### Error Handling 

   * `dot_product.rs`
     ```RUST
     if v1.len() != v2.len() {
         panic!("Vector dimensions do not match for dot product.");
     }

     ```
     The function dot_product checks for vector dimension mismatch and panics with an error message if the lengths of the input vectors are not equal.
   * `error_handling.rs`
     ```RUST
     enum MathError {
       DivisionByZero,
     }
     ```
     MathError is used to define specific error cases that might occur during mathematical operations. In this case, the specific error case is DivisionByZero, which indicates an attempt to divide by zero, an operation that is mathematically invalid.

### Static Typing
   * `matmul_dim.rs`
     ```RUST
     let matrix_a: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
     let matrix_b: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
     ```
     The types of matrix_a and matrix_b are explicitly declared as Array2<f64>. This ensures type safety at compile time.
   * `dot_product.rs`
     ```RUST
      fn dot_product(v1: &[f64], v2: &[f64]) -> f64 {
       // ...
      }
     ```
     The function dot_product and its arguments v1 and v2 are explicitly typed as slices [f64], ensuring type safety.
       
 
 ### Immutability
  * `matmul_dim.rs`
      ```RUST
      let matrix_a: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
      let matrix_b: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
      ```
      Variables matrix_a and matrix_b are immutable after initialization. This adheres to Rust's ownership model, promoting safety and preventing unintended modifications.
 * `dot_product.rs`
      ```RUST
      let result = dot_product(&v1, &v2);  // Compile-time error due to dimensions mismatch
      ```
      In main(), vectors v1 and v2 are immutable by default. Attempting to pass immutable references to dot_product enforces immutability.

  ### Borrowing
   * `n_net.rs`
       ```RUST
       let mut weights_input_hidden = vec![vec![rng.gen::<f64>(); hidden_size]; input_size];
       let mut biases_hidden = vec![rng.gen::<f64>(); hidden_size];
       let mut weights_hidden_output = vec![vec![rng.gen::<f64>()]; hidden_size];
       let mut bias_output = rng.gen::<f64>();
       ```
       The code uses borrowing and references extensively, where functions or calculations borrow values without taking ownership. When using vec![] to initialize vectors, the ownership of the created vectors is transferred to the variables (weights_input_hidden, biases_hidden, etc.).
        
      The variables are borrowed in various operations within loops for calculations but maintain their ownership throughout.
       

## Results 

* We consider the results of transpilation in wall clock time, memory consumption, and complexity in terms of issues encountered and regularity for potential automation.  
* We also consider what processes transpiled sources now allow.   
* Lines of code is not considered a feasible measure because the number of lines is almost the same, with differences being due to the differing formatters of each language.

## `RUST->`  
  ![rust](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/ea5e63ce-bd51-4467-81e5-39c0a7c96611)

## `PYTHON->`  
![python](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/4e3c5696-be7e-4d74-8fdc-fa174b636195)

* In the experiments, the parameters to the algorithm are built-into the library, which reduces reliability of the measurements for both the Python and the transpiled Rust implementations.  
* Measurements were taken with careful examination of allocations and verification of produced outputs.  
* After automatic syntax conversion, we used regular expressions extensively to fix remaining errors and library references.  
* Multiple manual implementations of expressions (< 1 % of all expressions) were required though each was straightforward with output from the Rust compiler.  

## `Graph`
![photo_2023-11-20_00-51-38](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/2bb3c037-a5dd-4a2b-8f74-4a1e61e15207)  
Size | RUST(s) | PYTHON(S)
| :--- | ---: | :---:
100        | 0.00612 | 0.190281
200          | 0.02204 | 1.566
300        | 0.06956 | 5.75
400          | 0.15942 | 13.24
500          | 0.31405 | 24.7

In this performance comparison between Rust and Python for processing different data sizes, Rust consistently demonstrates significantly lower execution times across varying data sizes, showcasing its superior efficiency and speed compared to Python for these computational tasks.  

## Potential for future work
* Using rust’s concurrency features to improve neural network performance.
* Testing neural network performance for rust on other datasets.


