# 2965. Find Missing and Repeated Values


'''
Link:

https://leetcode.com/problems/find-missing-and-repeated-values/


Given an n x n grid containing integers.

The grid should contain every number from:

1 → n²

exactly once.

But:

- One number appears twice.
- One number is missing.

Return:

[repeated, missing]


Example:

Input:

[
    [1, 3],
    [2, 2]
]

Output:

[2, 4]

2 appears twice.

4 is missing.
'''


'''
PATTERN:

One number repeated
        +
One number missing
        ↓
XOR / BIT MANIPULATION

The grid should contain:

1 → n²

But one value is repeated and one value is missing.

If we XOR:

Expected values ^ Actual values

all normal values appear twice and cancel because:

x ^ x = 0

So only:

repeated ^ missing

remains.

To separate these two values:

repeated ^ missing
        ↓
Find a different bit
        ↓
Split numbers into two groups
        ↓
XOR each group

Final pattern:

XOR + RIGHTMOST SET BIT + GROUPING
'''


'''
APPROACH 1 — BRUTE FORCE:

For every number from:

1 → n²

scan the complete grid.

If a number appears twice:

repeated

If it appears zero times:

missing

There are n² possible values.

For every value we scan n² cells.

Therefore:

TIME: O(n⁴)
SPACE: O(1)

This is useful for understanding the problem,
but it is not efficient.
'''


'''
BRUTE FORCE CODE:

class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        N = n * n

        repeated = -1
        missing = -1

        for target in range(1, N + 1):
            count = 0

            for row in grid:
                for num in row:
                    if num == target:
                        count += 1

            if count == 2:
                repeated = target
            elif count == 0:
                missing = target

        return [repeated, missing]
'''


'''
APPROACH 2 — FREQUENCY ARRAY:

The values are always between:

1 → n²

So we can store the frequency of every value.

Example:

grid = [
    [1, 3],
    [2, 2]
]

Frequency:

1 → 1
2 → 2
3 → 1
4 → 0

Therefore:

count[2] == 2
        ↓
2 is repeated

count[4] == 0
        ↓
4 is missing

TIME: O(n²)
SPACE: O(n²)

This is much better than brute force,
but we can reduce space to O(1) using XOR.
'''


'''
FREQUENCY ARRAY CODE:

class Solution:
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        N = n * n

        count = [0] * (N + 1)

        for row in grid:
            for num in row:
                count[num] += 1

        repeated = -1
        missing = -1

        for num in range(1, N + 1):
            if count[num] == 2:
                repeated = num
            elif count[num] == 0:
                missing = num

        return [repeated, missing]
'''


'''
APPROACH 3 — OPTIMAL / XOR:

Goal:

TIME: O(n²)
SPACE: O(1)

First XOR:

1 → n²

Then XOR every value in the grid.

Because:

x ^ x = 0

all normal values cancel.

Only:

repeated ^ missing

remains.

Example:

Expected:

1, 2, 3, 4

Actual:

1, 3, 2, 2

XOR:

1 ^ 2 ^ 3 ^ 4 ^ 1 ^ 3 ^ 2 ^ 2

Normal values cancel:

1 ^ 1 = 0
3 ^ 3 = 0
2 ^ 2 = 0

Remaining:

4 ^ 2

Therefore:

xor_all = repeated ^ missing
'''


'''
HOW DO WE SEPARATE THE TWO VALUES?

Suppose:

repeated = 2
missing = 4

Binary:

2 = 010
4 = 100

XOR:

010
100
---
110

There is at least one bit where they are different.

We extract the rightmost set bit using:

mask = xor_all & -xor_all

For:

xor_all = 6

Binary:

6  = 0110
-6 = 1010

AND:

0110
1010
----
0010

Therefore:

mask = 2

This bit is different between 2 and 4.
'''


