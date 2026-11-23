"""
324. WIGGLE SORT II
LeetCode: https://leetcode.com/problems/wiggle-sort-ii/

PROBLEM
Rearrange nums so nums[0] < nums[1] > nums[2] < nums[3] ...
The problem guarantees a valid answer exists.

Example: [1,5,1,1,6,4] -> one valid output [1,6,1,5,1,4]

PATTERN
Sorting + Two Pointers / Quickselect + Virtual Indexing

APPROACH 1 — SORT AND INTERLEAVE
Sort. Put the smaller half in reverse order at even indices and the
larger half in reverse order at odd indices.
Time O(n log n), space O(n).

APPROACH 2 — QUICKSELECT + VIRTUAL INDEXING
Find the median. Use virtual index (1 + 2*i) % (n | 1), then perform
three-way partitioning: values > median go to the front, values < median
go to the back, median values stay in the middle.
Average O(n) time, O(1) auxiliary space beyond working copy.

DRY RUN
Sorted [1,1,1,4,5,6]. Smaller half reversed [1,1,1].
Larger half reversed [6,5,4]. Interleave -> [1,6,1,5,1,4].

EDGE CASES
- Two elements; duplicate-heavy arrays; negatives.
- If every number is equal, strict inequalities are impossible;
  this is excluded by the valid-answer guarantee.

COMPLEXITY
Sort-and-interleave: O(n log n) time, O(n) space.
Quickselect + virtual partition: average O(n) time.

INTERVIEW EXPLANATION
"The simple approach sorts and interleaves two reversed halves. The
advanced approach finds the median and uses virtual indexing to put
large values at odd positions and small values at even positions."

COMMON MISTAKES
- Interleaving halves in the wrong direction.
- Forgetting virtual indices in the advanced solution.
- Assuming every input can satisfy strict wiggle inequalities.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The target is a strict alternating pattern, not simply sorted order. The simple method sorts and interleaves halves; the advanced method partitions around the median using virtual indices.


APPROACH ANALYSIS

APPROACH 1 — SORT + REVERSE INTERLEAVING (EASIER)
Sort a copy. Split into a smaller half and a larger half. Fill even positions using the smaller half in descending order, and odd positions using the larger half in descending order. Reversing each half helps separate duplicate middle values. Time O(n log n), space O(n).

APPROACH 2 — QUICKSELECT + VIRTUAL INDEXING (ADVANCED)
Find the median. Use virtual index (1+2*i) % (n|1) so the first partition positions correspond to odd physical indices, where larger values belong. Three-way partition values into >median, ==median, and <median through virtual positions. Average O(n) selection/partition time, O(1) extra space beyond the working copy.

The problem guarantees a valid arrangement; without that guarantee, strict inequalities may be impossible for some multisets.


WHY THE RECOMMENDED APPROACH WORKS

In the sorted-interleave approach, placing the larger half at odd positions makes peaks, while the smaller half at even positions makes valleys. Reversing each half puts the largest valley candidates and smallest peak candidates adjacent to the center boundary, reducing the chance of equal neighbors. In the advanced approach, virtual indexing directs large values to odd slots and small values to even slots while the three-way partition keeps median values in the middle.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[1,5,1,1,6,4]
Sorted=[1,1,1,4,5,6]
Smaller half reversed=[1,1,1]
Larger half reversed=[6,5,4]

Place smaller values at indices 0,2,4 and larger values at 1,3,5:
[1,6,1,5,1,4]
Check: 1<6>1<5>1<4.

Virtual-index formula maps logical positions through odd slots first; it prevents the high/low partitions from disturbing the desired physical arrangement.


EDGE CASES TO TEST

- Two elements.
- Duplicate-heavy input with a valid arrangement.
- Negative values.
- Odd and even lengths.
- All values equal: strict wiggle arrangement is impossible, so it is outside the guaranteed-valid input promise.


COMMON INTERVIEW MISTAKES

1. Interleaving smaller and larger halves in the wrong direction.
2. Placing all small values before all large values.
3. Forgetting the strict inequalities.
4. Applying ordinary indices in the virtual-index algorithm.
5. Claiming every input can be rearranged; strict wiggle may be impossible.


REUSABLE PATTERN TEMPLATE

ordered = sorted(nums)
half = (n+1)//2
small = ordered[:half][::-1]
large = ordered[half:][::-1]
nums[::2] = small
nums[1::2] = large

# Advanced virtual index:
virtual(i) = (1 + 2*i) % (n | 1)


COMPLEXITY ANALYSIS

Sort/interleave: O(n log n) time and O(n) space. Quickselect + virtual three-way partition: O(n) average time, O(1) auxiliary space beyond the copied working array; Quickselect can be O(n²) worst case.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"The straightforward solution sorts the values and interleaves the smaller and larger halves in reverse order, placing smaller values at even indices and larger values at odd indices. That takes O(n log n) time and O(n) space. For an average-linear solution, I select the median and perform a three-way partition through virtual indices so larger values occupy odd positions and smaller values occupy even positions."


PATTERN MEMORY

The target is a strict alternating pattern, not simply sorted order. The simple method sorts and interleaves halves; the advanced method partitions around the median using virtual indices.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain the required < > < > pattern.
[ ] Implement sort-and-interleave.
[ ] Explain why each half is reversed.
[ ] Check the result with strict comparisons.
[ ] Understand the virtual-index formula.
[ ] Explain the valid-answer guarantee.
[ ] State the complexity of the chosen approach honestly.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Start with sort + reverse interleaving because it is short, explainable, and O(n log n). If the interviewer explicitly asks for average O(n) time and O(1) extra space, explain median selection + virtual-index Dutch National Flag partitioning; it is much trickier and Quickselect has a worst-case O(n²) bound.

IMPLEMENTATIONS: The file contains both standard accepted algorithm families: sorting/interleaving and Quickselect/virtual-index three-way partition. There is no useful O(n²) brute-force permutation method for realistic constraints; it is not an interview solution.

"""

