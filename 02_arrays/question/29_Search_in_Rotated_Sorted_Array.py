
# 33. SEARCH IN ROTATED SORTED ARRAY

"""
PROBLEM

Given an ascending sorted array that may have been rotated,
find the index of target.

Return the index if target exists; otherwise, return -1.

Example:
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
Output = 4

Important:
- All values are distinct.
- The array was originally sorted in ascending order.
- The array may be rotated.
- Required time complexity: O(log n).
"""

"""
PATTERN

Sorted Array + Search + O(log n)
→ Modified Binary Search

The entire rotated array is not necessarily sorted.
However, at least one half of the current search range is sorted.

Main idea:
1. Find mid.
2. Check whether nums[mid] == target.
3. Identify the sorted half.
4. Check whether target belongs to that half.
5. Discard the impossible half.

Recognition:
Rotated Sorted Array → Modified Binary Search
"""

"""
APPROACH 1 — BRUTE FORCE

Scan every element.

If nums[i] == target, return i.
If target is not found, return -1.

TIME: O(n)
SPACE: O(1)

This works, but does not satisfy the required O(log n) time.
"""

# BRUTE FORCE CODE

def search_brute_force(nums: list[int], target: int) -> int:
    for i, num in enumerate(nums):
        if num == target:
            return i
    return -1


"""
APPROACH 2 — FIND PIVOT + BINARY SEARCH

First find the index of the smallest element.
This index is the rotation point.

The pivot divides the array into two sorted sections.
Choose the section that can contain target, then apply
normal binary search.

TIME: O(log n)
SPACE: O(1)

This works, but needs a separate pivot search.
Modified binary search can solve the problem in one loop.
"""

# PIVOT APPROACH CODE

def search_using_pivot(nums: list[int], target: int) -> int:
    n = len(nums)
    left, right = 0, n - 1

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid

    pivot = left

    left, right = 0, n - 1

    if nums[pivot] <= target <= nums[n - 1]:
        left = pivot
    else:
        right = pivot - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


"""
APPROACH 3 — OPTIMAL / MODIFIED BINARY SEARCH

Maintain:
left  = beginning of the search range
right = end of the search range
mid   = middle index

First check whether nums[mid] == target.

CASE 1: LEFT HALF IS SORTED

Condition:
nums[left] <= nums[mid]

Target belongs to the left half if:
nums[left] <= target < nums[mid]

If true:
    right = mid - 1
Otherwise:
    left = mid + 1

CASE 2: RIGHT HALF IS SORTED

If the left half is not sorted, the right half is sorted.

Target belongs to the right half if:
nums[mid] < target <= nums[right]

If true:
    left = mid + 1
Otherwise:
    right = mid - 1
"""

"""
WHY MODIFIED BINARY SEARCH?

Example:
[4, 5, 6, 7, 0, 1, 2]

The rotation breaks the complete sorted order.
But at least one half of the current range remains sorted.

Use that sorted half to determine whether target can be inside it.

If target belongs there, search that half.
Otherwise, discard it and search the other half.

This reduces the search range by approximately half each iteration.
"""

"""
STEP-BY-STEP THINKING

1. What is being asked?
   → Return target's index or -1.

2. What complexity is required?
   → O(log n), so use binary search.

3. Why not normal binary search?
   → The complete array may not be sorted.

4. What property can we use?
   → At least one half is sorted.

5. How do we identify a sorted left half?
   → nums[left] <= nums[mid].

6. How do we check target in the left half?
   → nums[left] <= target < nums[mid].

7. If target is not in the left half?
   → Search the right half.

8. If the left half is not sorted?
   → The right half is sorted.

9. How do we check target in the right half?
   → nums[mid] < target <= nums[right].

10. What if target equals nums[mid]?
    → Return mid.

11. What if the range becomes empty?
    → Return -1.
"""

# OPTIMAL CODE

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # Left half is sorted.
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted.
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1


"""
TEST CASE

The following code runs independently in Python 3.
"""

solution = Solution()

print(solution.search([4, 5, 6, 7, 0, 1, 2], 0))
print(solution.search([4, 5, 6, 7, 0, 1, 2], 3))
print(solution.search([1], 0))
print(solution.search([1, 2, 3, 4, 5], 4))


"""
OUTPUT

4
-1
-1
3
"""

"""
WHY DOES THE OPTIMAL APPROACH WORK?

If the left half is sorted:
- Its values lie between nums[left] and nums[mid].
- If target lies in that range, search the left half.
- Otherwise, target cannot be in that half.

If the left half is not sorted:
- The right half must be sorted.
- If target lies between nums[mid] and nums[right],
  search the right half.
- Otherwise, discard the right half.

Because all values are distinct, the sorted-half check is unambiguous.

Each iteration removes about half of the remaining candidates.
If target exists, the search eventually reaches it.
If the range becomes empty, target does not exist.

Therefore, the algorithm returns the correct index or -1.
"""

