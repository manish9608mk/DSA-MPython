"""
2009. MINIMUM NUMBER OF OPERATIONS TO MAKE ARRAY CONTINUOUS
LeetCode: https://leetcode.com/problems/minimum-number-of-operations-to-make-array-continuous/

PROBLEM
An array is continuous when it contains n unique consecutive integers.
In one operation, replace any element with any integer. Return the
minimum number of operations to make nums continuous.

Example: nums=[4,2,5,3] -> 0

PATTERN
Sorting + Deduplication + Sliding Window

KEY OBSERVATION
After choosing the smallest value x of the final consecutive range,
the range must be [x, x+n-1]. Keep as many existing distinct values
inside one such range as possible. Replace every other position.

APPROACH
1. Sort and remove duplicates.
2. Use two pointers to find the maximum number of distinct values
   within a range of width n: nums[right]-nums[left] < n.
3. Minimum operations = n - maximum window size.

DRY RUN
nums=[1,2,3,5,6], n=5.
The range [1,5] keeps 1,2,3,5 (4 distinct values).
One value must be replaced -> answer 1.

EDGE CASES
- Already continuous; all duplicates; one element; negative values.

COMPLEXITY
Sorting O(n log n), sliding window O(n), space O(n) for unique list.

INTERVIEW EXPLANATION
"I need a window of n consecutive integer positions. After sorting
unique values, I find the largest group whose max-min is less than n.
Those values can stay; all remaining positions need replacement."

COMMON MISTAKES
- Forgetting to deduplicate.
- Using <= n instead of < n for the range width.
- Returning the window size instead of n-window size.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

After sorting and removing duplicates, any final continuous array of length n is a window of n distinct consecutive integer values. Maximize how many original unique values can be kept in one such range.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE CHOOSE A START
Try every possible starting value and count how many unique numbers fall in [start,start+n-1]. This repeated range count can be O(n²).

APPROACH 2 — SORT + UNIQUE + SLIDING WINDOW (OPTIMAL)
Let unique be sorted(set(nums)). A continuous target range has n distinct integers. For each left pointer, move right while unique[right] <= unique[left]+n-1. This window contains the most existing distinct values that fit in a range of width n. Operations needed = n - window_size. Use two pointers so right never moves backwards.
Time O(n log n) for sorting, O(n) scan. Space O(n).


WHY THE RECOMMENDED APPROACH WORKS

A final continuous array must contain n consecutive distinct values. If we choose its smallest value as x, the allowed interval is [x,x+n-1]. Any unique original value inside this interval can be retained; duplicates beyond the first copy must be replaced because the final array has no duplicates. Therefore maximizing the number of unique values in any length-n value range minimizes replacements. Sorted order makes these candidates a sliding window.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[4,2,5,3]
unique=sorted(set(nums))=[2,3,4,5]
n=4
Window starting at 2 can include values <= 2+4-1=5.
It contains all four unique values.
keep=4, operations=4-4=0.

Example with duplicates: nums=[1,2,3,5,6]
unique=[1,2,3,5,6], n=5
Window [2,6] contains 2,3,5,6 -> keep=4.
Operations=5-4=1.


EDGE CASES TO TEST

- All values already form n unique consecutive integers -> 0.
- All values equal -> keep one unique value, replace n-1.
- Negative values.
- Duplicates: they count as extra replacements.
- Large gaps between distinct values.
- n=1 -> answer 0.


COMMON INTERVIEW MISTAKES

1. Forgetting to remove duplicates before the window.
2. Using n-1 as the range width incorrectly; the inclusive window [x,x+n-1] contains n integers.
3. Moving left and right pointers independently such that right goes backwards.
4. Returning number of duplicates only; gaps may also require changes.
5. Counting unique values outside the selected range.


REUSABLE PATTERN TEMPLATE

unique = sorted(set(nums))
left = 0
best = 0
for right, value in enumerate(unique):
    while value - unique[left] >= n:
        left += 1
    best = max(best, right-left+1)
return n-best


COMPLEXITY ANALYSIS

Sorting and deduplication O(n log n). Sliding window O(d), where d is number of distinct values <=n. Total O(n log n) time and O(n) space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"A continuous target array of length n must contain n distinct consecutive integers. I can keep original unique values that fit inside some range [x,x+n-1], and replace everything else. So I sort the unique values and use a sliding window to find the maximum number whose difference from the first is less than n. The minimum operations are n minus the largest window size. Sorting dominates at O(n log n)."


PATTERN MEMORY

After sorting and removing duplicates, any final continuous array of length n is a window of n distinct consecutive integer values. Maximize how many original unique values can be kept in one such range.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why duplicates are removed first.
[ ] Derive the inclusive range [x,x+n-1].
[ ] Use the condition unique[right]-unique[left] < n.
[ ] Explain why the largest window means fewest replacements.
[ ] Test duplicates and large gaps.
[ ] State O(n log n) time and O(n) space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Sorted unique values + sliding window is the clearest optimal answer: O(n log n) overall and O(d) window scan. If asked for another approach, use binary search for each left endpoint (O(d log d)); brute-force start enumeration is only a baseline.

ADDITIONAL IMPLEMENTATIONS: Brute force tries each distinct value as a possible range start and counts values that fit. Binary search finds the rightmost unique value below start+n for every left position. Sliding window avoids repeating searches by keeping the right pointer monotonic.

"""

def min_operations_continuous(nums: list[int]) -> int:
    n = len(nums)
    if n <= 1:
        return 0
    ordered = sorted(set(nums))
    best = 0
    right = 0
    for left in range(len(ordered)):
        while right < len(ordered) and ordered[right] - ordered[left] < n:
            right += 1
        best = max(best, right - left)
    return n - best


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        return min_operations_continuous(nums)


def run_tests() -> None:
    cases = [([4,2,5,3], 0), ([1,2,3,5,6], 1), ([1,10,100,1000], 3),
             ([8,5,9,9,8,4], 2), ([1], 0), ([-2,-1,0,1], 0)]
    for nums, expected in cases:
        assert min_operations_continuous(nums) == expected
    print("All Minimum Operations to Make Array Continuous test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def min_operations_continuous_bruteforce(nums: list[int]) -> int:
    """Brute-force over possible left endpoints after deduplication: O(d^2)."""
    n = len(nums)
    if n <= 1:
        return 0
    unique = sorted(set(nums))
    best = 0
    for start in unique:
        kept = sum(start <= value < start + n for value in unique)
        best = max(best, kept)
    return n - best


def min_operations_continuous_binary_search(nums: list[int]) -> int:
    """O(n log n + d log d): binary-search each window's right boundary."""
    from bisect import bisect_left
    n = len(nums)
    if n <= 1:
        return 0
    unique = sorted(set(nums))
    best = 0
    for left, start in enumerate(unique):
        right = bisect_left(unique, start + n, lo=left)
        best = max(best, right - left)
    return n - best


def run_additional_tests() -> None:
    cases = [([4, 2, 5, 3], 0), ([1, 2, 3, 5, 6], 1), ([1, 10, 100, 1000], 3),
             ([8, 5, 9, 9, 8, 4], 2), ([1], 0), ([-2, -1, 0, 1], 0), ([1, 1, 1, 1], 3)]
    for nums, expected in cases:
        assert min_operations_continuous_bruteforce(nums) == expected
        assert min_operations_continuous_binary_search(nums) == expected
        assert min_operations_continuous(nums) == expected
    print("Brute-force, binary-search and sliding-window continuous-array approaches passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
