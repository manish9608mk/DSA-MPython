# 118. Pascal's Triangle


from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result list
        triangle = []
        
        # Build each row
        for i in range(numRows):
            # Start each row with 1
            row = [1] * (i + 1)
            
            # Fill in the middle values
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
            
            # Add the row to the triangle
            triangle.append(row)
        
        return triangle

    
'''
PROBLEM

Given an integer `numRows`, return the first `numRows`
rows of Pascal's Triangle.

In Pascal's Triangle:

- First element of every row = 1.
- Last element of every row = 1.
- Every middle element is the sum of the two numbers
  directly above it.

Example:

numRows = 5

[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]

Important:

- Row `i` contains `i + 1` elements.
- The current row is built using the previous row.
- We need to return the complete triangle.
'''


'''
PATTERN

Array + Simulation + Previous Row Dependency

Pascal's Triangle
    ↓
Build row by row
    ↓
Current row depends on previous row
    ↓
First and last elements are 1
    ↓
Middle = two values above added together

Recognition:

Need to construct multiple levels / rows
    ↓
Current level depends on previous level
    ↓
Store previous levels
    ↓
Build current level

Core formula:

current[j] = previous[j-1] + previous[j]
'''


'''
APPROACH 1 — BRUTE FORCE

Calculate every element using the mathematical
combination formula:

C(n, r) = n! / (r! * (n-r)!)

For example, row 4:

C(4,0) = 1
C(4,1) = 4
C(4,2) = 6
C(4,3) = 4
C(4,4) = 1

So:

[1,4,6,4,1]

This works, but it is unnecessary because the problem
already gives us a direct relationship between adjacent
rows.

We would repeatedly calculate factorials / combinations
instead of using the previous row directly.

TIME:

O(numRows²) if combination values are computed efficiently.

With repeated factorial calculations, there is additional
unnecessary work.

SPACE:

O(numRows²) for the output.
'''


# BRUTE FORCE CODE

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for n in range(numRows):
            row = []

            for r in range(n + 1):
                value = 1

                for k in range(r):
                    value = value * (n - k) // (k + 1)

                row.append(value)

            triangle.append(row)

        return triangle


'''
This calculates every Pascal value independently.

It works, but we can directly use the actual definition
of Pascal's Triangle to make the solution much cleaner.
'''


'''
APPROACH 2 — BETTER APPROACH

Use the mathematical recurrence:

C(n, r) = C(n, r-1) * (n-r+1) / r

Instead of calculating factorials, generate each row from
the previous value in the same row.

For example, row 4:

Start with:

1

Next:

1 * 4 / 1 = 4

Next:

4 * 3 / 2 = 6

Next:

6 * 2 / 3 = 4

Next:

4 * 1 / 4 = 1

Result:

[1,4,6,4,1]

This avoids factorial calculations.

However, the problem itself tells us that every middle
value is the sum of the two values above it.

Therefore, using the previous row is more natural and
cleaner for this problem.

TIME:

O(numRows²)

SPACE:

O(numRows²) for the output.
'''


# BETTER CODE

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for n in range(numRows):
            row = [1]
            value = 1

            for r in range(1, n + 1):
                value = value * (n - r + 1) // r
                row.append(value)

            triangle.append(row)

        return triangle


'''
This is mathematically correct, but it does not use the
main structural property given by the problem.

So we prefer the previous-row approach.
'''


'''
APPROACH 3 — OPTIMAL / STANDARD

Build Pascal's Triangle row by row using the previous row.

For every row:

1. Create a row with `1`s.
2. Keep the first and last elements as `1`.
3. Calculate the middle elements using the previous row.
4. Add the completed row to the triangle.

Example:

Previous row:

[1,3,3,1]

Create current row:

[1,1,1,1,1]

Fill the middle:

1 + 3 = 4
3 + 3 = 6
3 + 1 = 4

Current row:

[1,4,6,4,1]

This directly follows the definition of Pascal's Triangle.


WHY PREVIOUS ROW?

Each number is defined by the two numbers directly above it.

Therefore:

triangle[i-1][j-1] → upper-left
triangle[i-1][j]   → upper-right

Add them:

row[j] = triangle[i-1][j-1] + triangle[i-1][j]
'''


