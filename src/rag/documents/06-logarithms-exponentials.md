# Logarithms and Exponentials (Algebra)

## Overview
Logarithmic and exponential functions are inverse operations. They appear in growth/decay problems, probability, and many advanced topics. Understanding their properties is essential.

## KEY FORMULAS

### Exponential Function
$$a^x \text{ where } a > 0, a \neq 1$$

### Logarithm Definition
$$\log_a(x) = y \Leftrightarrow a^y = x$$

### Common Logarithms
- Natural log: $\ln(x) = \log_e(x)$
- Common log: $\log_{10}(x)$
- Binary log: $\log_2(x)$

### Logarithm Properties
$$\log_a(xy) = \log_a(x) + \log_a(y)$$
$$\log_a\left(\frac{x}{y}\right) = \log_a(x) - \log_a(y)$$
$$\log_a(x^n) = n\log_a(x)$$
$$\log_a(x) = \frac{\log_b(x)}{\log_b(a)}$$ (Change of base)

### Exponential Properties
$$a^{m+n} = a^m \cdot a^n$$
$$a^{m-n} = \frac{a^m}{a^n}$$
$$a^{mn} = (a^m)^n$$
$$(ab)^n = a^n b^n$$

## SOLUTION PATTERN

### Solving Exponential Equations
1. Express both sides with same base if possible
2. Equate exponents
3. Solve for variable

### Solving Logarithmic Equations
1. Use logarithm properties to combine/expand
2. Convert to exponential form
3. Solve for variable
4. **Verify domain**: Argument must be positive

## EXAMPLES

### Example 1: Exponential Equation
**Problem**: Solve $2^x = 16$

**Solution**:
- Express 16 as power of 2: $2^x = 2^4$
- Equate exponents: $x = 4$

### Example 2: Logarithmic Equation
**Problem**: Solve $\log_2(x) + \log_2(x-1) = 3$

**Solution**:
- Combine logs: $\log_2[x(x-1)] = 3$
- Convert to exponential: $x(x-1) = 2^3 = 8$
- $x^2 - x - 8 = 0$
- $x = \frac{1 \pm \sqrt{33}}{2}$
- **Check domain**: $x > 1$ (both log arguments positive)
- **Solution**: $x = \frac{1 + \sqrt{33}}{2}$

## CONSTRAINTS

### Domain
- Exponential: defined for all real $x$
- Logarithm: $x > 0$ only

### Base Restrictions
- Base must be positive and not equal to 1

## WATCH OUT

❌ **Wrong**: Taking log of negative number
✅ **Correct**: Logarithm only defined for positive arguments

❌ **Wrong**: Forgetting to verify extraneous solutions
✅ **Correct**: Always check solutions in original equation

❌ **Wrong**: Incorrect base conversion
✅ **Correct**: Use formula $\log_a(b) = \frac{\ln(b)}{\ln(a)}$