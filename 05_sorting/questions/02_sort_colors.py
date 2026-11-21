"""
75. SORT COLORS
LeetCode: https://leetcode.com/problems/sort-colors/

PROBLEM
Given an array nums containing 0, 1, and 2, sort it in-place so that
objects of the same color are adjacent in the order 0, 1, 2.
Do not use the library sort function.

Example:
    nums = [2, 0, 2, 1, 1, 0]
    Output = [0, 0, 1, 1, 2, 2]

PATTERN
Dutch National Flag / Three Pointers / In-place Partitioning

APPROACH 1 — COUNTING
1. Count the number of 0s, 1s, and 2s.
2. Rewrite the array with those counts.
Time: O(n) | Space: O(1)

APPROACH 2 — DUTCH NATIONAL FLAG (OPTIMAL)
Maintain four regions:
    [0 ... low-1]       contains 0
    [low ... mid-1]     contains 1
    [mid ... high]      unknown
    [high+1 ... n-1]    contains 2

Rules:
- nums[mid] == 0: swap with low; increment low and mid.
- nums[mid] == 1: increment mid.
- nums[mid] == 2: swap with high; decrement high.
  Do not increment mid because the swapped-in value is not checked yet.

DRY RUN
nums = [2, 0, 2, 1, 1, 0]
The first 2 moves to the right, then 0s move left, and 1s remain
in the middle. Final array: [0, 0, 1, 1, 2, 2].

EDGE CASES
- Empty array or one element.
- All values equal.
- Already sorted or reverse sorted.
- Array contains only 0 and 2.

COMPLEXITY
Counting: O(n) time, O(1) auxiliary space.
Dutch National Flag: O(n) time, O(1) auxiliary space.

INTERVIEW EXPLANATION
"I use three pointers to divide the array into regions containing 0s,
1s, and 2s. The middle pointer examines the unknown region. A 0 is
moved left, a 2 is moved right, and a 1 stays in the middle."

COMMON MISTAKES
- Incrementing mid after swapping a 2 with high.
- Forgetting to decrement high.
- Creating another array when in-place partitioning is possible.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The array has only three categories, so a general-purpose comparison sort is unnecessary. The important decision is whether to use two-pass frequency counting or one-pass three-way partitioning.


APPROACH ANALYSIS

APPROACH 1 — BUILT-IN SORT (NOT THE INTENDED ANSWER)
Call nums.sort(). It gives the correct order, but the problem explicitly asks for an in-place solution without the library sort.
Time: O(n log n).

APPROACH 2 — COUNTING SORT (SIMPLE LINEAR SOLUTION)
Count the number of 0s, 1s, and 2s. Rewrite the array with all 0s first, then 1s, then 2s. The count array always has exactly three positions, so its space is O(1).
Time: O(n), Space: O(1), two passes.

APPROACH 3 — DUTCH NATIONAL FLAG (ONE PASS)
Maintain four regions: [0, low) contains 0; [low, mid) contains 1; [mid, high] is unknown; (high, n) contains 2. Inspect nums[mid]. For 0, swap with low and advance both low and mid. For 1, advance mid. For 2, swap with high and decrement high; do not advance mid because the incoming value is unknown.
Time: O(n), Space: O(1). The unknown region shrinks on every iteration.


WHY THE RECOMMENDED APPROACH WORKS

The invariant is the proof. Before every iteration, all positions before low are 0, positions from low through mid-1 are 1, and positions after high are 2. The only unclassified region is mid through high. Each branch places nums[mid] into a known region or moves the right boundary inward. When mid > high, the unknown region is empty and the array is sorted.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums = [2,0,2,1,1,0]
Start: low=0, mid=0, high=5

nums[mid]=2: swap nums[0] and nums[5]
    [0,0,2,1,1,2], high=4, mid stays 0
nums[mid]=0: swap nums[0] and nums[0]
    [0,0,2,1,1,2], low=1, mid=1
nums[mid]=0: swap nums[1] and nums[1]
    [0,0,2,1,1,2], low=2, mid=2
nums[mid]=2: swap nums[2] and nums[4]
    [0,0,1,1,2,2], high=3, mid stays 2
nums[mid]=1: mid=3; then mid=4
Now mid > high. Answer = [0,0,1,1,2,2].


EDGE CASES TO TEST

- Empty and one-element arrays.
- All 0s, all 1s, or all 2s.
- Already grouped input and reverse-grouped input.
- Alternating values such as [2,0,1,2,0,1].
- The original constraints guarantee only 0, 1, and 2; the implementation raises ValueError for another value.


COMMON INTERVIEW MISTAKES

1. Incrementing mid after swapping a 2 with high; this skips an unexamined value.
2. Forgetting to decrement high after placing a 2.
3. Moving a 1 unnecessarily; it already belongs in the middle region.
4. Using a set, which removes duplicates.
5. Claiming stability; Dutch National Flag swaps can change the relative order of equal values.


REUSABLE PATTERN TEMPLATE

low = mid = 0
high = len(nums) - 1
while mid <= high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1; mid += 1
    elif nums[mid] == 1:
        mid += 1
    else:
        nums[mid], nums[high] = nums[high], nums[mid]
        high -= 1  # mid does not move here


COMPLEXITY ANALYSIS

Counting: O(n) time, O(1) auxiliary space, two passes. Dutch National Flag: O(n) time, O(1) auxiliary space, one scan. Every iteration either advances mid or decreases high, so there are at most O(n) iterations.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"Only three values are present, so I can partition the array into three regions. I use low, mid, and high. Values before low are 0, between low and mid are 1, and after high are 2. A zero moves left, a one stays, and a two moves right. I do not advance mid after a two-swap because the value coming from the right is not yet inspected. The method is O(n) time and O(1) extra space."


PATTERN MEMORY

The array has only three categories, so a general-purpose comparison sort is unnecessary. The important decision is whether to use two-pass frequency counting or one-pass three-way partitioning.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain the four regions and pointer meanings.
[ ] Write the counting version.
[ ] Write the one-pass Dutch National Flag version.
[ ] Explain why mid does not move after swapping a 2.
[ ] Dry-run [2,0,2,1,1,0].
[ ] State O(n) time and O(1) extra space.
[ ] Explain why the algorithm is not necessarily stable.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Present Dutch National Flag as the final interview answer: one pass, O(n) time and O(1) extra space. Mention counting sort first as the simpler two-pass linear alternative. The built-in sort is not acceptable because the statement explicitly forbids it.

ADDITIONAL IMPLEMENTATION: A simple reference implementation using Python sorting is useful only to validate outputs; it violates the problem constraint. The two accepted algorithmic approaches in this file are frequency counting and three-way in-place partitioning.

"""

