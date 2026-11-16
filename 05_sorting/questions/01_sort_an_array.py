"""
SORTING — QUESTION 01
LeetCode 912 — Sort an Array

PROBLEM
Given an array of integers nums, return the array sorted in ascending order.

Example:
Input:  [5, 2, 3, 1]
Output: [1, 2, 3, 5]

PATTERN
Sorting — Divide and Conquer (Merge Sort)

APPROACHES
1. Bubble Sort
   Time: O(n^2), Space: O(1)
2. Insertion Sort
   Time: O(n^2), Space: O(1)
3. Merge Sort
   Time: O(n log n), Space: O(n)
4. Quick Sort
   Average Time: O(n log n)
   Worst Time: O(n^2)
   Average auxiliary space: O(log n) with recursive calls

INTERVIEW IDEA
For a guaranteed O(n log n) time complexity, use Merge Sort.
It divides the array into halves, sorts each half, and merges
the sorted halves.

DRY RUN — MERGE SORT
nums = [5, 2, 3, 1]

Split:
[5, 2] and [3, 1]
[5], [2], [3], [1]

Merge:
[2, 5] and [1, 3]
Final:
[1, 2, 3, 5]

IMPORTANT
- Merge Sort guarantees O(n log n) time.
- Merge Sort is stable when equal values are taken from the left half first.
- Python's built-in sorted() is usually preferred in production.
- The LeetCode solution below uses Merge Sort to demonstrate the algorithm.
"""


def bubble_sort(nums):
    arr = nums[:]
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break

    return arr


def insertion_sort(nums):
    arr = nums[:]

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    return arr


def merge_sort(nums):
    if len(nums) <= 1:
        return nums[:]

    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])

    return result


def quick_sort(nums):
    arr = nums[:]
    _quick_sort(arr, 0, len(arr) - 1)
    return arr


def _quick_sort(arr, low, high):
    if low >= high:
        return

    pivot_index = _partition(arr, low, high)
    _quick_sort(arr, low, pivot_index - 1)
    _quick_sort(arr, pivot_index + 1, high)


def _partition(arr, low, high):
    pivot = arr[high]
    i = low

    for j in range(low, high):
        if arr[j] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    arr[i], arr[high] = arr[high], arr[i]
    return i


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        if len(nums) <= 1:
            return nums

        mid = len(nums) // 2
        left = self.sortArray(nums[:mid])
        right = self.sortArray(nums[mid:])

        return self.merge(left, right)

    def merge(self, left: list[int], right: list[int]) -> list[int]:
        result = []
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result


def run_tests():
    test_cases = [
        [5, 2, 3, 1],
        [5, 1, 1, 2, 0, 0],
        [],
        [1],
        [3, -1, 0, -5, 8],
        [4, 3, 2, 1],
    ]

    algorithms = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort),
    ]

    for nums in test_cases:
        expected = sorted(nums)
        print(f"Input:    {nums}")
        for name, algorithm in algorithms:
            result = algorithm(nums)
            assert result == expected, f"{name} failed for {nums}"
            print(f"{name}: {result}")
        leetcode_result = Solution().sortArray(nums)
        assert leetcode_result == expected
        print(f"LeetCode Solution: {leetcode_result}")
        print()


if __name__ == "__main__":
    run_tests()
