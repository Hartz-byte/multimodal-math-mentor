# Derivative Rules Quick Reference (Solution Template)

## Purpose
Master all derivative rules systematically with decision tree and application guide for JEE problems.

## Derivative Rules Decision Tree

```
Given: Find d/dx[f(x)]

1. Is it a basic function?
   ├─ Power: x^n → nx^(n-1)
   ├─ Trig: sin/cos → cos/(-sin)
   ├─ Exp: e^x → e^x
   ├─ Log: ln(x) → 1/x
   └─ No: Continue

2. Is it a combination?
   ├─ Product: u·v → u'v + uv' (Product Rule)
   ├─ Quotient: u/v → (u'v - uv')/v² (Quotient Rule)
   ├─ Power of function: [f(x)]^n → n[f(x)]^(n-1)·f'(x) (Chain Rule)
   ├─ Composition: f(g(x)) → f'(g(x))·g'(x) (Chain Rule)
   └─ Sum/Difference: u ± v → u' ± v'
```

## Complete Rule Reference

### Basic Derivatives
| Function | Derivative | Condition |
|----------|-----------|-----------|
| c (constant) | 0 | - |
| x^n | nx^(n-1) | n ≠ 0 |
| sin(x) | cos(x) | - |
| cos(x) | -sin(x) | - |
| tan(x) | sec²(x) | cos(x) ≠ 0 |
| e^x | e^x | - |
| ln(x) | 1/x | x > 0 |
| a^x | a^x·ln(a) | a > 0 |

### Combination Rules

**Sum/Difference Rule**
```
d/dx[f(x) ± g(x)] = f'(x) ± g'(x)
```

**Product Rule** (Key: derivative of first × second + first × derivative of second)
```
d/dx[f(x)·g(x)] = f'(x)·g(x) + f(x)·g'(x)
Memory Aid: "First times derivative of second, plus second times derivative of first"
```

**Quotient Rule** (Mnemonic: "Low-d-high minus high-d-low, square the bottom")
```
d/dx[f(x)/g(x)] = [f'(x)·g(x) - f(x)·g'(x)] / [g(x)]²
```

**Chain Rule** (Derivative of outside × derivative of inside)
```
d/dx[f(g(x))] = f'(g(x)) · g'(x)
Alternative: If y = f(u) and u = g(x), then dy/dx = dy/du · du/dx
```

**Power Rule with Chain**
```
d/dx[[f(x)]^n] = n[f(x)]^(n-1) · f'(x)
```

## Solution Strategy

### Step 1: Identify Function Type
- Simple function → Use basic rule
- Multiple components → Identify structure (product, quotient, composition)

### Step 2: Choose Rule(s)
- Check highest-level structure first
- Apply appropriate rule

### Step 3: Apply Carefully
- Keep signs correct
- Maintain order (especially in quotient rule)
- Don't forget the chain rule multiplier

### Step 4: Simplify
- Factor out common terms
- Combine like terms
- Verify dimensions match original function

## Example Applications

### Example 1: Product Rule
**Problem**: Find d/dx[x²·sin(x)]

**Solution**:
- f(x) = x², g(x) = sin(x)
- f'(x) = 2x, g'(x) = cos(x)
- Result: (2x)·sin(x) + x²·cos(x) = 2x·sin(x) + x²·cos(x)

### Example 2: Chain Rule (Power with Composition)
**Problem**: Find d/dx[(3x² - 5)^7]

**Solution**:
- Outer function: u^7, Inner function: u = 3x² - 5
- d/dx[u^7] = 7u^6 · du/dx
- du/dx = 6x
- Result: 7(3x² - 5)^6 · 6x = 42x(3x² - 5)^6

### Example 3: Quotient Rule
**Problem**: Find d/dx[(3x² + 1)/(x² + 2)]

**Solution**:
- f(x) = 3x² + 1, g(x) = x² + 2
- f'(x) = 6x, g'(x) = 2x
- Result: [(6x)(x² + 2) - (3x² + 1)(2x)] / (x² + 2)²
- = [6x³ + 12x - 6x³ - 2x] / (x² + 2)²
- = 10x / (x² + 2)²

### Example 4: Multiple Rules (Product + Chain)
**Problem**: Find d/dx[x²·e^(3x)]

**Solution**:
- Product: u = x², v = e^(3x)
- u' = 2x
- v' = e^(3x)·3 (chain rule)
- Result: 2x·e^(3x) + x²·3e^(3x) = e^(3x)(2x + 3x²)

## Quick Tips

1. **Product vs Quotient**: Product rule is simpler when possible
2. **Simplify first**: Factor out before differentiating if it simplifies the rule choice
3. **Chain rule is universal**: Works for all composite functions
4. **Always check your work**: Substitute a test value to verify
5. **Keep track of order**: Especially important in quotient rule (numerator matters)

## Common Mistakes

- ❌ Forgetting chain rule multiplier
- ❌ Wrong order in quotient rule (high-d-low minus low-d-high)
- ❌ Not distributing properly in product rule
- ❌ Sign errors (especially with negative coefficients)
- ❌ Treating chain rule as optional for composite functions