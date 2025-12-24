# Sequences and Series (Algebra)

## Overview
Sequences and series involve ordered lists of numbers and their sums. Arithmetic and geometric progressions are fundamental patterns in mathematics and have numerous applications.

## KEY FORMULAS

### Arithmetic Progression (AP)
$$a_n = a_1 + (n-1)d$$
$$S_n = \frac{n}{2}(2a_1 + (n-1)d) = \frac{n}{2}(a_1 + a_n)$$

### Geometric Progression (GP)
$$a_n = a_1 \cdot r^{n-1}$$
$$S_n = a_1 \cdot \frac{1 - r^n}{1 - r} \quad (r \neq 1)$$
$$S_\infty = \frac{a_1}{1 - r} \quad (|r| < 1)$$

### Summation Formulas
$$\sum_{i=1}^{n} i = \frac{n(n+1)}{2}$$
$$\sum_{i=1}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}$$
$$\sum_{i=1}^{n} i^3 = \left[\frac{n(n+1)}{2}\right]^2$$

## SOLUTION PATTERN

### For AP Problems
1. Identify first term ($a_1$) and common difference ($d$)
2. Use $a_n$ formula to find specific terms
3. Use $S_n$ formula for sums

### For GP Problems
1. Identify first term ($a_1$) and common ratio ($r$)
2. Use $a_n$ formula to find specific terms
3. For sums: check if $|r| < 1$ for infinite series

## EXAMPLES

### Example 1: Arithmetic Progression
**Problem**: Find sum of first 20 terms of AP with first term 5 and common difference 3

**Solution**:
- $a_1 = 5, d = 3$
- $S_{20} = \frac{20}{2}(2 \cdot 5 + 19 \cdot 3) = 10(10 + 57) = 670$

### Example 2: Geometric Series (Infinite)
**Problem**: Find sum of series $2 + 1 + \frac{1}{2} + \frac{1}{4} + \ldots$

**Solution**:
- $a_1 = 2, r = \frac{1}{2}$
- $|r| = 0.5 < 1$, so series converges
- $S_\infty = \frac{2}{1 - 0.5} = \frac{2}{0.5} = 4$

## CONSTRAINTS
- AP/GP sum formulas assume arithmetic/geometric pattern throughout
- Geometric series converges only if $|r| < 1$

## WATCH OUT

❌ **Wrong**: Using infinite sum formula when $|r| \geq 1$
✅ **Correct**: Only use $S_\infty$ when $|r| < 1$

❌ **Wrong**: Confusing $a_n$ (nth term) with $S_n$ (sum to n terms)
✅ **Correct**: Use correct formula for what's being asked

❌ **Wrong**: Incorrect common difference/ratio
✅ **Correct**: Verify by checking second and third terms