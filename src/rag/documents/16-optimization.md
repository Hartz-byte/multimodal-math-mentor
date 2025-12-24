# Optimization and Curve Sketching (Calculus)

## Overview
Optimization uses calculus to find maximum and minimum values. Curve sketching synthesizes derivative information to graph functions accurately. Both are essential for applied mathematics.

## KEY FORMULAS

### First Derivative Test
For critical point $c$ where $f'(c) = 0$:
- If $f'$ changes from positive to negative: local maximum
- If $f'$ changes from negative to positive: local minimum
- If $f'$ doesn't change sign: neither (inflection point if $f''(c) = 0$)

### Second Derivative Test
For critical point $c$:
- If $f''(c) > 0$: local minimum
- If $f''(c) < 0$: local maximum
- If $f''(c) = 0$: inconclusive

### Concavity
- $f''(x) > 0$: concave up (∪)
- $f''(x) < 0$: concave down (∩)

### Inflection Points
Point where $f''(c) = 0$ and concavity changes

## OPTIMIZATION PATTERN

### Finding Absolute Extrema on Closed Interval [a,b]
1. Find all critical points in $(a,b)$
2. Evaluate $f$ at critical points
3. Evaluate $f$ at endpoints $a$ and $b$
4. Compare all values
5. Largest value is maximum, smallest is minimum

### Applied Optimization
1. **Set up problem**: Define variables
2. **Write objective function**: Expression to maximize/minimize
3. **Identify constraints**: Relationships between variables
4. **Express as single variable**: Use constraints to eliminate variables
5. **Find critical points**: Set derivative to zero
6. **Verify maximum/minimum**: Check second derivative or compare values
7. **Interpret**: Answer in context of problem

## CURVE SKETCHING STEPS

1. **Domain**: Find restrictions on $x$
2. **Symmetry**: Check even/odd, periodicity
3. **Intercepts**: Find $x$ and $y$ intercepts
4. **Asymptotes**:
   - Vertical: where denominator = 0
   - Horizontal: behavior as $x \to \pm\infty$
5. **First derivative**: Find increasing/decreasing intervals and extrema
6. **Second derivative**: Find concavity and inflection points
7. **Plot key points**: Intercepts, extrema, inflection points
8. **Sketch curve**: Connect smoothly through all information

## EXAMPLES

### Example 1: Optimization
**Problem**: Find dimensions of rectangle with maximum area inscribed in circle of radius 5

**Solution**:
- Let $x$ = half-width, $y$ = half-height
- Constraint: $x^2 + y^2 = 25$
- Objective: Maximize $A = 4xy$
- From constraint: $y = \sqrt{25 - x^2}$
- $A(x) = 4x\sqrt{25-x^2}$
- $A'(x) = 4\sqrt{25-x^2} + 4x \cdot \frac{-x}{\sqrt{25-x^2}}$
- $= \frac{4(25-2x^2)}{\sqrt{25-x^2}}$
- Set $A'(x) = 0$: $25 - 2x^2 = 0 \Rightarrow x = \frac{5}{\sqrt{2}}$
- $y = \frac{5}{\sqrt{2}}$
- **Answer**: Square with side $\frac{10}{\sqrt{2}} = 5\sqrt{2}$

### Example 2: Curve Sketching
**Problem**: Sketch $f(x) = x^3 - 3x$

**Solution**:
1. Domain: All real numbers
2. Symmetry: Odd function (passes through origin)
3. Intercepts: $y = 0$ at $x = 0, \pm\sqrt{3}$
4. No asymptotes
5. $f'(x) = 3x^2 - 3 = 3(x^2-1)$
   - Critical points: $x = \pm 1$
   - Increasing: $(-\infty,-1) \cup (1,\infty)$
   - Decreasing: $(-1,1)$
6. $f''(x) = 6x$
   - Concave down: $(-\infty,0)$
   - Concave up: $(0,\infty)$
   - Inflection point: $(0,0)$
7. Local max at $(-1,2)$, local min at $(1,-2)$

## WATCH OUT

❌ **Wrong**: Confusing critical point with extremum
✅ **Correct**: Not all critical points are extrema (could be inflection)

❌ **Wrong**: Forgetting to check endpoints in closed interval
✅ **Correct**: Absolute extrema occur at critical points or endpoints

❌ **Wrong**: Assuming critical point exists because $f'$ undefined
✅ **Correct**: Points where $f'$ undefined are critical but need special analysis

❌ **Wrong**: Incorrect sign analysis in first derivative test
✅ **Correct**: Test one point in each interval created by critical points