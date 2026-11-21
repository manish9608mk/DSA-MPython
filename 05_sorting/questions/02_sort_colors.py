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


if __name__ == "__main__":
    run_tests()
