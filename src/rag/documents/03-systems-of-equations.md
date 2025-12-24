# Systems of Linear Equations (Algebra)

## Overview
Systems of linear equations are sets of equations with multiple variables. They appear extensively in coordinate geometry, optimization, and physics problems. Multiple solution methods exist.

## KEY FORMULAS

### System of 2 Equations with 2 Variables
$$a_1x + b_1y = c_1$$
$$a_2x + b_2y = c_2$$

### Cramer's Rule (2×2)
$$x = \frac{\begin{vmatrix} c_1 & b_1 \\ c_2 & b_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}} = \frac{c_1b_2 - c_2b_1}{a_1b_2 - a_2b_1}$$

$$y = \frac{\begin{vmatrix} a_1 & c_1 \\ a_2 & c_2 \end{vmatrix}}{\begin{vmatrix} a_1 & b_1 \\ a_2 & b_2 \end{vmatrix}} = \frac{a_1c_2 - a_2c_1}{a_1b_2 - a_2b_1}$$

### Determinant (Coefficient Matrix)
$$\Delta = a_1b_2 - a_2b_1$$

## SOLUTION PATTERN

### Method 1: Substitution
1. Solve one equation for one variable
2. Substitute into second equation
3. Solve for remaining variable
4. Substitute back to find first variable

### Method 2: Elimination
1. Multiply equations to make coefficients equal
2. Subtract to eliminate one variable
3. Solve for remaining variable
4. Substitute back

### Method 3: Matrix Method
1. Express as $AX = B$ where $X = \begin{bmatrix} x \\ y \end{bmatrix}$
2. Calculate determinant of $A$
3. Use Cramer's rule

## EXAMPLES

### Example 1: Substitution Method
**Problem**: Solve
$$2x + y = 7$$
$$x - y = 2$$

**Solution**:
- From equation 2: $x = y + 2$
- Substitute in equation 1: $2(y+2) + y = 7$
- $2y + 4 + y = 7$
- $3y = 3 \Rightarrow y = 1$
- $x = 1 + 2 = 3$

**Verification**: $2(3) + 1 = 7$ ✓ and $3 - 1 = 2$ ✓

### Example 2: Elimination Method
**Problem**: Solve
$$3x + 2y = 12$$
$$5x - 2y = 8$$

**Solution**:
- Add equations (to eliminate $y$): $8x = 20 \Rightarrow x = 2.5$
- Substitute: $3(2.5) + 2y = 12 \Rightarrow 2y = 4.5 \Rightarrow y = 2.25$

## NATURE OF SOLUTIONS

- **Unique solution**: $\Delta \neq 0$ (lines intersect at one point)
- **Infinite solutions**: $\Delta = 0$ and consistency satisfied (lines coincident)
- **No solution**: $\Delta = 0$ but inconsistent (parallel lines)

## CONSTRAINTS
- Coefficient matrix must be non-singular for Cramer's rule
- Check consistency of system before solving

## WATCH OUT

❌ **Wrong**: Making arithmetic errors in elimination step
✅ **Correct**: Carefully multiply entire equations

❌ **Wrong**: Forgetting to substitute back
✅ **Correct**: Always verify solution in both original equations

❌ **Wrong**: Assuming unique solution always exists
✅ **Correct**: Check determinant first