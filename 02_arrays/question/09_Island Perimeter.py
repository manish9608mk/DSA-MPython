# 463. Island Perimeter

'''
Link:
https://leetcode.com/problems/island-perimeter/

Given a grid where:

1 = land
0 = water

Return the perimeter of the island.

A land cell has 4 sides.

A side contributes to the perimeter if:
    1. It touches water
    2. It is outside the grid
'''

'''
PATTERN:

Grid
    +
Check each land cell
    +
Check 4 neighbors
    +
Count exposed sides
    ↓
GRID TRAVERSAL

Think:

"For every land cell,
how many sides touch water or outside?"
'''


class Solution:

    def islandPerimeter(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        perimeter = 0

        directions = [
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1)    # right
        ]

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    continue

                for dr, dc in directions:

                    nr = r + dr
                    nc = c + dc

                    if nr < 0 or nr >= rows or nc < 0 or nc >= cols:
                        perimeter += 1

                    elif grid[nr][nc] == 0:
                        perimeter += 1

        return perimeter


# Test case
grid = [
    [0, 1, 0, 0],
    [1, 1, 1, 0],
    [0, 1, 0, 0],
    [1, 1, 0, 0]
]

solution = Solution()

result = solution.islandPerimeter(grid)

print("Perimeter =", result)


'''
Output:

Perimeter = 16
'''


'''
GRID TRAVERSAL TEMPLATE:

directions = [
    (-1, 0),  # up
    (1, 0),   # down
    (0, -1),  # left
    (0, 1)    # right
]

for r in range(rows):
    for c in range(cols):

        for dr, dc in directions:

            nr = r + dr
            nc = c + dc

            # check neighbor


KEY IDEA:

Land cell
    ↓
Check 4 sides
    ↓
Water or outside
    → perimeter += 1

Another land cell
    → shared side
    → do nothing


COMPLEXITY:

Time  : O(rows × cols)
Space : O(1)


RECOGNITION TRICKS:

1. Grid problem
2. Need to inspect cells
3. Need up/down/left/right neighbors
4. Counting boundaries or exposed sides
5. No need to find a connected component

→ Think GRID TRAVERSAL


INTERVIEW THINKING:

Need island perimeter
    ↓
Each land cell has 4 sides
    ↓
Check each side
    ↓
Water/outside → +1
    ↓
Land → +0
    ↓
Scan entire grid
    ↓
O(rows × cols)
'''


'''
And this becomes part of your Grid / Matrix family.

When you later see:

Island Perimeter
Number of Islands
Flood Fill
Max Area of Island
Rotting Oranges
Surrounded Regions
Pacific Atlantic Water Flow
Word Search

First ask:

"Do I need to inspect neighbors?"

    ↓
UP / DOWN / LEFT / RIGHT

Then decide:

Boundary counting
    → Grid Traversal

Connected component
    → DFS / BFS

Shortest path
    → BFS

Backtracking through cells
    → Backtracking
'''



class Solution:

    def islandPerimeter(self, grid: list[list[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 0:
                    continue

                # Up
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # Down
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1

                # Left
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1

                # Right
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

        return perimeter

