# Look at Python code → derive Time Complexity + Space Complexity.

# 11. Complexity Analysis Practice

'''
Complexity Analysis
===================

For every piece of code:

1. Identify the input size.
2. Count how many times the main operation executes.
3. Analyze loops.
4. Analyze nested loops.
5. Analyze recursive calls.
6. Check Python built-in operations.
7. Analyze extra memory.
8. Drop constants.
9. Drop lower-order terms.
10. Give final Time + Space Complexity.


---------------------------------------------------------
EXAMPLE 1 — CONSTANT
---------------------------------------------------------

def example(arr):
    x = arr[0]
    return x

Time  → O(1)
Space → O(1)


---------------------------------------------------------
EXAMPLE 2 — LINEAR
---------------------------------------------------------

def example(arr):
    for x in arr:
        print(x)

The loop runs n times.

Time  → O(n)
Space → O(1)


---------------------------------------------------------
EXAMPLE 3 — LINEAR WITH EXTRA SPACE
---------------------------------------------------------

def example(arr):
    result = []

    for x in arr:
        result.append(x)

    return result

Loop:
O(n)

Creating result:
O(n) space

Time  → O(n)
Space → O(n)


---------------------------------------------------------
EXAMPLE 4 — TWO SEQUENTIAL LOOPS
---------------------------------------------------------

def example(arr):
    for x in arr:
        print(x)

    for x in arr:
        print(x)

Time:

O(n) + O(n)
= O(2n)
= O(n)

Space → O(1)


---------------------------------------------------------
EXAMPLE 5 — NESTED LOOPS
---------------------------------------------------------

def example(arr):
    for x in arr:
        for y in arr:
            print(x, y)

n × n

Time  → O(n²)
Space → O(1)


---------------------------------------------------------
EXAMPLE 6 — DIFFERENT INPUT SIZES
---------------------------------------------------------

def example(arr1, arr2):
    for x in arr1:
        print(x)

    for y in arr2:
        print(y)

If:

len(arr1) = n
len(arr2) = m

Time:

O(n + m)

Space → O(1)


---------------------------------------------------------
EXAMPLE 7 — NESTED DIFFERENT INPUT SIZES
---------------------------------------------------------

def example(arr1, arr2):
    for x in arr1:
        for y in arr2:
            print(x, y)

Time:

O(n × m)

Space → O(1)


---------------------------------------------------------
EXAMPLE 8 — LOGARITHMIC
---------------------------------------------------------

def example(n):
    i = 1

    while i < n:
        print(i)
        i *= 2

Values:

1 → 2 → 4 → 8 → ...

Time  → O(log n)
Space → O(1)


---------------------------------------------------------
EXAMPLE 9 — O(n log n)
---------------------------------------------------------

def example(arr):
    for x in arr:

        i = 1

        while i < len(arr):
            i *= 2

Time:

O(n) × O(log n)

= O(n log n)

Space → O(1)


---------------------------------------------------------
EXAMPLE 10 — TRIANGULAR LOOP
---------------------------------------------------------

def example(n):
    for i in range(n):
        for j in range(i):
            print(i, j)

Iterations:

0 + 1 + 2 + ... + (n - 1)

= n(n - 1) / 2

Therefore:

Time  → O(n²)
Space → O(1)


---------------------------------------------------------
EXAMPLE 11 — CONSTANT INNER LOOP
---------------------------------------------------------

def example(arr):
    for x in arr:
        for i in range(10):
            print(x, i)

n × 10

= 10n

Time  → O(n)
Space → O(1)


---------------------------------------------------------
EXAMPLE 12 — LIST MEMBERSHIP
---------------------------------------------------------

def example(arr, target):
    if target in arr:
        return True

    return False

List membership:

target in arr
→ O(n)

Time  → O(n)
Space → O(1)


---------------------------------------------------------
EXAMPLE 13 — SET MEMBERSHIP
---------------------------------------------------------

def example(arr, target):
    seen = set(arr)

    if target in seen:
        return True

    return False

Creating set:
O(n)

Set lookup:
O(1) average

Total:

O(n) + O(1)
= O(n)

Space → O(n)


---------------------------------------------------------
EXAMPLE 14 — DICTIONARY FREQUENCY
---------------------------------------------------------

def example(arr):
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

Time  → O(n) average
Space → O(n)


---------------------------------------------------------
EXAMPLE 15 — SORTING
---------------------------------------------------------

def example(arr):
    arr.sort()

    for x in arr:
        print(x)

Sorting:
O(n log n)

Loop:
O(n)

Total:

O(n log n)

Space depends on the sorting implementation
and what exactly is being counted.


---------------------------------------------------------
EXAMPLE 16 — COPY + SORT
---------------------------------------------------------

def example(arr):
    result = sorted(arr)

Time:
O(n log n)

Extra space:
O(n)

Therefore:

Time  → O(n log n)
Space → O(n)


---------------------------------------------------------
EXAMPLE 17 — TWO POINTERS
---------------------------------------------------------

def example(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        if arr[left] < arr[right]:
            left += 1
        else:
            right -= 1

The pointers only move toward each other.

Each element is processed at most a constant number
of times.

Time  → O(n)
Space → O(1)


---------------------------------------------------------
EXAMPLE 18 — POP(0)
---------------------------------------------------------

def example(arr):
    while arr:
        arr.pop(0)

One pop from the front:
O(n)

Then:

n + (n - 1) + (n - 2) + ... + 1

= O(n²)

Time  → O(n²)
Space → O(1) auxiliary


---------------------------------------------------------
EXAMPLE 19 — APPEND
---------------------------------------------------------

def example(arr):
    result = []

    for x in arr:
        result.append(x)

append:
O(1) amortized

n appends:

O(n)

Time  → O(n)
Space → O(n)


---------------------------------------------------------
EXAMPLE 20 — RECURSION
---------------------------------------------------------

def example(n):
    if n <= 0:
        return

    example(n - 1)

One recursive call.

Depth:

n

Time  → O(n)
Space → O(n)


---------------------------------------------------------
EXAMPLE 21 — BINARY RECURSION
---------------------------------------------------------

def example(n):
    if n <= 1:
        return

    example(n - 1)
    example(n - 1)

Two branches at every level.

Time → O(2^n)

Maximum depth:

n

Space → O(n)


---------------------------------------------------------
EXAMPLE 22 — HALVING RECURSION
---------------------------------------------------------

def example(n):
    if n <= 1:
        return

    example(n // 2)

Input:

n → n/2 → n/4 → n/8 → ...

Time  → O(log n)
Space → O(log n)


---------------------------------------------------------
EXAMPLE 23 — RECURSION + LOOP
---------------------------------------------------------

def example(n):
    if n <= 0:
        return

    for i in range(n):
        print(i)

    example(n - 1)

Work:

n + (n - 1) + (n - 2) + ...

= O(n²)

Recursion depth:

O(n)

Therefore:

Time  → O(n²)
Space → O(n)


---------------------------------------------------------
EXAMPLE 24 — MATRIX
---------------------------------------------------------

def example(matrix):
    for row in matrix:
        for value in row:
            print(value)

If matrix is n × n:

Time → O(n²)

No additional data structure:

Space → O(1)


---------------------------------------------------------
EXAMPLE 25 — CREATE MATRIX
---------------------------------------------------------

def example(n):
    matrix = [[0] * n for _ in range(n)]

There are n² elements.

Time  → O(n²)
Space → O(n²)


---------------------------------------------------------
IMPORTANT INTERVIEW RULES
---------------------------------------------------------

Sequential:
O(n) + O(n)
→ O(n)


Nested:
O(n) × O(n)
→ O(n²)


Constant work:
O(1)


Fixed increment:
i += k
→ O(n)


Multiplicative change:
i *= k
→ O(log n)


n * log n:
→ O(n log n)


Keep dominant term:

O(n² + n)
→ O(n²)


Drop constants:

O(5n)
→ O(n)


Space:

Fixed variables
→ O(1)

New array of n elements
→ O(n)

n * n matrix
→ O(n²)

Recursion depth n
→ O(n)


FINAL INTERVIEW CHECKLIST
=========================

Before giving your answer, ask:

□ What is n?
□ How many times does the loop run?
□ Are loops sequential or nested?
□ Does a variable increase linearly or exponentially?
□ Are there recursive calls?
□ What Python built-ins are being used?
□ Am I creating extra data structures?
□ What is the maximum memory used at once?
□ Did I remove constants?
□ Did I keep only the dominant term?

Always answer:

Time Complexity → ?
Space Complexity → ?
'''