"""
DRY RUN

nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

STEP 1

left = 0
right = 6
mid = (0 + 6) // 2 = 3

nums[mid] = 7

Target is not found.

Check:
nums[left] <= nums[mid]
4 <= 7 → True

Left half [4, 5, 6, 7] is sorted.

Check:
nums[left] <= target < nums[mid]
4 <= 0 < 7 → False

Target cannot be in the left half.

Update:
left = mid + 1 = 4

STEP 2

left = 4
right = 6
mid = (4 + 6) // 2 = 5

nums[mid] = 1

Target is not found.

Check:
nums[left] <= nums[mid]
0 <= 1 → True

Left half [0, 1] is sorted.

Check:
0 <= target < 1
0 <= 0 < 1 → True

Target can be in the left half.

Update:
right = mid - 1 = 4

STEP 3

left = 4
right = 4
mid = (4 + 4) // 2 = 4

nums[mid] = 0

Target found.

Return 4.
"""

"""
EDGE CASE 1 — TARGET AT MID

nums = [4, 5, 6, 7, 0, 1, 2]
target = 7

The first mid index is 3.
nums[3] == 7.

Answer: 3
"""

"""
EDGE CASE 2 — TARGET DOES NOT EXIST

nums = [4, 5, 6, 7, 0, 1, 2]
target = 3

The algorithm discards impossible halves.
Eventually left > right.

Answer: -1
"""

"""
EDGE CASE 3 — SINGLE ELEMENT

nums = [1]
target = 0

left = 0, right = 0, mid = 0.
nums[mid] != target.

The search range becomes empty.

Answer: -1

If target = 1, the answer is 0.
"""

"""
EDGE CASE 4 — ARRAY NOT ROTATED

nums = [1, 2, 3, 4, 5]
target = 4

The same algorithm works on a normally sorted array.

Answer: 3
"""

"""
TIME & SPACE COMPLEXITY

Brute Force:
Time: O(n)
Space: O(1)

Pivot + Binary Search:
Time: O(log n)
Space: O(1)

Optimal Modified Binary Search:
Time: O(log n)
Space: O(1)

Why O(log n)?
Each iteration removes approximately half of the search range.

Why O(1) space?
Only left, right, and mid are used.
No additional array or recursion is needed.
"""

"""
INTERVIEW EXPLANATION

"I will use modified binary search because the required time
complexity is O(log n).

Although the array is rotated, at least one half of the current
range is always sorted.

After checking the middle element, I identify the sorted half
and check whether the target lies within its value range.
I discard the half that cannot contain the target and continue.

If I find the target, I return its index.
If the search range becomes empty, I return -1.

The time complexity is O(log n), and extra space is O(1)."
"""

"""
RECOGNITION TRICKS

1. Sorted array + search + O(log n)
   → Binary Search

2. Sorted array rotated at an unknown index
   → Modified Binary Search

3. nums[left] <= nums[mid]
   → Left half is sorted

4. nums[left] <= target < nums[mid]
   → Target can be in the sorted left half

5. Left half is not sorted
   → Right half is sorted

6. nums[mid] < target <= nums[right]
   → Target can be in the sorted right half

Mental pattern:

Find mid
→ Identify sorted half
→ Check target range
→ Discard impossible half
→ Repeat
"""

"""
REUSABLE TEMPLATE

left, right = 0, len(nums) - 1

while left <= right:
    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[left] <= nums[mid]:
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1
    else:
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

return -1

This template assumes all values are distinct.
Duplicates require additional handling.
"""

"""
FAMILY

Binary Search
    ↓
Modified Binary Search
    ↓
Search in Rotated Sorted Array

Related problems:
- Search in Rotated Sorted Array II
- Find Minimum in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array II
- Search a 2D Matrix
- Find Peak Element
- Binary Search
"""

"""
COMMON INTERVIEW MISTAKES

1. Assuming the entire rotated array is sorted.
   → Only one half is guaranteed to be sorted.

2. Forgetting to check nums[mid] == target first.

3. Using incorrect range boundaries.
   → Left: nums[left] <= target < nums[mid]
   → Right: nums[mid] < target <= nums[right]

4. Updating left = mid or right = mid.
   → This can cause an infinite loop.
   → Use mid + 1 or mid - 1.

5. Using while left < right with this exact implementation.
   → Use while left <= right to check a one-element range.

6. Returning nums[mid] instead of mid.
   → The problem asks for the index.

7. Forgetting to return -1 when target is absent.

8. Claiming O(n) time for the optimal approach.
   → The search range is halved each iteration.

9. Applying this exact logic to duplicate values without changes.
   → This problem guarantees distinct values.
"""

"""
MOST IMPORTANT THING TO REMEMBER

Rotated Sorted Array
→ Modified Binary Search
→ At least one half is sorted
→ Check whether target belongs to that half
→ Discard the impossible half
→ Repeat

Time: O(log n)
Space: O(1)

Remember these two checks:

nums[left] <= target < nums[mid]

nums[mid] < target <= nums[right]

First identify the sorted half.
Then decide which half to keep.
"""
