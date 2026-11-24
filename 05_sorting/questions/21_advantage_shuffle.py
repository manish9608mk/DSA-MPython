"""
870. ADVANTAGE SHUFFLE
LeetCode: https://leetcode.com/problems/advantage-shuffle/

PROBLEM
Return a permutation of nums1 that maximizes the number of indices i
where nums1[i] > nums2[i].

Example: nums1=[2,7,11,15], nums2=[1,10,4,11]
One optimal answer: [2,11,7,15]

PATTERN
Sorting + Greedy + Two Pointers

KEY OBSERVATION
Use the smallest available nums1 value that can beat the smallest
remaining nums2 value. If it cannot beat that value, sacrifice it
against the largest remaining nums2 value.

APPROACH — SORT + GREEDY
1. Sort nums1.
2. Sort (value,index) pairs of nums2 by value.
3. Use left/right pointers over sorted nums2.
4. Assign current nums1 value to beat the smallest nums2 if possible;
   otherwise place it against the largest nums2.
5. Write result at original nums2 index.

DRY RUN
nums1 sorted=[2,7,11,15]
nums2 sorted by value: 1,4,10,11.
2 beats 1; 7 beats 4; 11 beats 10; 15 beats 11.
Each assignment is put back at the corresponding original index.

EDGE CASES
- Equal values; duplicates; negative values; one element.

COMPLEXITY
O(n log n) time and O(n) extra space.

INTERVIEW EXPLANATION
"I sort both sides while preserving nums2's original indices. I use a
nums1 value to beat the smallest nums2 value whenever possible. If it
cannot win, I use it against the largest opponent so it is not wasted."

COMMON MISTAKES
- Losing original positions of nums2.
- Wasting a large nums1 value on a value it barely beats.
- Sorting nums2 in place without remembering its original indices.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The objective is to maximize winning positions, not to sort both arrays in the same order. Use a greedy matching: spend the smallest value that can beat the current opponent; otherwise sacrifice the smallest remaining value.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE PERMUTATIONS
Try all permutations of nums1 and count wins. Time O(n! * n), infeasible.

APPROACH 2 — SORT + TWO POINTERS (GREEDY)
Sort nums1 and keep low/high pointers. Process nums2 in descending order of opponent value. If the largest remaining nums1 value beats this opponent, use it. Otherwise sacrifice the smallest remaining nums1 value against this opponent. Store each selected value at the original index of nums2.
Time O(n log n), space O(n).

A max-heap approach is also possible, but sorting is simpler in Python.


WHY THE RECOMMENDED APPROACH WORKS

Process the strongest opponent first. If our largest remaining value cannot beat this opponent, no remaining value can, so sacrificing the smallest causes the least damage. If our largest value can win, assigning the smallest winning value is enough in a more general greedy interpretation; the two-pointer variant shown uses largest-vs-largest and preserves any unnecessary smaller values for weaker opponents. Each selected value is used once, so the result is a permutation of nums1.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums1=[2,7,11,15]
nums2=[1,10,4,11]
Sort nums1=[2,7,11,15]
Process nums2 from largest to smallest while storing at original indices:
Opponent 11 at index 3: 15 wins -> answer[3]=15
Opponent 10 at index 1: 11 wins -> answer[1]=11
Opponent 4 at index 2: 7 wins -> answer[2]=7
Opponent 1 at index 0: 2 wins -> answer[0]=2
Answer=[2,11,7,15], four wins.


EDGE CASES TO TEST

- Equal values do not count as a win because comparison is strict >.
- Some opponents cannot be beaten.
- Duplicate values in either array.
- Negative values.
- Empty arrays.


COMMON INTERVIEW MISTAKES

1. Processing nums2 in sorted order but forgetting original indices.
2. Using >= instead of >.
3. Reusing a nums1 value.
4. Sacrificing a large value when no win is possible; sacrifice the smallest.
5. Returning the sorted nums1 instead of arranging values against original nums2 positions.


REUSABLE PATTERN TEMPLATE

ordered_opponents = sorted((value, i) for i, value in enumerate(nums2), reverse=True)
ours = sorted(nums1)
low, high = 0, len(ours)-1
answer = [0]*len(nums1)
for opponent, original_i in ordered_opponents:
    if ours[high] > opponent:
        answer[original_i] = ours[high]; high -= 1
    else:
        answer[original_i] = ours[low]; low += 1


COMPLEXITY ANALYSIS

Sorting both arrays costs O(n log n). The matching loop is O(n). Result and sorted copies use O(n) space. Total O(n log n) time and O(n) space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I sort our values and process the opponent values from largest to smallest, preserving their original indices. If my largest remaining value beats the current opponent, I assign it there. Otherwise even my largest cannot win, so I sacrifice my smallest value. This greedy strategy uses each value once and maximizes the number of winning positions. Sorting dominates at O(n log n)."


PATTERN MEMORY

The objective is to maximize winning positions, not to sort both arrays in the same order. Use a greedy matching: spend the smallest value that can beat the current opponent; otherwise sacrifice the smallest remaining value.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] State that a win requires strict greater-than.
[ ] Sort nums1 and process nums2 strongest-first.
[ ] Preserve original indices.
[ ] Explain why sacrificing the smallest is safe when no win is possible.
[ ] Confirm output is a permutation of nums1.
[ ] Test ties and unwinnable positions.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Sorting + two pointers is the best interview answer: O(n log n), O(n) space, and an easy greedy argument. Explain the key rule: beat the smallest opponent with the smallest value that can win; otherwise sacrifice the smallest value against the largest opponent. Preserve original indices.

ADDITIONAL IMPLEMENTATIONS: A second greedy ordering processes opponents strongest-first and matches with the largest remaining value, sacrificing the smallest if a win is impossible. A brute-force permutation checker is useful only for tiny arrays to verify optimal scores.

"""

