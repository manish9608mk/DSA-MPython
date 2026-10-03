# 53. Maximum Subarray

'''
Link:
https://leetcode.com/problems/maximum-subarray/

Given an integer array nums, find the subarray with the largest sum,
and return its sum.

A subarray must be CONTIGUOUS.

Example:

nums = [-2,1,-3,4,-1,2,1,-5,4]

Best subarray:

[4,-1,2,1]

Sum:

4 + (-1) + 2 + 1 = 6

Answer = 6
'''


'''
PATTERN:

ARRAY
    +
CONTIGUOUS SUBARRAY
    +
MAXIMUM SUM
    ↓
KADANE'S ALGORITHM


KEY QUESTION:

At every element:

Should I:

1. Extend the previous subarray

        OR

2. Start a new subarray from the current element?

    ↓

current_sum + num
        OR
num

Take the larger one.
'''


'''
APPROACH 1 — BRUTE FORCE:

Try every possible subarray.

For every starting index,
try every ending index and calculate the sum.

Example:

[-2]
[-2,1]
[-2,1,-3]
[-2,1,-3,4]
...

There are O(n²) possible subarrays.

If we calculate each sum separately,
the complexity can become O(n³).

'''


'''
APPROACH 2 — BETTER BRUTE FORCE:

Fix the starting position
and keep adding elements while moving right.

Example:

for i in range(n):

    current_sum = 0

    for j in range(i, n):

        current_sum += nums[j]

        max_sum = max(max_sum, current_sum)


We avoid recalculating the same subarray sum.

COMPLEXITY:

Time  : O(n²)
Space : O(1)


Why not preferred?

n can be 10^5.

O(n²) will be too slow.
'''


'''
APPROACH 3 — OPTIMAL / KADANE'S ALGORITHM:

At every element, ask:

Should I extend the previous subarray?

current_sum + num


OR:

Should I start a new subarray?

num


Take the larger:

current_sum = max(num, current_sum + num)


Then update the best answer:

max_sum = max(max_sum, current_sum)


KEY IDEA:

current_sum
    ↓
Maximum sum of a subarray
ending at the CURRENT position


max_sum
    ↓
Maximum sum found
ANYWHERE in the array.
'''


class Solution:

    def maxSubArray(self, nums: list[int]) -> int:

        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:

            current_sum = max(num, current_sum + num)

            max_sum = max(max_sum, current_sum)

        return max_sum


# Test case
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

solution = Solution()

result = solution.maxSubArray(nums)

print("Result =", result)


'''
Output:

Result = 6
'''


'''
WHY THE OPTIMAL APPROACH WORKS:

Suppose:

current_sum = -3
num = 5

Two choices:

Continue:

-3 + 5 = 2

Start new:

5

Since 5 is larger,
we discard the negative previous sum.

So:

current_sum = max(5, -3 + 5)
             = 5


IMPORTANT OBSERVATION:

A negative previous sum can only make
the future subarray sum smaller.

Therefore:

Negative contribution
        ↓
Hurts future sum
        ↓
Discard it
        ↓
Start a new subarray


This is the core idea of Kadane's Algorithm.
'''


'''
DRY RUN:

nums = [-2,1,-3,4,-1,2,1,-5,4]


Start:

current_sum = -2
max_sum = -2


num = 1

current_sum = max(1, -2 + 1)
             = 1

max_sum = 1


num = -3

current_sum = max(-3, 1 - 3)
             = -2

max_sum = 1


num = 4

current_sum = max(4, -2 + 4)
             = 4

max_sum = 4


num = -1

current_sum = max(-1, 4 - 1)
             = 3

max_sum = 4


num = 2

current_sum = max(2, 3 + 2)
             = 5

max_sum = 5


num = 1

current_sum = max(1, 5 + 1)
             = 6

max_sum = 6


num = -5

current_sum = max(-5, 6 - 5)
             = 1

max_sum = 6


num = 4

current_sum = max(4, 1 + 4)
             = 5

max_sum = 6


Final answer:

6


Best subarray:

[4,-1,2,1]
'''


'''
IMPORTANT EDGE CASE:

All elements can be negative.

Example:

nums = [-5,-2,-8]

Answer:

-2


Therefore, DON'T initialize:

current_sum = 0
max_sum = 0


Instead:

current_sum = nums[0]
max_sum = nums[0]


This allows the algorithm to correctly handle
arrays containing only negative numbers.
'''


'''
COMPLEXITY:

Time  : O(n)
Space : O(1)


Why?

We visit every element exactly once.

Only two variables are maintained:

current_sum
max_sum
'''


'''
INTERVIEW THINKING:

Array
    ↓
Contiguous subarray
    ↓
Maximum sum
    ↓
Think KADANE


At every element:

Extend previous subarray?
        OR
Start new subarray?


current_sum + num
        OR
num

        ↓

Take maximum
        ↓
Update max_sum
'''


'''
INTERVIEW EXPLANATION:

"I need the maximum sum of a contiguous subarray.

At each element, I have two choices:
either extend the previous subarray or start a new
subarray from the current element.

I choose the larger of these two options and keep
track of the maximum sum seen so far.

This is Kadane's Algorithm.

The time complexity is O(n) because I scan the array
once, and the space complexity is O(1) because I only
use a few variables."
'''


'''
RECOGNITION TRICKS:

1. Array is given
2. We need a CONTIGUOUS subarray
3. We need maximum/minimum SUM
4. We can extend the previous subarray
5. Or start a new subarray
6. Negative contribution can hurt future sum

→ Think:

KADANE'S ALGORITHM


KEY QUESTION:

"Should I extend the current subarray
or start a new one?"

If you see this decision,
think Kadane.
'''


'''
REUSABLE TEMPLATE:

current_sum = nums[0]
max_sum = nums[0]

for num in nums[1:]:

    current_sum = max(num, current_sum + num)

    max_sum = max(max_sum, current_sum)


GENERAL IDEA:

Current best
    +
Current element
    ↓
Should I continue?

OR

Start fresh from current element
    ↓
Take the better choice

Then:

Update global best.
'''


'''
KADANE FAMILY:

Maximum Subarray
Maximum subarray sum
Maximum/minimum contiguous sum
Largest sum contiguous segment
Problems where a negative prefix should be discarded


When you see:

CONTIGUOUS
    +
SUM
    +
MAXIMUM / MINIMUM

Ask:

"Can I decide whether to extend
or restart at every element?"

    ↓

KADANE'S ALGORITHM
'''


'''
FOLLOW-UP:

LeetCode also mentions a
DIVIDE AND CONQUER approach.

That approach is another way to solve
Maximum Subarray, but Kadane's Algorithm
is the standard O(n) solution.

Kadane:

Time  : O(n)
Space : O(1)
'''