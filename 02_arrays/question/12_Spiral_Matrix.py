# 54. Spiral Matrix

'''
Link:
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix
in spiral order.

Example:

Input:
[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

Output:
[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

'''
PATTERN:

Matrix
    +
Need spiral order
    ↓
BOUNDARY TRAVERSAL

Use 4 boundaries:

top
bottom
left
right

Traversal:

TOP    → left to right
RIGHT  → top to bottom
BOTTOM → right to left
LEFT   → bottom to top

Then shrink the boundaries and repeat.
'''

'''
APPROACH 1 — BRUTE FORCE:

Use a visited matrix.

Start from the first cell and move:

RIGHT → DOWN → LEFT → UP

Whenever we reach:
- a boundary
- or an already visited cell

change direction.

Example:

→ → →
      ↓
      ↓
← ← ←
↑
↑

This works, but requires an extra visited matrix.

TIME:
O(m × n)

SPACE:
O(m × n)
'''

'''
APPROACH 2 — OPTIMAL:

Use four boundaries:

top = 0
bottom = rows - 1
left = 0
right = cols - 1

For every layer:

1. Traverse TOP: left → right
2. Traverse RIGHT: top → bottom
3. Traverse BOTTOM: right → left
4. Traverse LEFT: bottom → top

Then shrink:

top += 1
right -= 1
bottom -= 1
left += 1

Repeat until no unprocessed cells remain.
'''

'''
IMPORTANT:

After traversing the top row:

top += 1

After traversing the right column:

right -= 1

Before traversing the bottom row:

if top <= bottom:

Before traversing the left column:

if left <= right:

These checks prevent visiting the same element twice
when the matrix has only one row or one column.
'''

'''
STEP-BY-STEP THINKING:

For every layer ask:

1. What is the TOP boundary?
2. What is the RIGHT boundary?
3. What is the BOTTOM boundary?
4. What is the LEFT boundary?

Then:

TOP:
left → right

RIGHT:
top → bottom

BOTTOM:
right → left

LEFT:
bottom → top

Finally shrink all four boundaries.
'''

'''
OPTIMAL CODE:
'''

class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        result = []

        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1

        while top <= bottom and left <= right:

            # Top row: left → right
            for col in range(left, right + 1):
                result.append(matrix[top][col])
            top += 1

            # Right column: top → bottom
            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            # Bottom row: right → left
            if top <= bottom:
                for col in range(right, left - 1, -1):
                    result.append(matrix[bottom][col])
                bottom -= 1

            # Left column: bottom → top
            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result


'''
TEST CASE:

Input:

[
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
'''

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

solution = Solution()
result = solution.spiralOrder(matrix)

print("Result =", result)

'''
Output:

Result = [1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

'''
DRY RUN:

Matrix:

1 2 3
4 5 6
7 8 9

Initial:

top = 0
bottom = 2
left = 0
right = 2


1. TOP:

1 → 2 → 3

Result:

[1, 2, 3]

top = 1


2. RIGHT:

6
↓
9

Result:

[1, 2, 3, 6, 9]

right = 1


3. BOTTOM:

8 ← 7

Result:

[1, 2, 3, 6, 9, 8, 7]

bottom = 1


4. LEFT:

4
↑

Result:

[1, 2, 3, 6, 9, 8, 7, 4]

left = 1


Remaining:

5

TOP:

5

Final:

[1, 2, 3, 6, 9, 8, 7, 4, 5]
'''

'''
EXAMPLE 2:

Input:

[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

First outer layer:

1 → 2 → 3 → 4
              ↓
              8
              ↓
              12
← 11 ← 10 ← 9
↑
5

Result:

[1, 2, 3, 4, 8, 12, 11, 10, 9, 5]

Remaining:

6 7

Then:

6 → 7

Final:

[1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
'''

'''
WHY THE OPTIMAL APPROACH WORKS:

The four boundaries represent the unprocessed part
of the matrix.

Initially:

┌───────────────┐
│   UNPROCESSED │
│   UNPROCESSED │
│   UNPROCESSED │
└───────────────┘

After processing one layer:

top += 1
right -= 1
bottom -= 1
left += 1

So the remaining matrix becomes smaller.

Every element is processed exactly once.

When:

top > bottom
or
left > right

there are no elements left to process.
'''

'''
TIME & SPACE COMPLEXITY:

Time:
O(m × n)

Every matrix element is visited exactly once.

Extra Space:
O(1)

Only four boundary variables are used.

Output Space:
O(m × n)

Because the answer itself contains all matrix elements.
'''

'''
INTERVIEW THINKING:

When you see:

"Return matrix elements in spiral order"

Do not think about individual cells first.

Think about the OUTER LAYER.

Ask:

Can I describe the current unprocessed matrix
using four boundaries?

Yes:

top
bottom
left
right

Then process:

TOP → RIGHT → BOTTOM → LEFT

Then shrink the boundaries.

This is the main idea.
'''

'''
INTERVIEW EXPLANATION:

"I will process the matrix layer by layer using four
boundaries: top, bottom, left, and right.

For each layer, I traverse the top row from left to right,
the right column from top to bottom, the bottom row from
right to left, and the left column from bottom to top.

After each traversal I shrink the corresponding boundary.

I use checks before traversing the bottom row and left
column so that single-row or single-column matrices do not
cause duplicate elements.

This gives O(m × n) time and O(1) extra space."
'''

'''
RECOGNITION TRICKS:

If you see:

- Matrix
- Spiral order
- Clockwise traversal
- Outer layer → inner layer
- Boundary traversal

Think:

FOUR BOUNDARIES

top
bottom
left
right

Then:

TOP → RIGHT → BOTTOM → LEFT
        ↓
SHRINK BOUNDARIES
        ↓
REPEAT
'''

'''
COMMON INTERVIEW MISTAKES:

1. Forgetting to update boundaries.

Correct:

top += 1
right -= 1
bottom -= 1
left += 1


2. Traversing the bottom row without checking:

if top <= bottom:


3. Traversing the left column without checking:

if left <= right:


4. Mixing up directions.

Correct order:

TOP:
left → right

RIGHT:
top → bottom

BOTTOM:
right → left

LEFT:
bottom → top


5. Using a visited matrix when it is not necessary.

The boundary approach is cleaner and uses O(1)
extra working space.
'''

'''
REUSABLE TEMPLATE:

top = 0
bottom = rows - 1
left = 0
right = cols - 1

while top <= bottom and left <= right:

    # TOP
    left → right
    top += 1

    # RIGHT
    top → bottom
    right -= 1

    # BOTTOM
    if top <= bottom:
        right → left
        bottom -= 1

    # LEFT
    if left <= right:
        bottom → top
        left += 1
'''

'''
FAMILY:

This problem belongs to:

MATRIX
    ↓
MATRIX TRAVERSAL
    ↓
BOUNDARY TRAVERSAL
    ↓
SPIRAL TRAVERSAL

Related problems:

- Spiral Matrix II
- Spiral Matrix III
- Generate Matrix in Spiral Order
- Matrix Layer Traversal
- Rotate Image
- Boundary Traversal
'''

'''
ONE-LINE MEMORY:

TOP → RIGHT → BOTTOM → LEFT
        ↓
SHRINK ALL 4 BOUNDARIES
        ↓
REPEAT

Mental picture:

        TOP →
    ┌─────────┐
    │         ↓
LEFT↑         RIGHT
    │         ↓
    └─────────┘
      ← BOTTOM

or,

Real-World Analogy
Imagine walking around the boundary of a rectangular room:

→ → →
      ↓
      ↓
← ← ←
↑
↑

After completing the outer boundary, you enter the smaller rectangle inside and repeat.
'''

'''
FINAL PATTERN:

MATRIX
   ↓
FOUR BOUNDARIES
   ↓
TOP → RIGHT → BOTTOM → LEFT
   ↓
SHRINK
   ↓
REPEAT
'''