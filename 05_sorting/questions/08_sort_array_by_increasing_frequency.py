"""
1636. SORT ARRAY BY INCREASING FREQUENCY
LeetCode: https://leetcode.com/problems/sort-array-by-increasing-frequency/

PROBLEM
Sort values by increasing frequency. If frequencies tie, sort by
decreasing numeric value.

Example: [1,1,2,2,2,3] -> [3,1,1,2,2,2]

PATTERN
Hash Map / Frequency Counting + Custom Sort Key

KEY OBSERVATION
Use a tuple key: (frequency[value], -value). The first component sorts
frequency ascending; negative value sorts tied values descending.

APPROACH 1 — REPEATED COUNTING
Calling nums.count() for each item repeatedly is inefficient.
It can take O(n^2) just to count, plus sorting.

APPROACH 2 — COUNTER + SORT
Count once using Counter, then sort using the tuple key.
Time O(n log n), space O(d) frequency map plus sorting space.

DRY RUN
[1,1,2,2,2,3], frequencies {1:2, 2:3, 3:1}.
Keys: 3 -> (1,-3), 1 -> (2,-1), 2 -> (3,-2).
Output [3,1,1,2,2,2].

EDGE CASES
- Every value unique; all values equal; negative values; duplicates.

INTERVIEW EXPLANATION
"I build a frequency map, then sort by frequency ascending and value
descending using the key (frequency[value], -value)."

COMMON MISTAKES
- Using (frequency, value), which sorts ties ascending.
- Removing duplicates with set.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The sort key has two components: frequency ascending is primary, and numeric value descending is the tie-breaker. A tuple key expresses the rule directly.


APPROACH ANALYSIS

APPROACH 1 — REPEATED nums.count()
Sort with a key that calls nums.count(value). This performs a full scan for each element/key calculation and can take O(n²) frequency work. Avoid it.

APPROACH 2 — COUNTER + TUPLE KEY (STANDARD)
Build Counter(nums) once. Sort the original array with key=(frequency[value], -value). Python compares tuple components from left to right. The negative value makes larger values sort first when frequencies match. Time O(n log n); frequency map O(d).

APPROACH 3 — GROUP BY FREQUENCY
Group values by their count, process frequency levels ascending, sort values inside each level descending, and append each value count times. This makes the grouping idea explicit, though sorting groups still costs comparison time.


WHY THE RECOMMENDED APPROACH WORKS

The tuple key is equivalent to the problem statement. Its first component orders values by increasing frequency. Only when two frequencies are equal does Python compare the second component; using -value converts descending numeric order into ascending tuple order. Sorting nums rather than a set keeps every occurrence in the output.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[1,1,2,2,2,3]
frequency={1:2, 2:3, 3:1}
Keys:
3 -> (1,-3)
1 -> (2,-1)
2 -> (3,-2)

Sort tuple keys ascending:
(1,-3), (2,-1), (3,-2)
Expand original occurrences:
[3,1,1,2,2,2].

Tie-break example: if 4 and 9 both occur twice, keys (2,-4) and (2,-9) put 9 first.


EDGE CASES TO TEST

- Empty input.
- One distinct value.
- All values unique: all frequencies tie, so output is descending by value.
- Negative values.
- Several tie groups.
- Duplicates must remain.


COMMON INTERVIEW MISTAKES

1. Using (frequency[value], value), which sorts tied values ascending.
2. Repeatedly calling nums.count().
3. Sorting set(nums), which removes occurrences.
4. Reversing the whole result, which also reverses frequency order.
5. Forgetting the negative-value tie-break works for negative input too.


REUSABLE PATTERN TEMPLATE

frequency = Counter(nums)
answer = sorted(nums, key=lambda x: (frequency[x], -x))


COMPLEXITY ANALYSIS

Counter: O(n). Sorting: O(n log n) key comparisons. Total O(n log n) time. Frequency dictionary uses O(d) space, where d is the number of distinct values; sorting/output can require O(n) additional storage.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I count frequencies once with Counter. Then I sort the original list using a two-part key: frequency ascending, followed by negative value so larger values come first when frequencies tie. The original list is sorted rather than a set, so duplicates are preserved. The total time is O(n log n)."


PATTERN MEMORY

The sort key has two components: frequency ascending is primary, and numeric value descending is the tie-breaker. A tuple key expresses the rule directly.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain both sorting criteria in the correct priority.
[ ] Build Counter once.
[ ] Derive why -value means descending tie-break.
[ ] Test all values unique.
[ ] Test negative values and duplicates.
[ ] State O(n log n) time.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Counter + tuple key `(frequency[value], -value)` is the best first answer: concise, readable, O(n log n), and exactly matches both ordering rules. Grouping by frequency is a useful alternative when you want to build the answer explicitly by frequency.

ADDITIONAL IMPLEMENTATIONS: Repeated nums.count() is a brute-force reference and has O(n²) counting work. Frequency buckets group values by count; sorting each tie group descending preserves the required tie-break.

"""

from collections import Counter


def frequency_sort(nums: list[int]) -> list[int]:
    frequency = Counter(nums)
    return sorted(nums, key=lambda value: (frequency[value], -value))


class Solution:
    def frequencySort(self, nums: list[int]) -> list[int]:
        return frequency_sort(nums)


def run_tests() -> None:
    cases = [([1,1,2,2,2,3], [3,1,1,2,2,2]),
             ([2,3,1,3,2], [1,3,3,2,2]),
             ([-1,1,-1,2,2,2], [1,-1,-1,2,2,2]),
             ([5,5,5], [5,5,5]), ([], [])]
    for nums, expected in cases:
        assert frequency_sort(nums) == expected
    print("All Sort Array by Increasing Frequency test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def frequency_sort_bruteforce(nums: list[int]) -> list[int]:
    """Brute-force key repeatedly counts; intentionally inefficient O(n^2)."""
    return sorted(nums, key=lambda value: (nums.count(value), -value))


def frequency_sort_grouped(nums: list[int]) -> list[int]:
    """Group by frequency; sort frequency groups ascending and values descending."""
    from collections import Counter, defaultdict
    frequency = Counter(nums)
    groups = defaultdict(list)
    for value, count in frequency.items():
        groups[count].append(value)
    result = []
    for count in sorted(groups):
        for value in sorted(groups[count], reverse=True):
            result.extend([value] * count)
    return result


def run_additional_tests() -> None:
    cases = [
        ([1, 1, 2, 2, 2, 3], [3, 1, 1, 2, 2, 2]),
        ([2, 3, 1, 3, 2], [1, 3, 3, 2, 2]),
        ([1, 2, 3, 4], [4, 3, 2, 1]),
        ([-1, 1, -1, 2, 2, 2], [1, -1, -1, 2, 2, 2]),
    ]
    for nums, expected in cases:
        assert frequency_sort_bruteforce(nums) == expected
        assert frequency_sort_grouped(nums) == expected
    print("Brute-force key and frequency-grouping alternatives passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
