# Determinants and Invertible Matrices (Linear Algebra)

## Overview
The determinant is a scalar value associated with a square matrix that provides crucial information about the matrix's properties. Invertible matrices are non-singular matrices that have multiplicative inverses.

## KEY FORMULAS

### 2×2 Determinant
$$\det(A) = \begin{vmatrix} a & b \\ c & d \end{vmatrix} = ad - bc$$

### 3×3 Determinant (Rule of Sarrus)
$$\det(A) = \begin{vmatrix} a & b & c \\ d & e & f \\ g & h & i \end{vmatrix} = aei + bfg + cdh - ceg - afh - bdi$$

### General Determinant (Cofactor Expansion)
$$\det(A) = \sum_{j=1}^{n} (-1)^{i+j} a_{ij} M_{ij}$$
where $M_{ij}$ is minor (determinant of submatrix with row $i$ and column $j$ deleted)

### Matrix Inverse (2×2)
$$A^{-1} = \frac{1}{\det(A)} \begin{bmatrix} d & -b \\ -c & a \end{bmatrix}$$

### General Matrix Inverse
$$A^{-1} = \frac{1}{\det(A)} \text{adj}(A)$$
where adj$(A)$ is adjugate (transpose of cofactor matrix)

### Invertibility Condition
Matrix $A$ is invertible ⟺ $\det(A) \neq 0$

## SOLUTION PATTERN

### For Calculating 2×2 Determinant
1. Identify elements $a, b, c, d$
2. Calculate $ad - bc$
3. Simplify

### For Calculating 3×3 Determinant
1. Choose row or column for expansion
2. Calculate cofactors: $(-1)^{i+j}M_{ij}$
3. Sum contributions
4. Simplify

### For Finding Matrix Inverse
1. Calculate $\det(A)$
2. If $\det(A) = 0$: inverse doesn't exist
3. If $\det(A) \neq 0$: calculate adjugate or use formula
4. Multiply by $\frac{1}{\det(A)}$
5. Verify: $AA^{-1} = I$

## EXAMPLES

### Example 1: 2×2 Determinant
**Problem**: Find $\det(A)$ where $A = \begin{bmatrix} 3 & 2 \\ 1 & 4 \end{bmatrix}$

**Solution**:
$$\det(A) = 3(4) - 2(1) = 12 - 2 = 10$$

### Example 2: 3×3 Determinant (Expansion along first row)
**Problem**: Find $\det(B)$ where $B = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{bmatrix}$

**Solution**:
$$\det(B) = 1\begin{vmatrix} 5 & 6 \\ 8 & 9 \end{vmatrix} - 2\begin{vmatrix} 4 & 6 \\ 7 & 9 \end{vmatrix} + 3\begin{vmatrix} 4 & 5 \\ 7 & 8 \end{vmatrix}$$
$$= 1(45-48) - 2(36-42) + 3(32-35)$$
$$= -3 + 12 - 9 = 0$$

### Example 3: Matrix Inverse (2×2)
**Problem**: Find $A^{-1}$ where $A = \begin{bmatrix} 2 & 1 \\ 1 & 1 \end{bmatrix}$

**Solution**:
- $\det(A) = 2(1) - 1(1) = 1$
- $A^{-1} = \frac{1}{1} \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix} = \begin{bmatrix} 1 & -1 \\ -1 & 2 \end{bmatrix}$

## PROPERTIES

### Determinant Properties
- $\det(A^T) = \det(A)$
- $\det(AB) = \det(A)\det(B)$
- $\det(A^{-1}) = \frac{1}{\det(A)}$
- Swapping rows: $\det$ changes sign
- Scaling row by $c$: $\det$ multiplied by $c$
- Adding multiple of one row to another: $\det$ unchanged

## CONSTRAINTS
- Determinant only defined for square matrices
- Inverse exists only if $\det(A) \neq 0$

## WATCH OUT

❌ **Wrong**: Calculating 3×3 determinant incorrectly
✅ **Correct**: Know whether you're using rule of Sarrus or cofactor expansion

❌ **Wrong**: Using incorrect formula for matrix inverse
✅ **Correct**: For 2×2: swap diagonal, negate off-diagonal, divide by det

❌ **Wrong**: Not checking if matrix is invertible before finding inverse
✅ **Correct**: Always verify $\det(A) \neq 0$ first

❌ **Wrong**: Sign errors in cofactor expansion
✅ **Correct**: Alternating signs: $(-1)^{i+j}$ depends on position