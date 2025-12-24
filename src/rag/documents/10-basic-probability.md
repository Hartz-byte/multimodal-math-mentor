# Basic Probability (Probability)

## Overview
Probability measures the likelihood of events occurring. Understanding sample spaces, events, and basic probability rules is fundamental for solving complex probability problems in JEE.

## KEY FORMULAS

### Probability Definition
$$P(A) = \frac{\text{Number of favorable outcomes}}{\text{Total number of outcomes}} = \frac{|A|}{|S|}$$

### Probability Range
$$0 \leq P(A) \leq 1$$

### Complementary Probability
$$P(A^c) = 1 - P(A)$$

### Addition Rule
$$P(A \cup B) = P(A) + P(B) - P(A \cap B)$$

### Multiplication Rule (Independent Events)
$$P(A \cap B) = P(A) \cdot P(B)$$

### Conditional Probability
$$P(A|B) = \frac{P(A \cap B)}{P(B)}$$

## SOLUTION PATTERN

1. **Define sample space**: List all possible outcomes
2. **Identify favorable outcomes**: Count outcomes for event
3. **Count total outcomes**: Determine cardinality of sample space
4. **Apply appropriate rule**: Use addition/multiplication as needed
5. **Simplify and verify**: Check if result is between 0 and 1

## EXAMPLES

### Example 1: Simple Probability
**Problem**: What's probability of rolling a 4 on a fair die?

**Solution**:
- Favorable outcomes: {4} → Count = 1
- Total outcomes: {1, 2, 3, 4, 5, 6} → Count = 6
- $P(\text{rolling 4}) = \frac{1}{6}$

### Example 2: Compound Event
**Problem**: Probability of drawing a red card or a face card from standard deck

**Solution**:
- Red cards: 26
- Face cards: 12
- Red face cards: 6
- $P(\text{red or face}) = \frac{26 + 12 - 6}{52} = \frac{32}{52} = \frac{8}{13}$

### Example 3: Independent Events
**Problem**: Probability of rolling two dice and both showing even numbers

**Solution**:
- P(first even) = 3/6 = 1/2
- P(second even) = 3/6 = 1/2
- P(both even) = 1/2 × 1/2 = 1/4

## CONSTRAINTS
- Sample space must be well-defined
- All outcomes must be mutually exclusive or properly accounted
- Probabilities must sum to 1

## WATCH OUT

❌ **Wrong**: Counting same outcome multiple times
✅ **Correct**: Each outcome counted once only

❌ **Wrong**: Using addition rule when events overlap
✅ **Correct**: Subtract intersection: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

❌ **Wrong**: Assuming all outcomes equally likely without verification
✅ **Correct**: Verify uniform distribution before assuming

❌ **Wrong**: Confusing "and" with addition
✅ **Correct**: "And" = multiplication (if independent), "Or" = addition