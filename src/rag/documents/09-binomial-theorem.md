# Binomial Theorem (Algebra)

## Overview
The binomial theorem provides a formula for expanding powers of binomials. It's essential for probability, combinatorics, and polynomial expansion problems.

## KEY FORMULAS

### Binomial Expansion
$$(a + b)^n = \sum_{k=0}^{n} \binom{n}{k} a^{n-k} b^k$$

### Binomial Coefficient
$$\binom{n}{k} = \frac{n!}{k!(n-k)!}$$

### General Term
$$T_{k+1} = \binom{n}{k} a^{n-k} b^k$$

### Properties
- Number of terms: $n + 1$
- Sum of coefficients: $\binom{n}{0} + \binom{n}{1} + \cdots + \binom{n}{n} = 2^n$
- Pascal's Triangle: $\binom{n}{k} = \binom{n-1}{k-1} + \binom{n-1}{k}$

## SOLUTION PATTERN

1. **Identify values of $a$, $b$, and $n$**
2. **Determine which terms to find** (if not all)
3. **Use general term formula** for specific terms
4. **Calculate binomial coefficients** carefully
5. **Simplify** the expression

## EXAMPLES

### Example 1: Expansion
**Problem**: Expand $(x + 2)^3$

**Solution**:
$$(x + 2)^3 = \sum_{k=0}^{3} \binom{3}{k} x^{3-k} 2^k$$
$$= \binom{3}{0}x^3 + \binom{3}{1}x^2 \cdot 2 + \binom{3}{2}x \cdot 4 + \binom{3}{3} \cdot 8$$
$$= x^3 + 6x^2 + 12x + 8$$

### Example 2: Finding Specific Term
**Problem**: Find coefficient of $x^7$ in $(2x - \frac{1}{x})^{10}$

**Solution**:
- General term: $T_{k+1} = \binom{10}{k}(2x)^{10-k}(-\frac{1}{x})^k$
- $= \binom{10}{k} 2^{10-k} (-1)^k x^{10-2k}$
- For $x^7$: $10 - 2k = 7 \Rightarrow k = 1.5$ (not integer)
- For this binomial, $x^7$ doesn't appear cleanly

### Example 3: Finding Middle Term
**Problem**: Find middle term of $(a + b)^6$

**Solution**:
- Number of terms = 7
- Middle term is 4th term: $T_4 = \binom{6}{3}a^3b^3 = 20a^3b^3$

## CONSTRAINTS
- $n$ must be non-negative integer
- Terms are indexed from $k = 0$ to $k = n$

## WATCH OUT

❌ **Wrong**: Forgetting to apply exponent to both terms
✅ **Correct**: $(a+b)^n$ applies to both $a^{n-k}$ and $b^k$

❌ **Wrong**: Incorrect binomial coefficient calculation
✅ **Correct**: $\binom{n}{k} = \frac{n!}{k!(n-k)!}$

❌ **Wrong**: Missing negative signs in coefficients
✅ **Correct**: $(a - b)^n$ has alternating signs

❌ **Wrong**: Confusing term number with $k$ value
✅ **Correct**: $T_{k+1}$ is the $(k+1)$-th term