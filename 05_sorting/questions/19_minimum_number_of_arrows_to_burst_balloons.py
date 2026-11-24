"""
452. MINIMUM NUMBER OF ARROWS TO BURST BALLOONS
LeetCode: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

PROBLEM
Each balloon is an interval [x_start,x_end]. One arrow at x bursts all
balloons whose interval contains x. Return the minimum arrows needed.

Example: [[10,16],[2,8],[1,6],[7,12]] -> 2

PATTERN
Sorting + Greedy + Interval Scheduling

APPROACH — SORT BY END + GREEDY
1. Sort balloons by ending coordinate.
2. Shoot the first arrow at the first balloon's end.
3. If next balloon starts <= arrow position, it is already burst.
4. Otherwise shoot a new arrow at its end.

WHY SORT BY END?
Choosing the earliest finishing interval leaves the most room for
future intervals to share that arrow.

DRY RUN
Sorted: [[1,6],[2,8],[7,12],[10,16]]
Shoot at 6; [2,8] shares it. Shoot at 12; [10,16] shares it.
Answer=2.

EDGE CASES
- Empty input -> 0; all overlap -> 1; none overlap -> n.
- Touching endpoints can share an arrow.

COMPLEXITY
O(n log n) time, O(1) extra scan space apart from sorting.

INTERVIEW EXPLANATION
"I sort by end. I shoot at the end of the earliest-ending balloon.
Every later balloon starting at or before that point shares the arrow.
When a start is beyond it, I need another arrow."

COMMON MISTAKES
- Sorting by start with this exact greedy proof.
- Using < instead of <= for touching endpoints.
- Comparing balloon end instead of start to arrow position.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

This is the interval-stabbing version of interval scheduling. Sort by earliest end and shoot at that endpoint to cover as many future intervals as possible.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE SEARCH
Try candidate arrow positions and repeatedly remove all balloons they burst. Choosing the best point at each stage is expensive and unnecessary.

APPROACH 2 — SORT BY END + GREEDY (OPTIMAL)
Sort balloons by end coordinate. Shoot the first arrow at the end of the first balloon. Skip every later balloon whose start <= arrow_position. When a balloon starts > arrow_position, it cannot be burst by the current arrow, so shoot a new arrow at its end.
Time O(n log n), scan O(n), extra space O(1) beyond sorting.


WHY THE RECOMMENDED APPROACH WORKS

Consider the balloon with the earliest end. Any valid solution must shoot an arrow at some point inside it. Shooting at its end is at least as good as shooting earlier: every other balloon that overlaps an earlier point and begins before that point also contains the earliest end, while the endpoint leaves maximum room for balloons that begin later. Repeating this exchange argument gives the greedy algorithm.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

points=[[10,16],[2,8],[1,6],[7,12]]
Sort by end:
[[1,6],[2,8],[7,12],[10,16]]

Shoot at x=6 for [1,6]. [2,8] contains 6, so it is covered.
[7,12] starts after 6 -> need another arrow at 12.
[10,16] contains 12, so it is covered.
Total arrows=2.


EDGE CASES TO TEST

- Empty points -> 0.
- One balloon -> 1.
- All balloons overlap -> 1.
- Pairwise disjoint intervals -> n arrows.
- Touching endpoints can share an arrow.
- Negative coordinates.
- Very large coordinate values.


COMMON INTERVIEW MISTAKES

1. Sorting by start instead of end for this greedy choice.
2. Comparing balloon end with arrow position rather than balloon start.
3. Using start >= arrow_position; equality means an arrow at the endpoint bursts it.
4. Forgetting empty input.
5. Choosing the midpoint instead of the earliest end; that can reduce future overlap.


REUSABLE PATTERN TEMPLATE

points.sort(key=lambda p: p[1])
arrows = 0
arrow_x = None
for start, end in points:
    if arrow_x is None or start > arrow_x:
        arrows += 1
        arrow_x = end
return arrows


COMPLEXITY ANALYSIS

Sorting O(n log n), greedy scan O(n). Total O(n log n) time. Extra scan space O(1), apart from sorting implementation details.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I sort balloons by their end coordinate. I place an arrow at the end of the earliest-ending balloon. Every later balloon whose start is at or before that position is burst by the same arrow. If a balloon starts after the current arrow position, I need another arrow at its end. This greedy strategy minimizes arrows and takes O(n log n) time due to sorting."


PATTERN MEMORY

This is the interval-stabbing version of interval scheduling. Sort by earliest end and shoot at that endpoint to cover as many future intervals as possible.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why earliest end is the greedy choice.
[ ] Sort by end coordinate.
[ ] Use start > arrow_x to decide a new arrow.
[ ] Remember endpoint equality is covered.
[ ] Handle empty input.
[ ] State O(n log n) time.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Sort by end coordinate and greedily shoot at the earliest finishing balloon’s end. It is the clearest optimal greedy proof and takes O(n log n). A start-sorted intersection method is an equally valid alternative.

ADDITIONAL IMPLEMENTATION: Sort by start and maintain the intersection of the current group: update the common right boundary with min(end); when the next start exceeds that boundary, a new arrow is required.

"""

def find_min_arrow_shots(points: list[list[int]]) -> int:
    if not points:
        return 0
    ordered = sorted(points, key=lambda balloon: balloon[1])
    arrows = 1
    arrow_position = ordered[0][1]
    for start, end in ordered[1:]:
        if start > arrow_position:
            arrows += 1
            arrow_position = end
    return arrows


class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        return find_min_arrow_shots(points)


def run_tests() -> None:
    cases = [([[10,16],[2,8],[1,6],[7,12]], 2),
             ([[1,2],[3,4],[5,6],[7,8]], 4),
             ([[1,2],[2,3],[3,4],[4,5]], 2),
             ([[1,10],[2,9],[3,8]], 1), ([], 0), ([[-5,-1],[-3,0],[1,2]], 2)]
    for points, expected in cases:
        assert find_min_arrow_shots(points) == expected
    print("All Minimum Number of Arrows test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def min_arrows_sort_by_start(points: list[list[int]]) -> int:
    """Alternative greedy: sort by start and shrink the current intersection."""
    if not points:
        return 0
    ordered = sorted(points, key=lambda interval: interval[0])
    arrows = 0
    intersection_end = None
    for start, end in ordered:
        if intersection_end is None or start > intersection_end:
            arrows += 1
            intersection_end = end
        else:
            intersection_end = min(intersection_end, end)
    return arrows


def run_additional_tests() -> None:
    cases = [([[10, 16], [2, 8], [1, 6], [7, 12]], 2),
             ([[1, 2], [3, 4], [5, 6], [7, 8]], 4),
             ([[1, 2], [2, 3], [3, 4], [4, 5]], 2),
             ([[1, 10], [2, 9], [3, 8]], 1), ([], 0), ([[-5, -1], [-3, 0], [1, 2]], 2)]
    for points, expected in cases:
        assert min_arrows_sort_by_start(points) == expected
        assert find_min_arrow_shots(points) == expected
    print("Start-sorted interval-intersection greedy alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
