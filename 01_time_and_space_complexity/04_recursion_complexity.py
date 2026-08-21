# 7. Recursion Complexity
'''
Recursion Complexity
====================

Recursion means a function calls itself.

When analyzing recursive code, we mainly consider:

1. Time Complexity
   → How many recursive calls are made?

2. Space Complexity
   → How deep does the recursion call stack become?


---------------------------------------------------------
1. SIMPLE LINEAR RECURSION → O(n)
---------------------------------------------------------

def countdown(n):
    if n == 0:
        return

    countdown(n - 1)

Calls:

countdown(n)
    ↓
countdown(n - 1)
    ↓
countdown(n - 2)
    ↓
...
    ↓
countdown(0)

There are approximately n calls.

Time  → O(n)
Space → O(n)

Why Space O(n)?

Because all recursive calls remain on the call stack
until the base case is reached.


---------------------------------------------------------
2. RECURSION WITH CONSTANT WORK → O(n)
---------------------------------------------------------

def print_numbers(n):
    if n == 0:
        return

    print(n)
    print_numbers(n - 1)

Each call performs O(1) work.

There are n calls.

Time:

n × O(1)
= O(n)

Space:

n recursive calls
= O(n)


---------------------------------------------------------
3. RECURSION THAT DIVIDES INPUT → O(log n)
---------------------------------------------------------

def solve(n):
    if n <= 1:
        return

    solve(n // 2)

The input becomes:

n
n/2
n/4
n/8
n/16
...

After k calls:

n / 2^k = 1

Therefore:

k = log₂(n)

Time  → O(log n)
Space → O(log n)


---------------------------------------------------------
4. RECURSION THAT DIVIDES BY 2
---------------------------------------------------------

def halve(n):
    if n <= 1:
        return

    halve(n // 2)

Each recursive call cuts the problem in half.

Time  → O(log n)
Space → O(log n)


---------------------------------------------------------
5. TWO RECURSIVE CALLS → IMPORTANT
---------------------------------------------------------

def example(n):
    if n <= 1:
        return

    example(n - 1)
    example(n - 1)

Each call creates TWO more calls.

The recursion tree grows exponentially.

Time → O(2^n)

The recursion depth is still n.

Space → O(n)


---------------------------------------------------------
6. FIBONACCI — CLASSIC EXAMPLE
---------------------------------------------------------

def fibonacci(n):
    if n <= 1:
        return n

    return fibonacci(n - 1) + fibonacci(n - 2)

The recursion tree branches repeatedly.

Time → O(2^n)

More precisely, the tight bound is O(φ^n),
but O(2^n) is commonly used in interview discussions.

Maximum recursion depth:

n

Space → O(n)


---------------------------------------------------------
7. FACTORIAL
---------------------------------------------------------

def factorial(n):
    if n <= 1:
        return 1

    return n * factorial(n - 1)

There are n recursive calls.

Time  → O(n)
Space → O(n)


---------------------------------------------------------
8. RECURSION WITH TWO DIFFERENT CALLS
---------------------------------------------------------

def example(n):
    if n <= 1:
        return

    example(n - 1)
    example(n - 2)

This produces an exponential recursion tree.

Time → O(2^n)

Maximum depth is n.

Space → O(n)


---------------------------------------------------------
9. TAIL RECURSION
---------------------------------------------------------

def countdown(n):
    if n == 0:
        return

    countdown(n - 1)

Even though the recursive call is the last operation,
Python still creates stack frames.

Time  → O(n)
Space → O(n)

IMPORTANT:

Python does NOT perform tail-call optimization.


---------------------------------------------------------
10. RECURSION + LOOP
---------------------------------------------------------

def example(n):
    if n == 0:
        return

    for i in range(n):
        print(i)

    example(n - 1)

Work done:

n + (n - 1) + (n - 2) + ... + 1

This is:

n(n + 1) / 2

Therefore:

Time → O(n²)

Maximum recursion depth:

n

Space → O(n)


---------------------------------------------------------
11. RECURSION + LOGARITHMIC WORK
---------------------------------------------------------

def example(n):
    if n <= 1:
        return

    i = 1

    while i < n:
        i *= 2

    example(n // 2)

Each recursive level performs O(log n) work.

Number of levels → O(log n)

Total:

O(log n) × O(log n)

Time → O((log n)²)

Space → O(log n)


---------------------------------------------------------
12. RECURSION TREE IDEA
---------------------------------------------------------

For recursive problems, visualize:

                 f(n)
                /    \
             f(n-1) f(n-1)
             /  \     /  \
            ... ...   ... ...

The number of nodes in the recursion tree
helps determine time complexity.

The maximum depth of the tree
helps determine space complexity.


---------------------------------------------------------
13. ONE RECURSIVE CALL
---------------------------------------------------------

f(n)
 ↓
f(n-1)
 ↓
f(n-2)
 ↓
...
 ↓
f(1)

One branch.

Usually:

Time  → O(n)
Space → O(n)


---------------------------------------------------------
14. TWO RECURSIVE CALLS
---------------------------------------------------------

                 f(n)
                /    \
             f(n-1)  f(n-2)
              / \      / \
            ... ...   ... ...

Multiple branches.

Often leads to:

Time → O(2^n)

Space depends mainly on maximum depth.


---------------------------------------------------------
15. IMPORTANT:
TIME ≠ SPACE
---------------------------------------------------------

Example:

def example(n):
    if n == 0:
        return

    example(n - 1)
    example(n - 1)

Time → O(2^n)

Space → O(n)

Why?

There can be exponentially many calls overall,
but only O(n) calls exist along the deepest active path.


---------------------------------------------------------
16. RECURSION CALL STACK
---------------------------------------------------------

Example:

def f(n):
    if n == 0:
        return

    f(n - 1)

When calling:

f(4)

Stack becomes approximately:

f(4)
f(3)
f(2)
f(1)
f(0)

Maximum depth = 5

For asymptotic analysis:

Space → O(n)


---------------------------------------------------------
17. BASE CASE IS IMPORTANT
---------------------------------------------------------

Every recursive function should have
a condition that eventually stops recursion.

Example:

def f(n):
    if n == 0:
        return

    f(n - 1)

Without:

if n == 0:
    return

the recursion can continue indefinitely
until Python raises RecursionError.


---------------------------------------------------------
18. PYTHON RECURSION LIMIT
---------------------------------------------------------

Python has a recursion depth limit.

You can inspect it using:

import sys

print(sys.getrecursionlimit())

This is one reason recursion should be used carefully
in Python for very deep problems.


---------------------------------------------------------
19. COMMON RECURSION PATTERNS
---------------------------------------------------------

Pattern 1:

f(n - 1)

→ O(n)


Pattern 2:

f(n // 2)

→ O(log n)


Pattern 3:

f(n - 1)
f(n - 1)

→ O(2^n)


Pattern 4:

f(n - 1)
+ O(n) work

→ O(n²)


Pattern 5:

f(n // 2)
+ O(1) work

→ O(log n)


---------------------------------------------------------
20. QUICK REFERENCE
---------------------------------------------------------

Recursive Pattern                         Time

f(n - 1)                                  O(n)

f(n - 2)                                  O(n)

f(n // 2)                                 O(log n)

f(n - 1) + f(n - 1)                       O(2^n)

f(n - 1) + f(n - 2)                       O(2^n)

Loop O(n) + f(n - 1)                      O(n²)

Loop O(log n) + f(n // 2)                 O(log² n)


SPACE

One recursive chain of depth n             O(n)

One recursive chain of depth log n         O(log n)

Two recursive branches with depth n        O(n)


---------------------------------------------------------
21. INTERVIEW METHOD
---------------------------------------------------------

When you see recursion:

Step 1:
Find the base case.

Step 2:
Count how many recursive calls each function makes.

Step 3:
Determine how the input changes.

Step 4:
Determine the recursion depth.

Step 5:
Calculate total work.

Step 6:
Calculate maximum call-stack depth.

Step 7:
Give Time and Space separately.


FINAL RULE:

Number of recursive calls
→ helps determine TIME.

Maximum recursion depth
→ helps determine SPACE.





The patterns you must recognize:

f(n - 1)          → O(n)

f(n // 2)         → O(log n)

f(n - 1)
f(n - 1)          → O(2^n)

f(n - 1) + O(n)   → O(n²)

f(n // 2)         → O(log n)
'''