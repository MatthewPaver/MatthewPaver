"""
# Numpy, Matplotlib and Math preliminaries
Numpy is a python library that provides data structures useful for data mining such as arrays, and various functions on those data structures.

Features:
- Vector operations (addition, dot product, outer product)
- Matrix operations (addition, multiplication)
- Matrix properties (inverse, rank)
- Eigenvalue analysis
- Gradient descent visualization
"""

import numpy as np

"""
## Excercise 1
Given $\overline{X} = (1,2,3,4,5,6,7,8,9,10)^T$ and $\overline{Y} = (10,9,8,7,6,5,4,3,2,1)^T$ find

1. $\overline{X} + \overline{Y}$
2. $\overline{X}^T \overline{Y}$
2. $\overline{X}\overline{Y}^T$
"""

# Create vectors X and Y
X = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Y = np.array([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])

# 1. Vector addition X + Y
addition = X + Y
print("\n----------------------Excercise 1-------------------------------\n \n Part 1: Vector addition X + Y")
print("X + Y =", addition)

# 2. Inner product X^T * Y (dot product)
inner_product = np.dot(X, Y)
print("\nPart 2: Inner Product (dot product)\nX^T * Y =", inner_product)

# 3. Outer product X * Y^T
outer_product = np.outer(X, Y)
print("\nPart 3: Outer Product \nX * Y^T =")
print(outer_product)




"""---
## Excercise 2
Given two matrices
$\overline{A} = \begin{pmatrix}1 & 2 & 3 & 4 & 5\\ 6 & 7 & 8 & 9 & 10\\ 11 & 12 & 13 & 14 & 15\\ 16 & 17 & 18 & 19 & 20\\ 21 & 22 & 23 & 24 & 25 \end{pmatrix}$
and
$\overline{B} = \begin{pmatrix}0 & 1 & 0 & 1 & 0\\ 1 & 2 & 3 & 4 & 5\\ -1 & 0 & 1 & 0 & -1 \\ 5 & 4 & 3 & 2 & 5\\ -1 & 0 & 1 & 0 & -1 \end{pmatrix}$

1. Compute $\overline{A} + \overline{B}$
2. Compute $\overline{B} + \overline{A}$. Is it equal to $\overline{A} + \overline{B}$? Is it always the case?
3. Compute $\overline{A} \cdot \overline{B}$
4. Compute $\overline{B} \cdot \overline{A}$. Is it equal to $\overline{A} \cdot \overline{B}$?
"""

# Create matrices A and B
A = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
])

B = np.array([
    [0, 1, 0, 1, 0],
    [1, 2, 3, 4, 5],
    [-1, 0, 1, 0, -1],
    [5, 4, 3, 2, 5],
    [-1, 0, 1, 0, -1]
])

print("\n----------------------Exercise 2-------------------------------")

# 1. A + B
addition_AB = A + B
print("\n Part 1: A + B =\n", addition_AB)

# 2. B + A and comparison
addition_BA = B + A
print("\Part 2: B + A =\n", addition_BA)
print("\nAre A+B and B+A equal?", np.array_equal(addition_AB, addition_BA))
print("Note: Matrix addition is always commutative (A+B = B+A)")

# 3. A·B
mult_AB = np.dot(A, B)
print("\nPart 3: 3. A·B =\n", mult_AB)

# 4. B·A and comparison
mult_BA = np.dot(B, A)
print("\n4. B·A =\n", mult_BA)
print("\nAre A·B and B·A equal?", np.array_equal(mult_AB, mult_BA))
print("Note: Matrix multiplication is not commutative (A·B ≠ B·A in general)")

"""---
## Excercise 3
Compute the inverse of the following matrix
$\overline{A} = \begin{pmatrix} 1 & 2 & 4\\ -2 & 1 & 5 \\1 & 2 & 3 \end{pmatrix}$, if one exsits. Verify that the matrix product of $\overline{A}$ and its inverse is the 3x3 identity matrix.
"""

print("\n----------------------Exercise 3-------------------------------")

# Create matrix A
A = np.array([
    [1, 2, 4],
    [-2, 1, 5],
    [1, 2, 3]
])

