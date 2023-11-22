# Enhancing Numerical Computing with Rust

## Problem Statement

![Python-vs -Rust](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/assets/101893296/7eae0d54-142b-44da-b516-cfeb0957bb7e)

* The goal of this project is to optimize numerical and `scientific computing`.  
* Currently, `Numpy` is widely used for numerical and scientific computing, while Rust is known for its performance, safety, and system-level programming capabilities.   
* This project brings the advantages of Rust to the data science and scientific computing community.
* We initially started off by writing rust code for small elements of large algorithms such as matrix multiplication, matrix inverse calculation and dot productWe have used various Rust vs Python comparisons on the basis of performance and memory management using the files:
    * [Matrix Multiplication](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/matmul_dim.rs)
    * [Neural Network](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/n_net.rs)
    * [Dot Product](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/dot_product.rs)
    * [Error Handling](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/error_handling.rs)

## Software architecture

<img width="765" alt="Screenshot 2023-11-20 at 1 52 08 AM" src="https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/assets/101893296/19b96bb1-9b4c-4533-950d-ff0af53cdb27">



* Unit Tests: Writing tests for individual components to ensure their functionality.
* Integration and End-to-End Tests: Verifying the interactions and behaviors between components and the system as a whole.

* Testing component is placed locally and there is no database involved.  

## How to Compile and Run the project
  ### Python
  * Python code can be run using any code runner on any text editor like Visual Studio Code.
  ### Rust

  1. #### `Install Rust`
      If Rust isn't installed, use rustup, a toolchain manager for Rust.
      Follow the instructions on [Rust's official website](https://www.rust-lang.org/tools/install) to install it.
  2. #### `Project Setup`
     
      Edit the following changes in the [Cargo.toml](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/Cargo.toml) file
      * Change the name to the folder name. Also you can edit the version too.  
         ```sh
          [package]
          name = "POPL"  # The name of your project (it should match your folder name)
          version = "0.1.0"
          edition = "2018"
        ```
      * Add the required dependencies to your project.
        Here we have included dependencies like rand, rayon, ndarray, etc.  
        ```RUST
          [dependencies]
          rand = "0.8"
          rayon = "1.5"
          ndarray = "0.15.4"
          csv = "1.0"
        ```
      * Change the file name and its path according to the file which you are executing.
        ```RUST
          [[bin]]
          name = "matmul_dim"
          path = "matmul_dim.rs"
        ```
      
  3. #### `Build the Project`
      * Open a terminal or command prompt.
      * Navigate to your project directory using the cd command.
      * Run cargo build to compile the project. This command downloads dependencies (if any) and compiles the project.
  
  4. #### `Run the Compiled Binary`
      * After successful compilation, the binary will be available in the target/debug directory (for development build).
      * Run the binary by executing target/debug/matmul_dim in the terminal.


## POPL Aspects
  ### 1. Memory Management
   * [Neural Network](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/n_net.rs)
     
        ```RUST
        let mut X_train: Vec<(f64, f64)> = Vec::new();
        let mut y_train: Vec<i32> = Vec::new();
        // ... (similar declarations for other variables)
        ```
        Rust's ownership model ensures that memory is managed efficiently and safely by tracking ownership and enforcing strict rules about borrowing and mutability, thereby preventing issues like memory leaks or data races.
   * [Dot Product](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/dot_product.rs)
     
        ```RUST
        for i in 0..v1.len() {
            result += v1[i] * v2[i];
        }
        ```
        The loop in the dot_product function accesses elements of v1 and v2 without bounds checking, relying on Rust's memory safety guarantees through slice references.
  ### 2. Ownership 
   * [Neural Network](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/n_net.rs)
     
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

### 3. Error Handling 

   * [Dot Product](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/dot_product.rs)
     
     ```RUST
     if v1.len() != v2.len() {
         panic!("Vector dimensions do not match for dot product.");
     }

     ```
     The function dot_product checks for vector dimension mismatch and panics with an error message if the lengths of the input vectors are not equal.
   * [Error Handling](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/error_handling.rs)
     
     ```RUST
     enum MathError {
       DivisionByZero,
     }
     ```
     MathError is used to define specific error cases that might occur during mathematical operations. In this case, the specific error case is DivisionByZero, which indicates an attempt to divide by zero, an operation that is mathematically invalid.

### 4. Static Typing
   * [Matrix Multiplication](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/matmul_dim.rs)
     
     ```RUST
     let matrix_a: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
     let matrix_b: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
     ```
     The types of matrix_a and matrix_b are explicitly declared as Array2<f64>. This ensures type safety at compile time.
   * [Dot Product](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/dot_product.rs)
     
     ```RUST
      fn dot_product(v1: &[f64], v2: &[f64]) -> f64 {
       // ...
      }
     ```
     The function dot_product and its arguments v1 and v2 are explicitly typed as slices [f64], ensuring type safety.
       
 
 ### 5. Immutability
  * [Matrix Multiplication](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/matmul_dim.rs)
    
      ```RUST
      let matrix_a: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
      let matrix_b: Array2<f64> = Array2::from_shape_fn((500, 500), |_| rng.sample(Uniform::new(0.0, 1.0)));
      ```
      Variables matrix_a and matrix_b are immutable after initialization. This adheres to Rust's ownership model, promoting safety and preventing unintended modifications.
 * [Dot Product](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/dot_product.rs)
   
      ```RUST
      let result = dot_product(&v1, &v2);  // Compile-time error due to dimensions mismatch
      ```
      In main(), vectors v1 and v2 are immutable by default. Attempting to pass immutable references to dot_product enforces immutability.

  ### 6. Borrowing
   * [Neural Network](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/n_net.rs)
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

The results below are generated using VTune application.  
## Python:- 
![python](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/assets/101893296/3d0ade3e-e838-42c9-bed3-130ed0174fd1)
## Rust:-
![rust](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/assets/101893296/52e40649-7998-41f7-b60d-72fef550d6b1)


* In the experiments, the parameters to the algorithm are built-into the library, which reduces reliability of the measurements for both the Python and the transpiled Rust implementations.  
* Measurements were taken with careful examination of allocations and verification of produced outputs.  
* After automatic syntax conversion, we used regular expressions extensively to fix remaining errors and library references.  
* Multiple manual implementations of expressions (< 1 % of all expressions) were required though each was straightforward with output from the Rust compiler.  

## Graph:-
![photo_2023-11-20_00-51-38](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/assets/101893296/a3b4f3ce-654b-4a65-bf46-73b238cfa9a2)

This is the graph which represent time vs size of [Matrix Multiplication](https://github.com/Shlokkzz/POPL-MileStone-2-Enhancing-Numerical-Computing-with-Rust/blob/259e61b08cec4b3dc2dbe0c425f1d91d146e5d09/code-orig/matmul_dim.rs) operations.  
Y-axis represents time taken in seconds(s) and X-axis represents the size of the matrix. For example size=100 means a matrix with dimension 100x100.
Size | RUST(s) | PYTHON(s)
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


