def dot_product(v1, v2):
    if len(v1) != len(v2):
        raise ValueError("Vector dimensions do not match for dot product.")

    result = 0.0
    for i in range(len(v1)):
        # Access elements in both lists without bounds checking
        result += v1[i] * v2[i]

    return result

if __name__ == "__main__":
    v1 = [1.0, 2.0, 3.0]
    v2 = [4.0, 5.0]

    try:
        result = dot_product(v1, v2)  # Runtime error due to dimensions mismatch
        print("Dot product:", result)
    except ValueError as e:
        print(e)
