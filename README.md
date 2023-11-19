# Enhancing Numerical Computing with Rust

## Problem Statement
* The goal of this project is to optimize numerical and `scientific computing`.  
* Currently, Numpy is widely used for numerical and scientific computing, while Rust is known for its performance, safety, and system-level programming capabilities.   
* This project brings the advantages of Rust to the data science and scientific computing community while maintaining compatibility with existing Python-based workflows.

## Software architecture
 What is the software architecture of your soln? What parts have you reused and what parts have you developed on your own? Draw a figure to explain better. Is it a client-server architecture. Where is the testing component placed (local or remote)? Is there a database involved? etc.   

 ![Screenshot 2023-11-20 001356](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/23b30a15-582b-4378-a0f3-779de97cfff1)



## POPL Aspects
code pointers too  
What were the POPL aspects involved in the implementation. NOT theoretical answers. Have pointers to the lines of code and explain the POPL ideas/concepts involved and why they are necessary. I expect 5 to 10 points written on POPL aspects (bullet points, one after another). More the points you have the better it is. While writing the points also write your experience of the difficulties you faced  

```RUST
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}
```
```RUST
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}
```
## Results
Tests conducted. Dataset used. Benchmarks run. Show graphs. Line graphs, bar graphs, etc. How are you checking/validating that these results align with your initial problem statement. Data-driven proof points that the solution/system is working. Why should I be convinced it is working?    

* We consider the results of transpilation in wall clock time, memory consumption, and complexity in terms of issues encountered and regularity for potential automation.  
* We also consider what processes transpiled sources now allow.   
* Lines of code is not considered a feasible measure because the number of lines is almost the same, with differences being due to the differing formatters of each language.

## `RUST->`  
  ![rust](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/ea5e63ce-bd51-4467-81e5-39c0a7c96611)

## `PYTHON->`  
![python](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/4e3c5696-be7e-4d74-8fdc-fa174b636195)

Language | Execution time | Memory(peak)
| :--- | ---: | :---:
PYTHON        | Content Cell | Content Cell
RUST          | Content Cell | Content Cell



* In the experiments, the parameters to the algorithm are built-into the library, which reduces reliability of the measurements for both the Python and the transpiled Rust implementations.  
* Measurements were taken with careful examination of allocations and verification of produced outputs.  
* After automatic syntax conversion, we used regular expressions extensively to fix remaining errors and library references.  
* Multiple manual implementations of expressions (< 1 % of all expressions) were required though each was straightforward with output from the Rust compiler.  

## `Graph`
![photo_2023-11-20_00-51-38](https://github.com/Shlokkzz/POPL-MileStone2/assets/101893296/2bb3c037-a5dd-4a2b-8f74-4a1e61e15207)  
edit legends



## Potential for future work
Blah


