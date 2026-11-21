"""
SORTING — QUESTION 01
LEETCODE 912 — SORT AN ARRAY
Link: https://leetcode.com/problems/sort-an-array/

PROBLEM
Given an integer array nums, return the array sorted in ascending order.
For this study file, implement classic sorting algorithms rather than
relying only on Python's built-in sort.

Examples:
    [5,2,3,1] -> [1,2,3,5]
    [5,1,1,2,0,0] -> [0,0,1,1,2,5]
    [] -> []

PATTERN
Sorting / Comparison Sort / Divide and Conquer

RECOGNITION TRICKS
- The output must contain the same elements in ordered form.
- Sorting is often preprocessing for two pointers, greedy, intervals,
  binary search, and duplicate handling.
- For a guaranteed O(n log n) comparison sort, choose Merge Sort or
  Heap Sort.
- Quick Sort is average O(n log n), but worst O(n^2).
- Insertion Sort can be efficient on small or nearly sorted data.
- If this is production Python code, sorted() or list.sort() is normally
  better than a hand-written implementation.

REAL-WORLD ANALOGY
Arranging exam scores from lowest to highest. Each sorting algorithm
uses a different strategy to decide which score belongs next.

APPROACH 1 — BUBBLE SORT
Compare adjacent elements and swap if they are out of order. At the end
of each pass, the largest unsorted value reaches its final position.
An early-stop flag makes an already sorted array finish in O(n).
Time: O(n^2) average/worst; O(n) best with early stop.
Space: O(1). Stable if equal values are not swapped.

APPROACH 2 — INSERTION SORT
Maintain a sorted prefix. Take the next value as key, shift larger values
right, and insert key into its correct location.
Time: O(n^2) average/worst; O(n) best for already sorted data.
Space: O(1). Stable. Good for small or nearly sorted data.

APPROACH 3 — SELECTION SORT
For each position i, find the smallest value in nums[i:] and swap it
into position i.
Time: O(n^2) in all cases. Space: O(1). Basic selection sort is not
stable, but it performs at most n-1 swaps.

APPROACH 4 — MERGE SORT (GUARANTEED O(n log n))
Split into halves, recursively sort each half, then merge the two sorted
halves with two pointers. If values are equal, take from the left half
first to preserve stability.
Time: O(n log n) in all cases. Space: O(n) temporary array plus
O(log n) recursion stack. Stable.

APPROACH 5 — QUICK SORT
Choose a pivot, partition values into smaller and larger regions, then
recursively sort both regions.
Average time: O(n log n). Worst time: O(n^2) for unbalanced partitions.
Average recursion space: O(log n); worst O(n). Not stable.

APPROACH 6 — HEAP SORT
Build a max heap, repeatedly move the largest root to the end, shrink
heap size, and restore the heap property.
Time: O(n log n) in all cases. Auxiliary space: O(1) in an in-place
implementation. Not stable.

APPROACH 7 — PYTHON TIMSORT
sorted(nums) creates a new list; nums.sort() sorts the list in place.
Python's Timsort is stable, has O(n log n) worst-case time, and can take
advantage of existing ordered runs. Best-case behavior can be O(n).
Use it in real projects, but not when asked to implement a sorting
algorithm from scratch.

WHY MERGE SORT WORKS
A one-element array is already sorted. Assume the recursive calls sort
the left and right halves correctly. At merge time, the smallest value
not yet copied must be at the beginning of one of the two sorted halves.
Taking the smaller front value therefore places the next smallest item
into the output. Repeating this produces a sorted array. Taking from the
left half on equality preserves the original order of equal items.

STEP-BY-STEP INTERVIEW THINKING
1. Identify ascending order as the target.
2. Check whether the question gives a complexity or memory constraint.
3. Avoid O(n^2) algorithms for large n.
4. Use Merge Sort for guaranteed O(n log n) time and stability.
5. Use Heap Sort if constant auxiliary space is important.
6. Use Quick Sort when average performance is the focus, but mention
   the worst case.
7. In Python production code, use sorted() or list.sort().

DRY RUN — MERGE SORT
nums = [5,2,3,1]

Split:
    [5,2] and [3,1]
    [5] [2] [3] [1]

Merge first pair:
    compare 5 and 2 -> take 2, then 5 -> [2,5]

Merge second pair:
    compare 3 and 1 -> take 1, then 3 -> [1,3]

Final merge:
    compare 2 and 1 -> take 1
    compare 2 and 3 -> take 2
    compare 5 and 3 -> take 3
    append 5

Output = [1,2,3,5]

EDGE CASES
- Empty array and one value.
- Already sorted array.
- Reverse sorted array.
- All values equal.
- Duplicates mixed with negative numbers.
- Very large n, where quadratic methods become too slow.

COMMON INTERVIEW MISTAKES
1. Claiming every sorting algorithm is O(n log n).
2. Forgetting to append remaining elements after one merge pointer ends.
3. Taking the right item on equality and accidentally losing stability.
4. Claiming Quick Sort has O(n log n) worst-case time.
5. Mixing auxiliary space with output space.
6. Mutating the input when a new list is expected.
7. Using built-in sort when the challenge explicitly forbids it.

REUSABLE MERGE SORT TEMPLATE
    if len(nums) <= 1: return nums[:]
    mid = len(nums)//2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    return merge(left,right)

SIMILAR PROBLEMS
- LeetCode 148: Sort List
- LeetCode 88: Merge Sorted Array
- LeetCode 315: Count of Smaller Numbers After Self
- LeetCode 493: Reverse Pairs
- LeetCode 215: Kth Largest Element in an Array

COMPLEXITY SUMMARY
Algorithm       Best       Average      Worst       Auxiliary Space
Bubble          O(n)       O(n^2)       O(n^2)      O(1)
Insertion       O(n)       O(n^2)       O(n^2)      O(1)
Selection       O(n^2)     O(n^2)       O(n^2)      O(1)
Merge           O(nlogn)   O(nlogn)     O(nlogn)    O(n)
Quick           O(nlogn)   O(nlogn)     O(n^2)      O(logn) avg, O(n) worst
Heap            O(nlogn)   O(nlogn)     O(nlogn)    O(1)
Timsort         O(n) on runs O(nlogn)   O(nlogn)    O(n) worst

INTERVIEW EXPLANATION
"I would choose Merge Sort when a guaranteed O(n log n) bound is needed.
I recursively split the array into halves and merge the sorted halves
with two pointers. This takes O(n log n) time and O(n) auxiliary space.
If constant auxiliary memory is more important, Heap Sort is another
worst-case O(n log n) option. Quick Sort is usually fast on average but
has an O(n^2) worst case. In production Python, Timsort is preferred."

PATTERN MEMORY
Large input + guaranteed O(nlogn) -> Merge Sort / Heap Sort
Stable sort required -> Merge Sort
Average fast partition sort -> Quick Sort
Small or nearly sorted -> Insertion Sort
Production Python -> sorted() / list.sort()

REVISION CHECKLIST
[ ] Implement Bubble Sort and early stop.
[ ] Explain insertion-sort sorted-prefix invariant.
[ ] Explain why selection sort is not stable.
[ ] Implement merge sort and merge two sorted arrays.
[ ] Explain Quick Sort worst case.
[ ] Explain Heap Sort memory advantage.
[ ] Know stable vs unstable algorithms.
[ ] Distinguish sorted() from list.sort().
[ ] State time and auxiliary space accurately.

INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Explain Merge Sort first when a guaranteed O(n log n) bound is required. It is stable and has O(n) auxiliary space. If the interviewer prioritizes constant auxiliary space, follow up with Heap Sort. Quick Sort is a practical average-case option but has O(n²) worst case. In actual Python production code, use list.sort()/sorted() unless implementing the algorithm is the task.

ADDITIONAL IMPLEMENTATIONS: Heap Sort gives O(n log n) worst-case time and O(1) auxiliary space. Counting Sort is linear in n plus the value range and is useful only when that range is reasonably small. Python built-in sorting is included only as a production/reference alternative, not as an implementation answer.

"""


