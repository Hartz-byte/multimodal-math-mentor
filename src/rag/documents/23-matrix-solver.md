# Matrix Inversion and Systems Solver (Solution Template)

## Purpose
Systematic approach to solving systems of linear equations and inverting matrices - common in JEE problems.

## Method 1: Gaussian Elimination (Row Reduction)

### For System: AX = B

**Step 1**: Form Augmented Matrix
```
[a₁₁ a₁₂ | b₁]
[a₂₁ a₂₂ | b₂]
```

**Step 2**: Row Operations (Goal: Get identity matrix on left)
```
1. R₂ → R₂ - (a₂₁/a₁₁)R₁  (eliminate below first pivot)
2. R₁ ↔ R₂                  (swap if needed for better pivot)
3. R₂ → R₂/a₂₂              (make diagonal element 1)
4. R₁ → R₁ - (a₁₂)R₂        (eliminate above second pivot)
```

**Step 3**: Read Solution
```
[1 0 | x]
[0 1 | y]
Solution: x = value, y = value
```

**Step 4**: Verify by Substitution

## Method 2: Inverse Matrix Method

For System: AX = B, Solution: X = A⁻¹B

### Finding A⁻¹

**For 2×2 Matrix**: A = [a  b; c  d]
```
Step 1: Calculate det(A) = ad - bc
        If det(A) = 0: No inverse exists
        
Step 2: A⁻¹ = (1/det(A)) [d   -b]
                           [-c   a]

Step 3: Verify: AA⁻¹ = I
```

**For 3×3 Matrix**:
```
Step 1: Calculate det(A) using cofactor expansion
        If det(A) = 0: No inverse exists

Step 2: Create cofactor matrix C where C_ij = (-1)^(i+j)M_ij
        (M_ij = minor, determinant with row i and column j deleted)

Step 3: A⁻¹ = (1/det(A)) × C^T (transpose of cofactor matrix)

Step 4: Verify: AA⁻¹ = I
```

### Solving System Using Inverse

```
Step 1: Write system as AX = B
Step 2: Calculate A⁻¹
Step 3: X = A⁻¹B (matrix multiply)
Step 4: Verify solution
```

## Method 3: Cramer's Rule (2×2 and 3×3)

For system:
```
a₁x + b₁y = c₁
a₂x + b₂y = c₂
```

**Solution**:
```
x = |c₁ b₁| / |a₁ b₁|
    |c₂ b₂|   |a₂ b₂|
    
y = |a₁ c₁| / |a₁ b₁|
    |a₂ c₂|   |a₂ b₂|
```

Numerator = determinant with column replaced by constants
Denominator = determinant of coefficient matrix

## Example Worked Solutions

### Example 1: Gaussian Elimination (2×2)
**System**: 2x + 3y = 8, 4x - y = 2

**Augmented Matrix**:
```
[2   3 | 8]
[4  -1 | 2]
```

**Reduce**:
```
[2   3 | 8]      R₂ → R₂ - 2R₁      [2    3  |  8]
[4  -1 | 2]  →                   →  [0   -7  | -14]
           
R₂ → R₂/(-7)  →  [2    3  |  8]
                 [0    1  |  2]

R₁ → R₁ - 3R₂ →  [2    0  |  2]
                 [0    1  |  2]

R₁ → R₁/2    →   [1    0  |  1]
                 [0    1  |  2]
```

**Solution**: x = 1, y = 2

### Example 2: Cramer's Rule
**System**: 2x + 3y = 8, 4x - y = 2

```
x = |8   3| / |2   3|  = (8·(-1) - 3·2) / (2·(-1) - 3·4)
    |2  -1|   |4  -1|    = (-8-6) / (-2-12)
                          = -14 / -14 = 1

y = |2   8| / |2   3|  = (2·2 - 8·4) / (2·(-1) - 3·4)
    |4   2|   |4  -1|    = (4-32) / (-2-12)
                          = -28 / -14 = 2
```

**Solution**: x = 1, y = 2

### Example 3: Inverse Matrix Method
**System**: AX = B where A = [2  3; 4 -1], B = [8; 2]

```
Step 1: det(A) = 2(-1) - 3(4) = -2 - 12 = -14

Step 2: A⁻¹ = (1/-14) [-1  -3]  = [1/14   3/14]
                      [-4   2]    [4/14  -2/14]

Step 3: X = A⁻¹B = [1/14   3/14] [8]  = [8/14 + 6/14]  = [14/14]  = [1]
              [4/14  -2/14] [2]    [32/14 - 4/14]   [28/14]   [2]

Solution: x = 1, y = 2
```

## Decision Guide: Which Method to Use?

| Situation | Best Method |
|-----------|-------------|
| 2×2 system, quick | Cramer's Rule |
| Large system | Gaussian Elimination |
| Need A⁻¹ explicitly | Inverse Matrix |
| Verification needed | Multiple methods |
| 3×3 system | Any method (elimination simplest) |

## Key Checks

✓ Number of equations = Number of unknowns (unique solution possible)
✓ Determinant ≠ 0 (inverse exists)
✓ Substitution back into original equations gives true statements
✓ Dimensions match in matrix multiplication

## Common Errors

- ❌ Wrong sign in Cramer's rule
- ❌ Determinant calculation error
- ❌ Forgetting to multiply entire row
- ❌ Not verifying solution
- ❌ Division by zero (no inverse)