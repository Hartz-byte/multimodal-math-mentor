# Common Algebra Mistakes and How to Avoid Them

## Mistake 1: Sign Errors in Quadratic Formula

### ❌ WRONG:
For $ax^2 + bx + c = 0$, use: $x = \frac{b \pm \sqrt{b^2 - 4ac}}{2a}$

### ✅ CORRECT:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$

**Why it matters**: Missing negative sign gives completely wrong roots
**Prevention**: Always use $-b$ in numerator, never $+b$

---

## Mistake 2: Denominator Error in Quadratic Formula

### ❌ WRONG:
$$x = \frac{-b \pm \sqrt{\Delta}}{a}$$ (dividing by $a$ only)

### ✅ CORRECT:
$$x = \frac{-b \pm \sqrt{\Delta}}{2a}$$ (dividing by $2a$)

**Why it matters**: Gives roots that are twice the actual value
**Prevention**: Remember: denominator is $2a$, not just $a$

---

## Mistake 3: Incorrect Discriminant Calculation

### ❌ WRONG:
For $3x^2 - 5x + 2 = 0$:
- Calculate: $\Delta = (-5)^2 - 4(2) = 25 - 8 = 17$
- Problem: Forgot coefficient $a = 3$

### ✅ CORRECT:
$$\Delta = b^2 - 4ac = (-5)^2 - 4(3)(2) = 25 - 24 = 1$$

**Why it matters**: Wrong discriminant means wrong nature of roots
**Prevention**: $\Delta = b^2 - 4ac$ (all three coefficients)

---

## Mistake 4: Forgetting the ± Symbol

### ❌ WRONG:
"For $x^2 - 5x + 6 = 0$, $x = \frac{5 + \sqrt{1}}{2} = 3$ is the only solution"

### ✅ CORRECT:
$$x = \frac{5 \pm 1}{2} \Rightarrow x = 3 \text{ OR } x = 2$$

**Why it matters**: Misses one root entirely
**Prevention**: Always write $\pm$ and calculate both roots

---

## Mistake 5: Sign Handling in Coefficients

### ❌ WRONG:
For $2x^2 - 3x - 5 = 0$, treating coefficients as all positive
- Using $a = 2, b = 3, c = 5$

### ✅ CORRECT:
- $a = 2, b = -3, c = -5$
- Keep the signs as they appear in equation

**Why it matters**: Sign errors propagate through calculation
**Prevention**: Extract coefficients INCLUDING their signs

---

## Mistake 6: Not Reversing Inequality When Multiplying by Negative

### ❌ WRONG:
"Solve $-2x > 8$: $x > -4$"

### ✅ CORRECT:
"Solve $-2x > 8$: $x < -4$"
(Divide both sides by -2, REVERSE the inequality)

**Why it matters**: Solution set is completely backwards
**Prevention**: Always reverse inequality when multiply/divide by negative

---

## Mistake 7: Extraneous Solutions from Algebraic Manipulation

### ❌ WRONG:
Solve $\sqrt{x} = -2$
"Square both sides: $x = 4$"

### ✅ CORRECT:
- $\sqrt{x}$ is always non-negative, never equals $-2$
- No solution exists

**Why it matters**: Introduces false solutions
**Prevention**: Always verify final answer in ORIGINAL equation

---

## Mistake 8: Incorrect Logarithm Properties

### ❌ WRONG:
$$\log(a + b) = \log(a) + \log(b)$$

### ✅ CORRECT:
$$\log(ab) = \log(a) + \log(b)$$
$$\log(a + b) \neq \log(a) + \log(b)$$

**Why it matters**: Wrong simplification of logarithmic expressions
**Prevention**: Log applies to products/quotients, NOT sums/differences

---

## Mistake 9: Division by Zero in Equations

### ❌ WRONG:
$x^2 + 5x = 0$
"Divide by $x$: $x + 5 = 0$, so $x = -5$"

### ✅ CORRECT:
$x^2 + 5x = 0$
Factor: $x(x + 5) = 0$
Solutions: $x = 0$ OR $x = -5$

**Why it matters**: Loses one solution
**Prevention**: Never divide by variable (might be zero)

---

## Mistake 10: System of Equations - Not Checking Consistency

### ❌ WRONG:
System with parallel lines:
```
2x + y = 5
4x + 2y = 9
```
"Concluding there's a unique solution"

### ✅ CORRECT:
- Multiply first by 2: $4x + 2y = 10$
- But second says: $4x + 2y = 9$
- Contradiction! No solution exists

**Why it matters**: Misidentifies number of solutions
**Prevention**: Check if coefficient matrix is singular (det = 0)

---

## Key Prevention Strategies

### 1. Always Verify
Substitute your answer back into the ORIGINAL equation

### 2. Check Domain
Consider what values are allowed before solving

### 3. Watch Signs Carefully
Most errors come from sign mistakes

### 4. Use Alternative Methods
Solve two ways if possible to verify

### 5. Understand, Don't Memorize
Know WHY formulas work, not just how to use them

### 6. Practice with Edge Cases
Try examples with negative coefficients, zero discriminant, etc.

### 7. Write All Steps
Don't skip steps - makes errors visible