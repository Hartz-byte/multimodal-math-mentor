# Matrices and Matrix Operations (Linear Algebra)

## Overview
Matrices are rectangular arrays of numbers that represent linear transformations. Understanding matrix operations is fundamental to linear algebra and has applications in computer graphics, data analysis, and engineering.

## KEY FORMULAS

### Matrix Notation
$$A = \begin{bmatrix} a_{11} & a_{12} & \cdots & a_{1n} \\ a_{21} & a_{22} & \cdots & a_{2n} \\ \vdots & \vdots & \ddots & \vdots \\ a_{m1} & a_{m2} & \cdots & a_{mn} \end{bmatrix}, \quad A \in \mathbb{R}^{m \times n}$$

### Matrix Addition
$$(A + B)_{ij} = A_{ij} + B_{ij}$$

### Scalar Multiplication
$$(cA)_{ij} = c \cdot A_{ij}$$

### Matrix Multiplication
$$(AB)_{ij} = \sum_{k=1}^{n} A_{ik}B_{kj}$$
Note: Only defined if columns of $A$ = rows of $B$

### Transpose
$$(A^T)_{ij} = A_{ji}$$

### Special Matrices
- **Identity**: $I_n = \begin{bmatrix} 1 & 0 & \cdots & 0 \\ 0 & 1 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & 1 \end{bmatrix}$
- **Zero**: All entries are 0
- **Diagonal**: Non-zero only on diagonal

## SOLUTION PATTERN

1. **Verify dimensions**: Check compatibility for operations
2. **Identify operation type**: Addition, multiplication, transpose
3. **Apply operation systematically**
4. **Simplify result**
5. **Verify**: Check dimensions of result

## EXAMPLES

### Example 1: Matrix Multiplication
**Problem**: Find $AB$ where $A = \begin{bmatrix} 1 & 2 \\ 3 & 4 \end{bmatrix}$ and $B = \begin{bmatrix} 5 & 6 \\ 7 & 8 \end{bmatrix}$

**Solution**:
$$AB = \begin{bmatrix} 1(5)+2(7) & 1(6)+2(8) \\ 3(5)+4(7) & 3(6)+4(8) \end{bmatrix} = \begin{bmatrix} 19 & 22 \\ 43 & 50 \end{bmatrix}$$

### Example 2: Transpose
**Problem**: Find $A^T$ for $A = \begin{bmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{bmatrix}$

**Solution**:
$$A^T = \begin{bmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{bmatrix}$$

### Example 3: Matrix System
**Problem**: Express system in matrix form:
$$2x + 3y = 8$$
$$4x - y = 2$$

**Solution**:
$$\begin{bmatrix} 2 & 3 \\ 4 & -1 \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} = \begin{bmatrix} 8 \\ 2 \end{bmatrix}$$

## PROPERTIES

### Associativity
$$(AB)C = A(BC)$$

### Distributivity
$$A(B + C) = AB + AC$$

### Identity
$$AI = IA = A$$

### Non-Commutativity
$$AB \neq BA$$ in general

## CONSTRAINTS
- Matrix multiplication requires column count of first = row count of second
- Dimensions of result: $(m \times n) \times (n \times p) = (m \times p)$

## WATCH OUT

❌ **Wrong**: Assuming $AB = BA$
✅ **Correct**: Matrix multiplication is NOT commutative

❌ **Wrong**: Multiplying matrices with incompatible dimensions
✅ **Correct**: Check dimensions before multiplication

❌ **Wrong**: Confusing element-wise with matrix multiplication
✅ **Correct**: Matrix multiplication uses dot product of rows and columns