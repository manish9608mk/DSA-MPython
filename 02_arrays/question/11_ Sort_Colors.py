# 75. Sort Colors

'''
Link:
https://leetcode.com/problems/sort-colors/

Given an array containing only 0, 1, and 2,
sort the array in-place so that:

0s → first
1s → middle
2s → last

Do not use the library sorting function.
'''

'''
PATTERN:

Array
    +
Only 3 distinct values
    +
Need grouping
    +
In-place
    ↓
THREE-WAY PARTITIONING
    ↓
DUTCH NATIONAL FLAG

Think:

0 → goes LEFT
1 → stays in MIDDLE
2 → goes RIGHT
'''

'''
APPROACH 1 — COUNTING:

Count how many 0s, 1s, and 2s.

Then rewrite the array:

0 0 0 ... 1 1 1 ... 2 2 2

Example:

nums = [2, 0, 2, 1, 1, 0]

Count:
0 → 2
1 → 2
2 → 2

Rewrite:

[0, 0, 1, 1, 2, 2]

TIME:
O(n)

SPACE:
O(1)

This is valid, but it requires:
1. One pass to count
2. Another pass to rewrite

We can do it in one pass using three pointers.
'''

'''
APPROACH 2 — OPTIMAL:
DUTCH NATIONAL FLAG

Use three pointers:

low
mid
high

Meaning:

[0 ... low-1]       → all 0
[low ... mid-1]     → all 1
[mid ... high]      → UNKNOWN
[high+1 ... n-1]    → all 2

Initially:

low = 0
mid = 0
high = n - 1

The important part is the UNKNOWN region.

We process nums[mid].
'''

'''
CASE 1:

nums[mid] == 0

0 belongs on the LEFT.

Swap:

nums[low] ↔ nums[mid]

Then:

low += 1
mid += 1

Why increase both?

Because after the swap:
- 0 is correctly placed at low
- the element moved to mid is already known to be 1
  because everything before mid contains only 1s
'''

'''
CASE 2:

nums[mid] == 1

1 belongs in the MIDDLE.

It is already in the correct region.

So:

mid += 1
'''

'''
CASE 3:

nums[mid] == 2

2 belongs on the RIGHT.

Swap:

nums[mid] ↔ nums[high]

Then:

high -= 1

IMPORTANT:

Do NOT increase mid.

Why?

Because the element coming from nums[high]
has not been processed yet.

It could be:

0
1
2

So we must process nums[mid] again.
'''

'''
STEP-BY-STEP THINKING:

At every step ask:

What is nums[mid]?

0 → send LEFT
1 → keep in MIDDLE
2 → send RIGHT

This is the entire idea.

The three pointers simply maintain these regions:

0s | 1s | UNKNOWN | 2s
    ↑      ↑       ↑
   low    mid     high
'''

'''
OPTIMAL CODE:
'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1

            elif nums[mid] == 1:
                mid += 1

            else: # nums[mid] == 2
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1


'''
TEST CASE:

Input:
[2, 0, 2, 1, 1, 0]
'''

nums = [2, 0, 2, 1, 1, 0]

solution = Solution()
solution.sortColors(nums)

print("Result =", nums)

'''
Output:

Result = [0, 0, 1, 1, 2, 2]
'''

'''
DRY RUN:

nums = [2, 0, 2, 1, 1, 0]

Initial:

low = 0
mid = 0
high = 5

[2, 0, 2, 1, 1, 0]
 ↑              ↑
mid            high

nums[mid] = 2

Swap mid and high:

[0, 0, 2, 1, 1, 2]

high = 4
mid stays 0


Now nums[mid] = 0

Swap low and mid:

[0, 0, 2, 1, 1, 2]

low = 1
mid = 1


nums[mid] = 0

Swap low and mid:

[0, 0, 2, 1, 1, 2]

low = 2
mid = 2


nums[mid] = 2

Swap mid and high:

[0, 0, 1, 1, 2, 2]

high = 3
mid stays 2


nums[mid] = 1

mid = 3


nums[mid] = 1

mid = 4

Now:

mid > high

STOP.

Final:

[0, 0, 1, 1, 2, 2]
'''

'''
WHY THE OPTIMAL APPROACH WORKS:

We maintain four regions:

[0 ... low-1]
    → only 0s

[low ... mid-1]
    → only 1s

[mid ... high]
    → unknown

[high+1 ... n-1]
    → only 2s

Every operation makes the UNKNOWN region smaller.

If we see:

0 → move it to the 0 region
1 → move past it
2 → move it to the 2 region

Therefore, when mid crosses high,
there is no unknown element left.

The whole array is sorted.
'''

'''
TIME & SPACE COMPLEXITY:

Time:
O(n)

Why?

Each element is processed a constant number of times.

Space:
O(1)

Why?

Only three pointers are used.

The sorting is done in-place.
'''

'''
INTERVIEW THINKING:

If the interviewer gives:

"Array contains only 0, 1, and 2.
Sort it in-place.
Do not use sorting."

Do NOT immediately think:

"How do I sort?"

Instead ask:

1. How many distinct values?
   → Only 3

2. Do they have a natural order?
   → 0 < 1 < 2

3. Do I need in-place?
   → Yes

4. Can I divide the array into regions?
   → Yes

Therefore:

THREE-WAY PARTITIONING
    ↓
DUTCH NATIONAL FLAG
'''

'''
INTERVIEW EXPLANATION:

"I have only three possible values: 0, 1, and 2,
so instead of comparison-based sorting, I can partition
the array into three regions.

I use low, mid, and high.

0 goes to the left,
1 stays in the middle,
and 2 goes to the right.

When I encounter 2, I swap it with high,
but I don't increment mid because the element coming
from the right has not been processed yet.

This gives O(n) time and O(1) extra space."
'''

'''
RECOGNITION TRICKS:

Look for:

1. Only a few distinct values
   → 0, 1, 2

2. Need to group values
   → partitioning

3. In-place requirement
   → use pointers

4. No library sorting
   → think partitioning

5. Values have natural groups
   → left / middle / right

Common signal:

"Sort an array containing only 0, 1, and 2."

Immediately think:

DUTCH NATIONAL FLAG
'''

'''
IMPORTANT MISTAKE:

When nums[mid] == 2:

WRONG:

swap(mid, high)
high -= 1
mid += 1

Correct:

swap(mid, high)
high -= 1

Why?

Because the new nums[mid] is unknown.

We must inspect it again.
'''

'''
REUSABLE TEMPLATE:

low = 0
mid = 0
high = len(nums) - 1

while mid <= high:

    if nums[mid] == LEFT_VALUE:
        swap(low, mid)
        low += 1
        mid += 1

    elif nums[mid] == MIDDLE_VALUE:
        mid += 1

    else:
        swap(mid, high)
        high -= 1

The key idea:

LEFT_VALUE   → low
MIDDLE_VALUE  → mid
RIGHT_VALUE   → high
'''

'''
FAMILY:

This problem belongs to:

ARRAY
    ↓
PARTITIONING
    ↓
THREE-WAY PARTITION
    ↓
DUTCH NATIONAL FLAG

Related concepts:

- Quick Sort partitioning
- Two Pointers
- Three Pointers
- In-place rearrangement
- Partition around a value
'''

'''
ONE-LINE MEMORY:

0 → LEFT
1 → MIDDLE
2 → RIGHT

low → 0s
mid → unknown/current
high → 2s

If 2 comes:
SWAP + high--
DO NOT mid++

This is the key rule of Dutch National Flag.
'''