# Polynomials (Algebra)

## Overview
Polynomials are expressions with multiple terms involving powers of variables. Understanding polynomial operations, factorization, and roots is fundamental to advanced algebra.

## KEY FORMULAS

### Polynomial Definition
$$P(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0$$

### Remainder Theorem
If polynomial $P(x)$ is divided by $(x-a)$, remainder is $P(a)$

### Factor Theorem
$(x-a)$ is a factor of $P(x)$ if and only if $P(a) = 0$

### Rational Root Theorem
If $\frac{p}{q}$ is a rational root (in lowest terms), then:
- $p$ divides constant term
- $q$ divides leading coefficient

### Vieta's Formulas (for cubic $ax^3 + bx^2 + cx + d = 0$)
$$x_1 + x_2 + x_3 = -\frac{b}{a}$$
$$x_1x_2 + x_2x_3 + x_3x_1 = \frac{c}{a}$$
$$x_1x_2x_3 = -\frac{d}{a}$$

## SOLUTION PATTERN

### Factorization Strategy
1. Look for common factors
2. Try grouping
3. Check for special patterns (difference of squares, sum/difference of cubes)
4. Use rational root theorem to find one root
5. Use synthetic division or factorization
6. Repeat for quotient polynomial

### Finding Roots
1. Identify degree of polynomial
2. Use rational root theorem to test candidates
3. Verify root using remainder theorem
4. Perform polynomial division
5. Repeat for reduced polynomial

## EXAMPLES

### Example 1: Factorization
**Problem**: Factor $x^3 - 6x^2 + 11x - 6$

**Solution**:
- Possible rational roots: $\pm 1, \pm 2, \pm 3, \pm 6$
- Test $x=1$: $1 - 6 + 11 - 6 = 0$ ✓
- $(x-1)$ is a factor
- Divide: $x^3 - 6x^2 + 11x - 6 = (x-1)(x^2 - 5x + 6)$
- Factor $x^2 - 5x + 6 = (x-2)(x-3)$
- **Result**: $(x-1)(x-2)(x-3)$

### Example 2: Using Remainder Theorem
**Problem**: Find remainder when $P(x) = x^4 + 2x^3 - x + 5$ is divided by $(x-2)$

**Solution**:
- By remainder theorem, remainder = $P(2)$
- $P(2) = 16 + 16 - 2 + 5 = 35$
- **Remainder**: 35

## CONSTRAINTS
- Degree determines number of roots (counting multiplicity)
- Leading coefficient affects end behavior

## WATCH OUT

❌ **Wrong**: Missing all roots
✅ **Correct**: Count multiplicity (repeated roots)

❌ **Wrong**: Incorrect application of remainder theorem
✅ **Correct**: Evaluate $P(a)$ for divisor $(x-a)$

❌ **Wrong**: Ignoring complex roots
✅ **Correct**: Complex roots always appear in conjugate pairs for real polynomials