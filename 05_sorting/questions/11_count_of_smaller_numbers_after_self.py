"""
315. COUNT OF SMALLER NUMBERS AFTER SELF
LeetCode: https://leetcode.com/problems/count-of-smaller-numbers-after-self/

PROBLEM
For every nums[i], count the smaller values to its right.

Example: [5,2,6,1] -> [2,1,1,0]

PATTERN
Merge Sort + Original Index Tracking

APPROACH 1 — BRUTE FORCE
For every index, scan its suffix. O(n^2) time, O(n) output.

APPROACH 2 — MODIFIED MERGE SORT
Sort original indices by their values. During merge, every right-half
index moved before a left-half index is smaller and lies to its right.
When placing a left index, add the number of right elements already
moved (j-mid). Equal values must choose the left side first.

DRY RUN
[5,2,6,1]
5 has smaller right values 2 and 1 -> 2.
2 has smaller right value 1 -> 1.
6 has smaller right value 1 -> 1.
1 has none -> 0.

EDGE CASES
- Empty, one element; increasing/decreasing arrays; duplicates; negatives.

COMPLEXITY
O(n log n) time, O(n) extra space.

INTERVIEW EXPLANATION
"I attach each value to its original index and merge-sort the indices.
When a right-side value moves before a left-side value, it contributes
to that left value's count. I store the count at the original index."

COMMON MISTAKES
- Losing original indices.
- Counting equal values as smaller.
- Writing the count at the sorted rather than original position.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The original index matters. Sort indices by their values during Merge Sort, and count how many smaller right-half elements pass each left-half index.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE
For each index i, scan j=i+1..n-1 and count nums[j] < nums[i]. Time O(n²), extra output O(n).

APPROACH 2 — SORTED LIST + BINARY SEARCH
Scan right to left, binary-search the insertion point in a sorted list. The insertion itself shifts O(n) values in a Python list, so the overall worst case remains O(n²).

APPROACH 3 — INDEX MERGE SORT (OPTIMAL)
Sort an index array rather than the values. During merge, if nums[right_index] is smaller than nums[left_index], move it first. When placing a left index, every right-half element already moved is smaller and originally to its right. Add j-mid to result[original_index]. On equality, take the left side first because equal is not smaller. Time O(n log n), space O(n).


WHY THE RECOMMENDED APPROACH WORKS

When an index range is split into left and right halves, every original position in the left half precedes every position in the right half. If a right-half item is moved before a left-half item in ascending merge, it is a smaller value to the right of that left item. At the moment a left index is written, j-mid right-side indices have passed it. Each pair is counted at the recursion level where its indices first lie in separate halves.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[5,2,6,1]
index 0, value 5: smaller to right are 2 and 1 -> 2
index 1, value 2: smaller to right is 1 -> 1
index 2, value 6: smaller to right is 1 -> 1
index 3, value 1: none -> 0
Output=[2,1,1,0].

When merging left value 5 with right sorted [1,2], both right items move before 5. When 5 is finally placed, j-mid=2, so result[0] increases by 2. Equal values use the left-first branch and contribute zero.


EDGE CASES TO TEST

- Empty array -> [].
- Single element -> [0].
- Strictly increasing values -> all zero.
- Strictly decreasing values -> [n-1,n-2,...,0].
- Equal values must not count one another.
- Negative values.


COMMON INTERVIEW MISTAKES

1. Sorting values without original indices.
2. Counting equal elements; use <= to take left first.
3. Adding the count at sorted position instead of original index.
4. Counting every merged item instead of only right-half items that passed.
5. Using Python list insertion and assuming it is O(log n).


REUSABLE PATTERN TEMPLATE

indices = list(range(n))
counts = [0]*n
# During merge of [left,mid) and [mid,right):
if nums[indices[i]] <= nums[indices[j]]:
    counts[indices[i]] += j-mid
    take_left()
else:
    take_right()


COMPLEXITY ANALYSIS

Brute force O(n²). Index Merge Sort O(n log n) time with O(n) temporary index storage and answer array; total auxiliary space O(n).


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I preserve original positions by merge-sorting indices rather than values. During a merge, whenever a right-half value is smaller, I move it first. When I place a left index, the number of right-half elements already moved is exactly how many smaller values occur to its right. I add that number at the original index. Equal values are not counted, so I take the left side first on equality. This is O(n log n)."


PATTERN MEMORY

The original index matters. Sort indices by their values during Merge Sort, and count how many smaller right-half elements pass each left-half index.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why indices must be tracked.
[ ] Explain right-before-left counting.
[ ] Use <= for equality.
[ ] Store counts by original index.
[ ] Dry-run [5,2,6,1].
[ ] State O(n log n) time and O(n) extra space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Merge Sort with index tracking is the best sorting interview answer because it demonstrates how counting can be embedded in merge. Fenwick Tree + coordinate compression is a second O(n log n) solution and is useful for explaining order-statistics/prefix queries.

ADDITIONAL IMPLEMENTATION: Fenwick Tree processes values from right to left. The query gives the number of already-seen values strictly smaller than the current one; coordinate compression maps arbitrary values to ranks.

"""

