# 6. Space Complexity
'''
Space Complexity
================

Space Complexity measures how much memory an algorithm
uses as the input size n grows.

In DSA interviews, we usually focus on:

1. Auxiliary Space
   → Extra memory used by the algorithm.

2. Input Space
   → Memory occupied by the input itself.

Usually, when someone asks for "space complexity",
they mean auxiliary space unless stated otherwise.


---------------------------------------------------------
1. CONSTANT SPACE → O(1)
---------------------------------------------------------

Only a fixed number of variables are created.

Example:

x = 10
y = 20
total = x + y

The number of variables does not depend on n.

Space → O(1)


Example:

def sum_array(arr):
    total = 0

    for x in arr:
        total += x

    return total

The input arr already exists.
Only total and x are extra variables.

Time  → O(n)
Space → O(1)


---------------------------------------------------------
2. LINEAR SPACE → O(n)
---------------------------------------------------------

Extra memory grows with input size.

Example:

def copy_array(arr):
    result = []

    for x in arr:
        result.append(x)

    return result

If arr contains n elements,
result also contains n elements.

Time  → O(n)
Space → O(n)


---------------------------------------------------------
3. O(n) SPACE USING A SET
---------------------------------------------------------

def unique_elements(arr):
    seen = set()

    for x in arr:
        seen.add(x)

    return seen

In the worst case, the set can contain n elements.

Time  → O(n) average
Space → O(n)


---------------------------------------------------------
4. O(n) SPACE USING A DICTIONARY
---------------------------------------------------------

def count_frequency(arr):
    freq = {}

    for x in arr:
        freq[x] = freq.get(x, 0) + 1

    return freq

The dictionary can contain up to n different keys.

Time  → O(n) average
Space → O(n)


---------------------------------------------------------
5. O(n²) SPACE
---------------------------------------------------------

def create_matrix(n):
    matrix = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(0)

        matrix.append(row)

    return matrix

There are n rows.

Each row contains n elements.

Total elements:

n × n = n²

Space → O(n²)

Time  → O(n²)


---------------------------------------------------------
6. CONSTANT NUMBER OF VARIABLES → O(1)
---------------------------------------------------------

def example(arr):
    first = arr[0]
    last = arr[-1]
    middle = len(arr) // 2

    return first + last

Only a fixed number of variables are created.

Space → O(1)


---------------------------------------------------------
7. CREATING A NEW STRING → O(n)
---------------------------------------------------------

def reverse_string(s):
    result = s[::-1]

s[::-1] creates a new string.

If length of s = n:

Space → O(n)


---------------------------------------------------------
8. STRING CONCATENATION
---------------------------------------------------------

def build_string(arr):
    result = ""

    for word in arr:
        result += word

The final string can contain O(n) characters
(or more generally, O(total input characters)).

Space → O(n) with respect to the total output size.


---------------------------------------------------------
9. LIST COMPREHENSION → O(n)
---------------------------------------------------------

def double_values(arr):
    result = [x * 2 for x in arr]

result contains n elements.

Space → O(n)


---------------------------------------------------------
10. IN-PLACE MODIFICATION → O(1) AUXILIARY SPACE
---------------------------------------------------------

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

The original array is modified.

No additional array of size n is created.

Auxiliary Space → O(1)


---------------------------------------------------------
11. INPUT SPACE vs AUXILIARY SPACE
---------------------------------------------------------

def process(arr):
    result = []

    for x in arr:
        result.append(x)

Input:
arr → O(n)

Extra memory:
result → O(n)

Auxiliary Space → O(n)

If counting input + extra memory:

Total Space → O(n)


Usually in DSA interviews,
we report auxiliary space separately.


---------------------------------------------------------
12. OUTPUT SPACE
---------------------------------------------------------

def get_squares(arr):
    result = []

    for x in arr:
        result.append(x * x)

    return result

The output itself contains n elements.

Output Space → O(n)

Auxiliary Space depends on whether
the output is counted.

In interviews, clarify what the interviewer wants.


---------------------------------------------------------
13. LOOP DOES NOT AUTOMATICALLY MEAN O(n) SPACE
---------------------------------------------------------

def example(arr):
    total = 0

    for x in arr:
        total += x

There is a loop over n elements,
but we do NOT store all n elements.

Time  → O(n)
Space → O(1)


IMPORTANT:

Time and Space are independent.

A loop can be:

Time  → O(n)
Space → O(1)


---------------------------------------------------------
14. NESTED LOOPS DO NOT AUTOMATICALLY MEAN O(n²) SPACE
---------------------------------------------------------

def example(n):
    total = 0

    for i in range(n):
        for j in range(n):
            total += i + j

Time  → O(n²)
Space → O(1)

Why?

The loops perform n² operations,
but only a fixed number of variables are stored.


---------------------------------------------------------
15. NESTED DATA STRUCTURE → O(n²) SPACE
---------------------------------------------------------

def create_matrix(n):
    matrix = [[0] * n for _ in range(n)]

There are n rows.

Each row contains n elements.

Space → O(n²)


---------------------------------------------------------
16. RECURSION STACK
---------------------------------------------------------

def countdown(n):
    if n == 0:
        return

    countdown(n - 1)

There are n recursive calls.

The call stack stores n stack frames.

Time  → O(n)
Space → O(n)


---------------------------------------------------------
17. RECURSION WITH CONSTANT DEPTH
---------------------------------------------------------

def example(n):
    if n <= 0:
        return

    example(n - 1)

Although the function uses only a few local variables,
there are n active recursive calls.

Therefore:

Space → O(n)

The memory comes from the call stack.


---------------------------------------------------------
18. TIME AND SPACE CAN BE DIFFERENT
---------------------------------------------------------

def find_max(arr):
    maximum = arr[0]

    for x in arr:
        if x > maximum:
            maximum = x

Time  → O(n)
Space → O(1)


---------------------------------------------------------
19. O(n) TIME + O(n) SPACE
---------------------------------------------------------

def get_even_numbers(arr):
    result = []

    for x in arr:
        if x % 2 == 0:
            result.append(x)

Time  → O(n)
Space → O(n)

Worst case:
All n elements are even.


---------------------------------------------------------
20. O(n²) TIME + O(n) SPACE
---------------------------------------------------------

def find_duplicates(arr):
    seen = set()

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                seen.add(arr[i])

Time  → O(n²)
Space → O(n)


---------------------------------------------------------
21. O(n²) TIME + O(n²) SPACE
---------------------------------------------------------

def create_table(n):
    table = []

    for i in range(n):
        row = []

        for j in range(n):
            row.append(i * j)

        table.append(row)

Time  → O(n²)
Space → O(n²)


---------------------------------------------------------
22. IMPORTANT RULES
---------------------------------------------------------

RULE 1:
Fixed number of variables
→ O(1) space


RULE 2:
Data structure grows with n
→ O(n) space


RULE 3:
2D structure of n × n
→ O(n²) space


RULE 4:
Nested loops do NOT automatically mean O(n²) space.

Example:

for i in range(n):
    for j in range(n):
        ...

Space can still be O(1).


RULE 5:
Recursive calls use call-stack memory.

n recursive calls
→ O(n) space


RULE 6:
Modifying the input array in-place
can give O(1) auxiliary space.


RULE 7:
Creating a new array/list of n elements
→ O(n) space.


RULE 8:
Creating a set/dictionary containing up to n elements
→ O(n) average space.


RULE 9:
Time and Space are independent.

O(n) Time + O(1) Space
is completely possible.

O(n) Time + O(n) Space
is also possible.

O(n²) Time + O(1) Space
is also possible.


---------------------------------------------------------
23. QUICK REFERENCE
---------------------------------------------------------

Operation / Structure              Space

Fixed variables                    O(1)
Single integer                     O(1)
Single pointer/reference           O(1)
New list of n elements             O(n)
New set of n elements              O(n)
New dictionary of n elements       O(n)
New string of n characters         O(n)
2D matrix n × n                    O(n²)
n recursive calls                  O(n)


---------------------------------------------------------
24. INTERVIEW FORMULA
---------------------------------------------------------

When analyzing Space Complexity:

Step 1:
Ignore the input itself unless asked to count it.

Step 2:
Look for new data structures.

Step 3:
Ask:
"Can this structure grow with n?"

Step 4:
Check recursion depth / call stack.

Step 5:
Find the largest amount of memory used
at any point.

Step 6:
Drop constants and lower-order terms.


Examples:

O(n) + O(n)
→ O(n)

O(n²) + O(n)
→ O(n²)

O(1) + O(n)
→ O(n)


FINAL RULE:

Time Complexity
→ How much work?

Space Complexity
→ How much extra memory?
'''