# Quadratic Equation Solver Template (Solution Template)

## Purpose
This template provides a systematic approach to solving any quadratic equation, applicable to numerous JEE problems.

## Template Steps

### Step 1: Identify and Extract
```
Given equation: ax² + bx + c = 0
Extract: a = ___, b = ___, c = ___
Verify: a ≠ 0 (otherwise not quadratic)
```

### Step 2: Choose Solution Method
```
Method Selection Decision Tree:
├─ Can it be factored easily? (integer roots)
│  └─ Yes: Use factorization
├─ Are there perfect square terms?
│  └─ Yes: Try completing the square
└─ Otherwise: Use quadratic formula
```

### Step 3: Check Discriminant
```
Calculate: Δ = b² - 4ac
Interpretation:
├─ Δ > 0: Two distinct real roots
├─ Δ = 0: One repeated real root
└─ Δ < 0: Two complex conjugate roots
```

### Step 4: Solve Using Selected Method

**Method A: Factorization**
```
1. Rewrite: ax² + bx + c = a(x - r₁)(x - r₂)
2. Set each factor = 0
3. Solve: x = r₁ or x = r₂
4. Verify by substitution
```

**Method B: Quadratic Formula**
```
1. Apply: x = [-b ± √(b² - 4ac)] / (2a)
2. Simplify radical if possible
3. Compute both roots (with ± sign)
4. Rationalize if needed
```

**Method C: Completing the Square**
```
1. Rearrange: ax² + bx = -c
2. Divide by a: x² + (b/a)x = -c/a
3. Add [b/(2a)]² to both sides
4. Factor left side as perfect square
5. Take square root and solve
```

### Step 5: Verify and Interpret

```
For each root x:
├─ Substitute back: a(x)² + b(x) + c = 0 ✓
├─ Check domain restrictions
├─ Check problem context (physical feasibility)
└─ State final answer clearly
```

## Example Worked Solution

**Problem**: Solve 2x² - 7x + 3 = 0

**Step 1**: a = 2, b = -7, c = 3; a ≠ 0 ✓

**Step 2**: Not obvious factorization, use quadratic formula

**Step 3**: Δ = (-7)² - 4(2)(3) = 49 - 24 = 25 > 0
→ Two distinct real roots

**Step 4**: x = [7 ± √25] / (2·2) = [7 ± 5] / 4
- x₁ = 12/4 = 3
- x₂ = 2/4 = 1/2

**Step 5**: 
- Check x=3: 2(9) - 7(3) + 3 = 18 - 21 + 3 = 0 ✓
- Check x=1/2: 2(1/4) - 7(1/2) + 3 = 1/2 - 7/2 + 3 = 0 ✓

**Answer**: x = 3 or x = 1/2

## Key Points to Remember

1. **Always verify** that a ≠ 0
2. **Check discriminant** before calculating roots
3. **Use most efficient method** for given equation
4. **Verify answers** by substitution
5. **Consider context** for applied problems
6. **Keep answers exact** unless approximation requested
7. **Don't forget ±** in quadratic formula

## Common Pitfalls to Avoid

- ❌ Sign errors in formula (forgot the negative sign in front of b)
- ❌ Dividing by a instead of 2a
- ❌ Arithmetic errors in discriminant
- ❌ Not simplifying radical completely
- ❌ Losing a root by incomplete factorization