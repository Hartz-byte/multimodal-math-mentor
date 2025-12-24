# Common Probability Mistakes and How to Avoid Them

## Mistake 1: Confusing P(A|B) with P(B|A)

### ❌ WRONG:
"Given: P(Rain|Dark clouds) = 0.8"
"Therefore: P(Dark clouds|Rain) = 0.8"

### ✅ CORRECT:
$P(A|B)$ and $P(B|A)$ are generally different unless special symmetry
Use Bayes' theorem: $P(A|B) = \frac{P(B|A) \cdot P(A)}{P(B)}$

**Why it matters**: Reverses cause and effect
**Prevention**: Always explicitly state what is the condition

---

## Mistake 2: Assuming Independence Without Verification

### ❌ WRONG:
"Two students' exam scores are independent with P(pass) = 0.7 each"
"P(both pass) = 0.7 × 0.7 = 0.49"

### ✅ CORRECT:
First verify independence: Check if P(A∩B) = P(A)·P(B)
Or verify from context that events are actually independent

**Why it matters**: Dependent events require conditional probability
**Prevention**: Explicitly verify independence from problem statement

---

## Mistake 3: Double-Counting in Probability

### ❌ WRONG:
"Probability of red card OR face card"
"P = P(red) + P(face) = 26/52 + 12/52 = 38/52"

### ✅ CORRECT:
Some cards are BOTH red AND face cards
$$P(\text{red OR face}) = P(\text{red}) + P(\text{face}) - P(\text{red AND face})$$
$$= \frac{26}{52} + \frac{12}{52} - \frac{6}{52} = \frac{32}{52} = \frac{8}{13}$$

**Why it matters**: Counts overlap twice
**Prevention**: Use general addition rule: $P(A \cup B) = P(A) + P(B) - P(A \cap B)$

---

## Mistake 4: Incorrect Conditional Probability

### ❌ WRONG:
"Draw card without replacement. P(2nd red | 1st red)"
"Answer: 26/52 = 1/2" (Using original deck)

### ✅ CORRECT:
After first red card drawn, deck has 51 cards with 25 red
$$P(\text{2nd red | 1st red}) = \frac{25}{51}$$

**Why it matters**: Sample space shrinks
**Prevention**: Update total count and favorable outcomes for conditional

---

## Mistake 5: Applying Addition Rule When Should Multiply

### ❌ WRONG:
"Roll two dice. Both show 6"
"P = P(first 6) + P(second 6) = 1/6 + 1/6 = 1/3"

### ✅ CORRECT:
Sequential independent events use multiplication:
$$P(\text{both 6}) = P(\text{1st 6}) \times P(\text{2nd 6}) = \frac{1}{6} \times \frac{1}{6} = \frac{1}{36}$$

**Why it matters**: "And" means both must occur (multiplication)
**Prevention**: AND = multiply, OR = add (if mutually exclusive)

---

## Mistake 6: Forgetting Complementary Probability

### ❌ WRONG:
"P(at least one 6 in three dice rolls)"
"P = 1/6 + 1/6 + 1/6 = 1/2"

### ✅ CORRECT:
Using complement is simpler:
$$P(\text{at least one 6}) = 1 - P(\text{no 6s})$$
$$= 1 - \left(\frac{5}{6}\right)^3 = 1 - \frac{125}{216} = \frac{91}{216}$$

**Why it matters**: "At least one" is easier with complement
**Prevention**: Look for "at least" - use complement

---

## Mistake 7: Incorrect Binomial Probability

### ❌ WRONG:
"Flip 4 coins. Probability of exactly 2 heads"
"P = 2/4 = 1/2"

### ✅ CORRECT:
$$P(X = 2) = \binom{4}{2} p^2(1-p)^2 = 6 \times \frac{1}{2^4} = \frac{6}{16} = \frac{3}{8}$$

**Why it matters**: Must account for all ways to get 2 heads
**Prevention**: Use binomial formula: $P(X=k) = \binom{n}{k}p^k(1-p)^{n-k}$

---

## Mistake 8: Misapplying Bayes' Theorem

### ❌ WRONG:
"P(Disease|Positive test) = P(Positive test|Disease)"
Assuming they're equal

### ✅ CORRECT:
$$P(D|+) = \frac{P(+|D) \times P(D)}{P(+)}$$

Where:
- Sensitivity P(+|D) ≠ P(D|+) (precision)
- Must consider base rate P(D)

**Why it matters**: Base rate fallacy - ignores prior probability
**Prevention**: Always apply Bayes' formula correctly

---

## Mistake 9: Sample Space Not Equally Likely

### ❌ WRONG:
"Two children. One is a boy."
"P(both boys) = 1/2" (assuming BG and BB are equally likely given info)

### ✅ CORRECT:
Without other info: P(both boys | at least one boy) = ?
- Originally: BB, BG, GB, GG are equally likely (each 1/4)
- Given at least one boy: BB, BG, GB are equally likely (each 1/3)
- P(both boys | at least one boy) = 1/3

**Why it matters**: Conditioning changes sample space
**Prevention**: Explicitly list conditional sample space

---

## Mistake 10: Misunderstanding Probability Ranges

### ❌ WRONG:
"For binomial with n=5, p=0.7: P(X=7) = ?"

### ✅ CORRECT:
X ranges from 0 to 5 only. P(X=7) = 0 (impossible)

**Why it matters**: Probability undefined for impossible events
**Prevention**: Know the range of your random variable

---

## Mistake 11: Not Simplifying Conditional Probability

### ❌ WRONG:
"P(A|B) = P(A∩B) / P(B) = (0.15) / (0.5)"
Answer: 0.15/0.5 = ... wait, forgot to divide!

### ✅ CORRECT:
$$P(A|B) = \frac{0.15}{0.5} = 0.3$$

**Why it matters**: Arithmetic error
**Prevention**: Always complete division in conditional probability

---

## Quick Prevention Checklist

✓ **Define events clearly**: "What is the condition?"
✓ **Check independence**: Is it stated or derived?
✓ **Use correct formula**: AND→multiply, OR→add (minus overlap)
✓ **Update sample space**: For conditional probability
✓ **Consider complement**: For "at least one"
✓ **Verify reasonableness**: Is answer between 0 and 1?
✓ **Check for base rate**: When using Bayes' theorem
✓ **Count carefully**: Don't double-count overlapping outcomes