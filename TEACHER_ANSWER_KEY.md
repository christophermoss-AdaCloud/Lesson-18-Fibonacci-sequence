# Teacher Answer Key - Fibonacci Worksheet

## Task 1: Code Review and Predict (5 minutes)

### Question 1
**What is the purpose of the variable `nterms` in the code?**

**Answer:** `nterms` sets how many Fibonacci numbers the program will generate/print. It acts as the goal or target for the loop to reach.

### Question 2
**If `n1 = 5` and `n2 = 8`, what will the value of `nth` be in the next loop iteration?**

**Answer:** `13` (because nth = n1 + n2 = 5 + 8 = 13)

### Question 3
**Why is the line `count += 1` essential for the program to work correctly? (What happens if you remove it?)**

**Answer:** `count += 1` increments the counter each time through the loop, moving us closer to the goal (nterms). Without it, the condition `count < nterms` would always be true, creating an infinite loop that never stops.

---

## Task 2: Code Modification – The Fun Challenge (20 minutes)

### A. Print the sequence (Run 1)
**What is the last number printed when `nterms` is set to `10`?**

**Answer:** `34`

**Full sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

### B. Challenge 1: Find the 20th Term (Modify and Run 2)
**What is the final number printed in the 20-term sequence?**

**Answer:** `4181`

**Full sequence:** 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

### C. Challenge 2: Start with different numbers (Modify and Run 3)
**What are the first five numbers in your new sequence?**

**Answer:** `5, 10, 15, 25, 40`

**Explanation:** Starting with 5 and 10, each subsequent number is the sum of the previous two:
- 15 = 5 + 10
- 25 = 10 + 15
- 40 = 15 + 25

---

## Task 3: Commenting and Explanation (15 minutes)

| Line | Code | Suggested Comment |
|------|------|-------------------|
| ~12 | `n1 = 0` | `# Sets the first number of the sequence.` *(provided)* |
| ~22 | `while count < nterms:` | `# Loop continues as long as we haven't printed nterms numbers yet` |
| ~24 | `print(n1, end=' , ')` | `# Print the current number with a comma separator (not a new line)` |
| ~25 | `nth = n1 + n2` | `# Calculate the next Fibonacci number by adding the previous two` |
| ~27 | `n1 = n2` | `# Shift: move n2 to n1 (the "second" becomes the "first")` |
| ~29 | `count += 1` | `# Increment the counter to track how many numbers we've printed` |

**Note:** Student comments may vary in wording but should capture the same concepts.

---

## Task 4: Final Submission Check (5 minutes)

**Checklist:**
- [ ] File saved as `StudentName_Fibonacci_Challenge.py`
- [ ] All comments added to the code
- [ ] All worksheet questions answered
- [ ] File uploaded to Google Classroom

---

## Bonus Challenge (Extension)

**Make the program stop printing once numbers get larger than 1000.**

**Solution 1 - Using break:**
```python
while count < nterms:
    print(n1, end=' , ')
    if n1 > 1000:  # Check if number exceeds 1000
        break      # Exit the loop
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
```

**Solution 2 - Modifying the condition:**
```python
while count < nterms and n1 <= 1000:  # Add second condition
    print(n1, end=' , ')
    nth = n1 + n2
    n1 = n2
    n2 = nth
    count += 1
```

---

## Assessment Guidelines

### Task 1 (5 points)
- 2 points per correct answer for Q1 and Q3
- 1 point for Q2

### Task 2 (9 points)
- 3 points per challenge (A, B, C)
- Award full points if answer is correct
- Award 1-2 points if working is shown but answer is incorrect

### Task 3 (6 points)
- 1 point per comment
- Comments should demonstrate understanding, not just repeat the code

### Task 4 (5 points)
- 2 points for correct filename format
- 3 points for submission to Google Classroom on time

### Bonus Challenge (5 extra points)
- Award if student demonstrates any working solution

**Total: 25 points (30 with bonus)**

---

## Common Student Mistakes to Watch For

1. **Infinite Loop:** Forgetting `count += 1` or placing it outside the loop
2. **Off-by-One Errors:** Starting count at 1 instead of 0
3. **Variable Confusion:** Mixing up n1, n2, and nth
4. **Print Formatting:** Not understanding the `end=' , '` parameter
5. **Order of Operations:** Updating n1 and n2 in the wrong order

---

## Extension Activities

For students who finish early:
1. Calculate the ratio between consecutive Fibonacci numbers (approaches the Golden Ratio: ~1.618)
2. Create a function to find the position of a given Fibonacci number
3. Implement a recursive version of the Fibonacci calculator
4. Research and present real-world applications of Fibonacci numbers

---

## Timing Guide

- **Slides Presentation:** 15-20 minutes
- **Task 1 (Code Review):** 5 minutes
- **Task 2 (Modification):** 20 minutes
- **Task 3 (Commenting):** 15 minutes
- **Task 4 (Submission):** 5 minutes
- **Total:** 60-65 minutes (including setup and transitions)