'''
GROUPING:

Use:

num & mask

If non-zero:

GROUP 1

Otherwise:

GROUP 2

The repeated and missing values must go
into different groups because the selected bit
is different between them.

Example:

mask = 2

Expected:

1 → Group 2
2 → Group 1
3 → Group 1
4 → Group 2

Actual:

1 → Group 2
3 → Group 1
2 → Group 1
2 → Group 1

Now XOR both groups.

Normal values cancel again.

Group 1 leaves:

2

Group 2 leaves:

4

So the two unknown values are:

2 and 4

Finally, check which one appears twice
in the grid.
'''


'''
STEP-BY-STEP THINKING:

1. What values should the grid contain?

   1 → n²

2. One value is repeated and one is missing.

3. Can XOR cancel all normal values?

   Yes.

4. XOR expected + actual values.

   Result:

   repeated ^ missing

5. Can this directly tell us both values?

   No.

6. How can we separate them?

   Find a bit where they are different.

7. How do we find that bit?

   mask = xor_all & -xor_all

8. Use the mask to divide values into two groups.

9. XOR expected and actual values in each group.

10. Normal values cancel.

11. The two groups leave the repeated and missing values.

12. Check which value occurs twice.

13. Return:

   [repeated, missing]
'''


'''
OPTIMAL CODE:
'''

class Solution:
    def findMissingAndRepeatedValues(self, grid: list[list[int]]) -> list[int]:
        n = len(grid)
        N = n * n

        xor_all = 0

        # XOR expected numbers
        for num in range(1, N + 1):
            xor_all ^= num

        # XOR actual numbers
        for row in grid:
            for num in row:
                xor_all ^= num

        # Find rightmost set bit
        mask = xor_all & -xor_all

        group1 = 0
        group2 = 0

        # Group expected numbers
        for num in range(1, N + 1):
            if num & mask:
                group1 ^= num
            else:
                group2 ^= num

        # Group actual numbers
        for row in grid:
            for num in row:
                if num & mask:
                    group1 ^= num
                else:
                    group2 ^= num

        # Find which value is repeated
        count = 0

        for row in grid:
            for num in row:
                if num == group1:
                    count += 1

        if count == 2:
            return [group1, group2]

        return [group2, group1]


# Test Case

grid = [
    [1, 3],
    [2, 2]
]

solution = Solution()
answer = solution.findMissingAndRepeatedValues(grid)

print("Input:", grid)
print("Output:", answer)


'''
Output:

Input: [[1, 3], [2, 2]]
Output: [2, 4]
'''


'''
WHY DOES THE XOR APPROACH WORK?

Let:

Repeated = R
Missing = M

Every correct number appears:

once in expected
+
once in actual

Therefore:

x ^ x = 0

All correct numbers disappear.

The repeated number appears:

once in expected
+
twice in actual

So one copy remains.

The missing number appears:

once in expected
+
zero times in actual

So it also remains.

Therefore:

xor_all = R ^ M

Since R and M are different, R ^ M has
at least one set bit.

That bit separates R and M into different groups.

After XORing both groups:

one group → R
one group → M

Finally, check which value appears twice.
'''


'''
DRY RUN:

Input:

grid = [
    [1, 3],
    [2, 2]
]

n = 2

N = n² = 4

Expected:

1, 2, 3, 4

Actual:

1, 3, 2, 2

XOR everything:

1 ^ 2 ^ 3 ^ 4 ^ 1 ^ 3 ^ 2 ^ 2

Cancel:

1 ^ 1 = 0
3 ^ 3 = 0
2 ^ 2 = 0

Remaining:

4 ^ 2

Therefore:

xor_all = 6

Find mask:

6 & -6 = 2

So:

mask = 2

Group values:

Expected:

1 → Group 2
2 → Group 1
3 → Group 1
4 → Group 2

Actual:

1 → Group 2
3 → Group 1
2 → Group 1
2 → Group 1

XOR Group 1:

2 ^ 3 ^ 3 ^ 2 ^ 2

= 2

Therefore:

group1 = 2

XOR Group 2:

1 ^ 4 ^ 1

= 4

Therefore:

group2 = 4

Now check the grid.

2 appears twice.

Therefore:

repeated = 2
missing = 4

Final answer:

[2, 4]
'''


