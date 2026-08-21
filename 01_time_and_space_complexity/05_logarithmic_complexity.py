# Logarithmic Complexity — O(log n).
# This is extremely important for Binary Search, Trees, Heaps, and many optimized algorithms.

# 8. Logarithmic Complexity - O(log n)

'''
Logarithmic Complexity
======================

O(log n) occurs when the problem size is repeatedly
reduced by a constant factor.

The most common example:

n
n/2
n/4
n/8
n/16
...

The input is divided by 2 at every step.


---------------------------------------------------------
1. BASIC EXAMPLE → O(log n)
---------------------------------------------------------

i = 1

while i < n:
    print(i)
    i *= 2

Values of i:

1
2
4
8
16
32
64
...

The value doubles every iteration.

After k iterations:

2^k = n

Taking log:

k = log₂(n)

Therefore:

Time  → O(log n)
Space → O(1)


---------------------------------------------------------
2. HALVING → O(log n)
---------------------------------------------------------

i = n

while i > 1:
    print(i)
    i //= 2

Values:

n
n/2
n/4
n/8
n/16
...

The value is divided by 2 every iteration.

Time  → O(log n)
Space → O(1)


---------------------------------------------------------
3. WHY IS IT LOG n?
---------------------------------------------------------

Suppose:

n = 16

Divide by 2:

16 → 8 → 4 → 2 → 1

Number of steps = 4

And:

log₂(16) = 4


Suppose:

n = 1,000,000

We don't need 1,000,000 iterations.

Approximately:

log₂(1,000,000) ≈ 20

Only about 20 iterations!


---------------------------------------------------------
4. CONSTANT FACTOR DOES NOT MATTER
---------------------------------------------------------

i = 1

while i < n:
    i *= 3

The value becomes:

1
3
9
27
81
243
...

After k iterations:

3^k = n

Therefore:

k = log₃(n)

In Big-O:

O(log₃ n)
= O(log n)

The base of the logarithm is ignored
because it is a constant factor.


---------------------------------------------------------
5. MULTIPLYING BY A CONSTANT → O(log n)
---------------------------------------------------------

i = 1

while i < n:
    i *= 5

Each iteration multiplies i by 5.

Therefore:

Time → O(log n)


Similarly:

i *= 10
i *= 100
i *= 2

All are:

O(log n)


---------------------------------------------------------
6. DIVIDING BY A CONSTANT → O(log n)
---------------------------------------------------------

i = n

while i > 1:
    i //= 3

The input becomes:

n
n/3
n/9
n/27
...

Time → O(log n)


---------------------------------------------------------
7. BINARY SEARCH → O(log n)
---------------------------------------------------------

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return True

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return False

Every iteration eliminates approximately half
of the remaining search space.

n
n/2
n/4
n/8
...

Time → O(log n)
Space → O(1)


---------------------------------------------------------
8. RECURSION WITH HALVING → O(log n)
---------------------------------------------------------

def solve(n):
    if n <= 1:
        return

    solve(n // 2)

Input:

n
n/2
n/4
n/8
...

Time  → O(log n)
Space → O(log n)

Space is O(log n) because the recursion
depth is logarithmic.


---------------------------------------------------------
9. O(log n) DOES NOT MEAN LOOP VARIABLE MUST BE n
---------------------------------------------------------

i = 1

while i <= n:
    i *= 2

This is O(log n).

The important thing is:

The amount of remaining work is repeatedly
reduced by a constant factor.


---------------------------------------------------------
10. COMMON RECOGNITION TRICK
---------------------------------------------------------

Look for:

i *= 2
i *= 3
i *= k

OR:

i //= 2
i //= 3
i //= k

OR:

n //= 2
n //= 3
n //= k

These are strong signals for:

O(log n)


---------------------------------------------------------
11. IMPORTANT DIFFERENCE
---------------------------------------------------------

Example A:

for i in range(n):
    print(i)

The value increases by a constant amount:

0
1
2
3
4
...

Time → O(n)


Example B:

i = 1

while i < n:
    i *= 2

The value increases multiplicatively:

1
2
4
8
16
...

Time → O(log n)


Remember:

+ constant → usually O(n)

× or ÷ constant → usually O(log n)


---------------------------------------------------------
12. O(log n) WITH O(1) WORK
---------------------------------------------------------

i = n

while i > 1:
    print(i)
    i //= 2

Each iteration:

Work → O(1)

Number of iterations → O(log n)

Therefore:

Time → O(log n)


---------------------------------------------------------
13. O(log n) WITH O(n) WORK
---------------------------------------------------------

i = 1

while i < n:
    for j in range(n):
        print(j)

    i *= 2

Outer loop:

O(log n)

Inner loop:

O(n)

Total:

O(n log n)


---------------------------------------------------------
14. TWO LOGARITHMIC LOOPS SEQUENTIALLY
---------------------------------------------------------

i = 1

while i < n:
    i *= 2


j = 1

while j < n:
    j *= 2

First loop  → O(log n)
Second loop → O(log n)

Total:

O(log n) + O(log n)
= O(2 log n)
= O(log n)


---------------------------------------------------------
15. TWO LOGARITHMIC LOOPS NESTED
---------------------------------------------------------

i = 1

while i < n:
    j = 1

    while j < n:
        j *= 2

    i *= 2

Outer → O(log n)
Inner → O(log n)

Nested:

O(log n) × O(log n)

= O((log n)²)


---------------------------------------------------------
16. LOGARITHMIC LOOP WITH n HALVING
---------------------------------------------------------

n = 100

while n > 1:
    n //= 2

Iterations:

100
50
25
12
6
3
1

The exact number is approximately:

log₂(100)

Therefore:

Time → O(log n)


---------------------------------------------------------
17. O(log n) IN TREES
---------------------------------------------------------

For a balanced binary search tree:

             50
            /  \
          30    70
         / \    / \
       20  40  60  80

At every level, the search space is reduced.

Balanced BST search:

Time → O(log n)

Important:

This depends on the tree being balanced.

A completely skewed BST can become:

Time → O(n)


---------------------------------------------------------
18. LOGARITHM BASE DOES NOT MATTER IN BIG-O
---------------------------------------------------------

O(log₂ n)
O(log₃ n)
O(log₁₀ n)

All are:

O(log n)

Because:

log₃(n)
= log₂(n) / log₂(3)

The denominator is a constant.

Big-O ignores constant factors.


---------------------------------------------------------
19. COMMON MISTAKE
---------------------------------------------------------

Wrong:

i = 1

while i < n:
    i += 2

This is NOT O(log n).

It is:

O(n)

Because the value increases by a constant amount.

Correct logarithmic pattern:

i *= 2


---------------------------------------------------------
20. ANOTHER COMMON MISTAKE
---------------------------------------------------------

Wrong assumption:

"while loop = O(log n)"

Not true.

Example:

i = 0

while i < n:
    i += 1

This is:

O(n)

The loop type does not determine complexity.

The CHANGE in the variable determines complexity.


---------------------------------------------------------
21. QUICK RECOGNITION TABLE
---------------------------------------------------------

Code Pattern                         Complexity

i += 1                               O(n)

i += 5                               O(n)

i -= 1                               O(n)

i *= 2                               O(log n)

i *= 3                               O(log n)

i //= 2                              O(log n)

i //= 5                              O(log n)

n //= 2                              O(log n)

Binary Search                        O(log n)

Balanced BST Search                  O(log n)


---------------------------------------------------------
22. INTERVIEW THINKING PROCESS
---------------------------------------------------------

When you see a while loop:

Step 1:
Look at how the loop variable changes.

Step 2:
Ask:

"Does it increase/decrease by a fixed amount?"

If YES:

→ O(n)


Step 3:
Ask:

"Does it multiply/divide by a constant?"

If YES:

→ O(log n)


Step 4:
If there are nested loops,
multiply their complexities.


Step 5:
If there are sequential loops,
add their complexities.


---------------------------------------------------------
23. MOST IMPORTANT RULE
---------------------------------------------------------

Arithmetic change:

i += 1
i += 10
i -= 5

→ O(n)


Multiplicative change:

i *= 2
i *= 3
i //= 2
i //= 5

→ O(log n)


FINAL MEMORY TRICK:

+ / - constant
      ↓
    O(n)

× / ÷ constant
      ↓
   O(log n)




i += 1     → 1, 2, 3, 4, 5...       → O(n)

i *= 2     → 1, 2, 4, 8, 16...      → O(log n)

i //= 2    → n, n/2, n/4, n/8...    → O(log n)
'''