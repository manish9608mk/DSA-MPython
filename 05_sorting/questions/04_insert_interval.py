"""
57. INSERT INTERVAL
LeetCode: https://leetcode.com/problems/insert-interval/

PROBLEM
Given sorted, non-overlapping intervals and a new interval, insert it
and merge where necessary. Keep the result sorted and non-overlapping.

Example:
    intervals = [[1,3], [6,9]], newInterval = [2,5]
    Output = [[1,5], [6,9]]

PATTERN
Intervals + Greedy + Linear Scan

IMPORTANT
The input intervals are already sorted and non-overlapping. No extra
sorting is needed.

APPROACH — THREE PHASES
1. Copy intervals ending before newInterval starts.
2. Merge every interval whose start <= current merged end.
3. Append the merged interval, then append the remaining intervals.

DRY RUN
[[1,3], [6,9]], new = [2,5]
[1,3] overlaps and expands new to [1,5]. [6,9] is after it.
Output: [[1,5], [6,9]]

EDGE CASES
- Empty input.
- New interval before or after every interval.
- New interval overlaps all intervals.
- New interval is fully contained in an existing interval.

COMPLEXITY
O(n) time and O(n) output space.

INTERVIEW EXPLANATION
"Because intervals are already sorted, I scan once: first copy those
before the new interval, then merge overlaps, then append the rest."

COMMON MISTAKES
- Sorting again unnecessarily.
- Forgetting to append the merged interval.
- Mutating newInterval supplied by the caller.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The input is already sorted and non-overlapping, so sorting again wastes work. The answer is constructed with three phases: copy-before, merge-overlap, append-after.


APPROACH ANALYSIS

APPROACH 1 — APPEND + SORT + MERGE
Append the new interval, sort all intervals by start, then reuse Merge Intervals. It is correct but costs O(n log n).

APPROACH 2 — THREE-PHASE LINEAR SCAN (OPTIMAL)
Phase 1: while existing_end < new_start, copy the interval. It is strictly before the new interval.
Phase 2: while existing_start <= new_end, merge using start=min(start,existing_start) and end=max(end,existing_end). The new interval may expand during this phase.
Phase 3: append all remaining intervals; sorted order guarantees they are after the merged interval.
Every interval is visited once: O(n) time; output needs O(n) space.


WHY THE RECOMMENDED APPROACH WORKS

Because the original intervals are sorted and disjoint, every interval ending before the current new start can be safely copied. The first interval whose start is at most the merged end overlaps; merging may expand the range and allow the next interval to overlap too. Once an interval starts after the current end, no later interval can overlap because starts are sorted. This proves the three loops are correct and linear.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

Phase 1: [1,2] ends before 4 -> copy.
result = [[1,2]]

Phase 2:
[3,5] overlaps -> merged becomes [3,8]
[6,7] overlaps -> still [3,8]
[8,10] touches -> merged becomes [3,10]
[12,16] starts after 10 -> stop.

Append merged [3,10], then append [12,16].
Output = [[1,2],[3,10],[12,16]].


EDGE CASES TO TEST

- Empty intervals: output contains only newInterval.
- New interval is before all or after all intervals.
- New interval lies entirely inside one existing interval.
- New interval bridges several intervals.
- It overlaps exactly one interval.
- Endpoint equality is treated as overlap.
- The implementation should avoid mutating the supplied newInterval list.


COMMON INTERVIEW MISTAKES

1. Sorting the original input even though it is already sorted.
2. Using a fixed original end during the overlap loop instead of the updated merged end.
3. Forgetting to append the merged interval once.
4. Forgetting the remaining intervals after merging.
5. Using the wrong strict/non-strict boundary comparison.
6. Modifying input sublists unexpectedly.


REUSABLE PATTERN TEMPLATE

result = []
i = 0
start, end = new_interval
while i < n and intervals[i][1] < start:
    result.append(intervals[i][:]); i += 1
while i < n and intervals[i][0] <= end:
    start = min(start, intervals[i][0])
    end = max(end, intervals[i][1])
    i += 1
result.append([start, end])
result.extend(x[:] for x in intervals[i:])


COMPLEXITY ANALYSIS

Append + sort + merge: O(n log n) time. Three-phase scan: O(n) time because each interval is visited once. Output space is O(n).


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"The intervals are already sorted and non-overlapping, so I do not sort again. I first copy intervals that finish before the new interval. Then I merge every interval whose start is at most the current merged end, expanding start and end with min and max. Finally I append the merged interval and all remaining intervals. That is O(n) time."


PATTERN MEMORY

The input is already sorted and non-overlapping, so sorting again wastes work. The answer is constructed with three phases: copy-before, merge-overlap, append-after.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain all three phases.
[ ] Use the updated end in the overlap loop.
[ ] Dry-run an interval that bridges multiple ranges.
[ ] Handle empty input.
[ ] Explain why endpoint equality merges.
[ ] Compare linear scan with append-and-sort.

"""

def insert_interval(intervals: list[list[int]], new_interval: list[int]) -> list[list[int]]:
    result = []
    i = 0
    start, end = new_interval
    n = len(intervals)

    while i < n and intervals[i][1] < start:
        result.append(intervals[i][:])
        i += 1

    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1

    result.append([start, end])
    while i < n:
        result.append(intervals[i][:])
        i += 1
    return result


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        return insert_interval(intervals, newInterval)


def run_tests() -> None:
    cases = [([[1,3],[6,9]], [2,5], [[1,5],[6,9]]),
             ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8], [[1,2],[3,10],[12,16]]),
             ([], [5,7], [[5,7]]), ([[1,5]], [2,3], [[1,5]])]
    for intervals, new_interval, expected in cases:
        assert insert_interval(intervals, new_interval) == expected
    print("All Insert Interval test cases passed.")


if __name__ == "__main__":
    run_tests()
