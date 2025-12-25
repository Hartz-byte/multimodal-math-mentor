# Division and Remainders (Arithmetic)

## Overview
The Division Algorithm is the backbone of arithmetic operations. Understanding quotient, remainder relationships, and divisibility rules is critical for identifying factors and solving modular arithmetic problems.

## KEY CONCEPTS & FORMULAS

### The Division Algorithm
For any integer $a$ (dividend) and positive integer $b$ (divisor), there exist unique integers $q$ (quotient) and $r$ (remainder) such that:
$$a = bq + r, \quad 0 \leq r < b$$

### Modular Arithmetic Notation
If $a$ divided by $b$ leaves remainder $r$, we write:
$$a \equiv r \pmod{b}$$

### Divisibility Rules
*   **by 2**: Last digit is even.
*   **by 3**: Sum of digits is divisible by 3.
*   **by 4**: Last two digits form a number divisible by 4.
*   **by 5**: Last digit is 0 or 5.
*   **by 6**: Divisible by both 2 and 3.
*   **by 8**: Last three digits form a number divisible by 8.
*   **by 9**: Sum of digits is divisible by 9.
*   **by 10**: Last digit is 0.
*   **by 11**: Difference between sum of digits at odd places and sum of digits at even places is 0 or divisible by 11.

## SOLUTION PATTERNS

### Finding Remainder without Division
To find remainder of a large power, e.g., $2^{100}$ divided by 3:
1.  Look for a pattern in remainders of powers ($2^1, 2^2, \dots$).
2.  Or express base arithmetic: $2 \equiv -1 \pmod 3$.
3.  $2^{100} \equiv (-1)^{100} \pmod 3 \equiv 1 \pmod 3$.

### Long Division Steps (Polynomials)
1.  Arrange terms in descending order of power.
2.  Divide first term of dividend by first term of divisor.
3.  Multiply divisor by this result and subtract.
4.  Repeat with the new remainder.

## EXAMPLES

### Example 1: Basic Division Algorithm
**Problem**: A number when divided by 8 gives a quotient of 12 and remainder 5. Find the number.
**Solution**:
*   Formula: $Dividend = (Divisor \times Quotient) + Remainder$
*   $N = (8 \times 12) + 5$
*   $N = 96 + 5 = 101$

### Example 2: Divisibility by 9
**Problem**: Is the number 45,783 divisible by 9?
**Solution**:
*   Sum of digits: $4+5+7+8+3 = 27$
*   Since 27 is divisible by 9, the original number is divisible by 9.

### Example 3: Polynomial Division Remainder
**Problem**: Find remainder when $P(x) = x^3 - 2x^2 + x + 1$ is divided by $x-1$.
**Solution**:
*   Use **Remainder Theorem**: If $P(x)$ is divided by $x-a$, remainder is $P(a)$.
*   Here $a=1$.
*   $P(1) = 1^3 - 2(1)^2 + 1 + 1 = 1 - 2 + 1 + 1 = 1$.
*   Remainder is 1.

## COMMON MISTAKES

### Mistake 1: Negative Remainders
❌ **Wrong**: "Remainder is -2".
✅ **Correct**: In Euclidean division, remainder $r$ must satisfy $0 \leq r < b$. If you get -2 mod 5, correct remainder is $5 + (-2) = 3$.

### Mistake 2: Mixing Divisors
❌ **Wrong**: Applying rule of 3 to check divisibility by 9 (converse not true).
✅ **Correct**: Divisibility by 9 implies by 3, but divisibility by 3 does NOT imply by 9.

### Mistake 3: Zero Divisor
❌ **Wrong**: Dividing by zero.
✅ **Correct**: Division by zero is undefined.

## RELATED CONCEPTS
*   **Remainder Theorem**: For polynomial division.
*   **Factor Theorem**: Remainder is 0 $\iff$ $(x-a)$ is a factor.
*   **Euclidean Algorithm**: finding GCD using division.
*   **Congruences**: $a \equiv b \pmod n$.