# Check if matrix is invertible
det = np.linalg.det(A)
print("\nDeterminant of A:", det)

if det != 0:
    # Calculate inverse
    A_inv = np.linalg.inv(A)
    print("\nInverse of A:\n", A_inv)
    
    # Verify: A · A^(-1) should be identity matrix
    identity_check = np.dot(A, A_inv)
    print("\nA · A^(-1):\n", identity_check)
    
    # Check if result is close to identity matrix
    identity = np.eye(3)
    is_identity = np.allclose(identity_check, identity)
    print("\nIs A · A^(-1) equal to identity matrix?", is_identity)
else:
    print("\nMatrix is not invertible (singular)")

print("\n----------------------Exercise 4-------------------------------")

# Create matrix A
A = np.array([
    [1, 0, 1],
    [0, 1, 1],
    [0, 0, 0]
])

# Create matrix B
B = np.array([
    [1, 2, 1],
    [-2, -3, 1],
    [3, 5, 0]
])

# Calculate ranks
rank_A = np.linalg.matrix_rank(A)
rank_B = np.linalg.matrix_rank(B)

print("\nMatrix A:\n", A)
print("Rank of A:", rank_A)

print("\nMatrix B:\n", B)
print("Rank of B:", rank_B)



"""---
## Excercise 5
Find the eigenvalues of matrix
 $\overline{A} = \left(\begin{matrix} 4 & 2\\ 1 & 3\end{matrix}\right)$
"""

print("\n----------------------Exercise 5-------------------------------")

# Create matrix A
A = np.array([
    [4, 2],
    [1, 3]
])

# Calculate eigenvalues
eigenvalues = np.linalg.eigvals(A)

print("\nMatrix A:\n", A)
print("\nEigenvalues of A:", eigenvalues)

# Optional: Calculate eigenvectors too
eigenvalues, eigenvectors = np.linalg.eig(A)
print("\nEigenvectors of A:\n", eigenvectors)

"""---
## Excercise 6

For this excercise we will need [Matplotlib](https://matplotlib.org/index.html). Follow [the official Matplotlib tutorial](https://matplotlib.org/tutorials/introductory/pyplot.html#) and familiarize yourself with Matplotlib.

Recall from the lecture the Gradient Descent method for finding local minimum of a function:

1. Pick an initial point $\overline{X}_0$
2. Iterate according to $\overline{X}_{i+1} = \overline{X}_i - \gamma \cdot \big((\nabla_{\overline{X}} f)(\overline{X}_i) \big)$


Examine this method by trying to find the minimum of the function $f(x) = (x-3)^2$. More specifically, for every $\gamma \in \{0.01, 0.1, 0.9, 1, 2\}$:
1. Plot the graph of $f(x) = (x-3)^2$
2. Pick an intial point $x = -4$
3. Run 20 interations of the methods
4. In every iteration $i = 1, \ldots, 20$, plot the point $(x_i, f(x_i))$ on the same plot as the graph of the function $f(x)$

Interpret the results.
"""

import matplotlib.pyplot as plt

def f(x):
    return (x - 3)**2

def df(x):
    return 2 * (x - 3)

# Create x values for plotting
x = np.linspace(-5, 10, 100)
y = f(x)

# Gamma values to test
gammas = [0.01, 0.1, 0.9, 1, 2]

# Create subplots for each gamma
fig, axs = plt.subplots(2, 3, figsize=(15, 10))
axs = axs.ravel()

for idx, gamma in enumerate(gammas):
    # Plot function
    axs[idx].plot(x, y, 'b-', label='f(x)')
    
    # Initialize starting point
    x_i = -4
    points_x = [x_i]
    points_y = [f(x_i)]
    
    # Gradient descent iterations
    for _ in range(20):
        x_i = x_i - gamma * df(x_i)
        points_x.append(x_i)
        points_y.append(f(x_i))
    
    # Plot points
    axs[idx].scatter(points_x, points_y, c='r', s=50, alpha=0.5)
    axs[idx].set_title(f'γ = {gamma}')
    axs[idx].set_xlabel('x')
    axs[idx].set_ylabel('f(x)')
    axs[idx].grid(True)
    
plt.tight_layout()
plt.show()
