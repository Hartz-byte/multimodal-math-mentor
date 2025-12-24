# Conditional Probability and Bayes' Theorem (Probability)

## Overview
Conditional probability extends basic probability concepts to situations where prior information constrains the sample space. Bayes' theorem is essential for updating probabilities based on new evidence.

## KEY FORMULAS

### Conditional Probability
$$P(A|B) = \frac{P(A \cap B)}{P(B)}, \quad P(B) \neq 0$$

### Total Probability Rule
$$P(A) = P(A|B_1)P(B_1) + P(A|B_2)P(B_2) + \cdots + P(A|B_n)P(B_n)$$
where $B_1, B_2, \ldots, B_n$ form a partition of sample space

### Bayes' Theorem
$$P(B_i|A) = \frac{P(A|B_i)P(B_i)}{P(A)} = \frac{P(A|B_i)P(B_i)}{\sum_{j=1}^{n} P(A|B_j)P(B_j)}$$

### Independence Check
Events $A$ and $B$ are independent iff: $P(A \cap B) = P(A) \cdot P(B)$

## SOLUTION PATTERN

### For Conditional Probability
1. Identify the condition (given event)
2. Identify the target event
3. Calculate $P(A \cap B)$ and $P(B)$
4. Apply formula $P(A|B) = \frac{P(A \cap B)}{P(B)}$

### For Bayes' Theorem
1. Identify prior probabilities $P(B_i)$
2. Identify likelihoods $P(A|B_i)$
3. Calculate total probability $P(A)$
4. Apply Bayes' formula to find posterior $P(B_i|A)$

## EXAMPLES

### Example 1: Conditional Probability
**Problem**: A bag contains 3 red and 2 blue balls. Draw two without replacement. What's probability second is blue given first is red?

**Solution**:
- Given: First ball is red
- Remaining: 2 red, 2 blue (4 total)
- $P(\text{second blue | first red}) = \frac{2}{4} = \frac{1}{2}$

### Example 2: Total Probability
**Problem**: Factory has three machines producing parts. Machine A produces 50% with 2% defect rate, B produces 30% with 3% defect rate, C produces 20% with 1% defect rate. What's probability a randomly selected part is defective?

**Solution**:
$$P(\text{defect}) = P(\text{def}|A)P(A) + P(\text{def}|B)P(B) + P(\text{def}|C)P(C)$$
$$= 0.02(0.5) + 0.03(0.3) + 0.01(0.2)$$
$$= 0.01 + 0.009 + 0.002 = 0.021$$

### Example 3: Bayes' Theorem
**Problem**: Using data above, if part is defective, what's probability it came from machine A?

**Solution**:
$$P(A|\text{defect}) = \frac{P(\text{defect}|A)P(A)}{P(\text{defect})}$$
$$= \frac{0.02 \times 0.5}{0.021} = \frac{0.01}{0.021} = \frac{10}{21}$$

## CONSTRAINTS
- Conditional probability undefined if $P(B) = 0$
- Total probability requires complete partition
- Bayes' theorem valid only with non-zero denominators

## WATCH OUT

❌ **Wrong**: Confusing $P(A|B)$ with $P(B|A)$
✅ **Correct**: Always clearly identify condition and target

❌ **Wrong**: Forgetting to condition sample space
✅ **Correct**: Given event reduces sample space

❌ **Wrong**: Incorrect partition in total probability
✅ **Correct**: Events must be mutually exclusive and exhaustive

❌ **Wrong**: Using multiplication without verifying independence
✅ **Correct**: Check independence before applying $P(A \cap B) = P(A)P(B)$