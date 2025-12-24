# Eigenvalues and Eigenvectors (Linear Algebra)

## Overview
Eigenvalues and eigenvectors reveal important structural properties of linear transformations. They're essential in stability analysis, principal component analysis, and many engineering applications.

## KEY FORMULAS

### Eigenvalue Definition
For square matrix $A$, scalar $\lambda$ is eigenvalue if:
$$A\mathbf{v} = \lambda \mathbf{v}$$
for some non-zero vector $\mathbf{v}$ (eigenvector)

### Characteristic Polynomial
$$\det(A - \lambda I) = 0$$

### Eigenvalue Equation
For 2×2 matrix $A = \begin{bmatrix} a & b \\ c & d \end{bmatrix}$:
$$\lambda^2 - (a+d)\lambda + (ad-bc) = 0$$
$$\lambda^2 - \text{(trace)}  \lambda + \det(A) = 0$$

### Trace and Determinant
- Trace: $\text{tr}(A) = \sum a_{ii}$ (sum of diagonal)
- Sum of eigenvalues: $\lambda_1 + \lambda_2 = \text{tr}(A)$
- Product of eigenvalues: $\lambda_1 \lambda_2 = \det(A)$

## SOLUTION PATTERN

### Finding Eigenvalues
1. Set up characteristic equation: $\det(A - \lambda I) = 0$
2. Expand determinant
3. Solve polynomial equation
4. Each root is an eigenvalue

### Finding Eigenvectors
1. For each eigenvalue $\lambda$:
2. Solve $(A - \lambda I)\mathbf{v} = \mathbf{0}$
3. Find basis vectors for null space
4. These are eigenvectors corresponding to $\lambda$

## EXAMPLES

### Example 1: Finding Eigenvalues (2×2)
**Problem**: Find eigenvalues of $A = \begin{bmatrix} 4 & 1 \\ 1 & 3 \end{bmatrix}$

**Solution**:
$$\det(A - \lambda I) = \begin{vmatrix} 4-\lambda & 1 \\ 1 & 3-\lambda \end{vmatrix}$$
$$= (4-\lambda)(3-\lambda) - 1 = \lambda^2 - 7\lambda + 11$$
$$\lambda = \frac{7 \pm \sqrt{49-44}}{2} = \frac{7 \pm \sqrt{5}}{2}$$

### Example 2: Finding Eigenvector
**Problem**: Find eigenvector for $\lambda = 5$ of $A = \begin{bmatrix} 3 & 2 \\ 2 & 3 \end{bmatrix}$

**Solution**:
$$(A - 5I)\mathbf{v} = \begin{bmatrix} -2 & 2 \\ 2 & -2 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \mathbf{0}$$
- From first row: $-2x + 2y = 0 \Rightarrow x = y$
- Eigenvector: $\mathbf{v} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$ (or any scalar multiple)

### Example 3: Symmetric Matrix
**Problem**: For $A = \begin{bmatrix} 1 & 2 \\ 2 & 1 \end{bmatrix}$, find eigenvalues and eigenvectors

**Solution**:
- Characteristic equation: $\lambda^2 - 2\lambda - 3 = 0$
- $(\lambda - 3)(\lambda + 1) = 0 \Rightarrow \lambda = 3, -1$
- For $\lambda = 3$: $(A-3I)\mathbf{v} = 0 \Rightarrow \mathbf{v} = \begin{bmatrix} 1 \\ 1 \end{bmatrix}$
- For $\lambda = -1$: $(A+I)\mathbf{v} = 0 \Rightarrow \mathbf{v} = \begin{bmatrix} 1 \\ -1 \end{bmatrix}$

## PROPERTIES

### Symmetric Matrices
- All eigenvalues are real
- Eigenvectors are orthogonal
- Matrix can be diagonalized: $A = PDP^{-1}$

### Real Matrices
- Complex eigenvalues occur in conjugate pairs
- Non-symmetric matrices may have non-orthogonal eigenvectors

## CONSTRAINTS
- $n \times n$ matrix has exactly $n$ eigenvalues (counting multiplicity)
- Eigenvectors must be non-zero

## WATCH OUT

❌ **Wrong**: Confusing eigenvalue equation with its solution
✅ **Correct**: Set $\det(A - \lambda I) = 0$, then solve for $\lambda$

❌ **Wrong**: Forgetting to set $(A - \lambda I)\mathbf{v} = \mathbf{0}$ for eigenvectors
✅ **Correct**: Use null space of $(A - \lambda I)$

❌ **Wrong**: Treating zero vector as eigenvector
✅ **Correct**: Eigenvectors must be non-zero

❌ **Wrong**: Assuming eigenvectors are unique
✅ **Correct**: Any non-zero scalar multiple is also an eigenvector