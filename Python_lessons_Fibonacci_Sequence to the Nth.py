"""
Lesson 18: Fibonacci Sequence - While Loop Implementation
Unit 14: Software Development - FE Foundation Course

This program prints the Fibonacci sequence up to nterms numbers.

Instructions:
- Complete the worksheet tasks
- Add comments to explain the code
- Submit as YourName_Fibonacci_Challenge.py to Google Classroom
"""

# Starting values for the Fibonacci sequence
n1 = 0
n2 = 1

# How many terms to print
nterms = 100

# Check if the number of terms is valid
if nterms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    count = 0
    while count < nterms:
        print(n1, end=' , ')
        nth = n1 + n2
        # Shift the values: n1 becomes n2, and n2 becomes nth
        n1 = n2
        n2 = nth
        count += 1
