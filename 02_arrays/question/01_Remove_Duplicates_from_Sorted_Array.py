'''
The main pattern you should remember:
SORTED ARRAY
     ↓
DUPLICATES ARE ADJACENT
     ↓
TWO POINTERS
     ↓
slow = unique portion
fast = scanner
     ↓
new value?
     ↓
slow += 1
nums[slow] = nums[fast]
'''

# 26. Remove Duplicates from Sorted Array

'''
Link:
https://leetcode.com/problems/remove-duplicates-from-sorted-array/

Given a sorted array, remove duplicates in-place so that
each unique element appears only once.

Return the number of unique elements.
'''


'''
Input:
[1, 1, 1, 2, 2, 3, 3, 4, 4, 4]

Expected:
k = 4
nums = [1, 2, 3, 4, ...]
'''


'''
PATTERN:

Sorted array
     +
Remove duplicates
     +
In-place
     ↓
Two Pointers

Think:

slow → position of last unique element
fast → scans the array


IMPORTANT:

Because the array is sorted,
duplicates are always next to each other.

Example:

[1, 1, 1, 2, 2, 3, 3, 4, 4, 4]
 └───┘   └─┘   └─┘   └───┘
duplicates are adjacent
'''


def remove_duplicates(nums):
    if not nums:
        return 0

    slow = 0

    for fast in range(1, len(nums)):

        if nums[fast] != nums[slow]:
            slow += 1
            nums[slow] = nums[fast]

    return slow + 1


# Test case
nums = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4]

k = remove_duplicates(nums)

print("k =", k)
print("nums =", nums[:k])


'''
TWO POINTER TEMPLATE:

slow = 0

for fast in range(1, len(nums)):

    if nums[fast] != nums[slow]:
        slow += 1
        nums[slow] = nums[fast]

return slow + 1


KEY IDEA:

slow
 ↓
maintains the unique portion

fast
 ↓
scans the entire array


If:

nums[fast] == nums[slow]
    → duplicate
    → skip

nums[fast] != nums[slow]
    → new unique value
    → move slow
    → copy nums[fast]


Example:

[1, 1, 1, 2, 2, 3, 3, 4]
 ↑           ↑
slow        fast

new value found: 2

slow += 1
nums[slow] = nums[fast]


UNIQUE PORTION:

[1, 2, 3, 4]
 └────────┘
 first k elements


COMPLEXITY:

Time  : O(n)
Space : O(1)


RECOGNITION TRICKS:

1. Array is sorted
2. Duplicates are involved
3. Need to modify the array in-place
4. Need to preserve order
5. Need O(1) extra space

→ Think TWO POINTERS


IMPORTANT:

This exact technique works because
the array is SORTED.

For an unsorted array, this direct comparison
technique does not work.


RELATED PROBLEMS:

Remove Duplicates from Sorted Array
        ↓
Remove Duplicates from Sorted Array II
        ↓
Remove Element
        ↓
Move Zeroes
        ↓
Merge Sorted Array


INTERVIEW THINKING:

When you see:

"sorted array"
+
"remove duplicates"
+
"in-place"

Immediately think:

        TWO POINTERS
             ↓
       slow + fast
             ↓
        O(n) time
        O(1) space
'''

