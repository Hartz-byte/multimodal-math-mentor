# Integrals and Integration Rules (Calculus)

## Overview
Integration is the reverse of differentiation. It's used to find areas, volumes, and accumulation quantities. Understanding integration rules and techniques is essential for advanced calculus.

## KEY FORMULAS

### Indefinite Integral Definition
$$\int f(x) \, dx = F(x) + C$$
where $F'(x) = f(x)$ and $C$ is arbitrary constant

### Power Rule for Integration
$$\int x^n \, dx = \frac{x^{n+1}}{n+1} + C, \quad n \neq -1$$

### Special Integral
$$\int \frac{1}{x} \, dx = \ln|x| + C$$

### Exponential and Logarithmic Integrals
$$\int e^x \, dx = e^x + C$$
$$\int a^x \, dx = \frac{a^x}{\ln a} + C$$

### Trigonometric Integrals
$$\int \sin x \, dx = -\cos x + C$$
$$\int \cos x \, dx = \sin x + C$$
$$\int \tan x \, dx = -\ln|\cos x| + C = \ln|\sec x| + C$$

### Integration by Parts
$$\int u \, dv = uv - \int v \, du$$

### Definite Integral
$$\int_a^b f(x) \, dx = F(b) - F(a)$$
where $F$ is antiderivative of $f$

## SOLUTION PATTERN

1. **Identify integral type**: Direct, substitution, by parts, partial fractions, trigonometric
2. **Select technique**:
   - For power functions: use power rule
   - For composite functions: use substitution
   - For products: use integration by parts
   - For rational functions: use partial fractions
3. **Apply technique carefully**
4. **Add constant $C$** for indefinite integrals
5. **Evaluate limits** for definite integrals

## EXAMPLES

### Example 1: Power Rule
**Problem**: Find $\int (x^4 + 3x^2) \, dx$

**Solution**:
- $\int x^4 \, dx = \frac{x^5}{5}$
- $\int 3x^2 \, dx = x^3$
- **Answer**: $\frac{x^5}{5} + x^3 + C$

### Example 2: Integration by Substitution
**Problem**: Find $\int 2x \cos(x^2) \, dx$

**Solution**:
- Let $u = x^2$, then $du = 2x \, dx$
- $\int \cos u \, du = \sin u + C$
- **Answer**: $\sin(x^2) + C$

### Example 3: Integration by Parts
**Problem**: Find $\int x e^x \, dx$

**Solution**:
- Let $u = x$, $dv = e^x dx$
- Then $du = dx$, $v = e^x$
- $\int x e^x \, dx = x e^x - \int e^x \, dx$
- $= x e^x - e^x + C = e^x(x - 1) + C$

### Example 4: Definite Integral
**Problem**: Find $\int_0^2 (3x^2 - 2) \, dx$

**Solution**:
- Antiderivative: $F(x) = x^3 - 2x$
- $\int_0^2 (3x^2 - 2) \, dx = [x^3 - 2x]_0^2$
- $= (8 - 4) - (0 - 0) = 4$

## APPLICATIONS

### Area Under Curve
$$A = \int_a^b |f(x)| \, dx$$

### Volume of Revolution (Disk Method)
$$V = \pi \int_a^b [f(x)]^2 \, dx$$

## WATCH OUT

❌ **Wrong**: Forgetting constant $C$ in indefinite integrals
✅ **Correct**: Always add $+ C$ except in definite integrals

❌ **Wrong**: Incorrect substitution bounds in definite integrals
✅ **Correct**: Change bounds when changing variables

❌ **Wrong**: Sign errors in integration by parts
✅ **Correct**: $uv - \int v \, du$ (not $uv + \int v \, du$)