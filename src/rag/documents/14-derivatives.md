# Derivatives and Differentiation Rules (Calculus)

## Overview
Derivatives measure the rate of change of functions. Understanding derivative rules and applications is essential for optimization, curve sketching, and many physics problems.

## KEY FORMULAS

### Definition of Derivative
$$f'(x) = \lim_{h \to 0} \frac{f(x+h) - f(x)}{h}$$

### Power Rule
$$\frac{d}{dx}[x^n] = nx^{n-1}$$

### Product Rule
$$\frac{d}{dx}[f(x)g(x)] = f'(x)g(x) + f(x)g'(x)$$

### Quotient Rule
$$\frac{d}{dx}\left[\frac{f(x)}{g(x)}\right] = \frac{f'(x)g(x) - f(x)g'(x)}{[g(x)]^2}$$

### Chain Rule
$$\frac{d}{dx}[f(g(x))] = f'(g(x)) \cdot g'(x)$$

### Common Derivatives
$$\frac{d}{dx}[\sin x] = \cos x, \quad \frac{d}{dx}[\cos x] = -\sin x$$
$$\frac{d}{dx}[e^x] = e^x, \quad \frac{d}{dx}[\ln x] = \frac{1}{x}$$

## SOLUTION PATTERN

1. **Identify function type**: Power, product, quotient, composite, or combination
2. **Select appropriate rule**: Power, product, quotient, or chain
3. **Apply rule carefully**: Maintain signs and order
4. **Simplify result**: Factor and combine terms
5. **Verify**: Check reasonableness of answer

## EXAMPLES

### Example 1: Power Rule
**Problem**: Find derivative of $f(x) = x^5$

**Solution**:
- $f'(x) = 5x^4$

### Example 2: Product Rule
**Problem**: Find derivative of $f(x) = x^2 \sin x$

**Solution**:
- $f'(x) = (2x)(\sin x) + (x^2)(\cos x)$
- $= 2x \sin x + x^2 \cos x$

### Example 3: Chain Rule
**Problem**: Find derivative of $f(x) = (2x^3 - 5)^7$

**Solution**:
- Let $u = 2x^3 - 5$, then $f = u^7$
- $f'(x) = 7u^6 \cdot u'(x)$
- $= 7(2x^3 - 5)^6 \cdot 6x^2$
- $= 42x^2(2x^3 - 5)^6$

## APPLICATIONS

### Critical Points
- Find where $f'(x) = 0$ or undefined
- Evaluate $f$ at critical points and endpoints
- Compare to find max/min

### Curve Sketching
- Find $f'(x)$ for increasing/decreasing intervals
- Find $f''(x)$ for concavity
- Find inflection points where $f''(x) = 0$

## WATCH OUT

❌ **Wrong**: Applying chain rule incorrectly
✅ **Correct**: Derivative of outside × derivative of inside

❌ **Wrong**: Forgetting constant multiplier in product rule
✅ **Correct**: $[cf(x)]' = c \cdot f'(x)$

❌ **Wrong**: Incorrect application of quotient rule
✅ **Correct**: Numerator: $f'g - fg'$ (not $fg' - f'g$)