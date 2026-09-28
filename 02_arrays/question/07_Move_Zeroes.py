# 283. Move Zeroes

'''
Link:
https://leetcode.com/problems/move-zeroes/

Given an integer array nums, move all 0's to the end
while maintaining the relative order of the non-zero elements.

Do this in-place without making a copy of the array.

Example:

nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
'''

'''
PATTERN:

Array
    +
Move elements
    +
Maintain relative order
    +
In-place
    ↓
Two Pointers

Think:
"Keep a position for the next non-zero element."

slow → position for next non-zero
fast → scans the array
'''


def move_zeroes(nums):
    slow = 0

    for fast in range(len(nums)):

        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1


# Test case
nums = [0, 1, 0, 3, 12]

move_zeroes(nums)

print("Result =", nums)


'''
Output:

Result = [1, 3, 12, 0, 0]
'''


'''
TWO POINTERS TEMPLATE:

slow = 0

for fast in range(len(nums)):

    if nums[fast] != 0:
        nums[slow], nums[fast] = nums[fast], nums[slow]
        slow += 1


KEY IDEA:

fast
    → scans every element

slow
    → position for the next non-zero element

If nums[fast] == 0:
    → do nothing

If nums[fast] != 0:
    → move it to nums[slow]
    → slow += 1


Why relative order stays same?

fast scans from left to right.

So non-zero elements are moved
in the same order they are found.


COMPLEXITY:

Time  : O(n)
Space : O(1)


RECOGNITION TRICKS:

1. Move elements in an array
2. Maintain relative order
3. Modify array in-place
4. No extra array
5. Need O(1) extra space

→ Think TWO POINTERS


INTERVIEW THINKING:

Need to move zeroes
    ↓
Non-zero order must stay same
    ↓
Keep position for next non-zero
    ↓
slow = position
fast = scanner
    ↓
Non-zero found
    → swap
    → slow += 1
    ↓
O(n) time
O(1) space
'''


'''
And this becomes part of your Two Pointers family.

When you later see:

Remove Duplicates from Sorted Array
Remove Element
Move Zeroes
Merge Sorted Array
Two Sum II
Container With Most Water
3Sum

Ask:

"Can I solve this by keeping two useful positions/pointers?"

For Move Zeroes:

Scan
    ↓
Find non-zero
    ↓
Place at slow
    ↓
Move slow
    ↓
TWO POINTERS
'''