"""
Lesson 18: Fibonacci Sequence
Unit 14: Software Development - FE Foundation Course

Your task is to complete the missing functions below.
Read the instructions carefully and fill in the TODO sections.

The Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
Each number is the sum of the two preceding ones.
"""


def fibonacci_iterative(n):
    """
    Calculate the nth Fibonacci number using an iterative approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (starting from 0)
    
    Returns:
        int: The nth Fibonacci number
    
    Examples:
        fibonacci_iterative(0) -> 0
        fibonacci_iterative(1) -> 1
        fibonacci_iterative(5) -> 5
        fibonacci_iterative(10) -> 55
    """
    # TODO: Handle edge cases
    # Hint: What should happen when n is 0 or 1?
    # Hint: What should happen if n is negative?
    
    if n < 0:
        return None  # Invalid input
    # TODO: Add conditions for n == 0 and n == 1
    
    
    # TODO: Implement the iterative solution
    # Hint: You'll need to keep track of the previous two numbers
    # Hint: Use a loop to calculate each number in sequence
    
    # Initialize the first two Fibonacci numbers
    prev1 = 1  # F(1)
    prev2 = 0  # F(0)
    
    # Calculate from F(2) to F(n)
    for i in range(2, n + 1):
        current = 0  # TODO: Calculate the current Fibonacci number (sum of prev1 and prev2)
        prev2 = 0    # TODO: Update prev2 to be the old prev1
        prev1 = 0    # TODO: Update prev1 to be current
    
    return prev1


def fibonacci_recursive(n):
    """
    Calculate the nth Fibonacci number using a recursive approach.
    
    Args:
        n (int): The position in the Fibonacci sequence (starting from 0)
    
    Returns:
        int: The nth Fibonacci number
    
    Examples:
        fibonacci_recursive(0) -> 0
        fibonacci_recursive(1) -> 1
        fibonacci_recursive(5) -> 5
        fibonacci_recursive(10) -> 55
    """
    # TODO: Implement the recursive solution
    # Hint: What are the base cases? (n = 0 and n = 1)
    # Hint: For other cases, use the formula: F(n) = F(n-1) + F(n-2)
    
    if n < 0:
        return None  # Invalid input
    
    # Base cases
    # TODO: Add condition for n == 0 (should return 0)
    
    # TODO: Add condition for n == 1 (should return 1)
    
    
    # Recursive case
    # TODO: Implement the recursive formula: F(n) = F(n-1) + F(n-2)
    return 0


def fibonacci_sequence(n):
    """
    Generate a list of the first n Fibonacci numbers.
    
    Args:
        n (int): Number of Fibonacci numbers to generate
    
    Returns:
        list: A list containing the first n Fibonacci numbers
    
    Examples:
        fibonacci_sequence(5) -> [0, 1, 1, 2, 3]
        fibonacci_sequence(8) -> [0, 1, 1, 2, 3, 5, 8, 13]
    """
    # TODO: Generate a list of the first n Fibonacci numbers
    # Hint: You can use either the iterative or recursive function you implemented
    # Hint: Use a loop to generate each number and append it to a list
    
    if n <= 0:
        return []
    
    sequence = []
    # TODO: Use a loop to generate each Fibonacci number
    # TODO: Append each number to the sequence list
    # Hint: Use range(n) to loop from 0 to n-1
    
    
    return sequence


def run_tests():
    """
    Test all the Fibonacci functions.
    This will help you verify that your implementation is correct.
    """
    print("=" * 50)
    print("Testing Fibonacci Functions")
    print("=" * 50)
    
    # Test fibonacci_iterative
    print("\n📊 Testing fibonacci_iterative:")
    test_cases_single = [
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (5, 5),
        (10, 55),
        (15, 610)
    ]
    
    all_passed = True
    for n, expected in test_cases_single:
        result = fibonacci_iterative(n)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"  F({n}) = {result} (expected {expected}) {status}")
    
    # Test fibonacci_recursive
    print("\n🔄 Testing fibonacci_recursive:")
    for n, expected in test_cases_single[:6]:  # Test smaller values for recursion
        result = fibonacci_recursive(n)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"  F({n}) = {result} (expected {expected}) {status}")
    
    # Test fibonacci_sequence
    print("\n📝 Testing fibonacci_sequence:")
    sequence_tests = [
        (5, [0, 1, 1, 2, 3]),
        (8, [0, 1, 1, 2, 3, 5, 8, 13]),
        (10, [0, 1, 1, 2, 3, 5, 8, 13, 21, 34])
    ]
    
    for n, expected in sequence_tests:
        result = fibonacci_sequence(n)
        status = "✅ PASS" if result == expected else "❌ FAIL"
        if result != expected:
            all_passed = False
        print(f"  First {n} numbers: {result}")
        print(f"  Expected:         {expected} {status}")
    
    # Print final result
    print("\n" + "=" * 50)
    if all_passed:
        print("🎉 Congratulations! All tests passed!")
        print("You've successfully implemented the Fibonacci functions!")
    else:
        print("⚠️  Some tests failed. Review your code and try again.")
        print("Tip: Check the TODO sections and make sure you've")
        print("     completed all the required implementations.")
    print("=" * 50)


if __name__ == "__main__":
    # Run the test suite
    run_tests()
    
    # Optional: Demonstrate the sequence
    print("\n🌟 Fibonacci Sequence Demonstration:")
    print("First 15 Fibonacci numbers:")
    demo_sequence = fibonacci_sequence(15)
    print(demo_sequence)