'''
EDGE CASE 1:

Input:

[
    [1, 1],
    [3, 4]
]

Repeated = 1
Missing = 2

Output:

[1, 2]
'''


'''
EDGE CASE 2:

Input:

[
    [1, 2],
    [4, 4]
]

Repeated = 4
Missing = 3

Output:

[4, 3]
'''


'''
EDGE CASE 3:

Input:

[
    [1, 2],
    [3, 3]
]

Repeated = 3
Missing = 4

Output:

[3, 4]
'''


'''
TIME & SPACE COMPLEXITY:

We process the grid a constant number of times.

Grid contains n² elements.

Therefore:

TIME: O(n²)

Only a few variables are used.

Therefore:

SPACE: O(1)

The output array is not counted as extra
working space.
'''


'''
INTERVIEW EXPLANATION:

"I know the grid should contain every number from
1 to n², but one number is repeated and one is missing.

I'll XOR all expected numbers with all values in
the grid. Every correct number appears twice, so
those values cancel.

This leaves repeated ^ missing.

To separate them, I'll find the rightmost set bit
using xor_all & -xor_all.

I'll use that bit to divide expected and actual
values into two groups and XOR each group.

This gives the two unknown values separately.

Finally, I'll check which one occurs twice to
identify the repeated value.

The time complexity is O(n²) and the extra space
is O(1)."
'''


'''
RECOGNITION TRICKS:

When you see:

ONE MISSING
+
ONE REPEATED
+
KNOWN RANGE
+
O(1) EXTRA SPACE

Think:

XOR

The mental pattern:

Expected + Actual
        ↓
XOR
        ↓
Repeated ^ Missing
        ↓
Find different bit
        ↓
Split into groups
        ↓
XOR groups
        ↓
Get two values
        ↓
Check repeated
        ↓
[Repeated, Missing]
'''


'''
REUSABLE TEMPLATE:

xor_all = 0

# XOR expected values
for value in expected:
    xor_all ^= value

# XOR actual values
for value in actual:
    xor_all ^= value

# Find different bit
mask = xor_all & -xor_all

group1 = 0
group2 = 0

# Group expected values
for value in expected:
    if value & mask:
        group1 ^= value
    else:
        group2 ^= value

# Group actual values
for value in actual:
    if value & mask:
        group1 ^= value
    else:
        group2 ^= value

Now:

group1
group2

contain the two unknown values.

Finally determine which one is repeated.
'''


'''
FAMILY:

Missing Number
        ↓
Single Number
        ↓
Find Two Unique Numbers
        ↓
Missing + Repeated
        ↓
XOR / BIT MANIPULATION

Related ideas:

XOR cancellation
Rightmost set bit
Bit masking
Grouping by bits
'''


'''
COMMON INTERVIEW MISTAKES:

1. Forgetting that the grid is 2D.

   Use:

   for row in grid:
       for num in row:

2. Thinking XOR directly gives the repeated value.

   XOR gives:

   repeated ^ missing

3. Forgetting to find a different bit.

   Use:

   mask = xor_all & -xor_all

4. Confusing:

   ^

   with:

   &

   ^ → XOR
   & → AND

5. Not understanding:

   x & -x

   It extracts the rightmost set bit.

6. Forgetting to verify which value is repeated.

   Grouping gives the two values, but not
   which one is repeated.

7. Using a frequency array when O(1) extra
   space is required.

8. Trying to memorize the code without
   understanding the grouping idea.
'''


'''
MOST IMPORTANT THING TO REMEMBER:

Don't memorize the complete code.

Memorize this:

Missing + Repeated
        ↓
XOR expected + actual
        ↓
Repeated ^ Missing
        ↓
Find different bit
        ↓
mask = xor_all & -xor_all
        ↓
Split into two groups
        ↓
XOR each group
        ↓
Get two values
        ↓
Check which appears twice
        ↓
[Repeated, Missing]

When you see:

ONE MISSING
+
ONE REPEATED
+
O(1) SPACE

Think:

XOR
    ↓
DIFFERENT BIT
    ↓
GROUPING
    ↓
XOR AGAIN
'''