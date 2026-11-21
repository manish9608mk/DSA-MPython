"""
56. MERGE INTERVALS
LeetCode: https://leetcode.com/problems/merge-intervals/

PROBLEM
Given intervals [start, end], merge every overlapping interval and
return the non-overlapping intervals covering all input intervals.

Example:
    [[1,3], [2,6], [8,10], [15,18]] -> [[1,6], [8,10], [15,18]]

PATTERN
Sorting + Greedy + Interval Merging

KEY OBSERVATION
Sort by start. Once sorted, a new interval can overlap only the last
interval in the answer, so one scan is sufficient.

APPROACH — SORT + LINEAR SCAN
1. Sort intervals by their start value.
2. Add the first interval to the answer.
3. If current_start <= last_end, merge using max(last_end, current_end).
4. Otherwise, append a new interval.

DRY RUN
[[1,3], [2,6], [8,10], [15,18]]
[2,6] overlaps [1,3] -> [1,6].
[8,10] and [15,18] do not overlap.
Answer: [[1,6], [8,10], [15,18]]

EDGE CASES
- Empty list or one interval.
- All intervals overlap / none overlap.
- One interval is contained in another.
- Touching endpoints [1,4] and [4,5] merge.

COMPLEXITY
O(n log n) time for sorting + O(n) scan = O(n log n).
O(n) output space.

INTERVIEW EXPLANATION
"I sort by starting point. Then I scan once. If the next interval
starts before or at the end of the last merged interval, I extend it.
Otherwise, I start a new interval."

COMMON MISTAKES
- Checking current_end instead of current_start for overlap.
- Assigning current_end rather than max(last_end, current_end).
- Forgetting endpoint-touching intervals merge in this problem.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

Sorting converts a two-dimensional overlap search into a one-direction scan. Once intervals are ordered by start, only the last merged interval can overlap the next one.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE REPEATED MERGING
Compare pairs of intervals. Whenever two overlap, merge them and restart or recheck because the new wider interval might overlap another interval. This is easy to reason about for tiny input but can require many repeated scans. Worst-case time can be O(n²) or worse depending on the implementation.

APPROACH 2 — SORT BY START + SCAN (STANDARD)
1. Sort intervals by start.
2. Put the first interval into merged.
3. For each next [start,end], inspect merged[-1].
4. If start <= last_end, merge by assigning last_end=max(last_end,end).
5. Otherwise append a new interval.
Sorting costs O(n log n); the scan costs O(n).


WHY THE RECOMMENDED APPROACH WORKS

After sorting by start, all intervals begin in non-decreasing order. The last result interval represents the most recent connected block. If the current start is at most its end, the two intervals overlap or touch and their union ends at the larger endpoint. If current start is greater than that end, the current interval cannot overlap any earlier result interval either, so it begins a new block. Every input interval is processed exactly once after sorting.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

intervals = [[1,3],[2,6],[8,10],[15,18]]
After sorting: [[1,3],[2,6],[8,10],[15,18]]

Start merged = [[1,3]]
[2,6]: 2 <= 3, overlap -> end=max(3,6)=6
    merged = [[1,6]]
[8,10]: 8 > 6, separate -> append
    merged = [[1,6],[8,10]]
[15,18]: 15 > 10, separate -> append
    merged = [[1,6],[8,10],[15,18]]

Output = [[1,6],[8,10],[15,18]].
Boundary example: [1,4] and [4,5] merge because the comparison is <=.


EDGE CASES TO TEST

- Empty input returns [].
- One interval returns the same interval.
- All intervals overlap: one result interval.
- No intervals overlap: n result intervals.
- Containment: [1,10] with [2,3] remains [1,10].
- Touching endpoints count as overlap in this problem.
- Negative endpoints and unsorted input.


COMMON INTERVIEW MISTAKES

1. Sorting by end when the scan expects start order.
2. Checking current_end instead of current_start.
3. Assigning last_end=current_end instead of max(last_end,current_end), which can shrink a merged interval.
4. Using < instead of <= and missing endpoint-touching cases.
5. Forgetting empty input.
6. Accidentally mutating the caller’s interval lists when a new result is expected.


REUSABLE PATTERN TEMPLATE

ordered = sorted(intervals, key=lambda item: item[0])
merged = []
for start, end in ordered:
    if not merged or start > merged[-1][1]:
        merged.append([start, end])
    else:
        merged[-1][1] = max(merged[-1][1], end)
return merged


COMPLEXITY ANALYSIS

Repeated pairwise merging: typically O(n²) or worse. Sort + scan: O(n log n) time plus O(n) for the scan. Output is O(n) in the worst case. Sorting may also allocate internal memory depending on implementation.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I sort the intervals by their start time. Then I scan once, keeping a list of merged intervals. If the next start is at most the end of the last result interval, I extend that end using max. Otherwise I append a new interval. Sorting takes O(n log n), and the scan is O(n), so the overall complexity is O(n log n)."


PATTERN MEMORY

Sorting converts a two-dimensional overlap search into a one-direction scan. Once intervals are ordered by start, only the last merged interval can overlap the next one.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] State why sorting by start is useful.
[ ] Remember the overlap condition start <= last_end.
[ ] Use max() when extending the end.
[ ] Handle nested intervals.
[ ] Handle endpoint-touching intervals.
[ ] Handle empty input.
[ ] State O(n log n) time and O(n) result space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Sort by start and scan once. This is the standard optimal solution: O(n log n) overall, with an O(n) scan. Explain the invariant that only the last merged interval can overlap the next one. Use brute-force pair merging only to demonstrate why sorting is better.

ADDITIONAL IMPLEMENTATIONS: Pairwise repeated merging is a valid brute-force baseline but can take O(n³) with repeated comparisons and list deletions. The in-place sort-and-compact version avoids allocating a second result list but mutates the input.

"""

