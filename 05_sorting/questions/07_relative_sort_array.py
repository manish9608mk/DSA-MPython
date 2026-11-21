"""
1122. RELATIVE SORT ARRAY
LeetCode: https://leetcode.com/problems/relative-sort-array/

PROBLEM
Sort arr1 so its relative order follows arr2. Values absent from arr2
must appear at the end in ascending order.

Example:
arr1=[2,3,1,3,2,4,6,7,9,2,19]
arr2=[2,1,4,3,9,6]
Output=[2,2,2,1,4,3,3,9,6,7,19]

PATTERN
Frequency Counting / Counting Sort / Custom Sort Key

APPROACH 1 — CUSTOM KEY
Create a rank map from arr2 and sort arr1 by (rank, value).
Time O(n log n), space O(n+m).

APPROACH 2 — FREQUENCY MAP
1. Count arr1.
2. Emit each arr2 value according to its frequency.
3. Sort and emit remaining values.
Time O(n + m + r log r), where r is distinct leftover values.

DRY RUN
Counts: 2->3, 3->2, 1->1, 4->1, 6->1, 7->1, 9->1, 19->1.
Emit in arr2 order, then leftovers [7,19].

EDGE CASES
- Empty arr2; values absent from arr2; duplicates; negative values.

COMPLEXITY
O(n + m + r log r) time, O(n) extra space.

INTERVIEW EXPLANATION
"I count each value. Then I follow arr2 to write its values in the
required order. Finally, I append the remaining values in ascending
order."

COMMON MISTAKES
- Sorting everything numerically.
- Forgetting leftover values or duplicates.
- Converting arr2 to a set and losing its ordering.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

There are two separate ordering rules: values appearing in arr2 follow arr2 order; all other values come last in ascending order. A frequency map preserves duplicates.


APPROACH ANALYSIS

APPROACH 1 — CUSTOM SORT KEY
Build rank[value]=index for every item in arr2. Sort arr1 by (rank.get(value, len(arr2)), value). Values in arr2 follow their rank; unlisted values share the fallback rank and then sort numerically. Time O(n log n + m).

APPROACH 2 — COUNTER + EMIT (RECOMMENDED)
Count arr1 with Counter. Traverse arr2 in order and append each value count times, removing its key from the counter. Sort the remaining keys and append all their remaining copies. Time O(n+m+r log r), where r is the number of leftover distinct values.

APPROACH 3 — COUNTING ARRAY
When the value range R is small and known, use an array of counts and emit values in the required order. Time O(n+R), space O(R).


WHY THE RECOMMENDED APPROACH WORKS

The counter records multiplicity without needing to search the input repeatedly. Processing arr2 directly guarantees the required relative order. Removing processed keys leaves exactly the values not specified by arr2; sorting those keys gives the required ascending suffix. Extending by the stored count keeps every duplicate.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

arr1=[2,3,1,3,2,4,6,7,9,2,19]
arr2=[2,1,4,3,9,6]

Counter: 2:3, 3:2, 1:1, 4:1, 6:1, 7:1, 9:1, 19:1
Emit in arr2 order:
2 -> [2,2,2]
1 -> add [1]
4 -> add [4]
3 -> add [3,3]
9 -> add [9]
6 -> add [6]
Result = [2,2,2,1,4,3,3,9,6]
Leftover keys 7 and 19 -> append [7,19].


EDGE CASES TO TEST

- Empty arr1.
- Empty arr2: all values become ascending.
- arr2 contains a value absent from arr1.
- arr1 contains values not listed in arr2.
- Many duplicates.
- Negative values work with Counter and sorted leftovers.


COMMON INTERVIEW MISTAKES

1. Using set(arr1), which loses duplicates.
2. Sorting the whole array numerically and ignoring arr2.
3. Appending leftover distinct keys only once instead of count times.
4. Forgetting that arr2 might mention an absent value.
5. Using a tuple key in the wrong order.


REUSABLE PATTERN TEMPLATE

counts = Counter(arr1)
result = []
for value in arr2:
    result.extend([value] * counts.pop(value, 0))
for value in sorted(counts):
    result.extend([value] * counts[value])
return result


COMPLEXITY ANALYSIS

Counter + emit: O(n+m+r log r) time and O(n) storage for counts/output. Custom key: O(n log n + m) time and O(n+m) memory. Counting array: O(n+R) time and O(R) counts when the value range R is bounded.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I count the values in arr1. Then I iterate through arr2 in its exact order and append each value as many times as it occurs. After that, the remaining counter entries are values absent from arr2. I sort those remaining values and append all their copies. This satisfies both ordering rules and preserves duplicates."


PATTERN MEMORY

There are two separate ordering rules: values appearing in arr2 follow arr2 order; all other values come last in ascending order. A frequency map preserves duplicates.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain the two ordering rules.
[ ] Build a Counter.
[ ] Emit arr2 values in exact order.
[ ] Remove or zero out processed counts.
[ ] Append leftovers in ascending order and preserve counts.
[ ] Explain custom sort-key and counting-array alternatives.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: For the original bounded-value constraints, a counting array is a strong linear-time answer. For a general integer domain, Counter + emit arr2 order + sorted leftovers is the clearest robust solution. Custom sort key is the simplest one-liner alternative.

ADDITIONAL IMPLEMENTATION: Bounded counting sort uses an offset so it also supports negative values. Its time is O(n+R), where R=max-min+1; use it only when R is moderate.

"""

from collections import Counter


def relative_sort_array(arr1: list[int], arr2: list[int]) -> list[int]:
    counts = Counter(arr1)
    result = []
    for value in arr2:
        result.extend([value] * counts.pop(value, 0))
    remaining = []
    for value, count in counts.items():
        remaining.extend([value] * count)
    result.extend(sorted(remaining))
    return result


def relative_sort_array_custom_key(arr1: list[int], arr2: list[int]) -> list[int]:
    rank = {value: index for index, value in enumerate(arr2)}
    return sorted(arr1, key=lambda value: (rank.get(value, len(rank)), value))


class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:
        return relative_sort_array(arr1, arr2)


def run_tests() -> None:
    cases = [([2,3,1,3,2,4,6,7,9,2,19], [2,1,4,3,9,6],
              [2,2,2,1,4,3,3,9,6,7,19]),
             ([28,6,22,8,44,17], [22,28,8,6], [22,28,8,6,17,44]),
             ([1,2,3], [], [1,2,3]), ([-1,2,-1,3], [2], [2,-1,-1,3])]
    for a, b, expected in cases:
        assert relative_sort_array(a, b) == expected
        assert relative_sort_array_custom_key(a, b) == expected
    print("All Relative Sort Array test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def relative_sort_array_counting(arr1: list[int], arr2: list[int]) -> list[int]:
    """Counting-array approach; O(n+R) time and O(R) count space."""
    if not arr1:
        return []
    low, high = min(arr1), max(arr1)
    counts = [0] * (high - low + 1)
    for value in arr1:
        counts[value - low] += 1
    result = []
    for value in arr2:
        index = value - low
        if 0 <= index < len(counts):
            result.extend([value] * counts[index])
            counts[index] = 0
    for offset, count in enumerate(counts):
        if count:
            result.extend([low + offset] * count)
    return result


def run_additional_tests() -> None:
    cases = [
        ([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6], [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]),
        ([28, 6, 22, 8, 44, 17], [22, 28, 8, 6], [22, 28, 8, 6, 17, 44]),
        ([-1, 2, -1, 3], [2], [2, -1, -1, 3]),
    ]
    for a, b, expected in cases:
        assert relative_sort_array_counting(a, b) == expected
    print("Bounded counting-array Relative Sort alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