def wiggle_sort_sorted(nums: list[int]) -> None:
    ordered = sorted(nums)
    half = (len(nums) + 1) // 2
    nums[::2] = ordered[:half][::-1]
    nums[1::2] = ordered[half:][::-1]


def wiggle_sort_quickselect(nums: list[int]) -> None:
    n = len(nums)
    if n <= 1:
        return
    arr = nums[:]
    target = n // 2
    left, right = 0, n - 1

    while left <= right:
        pivot = arr[(left + right) // 2]
        low = current = left
        high = right
        while current <= high:
            if arr[current] < pivot:
                arr[low], arr[current] = arr[current], arr[low]
                low += 1
                current += 1
            elif arr[current] > pivot:
                arr[current], arr[high] = arr[high], arr[current]
                high -= 1
            else:
                current += 1
        if target < low:
            right = low - 1
        elif target > high:
            left = high + 1
        else:
            median = pivot
            break
    else:
        raise RuntimeError("Median selection failed")

    def virtual(i: int) -> int:
        return (1 + 2 * i) % (n | 1)

    low = current = 0
    high = n - 1
    while current <= high:
        mapped = virtual(current)
        if arr[mapped] > median:
            mapped_low = virtual(low)
            arr[mapped_low], arr[mapped] = arr[mapped], arr[mapped_low]
            low += 1
            current += 1
        elif arr[mapped] < median:
            mapped_high = virtual(high)
            arr[mapped], arr[mapped_high] = arr[mapped_high], arr[mapped]
            high -= 1
        else:
            current += 1
    nums[:] = arr


class Solution:
    def wiggleSort(self, nums: list[int]) -> None:
        wiggle_sort_sorted(nums)


def is_wiggle(nums: list[int]) -> bool:
    return all(nums[i] < nums[i + 1] if i % 2 == 0 else nums[i] > nums[i + 1]
               for i in range(len(nums) - 1))


def run_tests() -> None:
    cases = [[1,5,1,1,6,4], [1,3,2,2,3,1], [1,2], [4,5,5,6], [1,1,2,2,3,3]]
    for original in cases:
        for algorithm in (wiggle_sort_sorted, wiggle_sort_quickselect):
            result = original[:]
            algorithm(result)
            assert sorted(result) == sorted(original)
            assert is_wiggle(result), (original, result)
    print("All Wiggle Sort II test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def run_additional_tests() -> None:
    cases = [
        [1, 5, 1, 1, 6, 4],
        [1, 3, 2, 2, 3, 1],
        [1, 2],
        [4, 5, 5, 6],
        [1, 1, 2, 2, 3, 3],
        [1, 1, 1, 2, 2, 2],
    ]
    for original in cases:
        for implementation in (wiggle_sort_sorted, wiggle_sort_quickselect):
            values = original[:]
            implementation(values)
            assert sorted(values) == sorted(original)
            assert is_wiggle(values), (implementation.__name__, original, values)
    print("Both Wiggle Sort II approaches passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