def merge_intervals(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    ordered = sorted(intervals, key=lambda interval: interval[0])
    merged = [ordered[0][:]]
    for start, end in ordered[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    return merged


class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        return merge_intervals(intervals)


def run_tests() -> None:
    cases = [([[1,3],[2,6],[8,10],[15,18]], [[1,6],[8,10],[15,18]]),
             ([[1,4],[4,5]], [[1,5]]), ([[1,4],[2,3]], [[1,4]]), ([], [])]
    for source, expected in cases:
        assert merge_intervals(source) == expected
    print("All Merge Intervals test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def merge_intervals_pairwise(intervals: list[list[int]]) -> list[list[int]]:
    """Brute-force baseline: repeatedly merge any overlapping pair."""
    work = [interval[:] for interval in intervals]
    changed = True
    while changed:
        changed = False
        for i in range(len(work)):
            for j in range(i + 1, len(work)):
                a, b = work[i], work[j]
                if a[0] <= b[1] and b[0] <= a[1]:
                    work[i] = [min(a[0], b[0]), max(a[1], b[1])]
                    work.pop(j)
                    changed = True
                    break
            if changed:
                break
    return sorted(work, key=lambda x: x[0])


def merge_intervals_in_place(intervals: list[list[int]]) -> list[list[int]]:
    """Sort and compact the caller's list in-place; output aliases input."""
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    write = 0
    for start, end in intervals[1:]:
        if start <= intervals[write][1]:
            intervals[write][1] = max(intervals[write][1], end)
        else:
            write += 1
            intervals[write] = [start, end]
    del intervals[write + 1:]
    return intervals


def run_additional_tests() -> None:
    cases = [
        ([[1, 3], [2, 6], [8, 10], [15, 18]], [[1, 6], [8, 10], [15, 18]]),
        ([[1, 4], [4, 5]], [[1, 5]]),
        ([[1, 10], [2, 3], [4, 8]], [[1, 10]]),
        ([], []),
        ([[-5, -1], [-3, 0], [2, 4]], [[-5, 0], [2, 4]]),
    ]
    for source, expected in cases:
        assert merge_intervals_pairwise(source) == expected
        mutable = [x[:] for x in source]
        assert merge_intervals_in_place(mutable) == expected
    print("Pairwise and in-place Merge Intervals alternatives passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
