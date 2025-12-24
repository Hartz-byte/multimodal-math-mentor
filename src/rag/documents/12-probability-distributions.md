# Probability Distributions (Probability)

## Overview
Probability distributions describe the behavior of random variables. Understanding discrete and continuous distributions is essential for advanced probability and statistics problems.

## KEY FORMULAS

### Binomial Distribution
$$P(X = k) = \binom{n}{k} p^k (1-p)^{n-k}$$
$$E(X) = np, \quad \text{Var}(X) = np(1-p)$$

### Poisson Distribution
$$P(X = k) = \frac{e^{-\lambda} \lambda^k}{k!}$$
$$E(X) = \lambda, \quad \text{Var}(X) = \lambda$$

### Normal (Gaussian) Distribution
$$f(x) = \frac{1}{\sigma\sqrt{2\pi}} e^{-\frac{(x-\mu)^2}{2\sigma^2}}$$
$$E(X) = \mu, \quad \text{Var}(X) = \sigma^2$$

### Standard Normal Distribution
$$Z = \frac{X - \mu}{\sigma}$$
where $Z$ follows $N(0,1)$

## SOLUTION PATTERN

1. **Identify the distribution type**
2. **Determine parameters** (n, p for binomial; λ for Poisson; μ, σ for normal)
3. **Identify what to find** (P(X=k), P(X<k), expectation, etc.)
4. **Apply appropriate formula**
5. **Use tables or calculators** if needed for normal distribution

## EXAMPLES

### Example 1: Binomial Distribution
**Problem**: If 4 coins are flipped, what's probability of exactly 3 heads?

**Solution**:
- $n = 4, k = 3, p = 0.5$
- $P(X=3) = \binom{4}{3}(0.5)^3(0.5)^1$
- $= 4 \times 0.125 \times 0.5 = 0.25$

### Example 2: Poisson Distribution
**Problem**: Calls to customer service average 3 per minute. Probability of exactly 5 calls in next minute?

**Solution**:
- $\lambda = 3, k = 5$
- $P(X=5) = \frac{e^{-3} \times 3^5}{5!} = \frac{e^{-3} \times 243}{120} \approx 0.101$

### Example 3: Normal Distribution
**Problem**: Heights in population are normally distributed with μ=170cm, σ=10cm. Probability height > 180cm?

**Solution**:
- $Z = \frac{180-170}{10} = 1$
- $P(X > 180) = P(Z > 1) = 1 - \Phi(1) \approx 1 - 0.8413 = 0.1587$

## CONSTRAINTS
- Binomial: n must be positive integer, 0 ≤ p ≤ 1
- Poisson: λ > 0
- Normal: σ > 0

## WATCH OUT

❌ **Wrong**: Using binomial with large n without checking approximation validity
✅ **Correct**: Can approximate binomial with normal if $np > 5$ and $n(1-p) > 5$

❌ **Wrong**: Forgetting standardization for normal distribution
✅ **Correct**: Always convert to standard normal using $Z = \frac{X-\mu}{\sigma}$

❌ **Wrong**: Misreading normal distribution tables
✅ **Correct**: Standard tables give $P(Z \leq z)$, not $P(Z \geq z)$