def bubble_sort(nums: list[int]) -> list[int]:
    arr = nums[:]
    for end in range(len(arr) - 1, 0, -1):
        swapped = False
        for j in range(end):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def insertion_sort(nums: list[int]) -> list[int]:
    arr = nums[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(nums: list[int]) -> list[int]:
    arr = nums[:]
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def merge_sort(nums: list[int]) -> list[int]:
    if len(nums) <= 1:
        return nums[:]
    mid = len(nums) // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(nums: list[int]) -> list[int]:
    arr = nums[:]
    def sort(low: int, high: int) -> None:
        if low >= high:
            return
        pivot = arr[high]
        boundary = low
        for current in range(low, high):
            if arr[current] <= pivot:
                arr[boundary], arr[current] = arr[current], arr[boundary]
                boundary += 1
        arr[boundary], arr[high] = arr[high], arr[boundary]
        sort(low, boundary - 1)
        sort(boundary + 1, high)
    sort(0, len(arr) - 1)
    return arr


class Solution:
    def sortArray(self, nums: list[int]) -> list[int]:
        return merge_sort(nums)


def run_tests() -> None:
    test_cases = [
        [5, 2, 3, 1], [5, 1, 1, 2, 0, 0], [], [1],
        [3, -1, 0, -5, 8], [4, 3, 2, 1], [2, 2, 2, 2]
    ]
    algorithms = [bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort]
    for nums in test_cases:
        expected = sorted(nums)
        for algorithm in algorithms:
            assert algorithm(nums) == expected, (algorithm.__name__, nums)
    assert Solution().sortArray([5, 2, 3, 1]) == [1, 2, 3, 5]
    print("All Sort an Array test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def heap_sort(nums: list[int]) -> list[int]:
    """In-place max-heap sort on a copy: O(n log n), O(1) auxiliary."""
    arr = nums[:]
    n = len(arr)

    def sift_down(root: int, size: int) -> None:
        while True:
            largest = root
            left = 2 * root + 1
            right = left + 1
            if left < size and arr[left] > arr[largest]:
                largest = left
            if right < size and arr[right] > arr[largest]:
                largest = right
            if largest == root:
                return
            arr[root], arr[largest] = arr[largest], arr[root]
            root = largest

    # Bottom-up heap construction is O(n), not O(n log n).
    for root in range(n // 2 - 1, -1, -1):
        sift_down(root, n)

    for end in range(n - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(0, end)

    return arr


def counting_sort_range(nums: list[int], max_range: int = 100_000) -> list[int]:
    """O(n + range) sorting when max(nums)-min(nums) is small."""
    if not nums:
        return []
    low, high = min(nums), max(nums)
    span = high - low + 1
    if span > max_range:
        raise ValueError("value range is too large for counting sort")
    counts = [0] * span
    for value in nums:
        counts[value - low] += 1
    result = []
    for offset, count in enumerate(counts):
        result.extend([low + offset] * count)
    return result


def run_additional_tests() -> None:
    cases = [[], [1], [3, 2, 1], [0, -5, 3, -5, 2], [4, 4, 4], list(range(30, -1, -1))]
    for values in cases:
        expected = sorted(values)
        assert heap_sort(values) == expected
        assert counting_sort_range(values) == expected
        assert values == values  # all helpers return a sorted copy
    print("Heap Sort and Counting Sort alternatives passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
