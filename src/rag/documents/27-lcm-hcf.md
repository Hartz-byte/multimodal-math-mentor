# LCM and HCF (Number Theory)

## Overview
Least Common Multiple (LCM) and Highest Common Factor (HCF), also known as Greatest Common Divisor (GCD), are fundamental concepts in arithmetic and number theory. They are essential for solving problems involving periodicity, arrangements, and simplifying fractions.

## KEY DEFINITIONS & FORMULAS

### Highest Common Factor (HCF/GCD)
The largest positive integer that divides two or more integers without a remainder.
$$HCF(a, b) = \max \{k : k|a \text{ and } k|b\}$$

### Least Common Multiple (LCM)
The smallest positive integer that is divisible by both of two or more integers.
$$LCM(a, b) = \min \{m : a|m \text{ and } b|m, m > 0\}$$

### Relationship between HCF and LCM
For any two positive integers $a$ and $b$:
$$HCF(a, b) \times LCM(a, b) = a \times b$$
*Note: This formula holds true ONLY for two numbers.*

### HCF and LCM of Fractions
$$HCF(\frac{a}{b}, \frac{c}{d}) = \frac{HCF(a, c)}{LCM(b, d)}$$
$$LCM(\frac{a}{b}, \frac{c}{d}) = \frac{LCM(a, c)}{HCF(b, d)}$$

## SOLUTION METHODS

### Method 1: Prime Factorization (Standard)
1.  Write numbers as product of prime factors.
2.  **For HCF**: Take the product of *lowest* powers of common prime factors.
3.  **For LCM**: Take the product of *highest* powers of all prime factors involved.

### Method 2: Division Method (Long Division for HCF)
1.  Divide larger number by smaller number.
2.  Make the remainder the new divisor and the previous divisor the new dividend.
3.  Repeat until remainder is 0. The last divisor is the HCF.

## EXAMPLES

### Example 1: HCF and LCM of Integers
**Problem**: Find HCF and LCM of 12 and 18.
**Solution**:
*   Prime Factorization:
    *   $12 = 2^2 \times 3^1$
    *   $18 = 2^1 \times 3^2$
*   **HCF**: Lowest powers of common primes ($2^1$, $3^1$) $\rightarrow 2 \times 3 = 6$
*   **LCM**: Highest powers of all primes ($2^2$, $3^2$) $\rightarrow 4 \times 9 = 36$
*   *Verification*: $12 \times 18 = 216$. $6 \times 36 = 216$. Formula holds.

### Example 2: Word Problem (Periodicity)
**Problem**: Two bells ring at intervals of 10 and 15 minutes. If they ring together at 10 AM, when will they ring together next?
**Solution**:
*   We need a time interval divisible by both 10 and 15. This is **LCM**.
*   $LCM(10, 15) = 30$.
*   They will ring together after 30 minutes, i.e., at 10:30 AM.

## COMMON MISTAKES

### Mistake 1: Confusing HCF and LCM Logic
❌ **Wrong**: Using HCF for "when will they meet again" problems.
✅ **Correct**: Meeting/repetition problems usually imply LCM. Grouping/cutting problems usually imply HCF.

### Mistake 2: Product Formula for 3 Numbers
❌ **Wrong**: $HCF(a,b,c) \times LCM(a,b,c) = a \times b \times c$
✅ **Correct**: This formula works strictly for **two** numbers. It typically fails for three or more.

### Mistake 3: Fraction Rules
❌ **Wrong**: Calculating HCF of numerators only.
✅ **Correct**: For fractions, HCF = HCF(numerators) / LCM(denominators).

## TIPS FOR COMPETITIVE EXAMS
1.  **Co-primes**: If two numbers are co-prime (HCF=1), their LCM is simply their product.
2.  **Euclid's Algorithm**: Useful for HCF of very large numbers.
3.  **Polynomials**: These concepts apply to algebraic expressions too (e.g., LCM of $x^2-1$ and $x^2+2x+1$).