'''
WHY ARRAY + SIMULATION?

The output itself is a triangle of arrays.

We need to construct:

row 0
    ↓
row 1
    ↓
row 2
    ↓
row 3
    ↓
...

And every row depends on the row immediately before it.

So the natural solution is:

Store previous row
    ↓
Build current row
    ↓
Store current row
    ↓
Repeat
'''


'''
STEP-BY-STEP THINKING

1. What do we need?

→ The first `numRows` rows.

2. How many elements does row `i` contain?

→ `i + 1`.

3. What do we know about every row?

→ First = 1
→ Last = 1

4. What about the middle?

→ Sum the two values from the previous row.

5. How do we get the previous row?

→ Store every completed row in `triangle`.

6. How do we initialize the current row?

→

row = [1] * (i + 1)

7. Which indexes need calculation?

→ Only the middle:

range(1, i)

8. How do we calculate the middle?

→

triangle[i-1][j-1] + triangle[i-1][j]

9. After completing the row?

→ Append it to `triangle`.

10. After all rows?

→ Return `triangle`.

Final thinking:

Build Row
    ↓
Fill Middle Using Previous Row
    ↓
Store Row
    ↓
Build Next Row
'''

# OPTIMAL CODE

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []

        for i in range(numRows):
            row = [1] * (i + 1)

            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            triangle.append(row)

        return triangle

# TEST CASE

numRows = 5

solution = Solution()

answer = solution.generate(numRows)

print("Input:", numRows)
print("Output:", answer)


'''
OUTPUT

Input: 5

Output:

[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

Every Pascal row follows the same rule.

The first and last values are always:

1

Every middle value is:

upper-left + upper-right

For example:

Previous row:

[1,3,3,1]

Current row:

[1,?, ?, ?,1]

Middle values:

1 + 3 = 4
3 + 3 = 6
3 + 1 = 4

So:

[1,4,6,4,1]

Because we repeat this exact process for every row,
each generated row is correct.

Therefore the complete triangle is correct.
'''


'''
DRY RUN

Input:

numRows = 5


STEP 1

i = 0

Create:

row = [1] * 1

row:

[1]

Append:

triangle = [
    [1]
]


STEP 2

i = 1

Create:

row = [1] * 2

row:

[1,1]

range(1,1) is empty.

Append:

triangle = [
    [1],
    [1,1]
]


STEP 3

i = 2

Create:

row = [1] * 3

row:

[1,1,1]

j = 1

Use previous row:

triangle[1] = [1,1]

Calculate:

triangle[1][0] + triangle[1][1]
= 1 + 1
= 2

row becomes:

[1,2,1]

Append:

triangle = [
    [1],
    [1,1],
    [1,2,1]
]


STEP 4

i = 3

Create:

[1,1,1,1]

j = 1

1 + 2 = 3

j = 2

2 + 1 = 3

row:

[1,3,3,1]

Append:

triangle = [
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1]
]


STEP 5

i = 4

Create:

[1,1,1,1,1]

j = 1

1 + 3 = 4

j = 2

3 + 3 = 6

j = 3

3 + 1 = 4

row:

[1,4,6,4,1]

Append.

FINAL:

[
    [1],
    [1,1],
    [1,2,1],
    [1,3,3,1],
    [1,4,6,4,1]
]
'''


'''
EDGE CASE 1 — numRows = 1

Input:

numRows = 1

Only one row exists:

[1]

Output:

[[1]]
'''


