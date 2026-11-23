"""
493. REVERSE PAIRS
LeetCode: https://leetcode.com/problems/reverse-pairs/

PROBLEM
Count pairs (i,j) where i<j and nums[i] > 2*nums[j].

Example: [1,3,2,3,1] -> 2

PATTERN
Merge Sort + Divide and Conquer + Cross-Pair Counting

APPROACH 1 — BRUTE FORCE
Check every pair. Time O(n^2), space O(1).

APPROACH 2 — MODIFIED MERGE SORT
1. Count pairs entirely in the left half.
2. Count pairs entirely in the right half.
3. Count cross pairs while both halves are sorted.
4. Merge the halves.

For each left value, move a right pointer while nums[i] > 2*nums[j].
The right pointer never moves backward because both halves are sorted.

DRY RUN
[1,3,2,3,1] has two valid index pairs: (1,4) and (3,4),
whose values are (3,1) and (3,1). Answer=2.

EDGE CASES
- Empty or one element; negative values; duplicates; equality is NOT valid.

COMPLEXITY
O(n log n) time, O(n) extra space.

INTERVIEW EXPLANATION
"Merge sort gives sorted halves. For each left value, I advance one
pointer in the right half while the doubled-value condition holds.
Then I add the number of valid right values and perform the merge."

COMMON MISTAKES
- Checking nums[i] > nums[j] instead of 2*nums[j].
- Counting only during the ordinary merge.
- Using integer division in the comparison.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

This is inversion counting with a modified inequality. Merge Sort makes both halves sorted so cross pairs can be counted using a monotonic pointer.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE
Check every pair i<j and test nums[i] > 2*nums[j]. Time O(n²), space O(1). Use this as a small-input validator.

APPROACH 2 — MODIFIED MERGE SORT (OPTIMAL)
1. Recursively count reverse pairs in the left half.
2. Recursively count them in the right half.
3. Count cross pairs before merging. For each left value, advance a right pointer while nums[i] > 2*nums[j]. Add the number of right values passed.
4. Merge the two sorted halves.
The right pointer never moves backward because left values are visited in sorted non-decreasing order and the number of right values satisfying the inequality cannot decrease. Time O(n log n), space O(n).


WHY THE RECOMMENDED APPROACH WORKS

Each valid pair is either fully inside the left half, fully inside the right half, or crosses the split. Recursive calls count the first two classes. The cross scan counts exactly those with i in the left half and j in the right half. Since every left index is earlier than every right index, i<j is automatic. The sorted halves make the qualifying right values a prefix, counted by a moving pointer.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[1,3,2,3,1]
The valid original pairs are:
(i=1,j=4): 3 > 2*1 -> true
(i=3,j=4): 3 > 2*1 -> true
No other pair satisfies the strict inequality.
Answer=2.

Cross-count example:
left sorted=[3,5], right sorted=[1,2,4]
For left 3: 3>2*1 true; 3>2*2 false -> 1 right value.
For left 5: continue from current right pointer; 5>2*2 true; 5>2*4 false -> 2 right values.
The pointer is monotonic.


EDGE CASES TO TEST

- Empty and one-element arrays -> 0.
- Strict condition: nums[i] == 2*nums[j] is not a reverse pair.
- Duplicates.
- Negative values; do not alter the inequality.
- Very large integers.
- Sorted and reverse-sorted input.


COMMON INTERVIEW MISTAKES

1. Counting nums[i] > nums[j] instead of nums[i] > 2*nums[j].
2. Counting cross pairs only during the normal merge comparison.
3. Resetting the right pointer for each left item.
4. Counting after merging has changed the partition.
5. Forgetting that recursive left/right index ranges guarantee i<j for cross pairs.


REUSABLE PATTERN TEMPLATE

j = mid + 1
for i in range(left, mid+1):
    while j <= right and nums[i] > 2*nums[j]:
        j += 1
    count += j - (mid+1)
# Then perform the ordinary ascending merge.


COMPLEXITY ANALYSIS

Brute force O(n²) time and O(1) extra space. Modified Merge Sort O(n log n) time, O(n) merge buffer plus O(log n) recursion stack; total auxiliary space O(n).


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I divide the array with Merge Sort. Recursive calls count pairs within each half. Both halves are then sorted, so I count cross pairs with a moving right pointer. For each left value, I advance while nums[i] > 2*nums[j], and the number of passed right values is added to the count. Then I merge the halves. Every pair is counted once, and the time is O(n log n)."


PATTERN MEMORY

This is inversion counting with a modified inequality. Merge Sort makes both halves sorted so cross pairs can be counted using a monotonic pointer.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] State the exact inequality and i<j condition.
[ ] Explain the three classes of pairs.
[ ] Count cross pairs before merging.
[ ] Explain why the right pointer only moves forward.
[ ] Test equality boundary.
[ ] Compare brute force and merge sort complexity.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Modified Merge Sort is the clearest optimal answer for a sorting-focused interview. It counts left, right, and cross pairs in O(n log n). Fenwick Tree + coordinate compression is an equally asymptotic alternative if the interviewer prefers prefix-frequency data structures.

ADDITIONAL IMPLEMENTATION: Fenwick Tree scans from left to right and counts previously seen values greater than 2*current. Coordinate compression plus binary search converts the threshold into a prefix query.

"""

