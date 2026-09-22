"""
============================================================
88. MERGE SORTED ARRAY
============================================================

LeetCode:
https://leetcode.com/problems/merge-sorted-array/

------------------------------------------------------------
PROBLEM
------------------------------------------------------------

You are given two sorted arrays nums1 and nums2.

nums1 has enough extra space at the end to store nums2.

Merge both arrays into nums1 in sorted order.

The result must be stored inside nums1.
The function should not return anything.

Example:

nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6], n = 3

Output:

[1,2,2,3,5,6]


============================================================
PATTERN
============================================================

PATTERN: TWO POINTERS

Recognition:

Two sorted arrays
        +
Merge
        +
In-place
        +
Extra space at the end
        ↓
Two Pointers from BACK

Mental Trigger:

"Two sorted arrays + merge in-place + empty space at end"
→ Use 3 pointers from the back.

Pointers:

i → last real element of nums1
j → last element of nums2
k → last position of nums1


============================================================
SOLUTION
============================================================
"""

class Solution:

    def merge(self, nums1: list[int], m: int,
              nums2: list[int], n: int) -> None:

        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:

            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1

        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


"""
============================================================
VS CODE TEST
============================================================
"""

nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

solution = Solution()
solution.merge(nums1, m, nums2, n)

print(nums1)

# Output:
# [1, 2, 2, 3, 5, 6]


"""
============================================================
TWO POINTERS TEMPLATE
============================================================

i = m - 1
j = n - 1
k = m + n - 1

while i >= 0 and j >= 0:

    if nums1[i] > nums2[j]:
        nums1[k] = nums1[i]
        i -= 1
    else:
        nums1[k] = nums2[j]
        j -= 1

    k -= 1

while j >= 0:
    nums1[k] = nums2[j]
    j -= 1
    k -= 1


============================================================
KEY IDEA
============================================================

Compare the largest remaining elements.

nums1[i] vs nums2[j]

Put the larger element at nums1[k].

Then move that pointer backwards.

Why from the back?

nums1 already contains empty spaces at the end.

So we can safely put the largest elements there without
overwriting the useful elements of nums1.


============================================================
IMPORTANT
============================================================

We only need:

while j >= 0

We do NOT need:

while i >= 0

If nums2 is finished first, the remaining elements of nums1
are already in their correct positions.


============================================================
COMPLEXITY
============================================================

Time:
O(m + n)

Space:
O(1)


============================================================
RECOGNITION TRICKS
============================================================

Look for:

1. Two sorted arrays
2. Merge them
3. In-place modification
4. Extra space at the end
5. O(1) extra space

Think:

Sorted + Merge + In-place
        ↓
Two Pointers
        ↓
Start from BACK
        ↓
i, j, k


============================================================
RELATED PROBLEMS
============================================================

#26  Remove Duplicates from Sorted Array
#27  Remove Element
#80  Remove Duplicates from Sorted Array II
#283 Move Zeroes
#88  Merge Sorted Array


============================================================
INTERVIEW THINKING
============================================================

When you see:

"Merge two sorted arrays in-place and nums1 has empty
space at the end."

Think immediately:

Two sorted arrays
        ↓
Two Pointers
        ↓
Merge from BACK
        ↓
i = m - 1
j = n - 1
k = m + n - 1
        ↓
Compare nums1[i] and nums2[j]
        ↓
Put larger at nums1[k]
        ↓
Move pointer backwards
        ↓
O(m+n) time
O(1) space


FINAL MEMORY TRIGGER:

"Sorted + Merge + In-place + Empty space at END"
                    ↓
          BACKWARD TWO POINTERS
"""