def sort_colors_counting(nums: list[int]) -> None:
    counts = [0, 0, 0]
    for value in nums:
        if value not in (0, 1, 2):
            raise ValueError("nums may contain only 0, 1, and 2")
        counts[value] += 1
    index = 0
    for value, count in enumerate(counts):
        for _ in range(count):
            nums[index] = value
            index += 1


def sort_colors_dutch_flag(nums: list[int]) -> None:
    low, mid, high = 0, 0, len(nums) - 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        elif nums[mid] == 2:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
        else:
            raise ValueError("nums may contain only 0, 1, and 2")


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        sort_colors_dutch_flag(nums)


def run_tests() -> None:
    cases = [([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
             ([2, 0, 1], [0, 1, 2]), ([0], [0]), ([2, 2], [2, 2]), ([], [])]
    for original, expected in cases:
        a, b = original[:], original[:]
        sort_colors_counting(a)
        sort_colors_dutch_flag(b)
        assert a == expected and b == expected
    print("All Sort Colors test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def sort_colors_reference_only(nums: list[int]) -> list[int]:
    """Correct reference for tests only; NOT a valid submission approach."""
    return sorted(nums)


def run_additional_tests() -> None:
    cases = [[], [0], [2, 1, 0], [2, 2, 1, 1, 0, 0], [1, 1, 1], [0, 2, 0, 2]]
    for original in cases:
        expected = sort_colors_reference_only(original)
        a, b = original[:], original[:]
        sort_colors_counting(a)
        sort_colors_dutch_flag(b)
        assert a == expected and b == expected
    print("Sort Colors counting and Dutch National Flag implementations passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