'''
EDGE CASE 2 — numRows = 2

Input:

numRows = 2

Rows:

[1]
[1,1]

Output:

[
    [1],
    [1,1]
]
'''


'''
EDGE CASE 3 — First / Last Elements

Every row must begin and end with `1`.

Example:

[1,4,6,4,1]

Do not calculate these boundary elements using
the previous row.

They are already known.
'''


'''
EDGE CASE 4 — Small Rows

For:

i = 0

There are no middle elements.

For:

i = 1

There are no middle elements.

For:

i >= 2

Middle elements exist.

The loop:

range(1, i)

handles this automatically.
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = numRows

TIME:

O(n²)

Why?

We generate:

1 + 2 + 3 + ... + n

elements.

The sum is:

n(n + 1) / 2

which is:

O(n²)


SPACE:

O(n²)

Why?

The returned triangle contains O(n²) numbers.

There is also a current row of O(n) size.

So:

Total space including output:

O(n²)

Extra working space excluding output:

O(n)

Final:

Time  = O(n²)
Space = O(n²) including output
'''


'''
INTERVIEW EXPLANATION

"I build Pascal's Triangle row by row.

For every row, I initialize all positions with `1` because
the first and last elements are always `1`.

Then I fill only the middle positions using the previous row.

For a middle position `j`, I use:

previous[j-1] + previous[j]

After completing the row, I append it to the result so it
can be used to build the next row.

The time complexity is O(n²) because we generate O(n²)
elements, and the space complexity is O(n²) because the
complete triangle is part of the output."
'''


'''
RECOGNITION TRICKS

1. "Each number is the sum of two numbers directly above."

→ Previous Row Dependency

2. "Return multiple rows / levels."

→ Build level by level

3. "First and last elements are fixed."

→ Initialize boundaries first

4. "Middle values depend on adjacent values from previous row."

→

previous[j-1] + previous[j]

Quick pattern:

Previous Row
    ↓
Adjacent Values
    ↓
Add
    ↓
Current Row
'''


'''
REUSABLE TEMPLATE

result = []

for i in range(num_rows):
    row = [1] * (i + 1)

    for j in range(1, i):
        row[j] = result[i - 1][j - 1] + result[i - 1][j]

    result.append(row)

Remember:

- `[1] * (i + 1)` → create row
- `range(1, i)` → only middle
- `result[i-1]` → previous row
- `j-1` and `j` → two values above
'''


'''
FAMILY

Pascal's Triangle
    ↓
Previous Row / Previous State
    ↓
Build Current Row

Related concepts:

- Array simulation
- Dynamic construction
- Previous-state dependency
- Level-by-level building

Main reusable idea:

Current state can be built directly from the
previous state.
'''


'''
COMMON INTERVIEW MISTAKES

1. Forgetting that row `i` has `i + 1` elements.

2. Using the wrong indexes.

Correct:

triangle[i-1][j-1] + triangle[i-1][j]

3. Modifying the first and last elements.

They must remain `1`.

4. Using:

range(1, i + 1)

This includes the last element.

Correct:

range(1, i)

5. Forgetting to append the completed row:

triangle.append(row)

6. Trying to use normal Binary Search / Two Pointers /
   Hashing.

This is simply a construction / simulation problem.

7. Overcomplicating the solution with factorials.

The previous-row relationship is simpler and more natural.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Pascal's Triangle is:

Create Row
    ↓
First = 1
    ↓
Last = 1
    ↓
Middle = Previous Left + Previous Right
    ↓
Store Row
    ↓
Repeat

Core formula:

row[j] = triangle[i-1][j-1] + triangle[i-1][j]

Core code:

for i in range(numRows):

    row = [1] * (i + 1)

    for j in range(1, i):
        row[j] = triangle[i-1][j-1] + triangle[i-1][j]

    triangle.append(row)

One-line mental model:

Previous Row
    ↓
Add Adjacent Values
    ↓
Build Current Row
    ↓
Repeat
'''