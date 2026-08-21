# 12. Final Time & Space Complexity Cheat Sheet

'''
=========================================================
TIME & SPACE COMPLEXITY — FINAL REVISION
=========================================================


1. BIG-O ORDER
---------------------------------------------------------

Best → Worst

O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2^n)
O(n!)


For large n:

O(1) < O(log n) < O(n) < O(n log n)
     < O(n²) < O(n³) < O(2^n) < O(n!)


---------------------------------------------------------
2. BASIC LOOP PATTERNS
---------------------------------------------------------

for i in range(n):
    ...

→ O(n)


for i in range(n):
    for j in range(n):
        ...

→ O(n²)


i = 1

while i < n:
    i *= 2

→ O(log n)


i = n

while i > 1:
    i //= 2

→ O(log n)


for i in range(n):
    j = 1

    while j < n:
        j *= 2

→ O(n log n)


---------------------------------------------------------
3. LOOP RULES
---------------------------------------------------------

Sequential loops:

O(n) + O(n)
→ O(n)


Nested loops:

O(n) * O(n)
→ O(n²)


Nested:

O(n) * O(log n)
→ O(n log n)


Three nested:

O(n) * O(n) * O(n)
→ O(n³)


---------------------------------------------------------
4. INCREMENT VS MULTIPLICATION
---------------------------------------------------------

i += 1
i += 5
i -= 10

→ O(n)


i *= 2
i *= 3
i //= 2
i //= 5

→ O(log n)


MEMORY TRICK:

+ / - constant
→ O(n)

* / ÷ constant
→ O(log n)


---------------------------------------------------------
5. PYTHON LIST COMPLEXITY
---------------------------------------------------------

arr[i]              → O(1)

arr.append(x)       → O(1) amortized

arr.pop()           → O(1)

arr.pop(i)          → O(n)

arr.insert(i, x)    → O(n)

x in arr            → O(n)

arr.remove(x)       → O(n)

arr.reverse()       → O(n)

arr.sort()          → O(n log n)

arr.copy()          → O(n)


IMPORTANT:

append()
→ O(1) amortized

pop()
→ O(1)

pop(0)
→ O(n)


---------------------------------------------------------
6. DICTIONARY COMPLEXITY
---------------------------------------------------------

d[key]
→ O(1) average


d[key] = value
→ O(1) average


d.get(key)
→ O(1) average


d.pop(key)
→ O(1) average


key in d
→ O(1) average


Dictionary iteration:

for key in d:
    ...

→ O(n)


---------------------------------------------------------
7. SET COMPLEXITY
---------------------------------------------------------

s.add(x)
→ O(1) average


s.remove(x)
→ O(1) average


s.discard(x)
→ O(1) average


x in s
→ O(1) average


s.pop()
→ O(1) average


Set iteration:

for x in s:
    ...

→ O(n)


---------------------------------------------------------
8. STRING COMPLEXITY
---------------------------------------------------------

s[i]
→ O(1)


len(s)
→ O(1)


x in s
→ O(n)


s + t
→ O(n + m)


s.lower()
→ O(n)


s.upper()
→ O(n)


s.strip()
→ O(n)


s.split()
→ O(n) with respect to total characters processed


s.replace(a, b)
→ O(n)


s[::-1]
→ O(n)


s.count(x)
→ O(n)


---------------------------------------------------------
9. SPACE COMPLEXITY
---------------------------------------------------------

Fixed variables:

x = 10
y = 20

→ O(1)


New list of n elements:

result = [0] * n

→ O(n)


Set containing n elements:

seen = set(arr)

→ O(n)


Dictionary containing n entries:

freq = {}

→ O(n)


n * n matrix:

matrix = [[0] * n for _ in range(n)]

→ O(n²)


---------------------------------------------------------
10. INPUT SPACE VS AUXILIARY SPACE
---------------------------------------------------------

Input:

arr
→ O(n)

If we only use variables:

maximum = arr[0]

Auxiliary Space:
→ O(1)


If we create:

result = []

and store n elements:

Auxiliary Space:
→ O(n)


Usually interviewers mean:

Auxiliary Space

unless they explicitly ask for total space.


---------------------------------------------------------
11. IN-PLACE ALGORITHM
---------------------------------------------------------

An algorithm that modifies the input
without creating another data structure
of size n.

Example:

def reverse(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

Time  → O(n)
Space → O(1)


---------------------------------------------------------
12. RECURSION
---------------------------------------------------------

f(n - 1)

→ Time O(n)
→ Space O(n)


f(n // 2)

→ Time O(log n)
→ Space O(log n)


f(n - 1)
f(n - 1)

→ Time O(2^n)
→ Space O(n)


IMPORTANT:

Total number of calls
→ Time


Maximum active recursion depth
→ Space


---------------------------------------------------------
13. O(n log n)
---------------------------------------------------------

Common situations:

n elements
*
log n levels

→ O(n log n)


Examples:

Merge Sort
→ O(n log n)


Heap Sort
→ O(n log n)


Python sorting worst case
→ O(n log n)


Example:

for i in range(n):

    j = 1

    while j < n:
        j *= 2

→ O(n log n)


---------------------------------------------------------
14. SORTING
---------------------------------------------------------

arr.sort()

→ O(n log n) worst case


sorted(arr)

→ O(n log n) worst case

sorted(arr) also creates a new list:

Space → O(n)


---------------------------------------------------------
15. DOMINANT TERM RULE
---------------------------------------------------------

O(n² + n)

→ O(n²)


O(n³ + n² + n)

→ O(n³)


O(n log n + n)

→ O(n log n)


O(5n + 10)

→ O(n)


---------------------------------------------------------
16. CONSTANTS ARE IGNORED
---------------------------------------------------------

O(2n)
→ O(n)


O(5n)
→ O(n)


O(100n)
→ O(n)


O(3n²)
→ O(n²)


O(10n log n)
→ O(n log n)


---------------------------------------------------------
17. SEQUENTIAL VS NESTED
---------------------------------------------------------

Sequential:

A → O(n)
B → O(n)

Total:

O(n) + O(n)
= O(n)


Nested:

A → O(n)
B → O(n)

Total:

O(n) × O(n)
= O(n²)


---------------------------------------------------------
18. TWO DIFFERENT INPUTS
---------------------------------------------------------

def solve(arr1, arr2):

    for x in arr1:
        ...

    for y in arr2:
        ...

If:

len(arr1) = n
len(arr2) = m

Time:

O(n + m)


Nested:

for x in arr1:
    for y in arr2:
        ...

Time:

O(n * m)


Do NOT automatically replace
n and m with one variable.


---------------------------------------------------------
19. COMMON COMPLEXITIES
---------------------------------------------------------

O(1)
→ Array indexing
→ Hash lookup average
→ Set lookup average


O(log n)
→ Binary Search
→ Balanced BST search
→ Halving/doubling loop


O(n)
→ Array traversal
→ Linear Search
→ Counting frequency


O(n log n)
→ Efficient comparison sorting
→ Merge Sort
→ Heap Sort


O(n²)
→ Nested loops
→ Bubble Sort
→ Selection Sort
→ Insertion Sort worst case


O(2^n)
→ Naive recursive Fibonacci
→ Some subset/decision recursion


O(n!)
→ Permutations using brute force


---------------------------------------------------------
20. AMORTIZED COMPLEXITY
---------------------------------------------------------

Python list:

arr.append(x)

→ O(1) amortized


Why?

Most appends:
→ O(1)

Occasional resize:
→ O(n)

Across many operations:

Total:
→ O(n)

Average per operation:
→ O(1) amortized


---------------------------------------------------------
21. TIME + SPACE EXAMPLES
---------------------------------------------------------

Example 1:

def solve(arr):
    for x in arr:
        print(x)

Time  → O(n)
Space → O(1)


Example 2:

def solve(arr):
    result = []

    for x in arr:
        result.append(x)

Time  → O(n)
Space → O(n)


Example 3:

def solve(arr):
    for x in arr:
        for y in arr:
            print(x, y)

Time  → O(n²)
Space → O(1)


Example 4:

def solve(n):
    while n > 1:
        n //= 2

Time  → O(log n)
Space → O(1)


Example 5:

def solve(n):
    if n <= 1:
        return

    solve(n - 1)

Time  → O(n)
Space → O(n)


Example 6:

def solve(arr):
    arr.sort()

    for x in arr:
        print(x)

Time:

O(n log n) + O(n)
= O(n log n)

Space depends on the operation/implementation
and what is being counted.


---------------------------------------------------------
22. INTERVIEW ANALYSIS CHECKLIST
---------------------------------------------------------

Whenever you see code:

STEP 1:
Identify input size.

What is n?

STEP 2:
Analyze each loop.

How many times does it execute?

STEP 3:
Check how variables change.

+= constant
→ O(n)

*= constant
→ O(log n)

STEP 4:
Check nested loops.

Multiply.

STEP 5:
Check sequential operations.

Add.

STEP 6:
Check recursion.

Count:

→ Number of calls
→ Recursion depth

STEP 7:
Check Python built-ins.

Example:

x in list
→ O(n)

x in set
→ O(1) average

arr.sort()
→ O(n log n)

STEP 8:
Check extra memory.

New list?
New set?
New dictionary?
Recursion stack?

STEP 9:
Drop constants.

STEP 10:
Drop lower-order terms.

STEP 11:
State both:

Time → ?
Space → ?


=========================================================
FINAL MEMORY MAP
=========================================================

Constant work
     ↓
   O(1)

Linear growth
     ↓
   O(n)

Repeated halving
     ↓
 O(log n)

Linear * logarithmic
     ↓
 O(n log n)

Nested linear loops
     ↓
  O(n²)

Three nested linear loops
     ↓
  O(n³)

Branching recursion
     ↓
  O(2^n)

All permutations
     ↓
  O(n!)


FINAL QUESTION TO ASK YOURSELF:

"How many times does the work happen?"
             ↓
        TIME COMPLEXITY

"How much extra memory is needed?"
             ↓
       SPACE COMPLEXITY
'''