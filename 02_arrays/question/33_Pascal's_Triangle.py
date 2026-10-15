# 118. PASCAL'S TRIANGLE

"""
PROBLEM

Given an integer numRows, return the first numRows of Pascal's Triangle.

Rules:
1. Every row starts and ends with 1.
2. Every middle element is the sum of the two elements directly above it.
3. Row 0 contains 1 element, row 1 contains 2 elements, and so on.

Example:
Input: numRows = 5

Output:
[[1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]]
"""

"""
PATTERN

Array + Simulation + Dynamic Programming

We build each row using the previous row.

Formula:
row[j] = previous_row[j - 1] + previous_row[j]

Recognition:
- Each element depends on previous elements.
- The first and last elements are always 1.
- We must generate multiple rows in order.
"""

"""
APPROACH 1 — BRUTE FORCE

Calculate each element using the binomial coefficient formula:

C(i, j) = i! / (j! * (i - j)!)

Here, i is the row index and j is the element index.

This approach works, but calculating factorials repeatedly is
unnecessary when we can build the triangle from previous rows.
"""

# BRUTE FORCE CODE

import math

def generate_brute(numRows):
    result = []

    for i in range(numRows):
        row = []

        for j in range(i + 1):
            value = math.factorial(i) // (
                math.factorial(j) * math.factorial(i - j)
            )
            row.append(value)

        result.append(row)

    return result


"""
Complexity:
Time: O(n^2) arithmetic operations, assuming factorial operations
      are treated as constant-time for basic analysis.
Space: O(n^2) for the output.

Note:
With arbitrary-precision integer arithmetic, factorial calculations
have additional costs. This approach is mainly for understanding.
"""

"""
APPROACH 2 — OPTIMAL / STANDARD

Build each row using the previous row.

Steps:
1. Create an empty result list.
2. For row index i, create a row containing i + 1 ones.
3. Keep the first and last elements as 1.
4. Calculate the middle elements from the previous row.
5. Append the completed row to result.
6. Return result.

Why initialize with ones?
The first and last elements of every row must be 1.
Only the middle elements need calculations.
"""

# OPTIMAL CODE

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        result = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = result[i - 1][j - 1] + result[i - 1][j]

            result.append(row)

        return result


"""
WHY DYNAMIC PROGRAMMING?

Each row uses values already calculated in the previous row.

Instead of calculating every element independently, we reuse
previous results.

This is a simple form of bottom-up dynamic programming.
"""

"""
STEP-BY-STEP THINKING

Suppose numRows = 4.

i = 0:
row = [1]
result = [[1]]

i = 1:
row = [1, 1]
result = [[1], [1, 1]]

i = 2:
Start with [1, 1, 1]
Middle element = 1 + 1 = 2
row = [1, 2, 1]

i = 3:
Start with [1, 1, 1, 1]
Middle element 1 = 1 + 2 = 3
Middle element 2 = 2 + 1 = 3
row = [1, 3, 3, 1]

Final result:
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
"""

"""
DRY RUN

Input:
numRows = 5

Previous row     New row
--------------------------------
No previous row  [1]
[1]              [1, 1]
[1, 1]           [1, 2, 1]
[1, 2, 1]        [1, 3, 3, 1]
[1, 3, 3, 1]     [1, 4, 6, 4, 1]

For the final row:
1 + 3 = 4
3 + 3 = 6
3 + 1 = 4

Output:
[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1],
 [1, 4, 6, 4, 1]]
"""

"""
WHY DOES THE OPTIMAL APPROACH WORK?

1. The first and last elements are always 1.
2. Every middle element equals the sum of two elements above it.
3. The previous row has already been calculated and stored.
4. Therefore, each new row can be generated correctly.

Building rows in order guarantees that all required previous
values are available.
"""

"""
EDGE CASES

1. numRows = 1
   Output: [[1]]

2. numRows = 2
   Output: [[1], [1, 1]]

3. numRows = 5
   Output: [[1], [1, 1], [1, 2, 1],
            [1, 3, 3, 1], [1, 4, 6, 4, 1]]

4. Constraint:
   1 <= numRows <= 30
"""

"""
TIME & SPACE COMPLEXITY

Let n = numRows.

Time Complexity: O(n^2)
There are n rows, containing 1, 2, 3, ..., n elements.

Space Complexity: O(n^2)
The result stores all elements of Pascal's Triangle.

Auxiliary Space: O(n)
The current row requires O(n) space, excluding the output.
"""

"""
INTERVIEW EXPLANATION

"I generate Pascal's Triangle row by row. Each new row starts
and ends with 1. For every middle position, I add the two
corresponding elements from the previous row.

I append each completed row to the result and return the
triangle. The time and output space complexities are O(n^2)."
"""

"""
RECOGNITION TRICKS

If every element depends on previously calculated elements:
Think about Dynamic Programming.

If the first and last values are fixed:
Initialize the row with those values.

If a problem asks you to generate rows in sequence:
Build each row from the previous row.

Pascal's Triangle:
Previous row + Adjacent sum = Next row
"""

"""
REUSABLE TEMPLATE

result = []

for i in range(numRows):
    row = [1] * (i + 1)

    for j in range(1, i):
        row[j] = result[i - 1][j - 1] + result[i - 1][j]

    result.append(row)

return result
"""

"""
COMMON INTERVIEW MISTAKES

1. Forgetting that row i contains i + 1 elements.
2. Changing the first or last element from 1.
3. Starting the inner loop at 0 instead of 1.
4. Using j <= i instead of j < i for middle elements.
5. Accessing the previous row when i = 0.
6. Forgetting to append each completed row.
7. Returning only the final row instead of the whole triangle.
8. Recalculating factorials when previous rows are available.
"""

"""
TEST CASE
"""

sol = Solution()

print(sol.generate(5))
print(sol.generate(1))

"""
OUTPUT

[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
[[1]]
"""

"""
MOST IMPORTANT THING TO REMEMBER

Pascal's Triangle = Build each row from the previous row.

First element = 1
Last element = 1
Middle element = previous[j - 1] + previous[j]

Time: O(n^2)
Space: O(n^2) including the output
"""