def reverse_pairs_brute(nums: list[int]) -> int:
    return sum(1 for i in range(len(nums)) for j in range(i + 1, len(nums))
               if nums[i] > 2 * nums[j])


def reverse_pairs_merge_sort(nums: list[int]) -> int:
    arr = nums[:]
    temp = [0] * len(arr)

    def sort_count(left: int, right: int) -> int:
        if left >= right:
            return 0
        mid = (left + right) // 2
        count = sort_count(left, mid) + sort_count(mid + 1, right)

        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and arr[i] > 2 * arr[j]:
                j += 1
            count += j - (mid + 1)

        i, j, write = left, mid + 1, left
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[write] = arr[i]
                i += 1
            else:
                temp[write] = arr[j]
                j += 1
            write += 1
        while i <= mid:
            temp[write] = arr[i]
            i += 1
            write += 1
        while j <= right:
            temp[write] = arr[j]
            j += 1
            write += 1
        arr[left:right + 1] = temp[left:right + 1]
        return count

    return sort_count(0, len(arr) - 1)


class Solution:
    def reversePairs(self, nums: list[int]) -> int:
        return reverse_pairs_merge_sort(nums)


def run_tests() -> None:
    cases = [([1,3,2,3,1], 2), ([2,4,3,5,1], 3), ([], 0), ([1], 0),
             ([5,4,3,2,1], 4), ([1,1,1], 0), ([-5,-5], 1)]
    for nums, expected in cases:
        assert reverse_pairs_brute(nums) == expected
        assert reverse_pairs_merge_sort(nums) == expected
    print("All Reverse Pairs test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def reverse_pairs_fenwick(nums: list[int]) -> int:
    """Coordinate compression + Fenwick tree; O(n log n) time, O(n) space."""
    from bisect import bisect_right
    if not nums:
        return 0
    values = sorted(set(nums))
    tree = [0] * (len(values) + 1)

    def add(index: int) -> None:
        while index < len(tree):
            tree[index] += 1
            index += index & -index

    def prefix(count: int) -> int:
        total = 0
        while count > 0:
            total += tree[count]
            count -= count & -count
        return total

    answer = 0
    seen = 0
    for value in nums:
        # Number of compressed values <= 2*value.
        upto = bisect_right(values, 2 * value)
        answer += seen - prefix(upto)
        rank = bisect_right(values, value)
        add(rank)
        seen += 1
    return answer


def run_additional_tests() -> None:
    cases = [([1, 3, 2, 3, 1], 2), ([2, 4, 3, 5, 1], 3), ([-5, -5], 1), ([1, 1, 1], 0), ([2147483647, -2147483647, -2147483647], 3)]
    for nums, expected in cases:
        assert reverse_pairs_fenwick(nums) == expected
        assert reverse_pairs_merge_sort(nums) == expected
    print("Fenwick Tree Reverse Pairs alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
