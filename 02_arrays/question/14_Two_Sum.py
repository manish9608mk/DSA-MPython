# Two Sum

'''
Link:
https://leetcode.com/problems/two-sum/

Given an array of integers nums and an integer target,
return the indices of the two numbers such that they
add up to target.

You may not use the same element twice.

There is exactly one valid solution.

Example:

Input:
nums = [2,7,11,15]
target = 9

Output:
[0,1]

Because:

nums[0] + nums[1]
= 2 + 7
= 9
'''

'''
PATTERN:

Array
    +
Find TWO elements
    +
Their SUM must equal TARGET
    ↓
TWO SUM PATTERN
    ↓
HASH MAP / COMPLEMENT LOOKUP

For every number:

needed = target - current

Ask:

"Have I already seen the number I need?"

If yes:
    answer found

If no:
    store current number and its index.
'''

'''
APPROACH 1 — BRUTE FORCE:

Check every possible pair.

For every i:

    for every j after i:

        if nums[i] + nums[j] == target:
            return [i, j]

Example:

nums = [2,7,11,15]
target = 9

Check:

2 + 7 = 9
    ↓
return [0,1]

CODE:

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]

TIME:
O(n²)

SPACE:
O(1)

Why?

We may need to check almost every pair.
'''

'''
APPROACH 2 — BETTER:

We can use a hash map.

Instead of checking every pair, for each number
we calculate the number we need.

Example:

nums = [2,7,11,15]
target = 9

Current:

2

Needed:

9 - 2 = 7

Have we seen 7?

No.

Store:

2 → index 0


Next:

7

Needed:

9 - 7 = 2

Have we seen 2?

Yes.

2 is at index 0.

Current 7 is at index 1.

Answer:

[0,1]
'''

'''
WHY HASH MAP?

A hash map gives average O(1) lookup.

Instead of:

"Search the entire array for the number I need."

We ask:

"Have I already seen this number?"

The hash map answers this quickly.

Store:

number → index
'''

'''
IMPORTANT:

Check BEFORE storing the current number.

Example:

nums = [3,3]
target = 6

First 3:

needed = 6 - 3 = 3

3 is not in map.

Store:

3 → 0


Second 3:

needed = 6 - 3 = 3

3 IS in map.

Return:

[0,1]

This also ensures we don't use the same element twice.
'''

'''
OPTIMAL CODE:
'''

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {} # map

        for i, num in enumerate(nums):
            needed = target - num

            if needed in seen:
                return [seen[needed], i]

            seen[num] = i


'''
TEST CASE:

Input:

nums = [2,7,11,15]
target = 9
'''

nums = [2, 7, 11, 15]
target = 9

solution = Solution()
result = solution.twoSum(nums, target)

print("Result =", result)

'''
Output:

Result = [0, 1]
'''

'''
DRY RUN:

nums = [2,7,11,15]
target = 9

Initially:

seen = {}


i = 0
num = 2

needed = 9 - 2
needed = 7

Is 7 in seen?

No.

Store:

seen = {
    2: 0
}


i = 1
num = 7

needed = 9 - 7
needed = 2

Is 2 in seen?

YES.

seen[2] = 0
current index = 1

Return:

[0,1]
'''

'''
DRY RUN — DUPLICATE CASE:

nums = [3,3]
target = 6

Initially:

seen = {}


i = 0
num = 3

needed = 6 - 3
needed = 3

3 not in seen.

Store:

seen = {
    3: 0
}


i = 1
num = 3

needed = 3

3 is in seen.

Return:

[0,1]
'''

'''
WHY THE OPTIMAL APPROACH WORKS:

For every number x, there is only one number
that can complete the target:

needed = target - x

So instead of searching for every possible pair,
we remember numbers that we have already visited.

When we encounter x:

1. Calculate target - x.
2. Check whether that number was seen before.
3. If yes, we found the pair.
4. If no, store x and its index.

Because the hash map gives average O(1) lookup,
the complete algorithm takes O(n) time.
'''

'''
TIME & SPACE COMPLEXITY:

Time:
O(n)

We traverse the array once.

Hash map lookup:
O(1) average.

Space:
O(n)

In the worst case, we store almost every element
in the hash map.
'''

'''
INTERVIEW THINKING:

When you see:

"Find two numbers whose sum equals target"

Do NOT immediately think nested loops.

Ask:

What number do I need?

For current number:

needed = target - current

Then ask:

Have I seen needed before?

If yes → answer.

If no → store current.

This is the key Two Sum thought process.
'''

'''
INTERVIEW EXPLANATION:

"I'll use a hash map to store each number along
with its index.

For every current number, I calculate its complement:

target - current

Then I check whether that complement is already
in the hash map.

If it is, I return the stored index and the current
index. Otherwise, I store the current number and
continue.

This gives O(n) time and O(n) space."
'''

'''
RECOGNITION TRICKS:

Look for:

1. Array
2. Find TWO elements
3. Their sum/value must satisfy a TARGET
4. Need indices or elements
5. Fast lookup is useful

Think:

TWO SUM
   ↓
COMPLEMENT
   ↓
HASH MAP

The magic formula:

needed = target - current
'''

'''
COMMON INTERVIEW MISTAKES:

1. Using O(n²) immediately.

Nested loops work, but hash map gives O(n).


2. Storing before checking.

Prefer:

if needed in seen:
    return ...

seen[num] = i


3. Storing only the value.

We need indices, so store:

number → index


4. Sorting the array.

Sorting can destroy the original indices unless
we store them separately.

Hash map is simpler here.


5. Using the same element twice.

Checking before storing prevents this.

Example:

[3,3], target = 6

The first 3 is stored.

The second 3 finds the first one.

We never use one occurrence twice.
'''

'''
REUSABLE TEMPLATE:

seen = {}

for i, num in enumerate(nums):

    needed = target - num

    if needed in seen:
        return [seen[needed], i]

    seen[num] = i
'''

'''
GENERAL COMPLEMENT PATTERN:

The idea is bigger than Two Sum.

For a target relationship:

current + needed = target

Therefore:

needed = target - current

Then use a hash map/set to check whether
the needed value already exists.

This pattern appears in:

- Two Sum
- Four Sum variations
- Pair with given difference
- Subarray Sum
- Counting pair problems
- Frequency/complement problems
'''

'''
FAMILY:

This problem belongs to:

ARRAY
    ↓
HASHING
    ↓
COMPLEMENT LOOKUP
    ↓
TWO SUM

Related problems:

- 3Sum
- 4Sum
- Two Sum II
- Two Sum IV
- Subarray Sum Equals K
- Count Number of Pairs With Given Sum
'''

'''
ONE-LINE MEMORY:

For every number:

TARGET - CURRENT
       ↓
    NEEDED
       ↓
"Have I seen it?"
       ↓
YES → ANSWER
NO  → STORE CURRENT
'''

'''
FINAL PATTERN:

TWO NUMBERS
     +
TARGET
     ↓
COMPLEMENT
     ↓
HASH MAP
     ↓
O(n) TIME
O(n) SPACE
'''