def advantage_count(nums1: list[int], nums2: list[int]) -> list[int]:
    if len(nums1) != len(nums2):
        raise ValueError("arrays must have equal lengths")
    ordered_a = sorted(nums1)
    ordered_b = sorted((value, index) for index, value in enumerate(nums2))
    result = [0] * len(nums2)
    left, right = 0, len(nums2) - 1
    for value in ordered_a:
        if left <= right and value > ordered_b[left][0]:
            _, original_index = ordered_b[left]
            left += 1
        else:
            _, original_index = ordered_b[right]
            right -= 1
        result[original_index] = value
    return result


class Solution:
    def advantageCount(self, nums1: list[int], nums2: list[int]) -> list[int]:
        return advantage_count(nums1, nums2)


def advantage_score(result: list[int], nums2: list[int]) -> int:
    return sum(a > b for a, b in zip(result, nums2))


def run_tests() -> None:
    cases = [([2,7,11,15], [1,10,4,11], 4),
             ([12,24,8,32], [13,25,32,11], 3),
             ([1,1,1], [1,1,1], 0), ([5], [3], 1)]
    for a, b, expected_score in cases:
        result = advantage_count(a, b)
        assert sorted(result) == sorted(a)
        assert advantage_score(result, b) == expected_score
    print("All Advantage Shuffle test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def advantage_count_strongest_first(nums1: list[int], nums2: list[int]) -> list[int]:
    """Equivalent greedy: process strongest opponent first."""
    if len(nums1) != len(nums2):
        raise ValueError("arrays must have equal lengths")
    ours = sorted(nums1)
    opponents = sorted(((value, index) for index, value in enumerate(nums2)), reverse=True)
    low, high = 0, len(ours) - 1
    result = [0] * len(nums2)
    for opponent, original_index in opponents:
        if ours[high] > opponent:
            result[original_index] = ours[high]
            high -= 1
        else:
            result[original_index] = ours[low]
            low += 1
    return result


def advantage_count_bruteforce(nums1: list[int], nums2: list[int]) -> list[int]:
    """Tiny-input oracle: enumerate permutations and retain a max-score one."""
    from itertools import permutations
    best = None
    best_score = -1
    for candidate in permutations(nums1):
        score = sum(a > b for a, b in zip(candidate, nums2))
        if score > best_score:
            best_score = score
            best = list(candidate)
    return best if best is not None else []


def run_additional_tests() -> None:
    cases = [([2, 7, 11, 15], [1, 10, 4, 11]), ([12, 24, 8, 32], [13, 25, 32, 11]),
             ([1, 1, 1], [1, 1, 1]), ([5], [3]), ([2, 2, 3], [2, 3, 1])]
    for a, b in cases:
        result = advantage_count_strongest_first(a, b)
        assert sorted(result) == sorted(a)
        assert advantage_score(result, b) == advantage_score(advantage_count(a, b), b)
        if len(a) <= 7:
            oracle = advantage_count_bruteforce(a, b)
            assert advantage_score(result, b) == advantage_score(oracle, b)
    print("Strongest-first greedy and brute-force oracle passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