def count_smaller_brute(nums: list[int]) -> list[int]:
    return [sum(candidate < value for candidate in nums[i + 1:])
            for i, value in enumerate(nums)]


def count_smaller_merge_sort(nums: list[int]) -> list[int]:
    n = len(nums)
    counts = [0] * n
    indices = list(range(n))
    temp = [0] * n

    def sort(left: int, right: int) -> None:
        if right - left <= 1:
            return
        mid = (left + right) // 2
        sort(left, mid)
        sort(mid, right)
        i, j, write = left, mid, left

        while i < mid and j < right:
            if nums[indices[i]] <= nums[indices[j]]:
                counts[indices[i]] += j - mid
                temp[write] = indices[i]
                i += 1
            else:
                temp[write] = indices[j]
                j += 1
            write += 1

        while i < mid:
            counts[indices[i]] += j - mid
            temp[write] = indices[i]
            i += 1
            write += 1
        while j < right:
            temp[write] = indices[j]
            j += 1
            write += 1
        indices[left:right] = temp[left:right]

    sort(0, n)
    return counts


class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        return count_smaller_merge_sort(nums)


def run_tests() -> None:
    cases = [([5,2,6,1], [2,1,1,0]), ([-1], [0]), ([-1,-1], [0,0]),
             ([5,4,3,2,1], [4,3,2,1,0]), ([1,2,3], [0,0,0]),
             ([2,0,1], [2,0,0]), ([], [])]
    for nums, expected in cases:
        assert count_smaller_brute(nums) == expected
        assert count_smaller_merge_sort(nums) == expected
    print("All Count of Smaller Numbers After Self test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def count_smaller_fenwick(nums: list[int]) -> list[int]:
    """Fenwick Tree + coordinate compression; O(n log n) time."""
    from bisect import bisect_left
    if not nums:
        return []
    values = sorted(set(nums))
    tree = [0] * (len(values) + 1)

    def add(index: int) -> None:
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    def query(index: int) -> int:
        total = 0
        while index > 0:
            total += tree[index]
            index -= index & -index
        return total

    result = [0] * len(nums)
    for i in range(len(nums) - 1, -1, -1):
        rank = bisect_left(values, nums[i]) + 1
        result[i] = query(rank - 1)
        add(rank)
    return result


def run_additional_tests() -> None:
    cases = [([5, 2, 6, 1], [2, 1, 1, 0]), ([-1, -1], [0, 0]), ([5, 4, 3, 2, 1], [4, 3, 2, 1, 0]), ([2, 0, 1], [2, 0, 0]), ([], [])]
    for nums, expected in cases:
        assert count_smaller_fenwick(nums) == expected
        assert count_smaller_merge_sort(nums) == expected
    print("Fenwick Tree Count Smaller alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
