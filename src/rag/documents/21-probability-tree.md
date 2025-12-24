# Probability Tree Diagram Template (Solution Template)

## Purpose
This template provides a structured approach to solving multi-stage probability problems using visual tree diagrams and systematic calculation.

## When to Use
- Sequential/conditional events
- Multiple stages with branching outcomes
- Bayes' theorem applications
- Scenarios involving "and" and "or" logic

## Template Structure

### Step 1: Define the Problem

```
Problem Type: 
├─ Sequential events (coin flips, draws without replacement)
├─ Conditional events (given information constraints)
├─ Bayes' theorem (finding prior from posterior)
└─ Counting paths in tree

Sample Space Structure:
├─ Stage 1: Possible outcomes = {A₁, A₂, ...}
├─ Stage 2: Possible outcomes = {B₁, B₂, ...}
└─ Stage 3: Possible outcomes = {C₁, C₂, ...}
```

### Step 2: Build the Tree

```
                Start
                  │
        ┌─────────┼─────────┐
       /A₁ (p₁)  /A₂ (p₂)  ...
      /          /
    /           /
   B₁(p₁₁)   B₁(p₂₁)
   /            /
  /            /
outcome₁    outcome₂
Path prob:    Path prob:
P = p₁×p₁₁   P = p₂×p₂₁
```

### Step 3: Calculate Path Probabilities

```
For each complete path from root to leaf:
Probability = P(Event₁) × P(Event₂|Event₁) × P(Event₃|Event₁,Event₂)

Rule of Multiplication (Sequential):
P(A and B and C) = P(A) × P(B|A) × P(C|A,B)
```

### Step 4: Combine Paths for Final Answer

```
For mutually exclusive outcomes:
P(outcome) = Sum of all paths leading to that outcome

Using Addition Rule:
P(A or B) = P(path to A) + P(path to B) - P(A and B)
```

### Step 5: Verify

```
✓ All path probabilities sum to 1
✓ Answer between 0 and 1
✓ Check reasonableness
```

## Example Worked Solution

**Problem**: Draw 2 cards from standard deck without replacement. Find P(both red).

**Step 1**: 
- Stage 1: First draw - Red or Black
- Stage 2: Second draw - Red or Black (reduced deck)
- Question: Both cards are red

**Step 2**: Build tree
```
                Start
                  │
        ┌─────────┼─────────┐
     Red(26/52)   Black(26/52)
      /              \
     /                \
 Red(25/51)        Red(26/51)
    /                  \
Both Red            One Red
  (target)          (not target)
```

**Step 3**: Calculate path probability for "Both Red"
- P(Red on 1st) = 26/52 = 1/2
- P(Red on 2nd | Red on 1st) = 25/51
- P(Both Red) = (1/2) × (25/51) = 25/102

**Step 4**: This is the only path to "both red", so answer is 25/102

**Step 5**: Verify
- 25/102 ≈ 0.245 ✓ (between 0 and 1)
- Reasonable: roughly 1/4 ✓

## Common Applications

### Bayes' Theorem via Tree
```
Prior Probabilities (P(Hypothesis)):
├─ P(Machine A) = 0.5, P(Machine B) = 0.3, P(Machine C) = 0.2

Likelihoods (P(Evidence|Hypothesis)):
├─ P(Defect|A) = 0.02
├─ P(Defect|B) = 0.03
└─ P(Defect|C) = 0.01

Path Probabilities:
├─ P(Defect ∩ A) = 0.5 × 0.02 = 0.01
├─ P(Defect ∩ B) = 0.3 × 0.03 = 0.009
└─ P(Defect ∩ C) = 0.2 × 0.01 = 0.002

Total: P(Defect) = 0.01 + 0.009 + 0.002 = 0.021

Posterior (P(Hypothesis|Evidence)):
P(A|Defect) = 0.01/0.021 = 10/21
```

## Key Points

1. **Sequential multiplication**: P(A and B) = P(A) × P(B|A)
2. **Path summation**: Add probabilities of disjoint paths
3. **Conditional probabilities**: Change sample space in branches
4. **Without replacement**: Denominator and numerators change each stage
5. **Independence**: If independent, P(B|A) = P(B)

## Common Mistakes to Avoid

- ❌ Multiplying independent event probabilities when should add
- ❌ Forgetting to update sample space in "without replacement" scenarios
- ❌ Not identifying all paths to target outcome
- ❌ Confusing P(A|B) with P(B|A)