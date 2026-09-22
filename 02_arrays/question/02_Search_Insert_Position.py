# 88. Merge Sorted Array

'''
Link:
https://leetcode.com/problems/merge-sorted-array/

You are given two sorted arrays nums1 and nums2.

Merge nums1 and nums2 into nums1 in sorted order.

nums1 has extra space at the end to store nums2.

The result must be stored inside nums1.
The function should not return anything.
'''

'''
PATTERN:

Two sorted arrays
    +
Merge
    +
In-place
    +
Extra space at the end
    ↓
Two Pointers from the BACK

Think:
"Where is the empty space?"
    ↓
At the end of nums1
    ↓
Start merging from the back
'''


def merge(nums1, m, nums2, n):
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

    # If nums2 still has elements,
    # copy them into nums1.
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1


# Test case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3

nums2 = [2, 5, 6]
n = 3

merge(nums1, m, nums2, n)

print(nums1)


'''
Output:

[1, 2, 2, 3, 5, 6]
'''


'''
TWO POINTERS TEMPLATE:

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


KEY IDEA:

Compare the largest remaining elements.

nums1[i] vs nums2[j]

Larger element
    → put it at nums1[k]
    → move that pointer backward

Then:

k -= 1


Why from the back?

nums1 has empty space at the end.

So we can place the largest elements there
without overwriting the useful elements of nums1.


Why only copy nums2 at the end?

If nums2 is finished:
    → remaining nums1 elements are already in place.

If nums1 is finished:
    → nums2 elements still need to be copied.


COMPLEXITY:

Time  : O(m + n)
Space : O(1)


RECOGNITION TRICKS:

1. Two arrays are sorted
2. Need to merge them
3. Result must be stored in nums1
4. nums1 has extra space at the end
5. Need O(1) extra space

→ Think TWO POINTERS

Special case:

Extra space at the end
    ↓
Merge from BACK


INTERVIEW THINKING:

Two sorted arrays
    ↓
Need to merge
    ↓
In-place
    ↓
Empty space at end
    ↓
Use 3 pointers
    ↓
i, j, k
    ↓
Compare from the back
    ↓
Put larger element at k
    ↓
O(m + n) time
O(1) space
'''


'''
And this becomes part of your Two Pointers family.

When you later see:

Remove Duplicates
Remove Element
Move Zeroes
Merge Sorted Array
Merge Two Sorted Lists
Container With Most Water
3Sum
Two Sum II

You should first ask:

Can I use two pointers?

For Merge Sorted Array specifically:

Two sorted arrays
        ↓
In-place
        ↓
Empty space at end
        ↓
BACKWARD TWO POINTERS
'''