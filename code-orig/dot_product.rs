fn dot_product(v1: &[f64], v2: &[f64]) -> f64 {
    if v1.len() != v2.len() {
        panic!("Vector dimensions do not match for dot product.");
    }

    let mut result = 0.0;
    for i in 0..v1.len() {
        // Access elements in both vectors without bounds checking
        result += v1[i] * v2[i];
    }

    result
}

fn main() {
    let v1 = vec![1.0, 2.0, 3.0];
    let v2 = vec![4.0, 5.0];

    let result = dot_product(&v1, &v2);  // Compile-time error due to dimensions mismatch

    println!("Dot product: {}", result);
}
