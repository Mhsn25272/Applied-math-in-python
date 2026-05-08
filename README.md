# Applied Math in Python 🧮
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A repository dedicated to bridging the gap between abstract mathematical concepts and practical Python implementation. This project focuses on building foundational tools for Data Science and Machine Learning from first principles.

## 🎯 Project Goals
The main objective is to gain a deep understanding of the "mechanics" behind data algorithms by implementing them without relying heavily on high-level libraries initially.

## 🗺️ Learning Roadmap
- [x] **Calculus**: Power Rule, Derivatives, and Gradient Descent concepts.
- [x] **Algebra**: Polynomials, functions, and equation solvers.
- [ ] **Statistics & Probability**: Distributions, Mean/Median/Mode, Variance, etc.
- [ ] **Linear Algebra**: Matrix operations, Vectors, and Eigenvalues.

## 🚀 Featured Implementation: Polynomial Derivative
This script calculates the derivative of a polynomial function $f(x) = 3x^n + 12x - i$ using the **Power Rule**.

### Mathematical Background
The derivative of $x^n$ is $nx^{n-1}$. Therefore:
- Function: $f(x) = 3x^n + 12x - i$
- Derivative: $f'(x) = 3nx^{n-1} + 12$

### Code Snippet
```python
# Simple implementation of the Power Rule
x = float(input('Enter value for x: '))
n = float(input('Enter exponent n: '))
i = float(input('Enter constant i: '))

# Function Calculation
fx = 3 * x**n + 12 * x - i
# Derivative Calculation (f')
dfx = 3 * n * x**(n-1) + 12

print(f"f({x}) = {fx}")
print(f"f'({x}) = {dfx}")
```
## 🛠️ Requirements
Python 3.x

No external libraries required (Pure Python)
## 📄 License
This project is licensed under the MIT License - see the LICENSE file for details.
