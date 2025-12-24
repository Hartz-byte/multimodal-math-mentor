# Quadratic Equations (Algebra)

## Overview
Quadratic equations are polynomial equations of degree 2. They are fundamental in algebra and appear frequently in JEE problems. Understanding multiple solution methods is crucial.

## KEY FORMULAS

### Standard Form
$$ax^2 + bx + c = 0, \quad a \neq 0$$

### Quadratic Formula (Universal Method)
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

### Discriminant
$$\Delta = b^2 - 4ac$$

### Nature of Roots
- If $\Delta > 0$: Two distinct real roots
- If $\Delta = 0$: One real root (repeated)
- If $\Delta < 0$: Two complex conjugate roots

### Sum and Product of Roots
$$x_1 + x_2 = -\frac{b}{a}$$
$$x_1 \cdot x_2 = \frac{c}{a}$$

### Factored Form
$$a(x - x_1)(x - x_2) = 0$$

## SOLUTION PATTERN

### Step-by-Step Method
1. **Identify coefficients**: Determine $a$, $b$, $c$ from equation
2. **Check if $a \neq 0$**: Ensure it's quadratic, not linear
3. **Calculate discriminant**: $\Delta = b^2 - 4ac$
4. **Determine nature of roots**: Check sign of $\Delta$
5. **Apply appropriate method**:
   - For factorization: Check if roots are integers/simple
   - For quadratic formula: Use when factorization difficult
   - For completing square: When special form is needed
6. **Verify**: Substitute back into original equation

### Alternative Methods
- **Factorization**: $(px + q)(rx + s) = 0$
- **Completing the Square**: $(x + \frac{b}{2a})^2 = \frac{\Delta}{4a^2}$
- **Graphical**: Find x-intercepts of parabola $y = ax^2 + bx + c$

## EXAMPLES

### Example 1: Two Real Roots
**Problem**: Solve $x^2 - 5x + 6 = 0$

**Solution**:
- $a = 1, b = -5, c = 6$
- $\Delta = (-5)^2 - 4(1)(6) = 25 - 24 = 1 > 0$
- Two distinct real roots exist
- $x = \frac{5 \pm \sqrt{1}}{2} = \frac{5 \pm 1}{2}$
- $x_1 = 3, x_2 = 2$

**Verification**: $(3)^2 - 5(3) + 6 = 9 - 15 + 6 = 0$ ✓

**Alternative (Factorization)**: $(x-2)(x-3) = 0 \Rightarrow x = 2$ or $x = 3$

### Example 2: Complex Roots
**Problem**: Solve $x^2 + 2x + 5 = 0$

**Solution**:
- $a = 1, b = 2, c = 5$
- $\Delta = 4 - 20 = -16 < 0$
- Complex roots exist
- $x = \frac{-2 \pm \sqrt{-16}}{2} = \frac{-2 \pm 4i}{2} = -1 \pm 2i$

### Example 3: Using Sum and Product
**Problem**: If roots are 2 and 3, find equation

**Solution**:
- Sum of roots: $s = 2 + 3 = 5$
- Product of roots: $p = 2 \times 3 = 6$
- Equation: $x^2 - sx + p = 0$
- $x^2 - 5x + 6 = 0$

## CONSTRAINTS & DOMAIN RESTRICTIONS

1. **Coefficient constraint**: $a \neq 0$ (otherwise linear equation)
2. **Real roots condition**: $\Delta \geq 0$ for real solutions
3. **Domain of variables**: Check for context-specific restrictions
4. **Physical constraints**: In applied problems, roots must satisfy context
   - Example: Distance cannot be negative
   - Example: Probability must be between 0 and 1

## WATCH OUT - COMMON MISTAKES

### Mistake 1: Sign Error in Formula
❌ **Wrong**: $x = \frac{b \pm \sqrt{\Delta}}{2a}$ (forgot negative sign)
✅ **Correct**: $x = \frac{-b \pm \sqrt{\Delta}}{2a}$

### Mistake 2: Denominator Error
❌ **Wrong**: $x = \frac{-b \pm \sqrt{\Delta}}{a}$
✅ **Correct**: $x = \frac{-b \pm \sqrt{\Delta}}{2a}$ (denominator is $2a$, not $a$)

### Mistake 3: Discriminant Calculation
❌ **Wrong**: $\Delta = b^2 - 4c$ (forgot the $a$)
✅ **Correct**: $\Delta = b^2 - 4ac$

### Mistake 4: Forgetting the ±
❌ **Wrong**: $x = \frac{-b + \sqrt{\Delta}}{2a}$ (only positive root)
✅ **Correct**: $x = \frac{-b \pm \sqrt{\Delta}}{2a}$ (both roots)

### Mistake 5: Sign of Coefficients
❌ **Problem**: For $2x^2 - 3x - 5 = 0$, using $b = -3$ as positive
✅ **Correct**: $a = 2, b = -3, c = -5$ (keep signs)

### Mistake 6: Not Checking Nature of Roots First
❌ **Wrong**: Applying quadratic formula when roots are complex without realizing
✅ **Correct**: Check $\Delta$ first; if negative, expect complex roots

## RELATED CONCEPTS
- Polynomial functions
- Parabolas and conic sections
- Systems of quadratic equations
- Applications in physics and optimization

## TIPS FOR JEE
1. **Quick factorization check**: For integer roots, use factor theorem
2. **Mental math**: For $\Delta$, practice calculating $b^2 - 4ac$ quickly
3. **Completing the square**: Useful for certain algebraic manipulations
4. **Graphical understanding**: Visualize the parabola's position relative to x-axis
5. **Sylvester's criterion**: For systems with quadratics