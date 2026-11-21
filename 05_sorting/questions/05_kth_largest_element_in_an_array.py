"""
215. KTH LARGEST ELEMENT IN AN ARRAY
LeetCode: https://leetcode.com/problems/kth-largest-element-in-an-array/

PROBLEM
Return the kth largest element. Duplicates count as separate positions.

Example: nums = [3,2,1,5,6,4], k = 2 -> 5

PATTERN
Sorting / Heap / Quickselect

APPROACH 1 — SORTING
Sort descending and return index k-1.
Time: O(n log n), extra space O(n) for sorted copy.

APPROACH 2 — MIN HEAP OF SIZE K
Keep only the k largest values. When heap length exceeds k, pop the
smallest. At the end heap[0] is kth largest.
Time: O(n log k), space O(k).

APPROACH 3 — QUICKSELECT
For ascending order, the target index is n-k. Partition around a pivot
and continue only in the partition containing the target.
Average time O(n); worst time O(n^2). This version uses 3-way partition
to handle duplicates efficiently.

DRY RUN
[3,2,1,5,6,4], k=2 -> target ascending index = 6-2 = 4.
Sorted order is [1,2,3,4,5,6], so answer is 5.
Quickselect finds that position without fully sorting the array.

EDGE CASES
- k=1 -> maximum; k=n -> minimum.
- Duplicates, all equal, negative values, one-element array.

COMPLEXITY
Sorting O(n log n); heap O(n log k), O(k) space;
Quickselect average O(n), worst O(n^2), O(1) auxiliary beyond copy.

INTERVIEW EXPLANATION
"I only need one order statistic, not a fully sorted array. Quickselect
partitions and discards the side that cannot contain the target index."

COMMON MISTAKES
- Returning index k rather than k-1 after sorting.
- Using target=k-1 for an ascending partition.
- Claiming Quickselect has O(n) worst-case time.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

This is an order-statistic problem. The key is to find one rank without necessarily sorting all n values.


APPROACH ANALYSIS

APPROACH 1 — FULL SORT
Sort descending and return index k-1. Correct and easy to explain. Time O(n log n); sorted copy uses O(n) space.

APPROACH 2 — MIN HEAP OF SIZE K
Push each value into a min heap. Whenever size exceeds k, pop the smallest. The heap retains the k largest values seen so far; its root is the smallest among those k, which is the kth largest. Time O(n log k), space O(k). Useful when k is small or values arrive as a stream.

APPROACH 3 — QUICKSELECT
The kth largest is at ascending index target=n-k. Partition around a pivot. Continue only in the side that contains target; if target lies in the pivot-equal region, return it. Three-way partitioning handles duplicates. Average O(n), worst O(n²), iterative auxiliary space O(1) beyond the copy.


WHY THE RECOMMENDED APPROACH WORKS

For the heap, maintain the invariant that the heap stores the k largest values processed so far. If there are k+1 candidates, the smallest can be discarded. At the end, the smallest of the retained k is exactly kth largest. For Quickselect, partitioning fixes a pivot rank; every item on the discarded side is known to be irrelevant to the target position.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[3,2,1,5,6,4], k=2

Sorted descending: [6,5,4,3,2,1] -> index 1 -> 5.

Size-2 min heap:
3 -> [3]
2 -> [2,3]
1 -> temporarily [1,2,3], pop 1 -> [2,3]
5 -> pop 2 -> [3,5]
6 -> pop 3 -> [5,6]
4 -> pop 4 -> [5,6]

The two largest values are 5 and 6. The smallest among them is 5.
Quickselect's ascending target is n-k=4, whose value is also 5.


EDGE CASES TO TEST

- k=1 gives maximum; k=n gives minimum.
- All values equal.
- Duplicates count as separate positions.
- Negative values.
- Sorted and reverse-sorted input.
- Single-element input.


COMMON INTERVIEW MISTAKES

1. Using target=k-1 in an ascending partition; that finds kth smallest.
2. Using a max heap for the size-k kth-largest method.
3. Forgetting to pop when heap size exceeds k.
4. Treating duplicates as one distinct value.
5. Claiming Quickselect has a guaranteed O(n) worst case.
6. Assuming the internal heap array is fully sorted.


REUSABLE PATTERN TEMPLATE

# size-k min heap
for value in nums:
    heappush(heap, value)
    if len(heap) > k:
        heappop(heap)
return heap[0]

# Quickselect ascending target
target = len(nums) - k


COMPLEXITY ANALYSIS

Full sorting: O(n log n) time, O(n) copy. Size-k min heap: O(n log k) time and O(k) space. Quickselect: O(n) average, O(n²) worst, O(1) auxiliary beyond the working copy for iterative partitioning.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I only need one rank, not a fully sorted array. A size-k min heap keeps the k largest values seen so far; when it grows beyond k, I remove the smallest. At the end heap[0] is the kth largest. This takes O(n log k) time and O(k) space. For average linear time, I can use Quickselect with target index n-k, noting its worst case is O(n²)."


PATTERN MEMORY

This is an order-statistic problem. The key is to find one rank without necessarily sorting all n values.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Convert kth largest into ascending index n-k.
[ ] Implement sorting and heap approaches.
[ ] Explain the size-k heap invariant.
[ ] Implement Quickselect.
[ ] Explain duplicates and three-way partition.
[ ] State average and worst Quickselect complexity.

"""

from heapq import heappush, heappop


def kth_largest_sorting(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    return sorted(nums, reverse=True)[k - 1]


def kth_largest_heap(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    heap = []
    for value in nums:
        heappush(heap, value)
        if len(heap) > k:
            heappop(heap)
    return heap[0]


def kth_largest_quickselect(nums: list[int], k: int) -> int:
    if not 1 <= k <= len(nums):
        raise ValueError("k must be between 1 and len(nums)")
    arr = nums[:]
    target = len(arr) - k
    left, right = 0, len(arr) - 1
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
            return arr[target]
    raise RuntimeError("Quickselect failed")


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        return kth_largest_quickselect(nums, k)


def run_tests() -> None:
    cases = [([3,2,1,5,6,4], 2, 5), ([3,2,3,1,2,4,5,5,6], 4, 4),
             ([7,7,7], 2, 7), ([-1,-2,-3], 1, -1), ([1], 1, 1)]
    for nums, k, expected in cases:
        assert kth_largest_sorting(nums, k) == expected
        assert kth_largest_heap(nums, k) == expected
        assert kth_largest_quickselect(nums, k) == expected
    print("All Kth Largest Element test cases passed.")


if __name__ == "__main__":
    run_tests()
