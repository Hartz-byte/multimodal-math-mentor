# Limits and Continuity (Calculus)

## Overview
Limits form the foundation of calculus. They describe the behavior of functions as inputs approach specific values. Understanding limits is crucial for derivatives and integrals.

## KEY FORMULAS

### Limit Definition
$$\lim_{x \to a} f(x) = L \text{ means: for every } \epsilon > 0, \exists \delta > 0 \text{ such that } |x-a| < \delta \implies |f(x)-L| < \epsilon$$

### Limit Laws
$$\lim_{x \to a} [f(x) + g(x)] = \lim_{x \to a} f(x) + \lim_{x \to a} g(x)$$
$$\lim_{x \to a} [f(x) \cdot g(x)] = \lim_{x \to a} f(x) \cdot \lim_{x \to a} g(x)$$
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \frac{\lim_{x \to a} f(x)}{\lim_{x \to a} g(x)}, \quad \text{if } \lim_{x \to a} g(x) \neq 0$$

### Indeterminate Forms
$$\frac{0}{0}, \frac{\infty}{\infty}, 0 \cdot \infty, \infty - \infty, 0^0, 1^\infty, \infty^0$$

### L'Hôpital's Rule
$$\lim_{x \to a} \frac{f(x)}{g(x)} = \lim_{x \to a} \frac{f'(x)}{g'(x)}$$
when limit is indeterminate form $\frac{0}{0}$ or $\frac{\infty}{\infty}$

### Squeeze Theorem
If $g(x) \leq f(x) \leq h(x)$ near $a$ and $\lim_{x \to a} g(x) = \lim_{x \to a} h(x) = L$, then $\lim_{x \to a} f(x) = L$

## SOLUTION PATTERN

1. **Direct substitution**: Try plugging in value
2. **Check for indeterminate form**: If undefined, identify which form
3. **Simplify**: 
   - Factor and cancel
   - Rationalize if square roots
   - Combine fractions
4. **Use algebraic manipulation** or **L'Hôpital's rule**
5. **Verify** by checking limit from both sides

## EXAMPLES

### Example 1: Direct Substitution
**Problem**: Find $\lim_{x \to 2} (x^2 + 3x)$

**Solution**:
- Direct substitution: $(2)^2 + 3(2) = 4 + 6 = 10$
- **Answer**: 10

### Example 2: Factoring and Canceling
**Problem**: Find $\lim_{x \to 2} \frac{x^2 - 4}{x - 2}$

**Solution**:
- Direct substitution gives $\frac{0}{0}$ (indeterminate)
- Factor: $\frac{(x-2)(x+2)}{x-2}$
- Cancel: $\lim_{x \to 2} (x + 2) = 4$

### Example 3: L'Hôpital's Rule
**Problem**: Find $\lim_{x \to 0} \frac{\sin x}{x}$

**Solution**:
- Direct substitution: $\frac{0}{0}$ (indeterminate)
- Apply L'Hôpital: $\lim_{x \to 0} \frac{\cos x}{1} = 1$

## CONTINUITY

A function is continuous at $x = a$ if:
1. $f(a)$ is defined
2. $\lim_{x \to a} f(x)$ exists
3. $\lim_{x \to a} f(x) = f(a)$

## WATCH OUT

❌ **Wrong**: Using L'Hôpital's rule for non-indeterminate forms
✅ **Correct**: Only use for $\frac{0}{0}$ or $\frac{\infty}{\infty}$

❌ **Wrong**: Assuming limit doesn't exist when substitution fails
✅ **Correct**: Try algebraic manipulation first

❌ **Wrong**: Forgetting to check one-sided limits
✅ **Correct**: Limit exists only if left and right limits are equal