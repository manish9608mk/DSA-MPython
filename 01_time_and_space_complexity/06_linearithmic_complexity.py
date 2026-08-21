# This is one of the most important complexities for DSA because you'll see it in Merge Sort, Heap Sort, efficient sorting, divide-and-conquer algorithms, etc.

# 9. O(n log n) - Linearithmic Complexity

'''
O(n log n)
==========

O(n log n) is a combination of:

O(n)       → Linear work
O(log n)   → Logarithmic levels

It commonly appears when:

1. We have O(log n) levels
2. Each level performs O(n) work

Therefore:

O(n) × O(log n)
= O(n log n)


---------------------------------------------------------
1. BASIC EXAMPLE
---------------------------------------------------------

for i in range(n):

    j = 1

    while j < n:
        print(i, j)
        j *= 2

Outer loop:

O(n)

Inner loop:

O(log n)

Because the inner variable doubles:

1 → 2 → 4 → 8 → ...

Total:

O(n) × O(log n)

= O(n log n)

Time  → O(n log n)
Space → O(1)


---------------------------------------------------------
2. ANOTHER EXAMPLE
---------------------------------------------------------

for i in range(n):

    x = n

    while x > 1:
        x //= 2

Outer loop:
O(n)

Inner loop:
O(log n)

Therefore:

Time → O(n log n)

Space → O(1)


---------------------------------------------------------
3. WHY n log n?
---------------------------------------------------------

Imagine:

n elements

and

log n levels.

At every level we process all n elements.

Level 1:
n work

Level 2:
n work

Level 3:
n work

...

Number of levels:
log n

Therefore:

n + n + n + ... (log n times)

= n log n


---------------------------------------------------------
4. MERGE SORT
---------------------------------------------------------

Merge Sort is the classic example.

Conceptually:

                 n
              /     \
            n/2     n/2
           /  \     /  \
         n/4  n/4 n/4  n/4
          ...
        
Each level divides the array into smaller pieces.

Number of levels:

O(log n)

At every level, merging all elements costs:

O(n)

Therefore:

O(n) × O(log n)

= O(n log n)

Merge Sort:

Time → O(n log n)
Space → O(n)


---------------------------------------------------------
5. DIVIDE AND CONQUER
---------------------------------------------------------

Many divide-and-conquer algorithms follow:

1. Divide the problem.
2. Solve smaller problems.
3. Combine the results.

If:

Number of levels = O(log n)

and

Work per level = O(n)

Then:

Time = O(n log n)


---------------------------------------------------------
6. MERGE SORT BREAKDOWN
---------------------------------------------------------

Suppose:

n = 8

Divide:

8
↓
4 + 4
↓
2 + 2 + 2 + 2
↓
1 + 1 + 1 + 1 + 1 + 1 + 1 + 1

Levels:

log₂(8) = 3

At each level, approximately n elements
are processed.

Therefore:

8 × 3

= 24

General:

n log n


---------------------------------------------------------
7. PYTHON SORTING
---------------------------------------------------------

Python:

arr.sort()

and:

sorted(arr)

use Timsort.

Worst-case time complexity:

O(n log n)

Typical interview answer:

Time → O(n log n)


---------------------------------------------------------
8. SORTING EXAMPLE
---------------------------------------------------------

def solve(arr):

    arr.sort()

    for x in arr:
        print(x)

Sorting:

O(n log n)

Loop:

O(n)

Total:

O(n log n) + O(n)

Keep the dominant term:

O(n log n)


---------------------------------------------------------
9. O(n log n) + O(n)
---------------------------------------------------------

Suppose:

O(n log n) + O(n)

Because:

n log n > n

for sufficiently large n,

we keep:

O(n log n)


Therefore:

O(n log n) + O(n)
= O(n log n)


---------------------------------------------------------
10. O(n log n) + O(n²)
---------------------------------------------------------

Suppose:

O(n log n) + O(n²)

The dominant term is:

O(n²)

Therefore:

O(n log n) + O(n²)
= O(n²)


Important:

Do NOT automatically answer O(n log n)
just because you see sorting.


---------------------------------------------------------
11. O(n log n) WITH O(n) SPACE
---------------------------------------------------------

def example(arr):

    result = sorted(arr)

sorted(arr) creates a new list.

Time:

O(n log n)

Additional space:

O(n)

So:

Time  → O(n log n)
Space → O(n)


---------------------------------------------------------
12. O(n log n) TIME + O(1) SPACE
---------------------------------------------------------

An algorithm can have:

Time  → O(n log n)
Space → O(1)

Time and space are independent.

Do not assume:

O(n log n) time
means
O(n log n) space.


---------------------------------------------------------
13. TWO SEQUENTIAL O(n log n) OPERATIONS
---------------------------------------------------------

sort(arr)       # O(n log n)

sort(arr)       # O(n log n)

Total:

O(n log n) + O(n log n)

= O(2n log n)

= O(n log n)


---------------------------------------------------------
14. NESTED O(n) AND O(log n)
---------------------------------------------------------

for i in range(n):

    j = 1

    while j < n:
        j *= 2

Nested complexities:

O(n) × O(log n)

= O(n log n)


---------------------------------------------------------
15. THREE NESTED LEVELS
---------------------------------------------------------

for i in range(n):

    j = 1

    while j < n:

        k = 1

        while k < n:
            k *= 2

        j *= 2

Complexities:

Outer loop:
O(n)

Middle loop:
O(log n)

Inner loop:
O(log n)

Total:

O(n × log n × log n)

= O(n(log n)²)


---------------------------------------------------------
16. IMPORTANT DISTINCTION
---------------------------------------------------------

This:

for i in range(n):
    for j in range(n):
        print(i, j)

is:

O(n²)

NOT:

O(n log n)

Because both loops run n times.


This:

for i in range(n):

    j = 1

    while j < n:
        j *= 2

is:

O(n log n)

because:

n × log n


---------------------------------------------------------
17. O(n log n) VS O(n²)
---------------------------------------------------------

For large n:

O(n log n)

is significantly better than:

O(n²)


Example:

n = 1,000,000

Approximately:

n log₂ n
≈ 20,000,000

while:

n²
= 1,000,000,000,000

Huge difference.


---------------------------------------------------------
18. COMMON O(n log n) ALGORITHMS
---------------------------------------------------------

Important examples:

Merge Sort
→ O(n log n)

Heap Sort
→ O(n log n)

Efficient comparison sorting
→ O(n log n)

Python Timsort
→ O(n log n) worst case


---------------------------------------------------------
19. RECOGNITION TRICKS
---------------------------------------------------------

Look for:

Pattern 1:

for i in range(n):
    while condition:
        value *= 2

→ O(n log n)


Pattern 2:

n elements processed at
log n levels

→ O(n log n)


Pattern 3:

Divide-and-conquer with
O(n) work per level

→ O(n log n)


Pattern 4:

Efficient comparison sorting

→ Usually O(n log n)


---------------------------------------------------------
20. IMPORTANT RULE
---------------------------------------------------------

O(n log n) usually appears when:

Linear work
      ×
Logarithmic number of levels

       ↓

O(n log n)


---------------------------------------------------------
21. QUICK COMPARISON
---------------------------------------------------------

Complexity        Growth

O(1)              Constant

O(log n)          Very slow growth

O(n)              Linear

O(n log n)        Linearithmic

O(n²)             Quadratic

O(2^n)            Exponential


Generally:

O(n log n) < O(n²)

for large n.


---------------------------------------------------------
22. INTERVIEW METHOD
---------------------------------------------------------

When you see code:

Step 1:
Analyze the outer loop.

Step 2:
Analyze the inner loop.

Step 3:
If nested → multiply.

Step 4:
If sequential → add.

Step 5:
Remove constants.

Step 6:
Keep the dominant term.

Example:

O(n log n) + O(n)

→ O(n log n)


FINAL MEMORY TRICK:

O(n)
+
O(log n) nested
      ↓
O(n log n)

OR:

O(log n) levels
*
O(n) work per level
      ↓
O(n log n)




What you should recognize instantly:

n iterations
*
log n iterations
        ↓
   O(n log n)



And the three major patterns you've learned now:
i += 1       → O(n)

i *= 2       → O(log n)

n work * log n levels
             → O(n log n)
'''