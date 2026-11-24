"""
1051. HEIGHT CHECKER
LeetCode: https://leetcode.com/problems/height-checker/

PROBLEM
Return the number of indices where heights differs from its expected
non-decreasing sorted order.

Example:
[1,1,4,2,1,3] -> expected [1,1,1,2,3,4] -> answer 3

PATTERN
Sorting + Position Comparison / Counting Sort

APPROACH 1 — SORTED COPY
Create expected=sorted(heights), then count mismatching positions.
Time O(n log n), space O(n).

APPROACH 2 — COUNTING SORT
When the height range is small, count each height, rebuild the expected
sequence, and compare. Time O(n+range), space O(range).

DRY RUN
Original [1,1,4,2,1,3]
Expected [1,1,1,2,3,4]
Mismatches occur at indices 2, 4, 5 -> answer 3.

EDGE CASES
- Already sorted -> 0; all equal -> 0; one student; duplicates.

COMPLEXITY
Sorted-copy: O(n log n) time, O(n) space.
Counting: O(n+range) time, O(range) space.

INTERVIEW EXPLANATION
"The target arrangement is the sorted copy. I compare the original
and expected values at each index and count differences."

COMMON MISTAKES
- Counting swaps rather than mismatched positions.
- Sorting original input and losing its order.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The expected order is simply the sorted copy of the input. The task asks for mismatched positions, not the number of swaps needed.


APPROACH ANALYSIS

APPROACH 1 — SORTED COPY + COMPARISON (STANDARD)
Create expected=sorted(heights), then count indices where heights[i] != expected[i]. Time O(n log n), space O(n).

APPROACH 2 — COUNTING SORT
The original problem restricts heights to a small positive range. Count each height, reconstruct the expected order, and compare it against the original array. Time O(n+R), space O(R), where R is the value range. This is effectively linear when R is fixed.

WHY COUNT MISMATCHED INDICES?
The question defines the answer as positions that differ from expected order. It does not ask for the minimum number of swaps or the number of adjacent swaps.


WHY THE RECOMMENDED APPROACH WORKS

The sorted array is the unique expected non-decreasing sequence. Each index can be checked independently: if the original value differs from the value expected at that position, that position is incorrect. Summing these boolean comparisons counts exactly the requested number of indices.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

heights=[1,1,4,2,1,3]
expected=sorted(heights)=[1,1,1,2,3,4]
Index:       0 1 2 3 4 5
Original:    1 1 4 2 1 3
Expected:    1 1 1 2 3 4
Mismatch:    - - X - X X
Answer=3.


EDGE CASES TO TEST

- Already sorted -> 0.
- Reverse sorted.
- All values equal -> 0.
- One element -> 0.
- Duplicate heights.
- Empty input.


COMMON INTERVIEW MISTAKES

1. Counting swaps rather than positions that mismatch.
2. Sorting the original list in place and losing the original arrangement before comparison.
3. Comparing only adjacent pairs.
4. Returning the sorted array instead of an integer mismatch count.
5. Using counting sort without considering the allowed value range.


REUSABLE PATTERN TEMPLATE

expected = sorted(heights)
answer = sum(actual != target for actual, target in zip(heights, expected))


COMPLEXITY ANALYSIS

Sorted-copy approach: O(n log n) time and O(n) extra space. Counting approach: O(n+R) time and O(R) count storage, where R is the bounded height range.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I create the expected order by sorting a copy of heights. Then I compare the original and expected arrays at each index and count mismatches. That directly matches the definition of the problem. It takes O(n log n) time. Since the height range is bounded, a counting-sort version can achieve O(n+R)."


PATTERN MEMORY

The expected order is simply the sorted copy of the input. The task asks for mismatched positions, not the number of swaps needed.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain that the answer counts mismatched indices.
[ ] Do not mutate original input before comparison.
[ ] Implement sorted-copy solution.
[ ] Explain the bounded-range counting alternative.
[ ] Test already sorted and all-equal input.
[ ] State O(n log n) or O(n+R) according to the approach.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Sorting a copy and counting mismatched indices is the clearest answer. If the interviewer points out the small bounded height range, switch to counting sort for O(n+R) time. Do not confuse mismatched positions with minimum swaps.

ADDITIONAL IMPLEMENTATION: A Counter-based expected-order reconstruction avoids allocating a count array indexed by the height itself. It is useful when heights may be negative or the domain is not a small dense range.

"""

def height_checker_sorting(heights: list[int]) -> int:
    expected = sorted(heights)
    return sum(actual != target for actual, target in zip(heights, expected))


def height_checker_counting(heights: list[int]) -> int:
    if not heights:
        return 0
    if min(heights) < 0:
        raise ValueError("counting implementation expects non-negative heights")
    counts = [0] * (max(heights) + 1)
    for height in heights:
        counts[height] += 1
    index = mismatches = 0
    for height, count in enumerate(counts):
        for _ in range(count):
            if heights[index] != height:
                mismatches += 1
            index += 1
    return mismatches


class Solution:
    def heightChecker(self, heights: list[int]) -> int:
        return height_checker_sorting(heights)


def run_tests() -> None:
    cases = [([1,1,4,2,1,3], 3), ([5,1,2,3,4], 5), ([1,2,3,4], 0),
             ([1,1,1], 0), ([1], 0), ([], 0)]
    for heights, expected in cases:
        assert height_checker_sorting(heights) == expected
        assert height_checker_counting(heights) == expected
    print("All Height Checker test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def height_checker_counter(heights: list[int]) -> int:
    """Frequency-map alternative; O(n + d log d) time."""
    from collections import Counter
    frequency = Counter(heights)
    expected = []
    for value in sorted(frequency):
        expected.extend([value] * frequency[value])
    return sum(actual != target for actual, target in zip(heights, expected))


def run_additional_tests() -> None:
    cases = [([1, 1, 4, 2, 1, 3], 3), ([5, 1, 2, 3, 4], 5),
             ([1, 2, 3, 4, 5], 0), ([1, 1, 1], 0), ([-2, 0, -1], 2), ([], 0)]
    for values, expected in cases:
        assert height_checker_counter(values) == expected
        assert height_checker_sorting(values) == expected
    print("Counter-based Height Checker alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
