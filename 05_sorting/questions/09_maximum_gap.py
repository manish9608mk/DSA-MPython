"""
164. MAXIMUM GAP
LeetCode: https://leetcode.com/problems/maximum-gap/

PROBLEM
Return the largest difference between successive values in sorted nums.
Return 0 if fewer than two values exist. Target: linear time and space.

Example: [3,6,9,1] -> sorted [1,3,6,9] -> answer 3

PATTERN
Bucket Sort / Pigeonhole Principle

APPROACH 1 — SORTING
Sort and scan adjacent values: O(n log n).

APPROACH 2 — BUCKET SORT
Let minimum=min(nums), maximum=max(nums). Use bucket size at least
ceil((maximum-minimum)/(n-1)). Store only min and max per bucket.
The maximum successive gap must occur between non-empty buckets.

DRY RUN
[3,6,9,1], min=1, max=9, n=4, bucket size=ceil(8/3)=3.
Bucket 0 contains 1,3; bucket 1 contains 6; bucket 2 contains 9.
Gaps between buckets: 6-3=3 and 9-6=3. Answer=3.

EDGE CASES
- Fewer than two values; all equal; negative values; two values only.

COMPLEXITY
O(n) time and O(n) extra space.

INTERVIEW EXPLANATION
"I choose bucket size using the average gap. The maximum gap cannot
be inside one bucket, so I compare the minimum of each non-empty
bucket with the maximum of the previous non-empty bucket."

COMMON MISTAKES
- Zero bucket size for equal values.
- Forgetting empty buckets.
- Using floor instead of ceiling for bucket size.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The required linear time rules out comparison sorting. The pigeonhole principle guarantees that the maximum adjacent gap is at least the average gap, allowing bucket summaries to replace full sorting.


APPROACH ANALYSIS

APPROACH 1 — SORT + ADJACENT SCAN
Sort nums and calculate max(nums[i]-nums[i-1]). It is the simplest correct solution but takes O(n log n), so it misses the target.

APPROACH 2 — BUCKET SORT + PIGEONHOLE PRINCIPLE
Let n be input size, lo=min(nums), hi=max(nums). There are n-1 adjacent gaps, so maximum gap >= (hi-lo)/(n-1). Set bucket width to ceil((hi-lo)/(n-1)), at least 1. Put each value in a bucket based on (value-lo)//bucket_width. Keep only min and max in each bucket. The maximum successive gap must be between consecutive non-empty buckets. Scan them and compare current_bucket_min - previous_bucket_max.
Time O(n), space O(n).


WHY THE RECOMMENDED APPROACH WORKS

There are n values distributed over a range of width hi-lo, producing n-1 adjacent gaps. Their sum is hi-lo, so at least one gap is at least their average. With the bucket width chosen from that average, an adjacent gap larger than the bucket width cannot be internal to one bucket. Therefore the global maximum gap is captured between non-empty buckets. Inside a bucket, only its minimum and maximum are relevant for neighboring gaps.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[3,6,9,1], n=4
lo=1, hi=9, range=8
Average gap=8/3, bucket width=ceil(8/3)=3

Bucket index = (value-lo)//3:
1 -> bucket 0
3 -> bucket 0
6 -> bucket 1
9 -> bucket 2

Summaries:
bucket 0: min=1,max=3
bucket 1: min=6,max=6
bucket 2: min=9,max=9

Gaps between non-empty buckets:
6-3=3
9-6=3
Answer=3.


EDGE CASES TO TEST

- n<2 -> 0.
- All values equal -> 0; handle before division.
- Negative values: subtract global minimum when computing bucket index.
- Large numeric range.
- Duplicate values.
- Empty buckets must be skipped.


COMMON INTERVIEW MISTAKES

1. Bucket width becomes zero for all-equal values.
2. Using floor average instead of a ceiling width.
3. Forgetting to offset negative values by lo.
4. Comparing bucket maxima to bucket maxima; the gap is current min minus previous non-empty max.
5. Considering empty buckets as if they contain values.
6. Calling sorted() in the claimed linear implementation.


REUSABLE PATTERN TEMPLATE

bucket_width = max(1, (hi-lo+n-2)//(n-1))
count = (hi-lo)//bucket_width + 1
bucket_min = [None]*count
bucket_max = [None]*count
for x in nums:
    idx = (x-lo)//bucket_width
    # update bucket min/max
previous_max = lo
answer = 0
for i in range(count):
    if bucket_min[i] is None: continue
    answer = max(answer, bucket_min[i]-previous_max)
    previous_max = bucket_max[i]


COMPLEXITY ANALYSIS

Sorting: O(n log n). Bucket placement and scanning: O(n + B), where B is bucket count and B=O(n). Total O(n) time and O(n) bucket storage.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"Because the problem asks for linear time, I avoid sorting. I find the minimum and maximum and divide the range into buckets. The maximum adjacent gap is at least the average range divided by n-1. So I choose a bucket width based on that average and store each bucket’s minimum and maximum. The maximum gap is between consecutive non-empty buckets, which I can scan in linear time."


PATTERN MEMORY

The required linear time rules out comparison sorting. The pigeonhole principle guarantees that the maximum adjacent gap is at least the average gap, allowing bucket summaries to replace full sorting.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why sort+scan misses the target complexity.
[ ] Derive the average-gap lower bound.
[ ] Handle all-equal input.
[ ] Use ceiling for bucket width.
[ ] Offset values by global minimum.
[ ] Compare current bucket min against previous bucket max.
[ ] Skip empty buckets.
[ ] State O(n) time and O(n) space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Because the prompt explicitly requires linear time and linear extra space, use the bucket method based on the pigeonhole principle. Start with sorting as a baseline, then derive the average-gap lower bound and compare non-empty buckets.

ADDITIONAL IMPLEMENTATION: LSD Radix Sort followed by an adjacent scan is another linear-time-style option for bounded-width integers. For Python arbitrary-precision integers, the number of digit passes depends on the bit length, so describe its complexity as O(d*(n+base)), not simply O(n) for unbounded values.

"""

def maximum_gap_sorting(nums: list[int]) -> int:
    if len(nums) < 2:
        return 0
    ordered = sorted(nums)
    return max(ordered[i] - ordered[i - 1] for i in range(1, len(ordered)))


def maximum_gap_bucket(nums: list[int]) -> int:
    n = len(nums)
    if n < 2:
        return 0
    minimum, maximum = min(nums), max(nums)
    if minimum == maximum:
        return 0

    bucket_size = max(1, (maximum - minimum + n - 2) // (n - 1))
    bucket_count = (maximum - minimum) // bucket_size + 1
    bucket_min = [None] * bucket_count
    bucket_max = [None] * bucket_count

    for value in nums:
        index = (value - minimum) // bucket_size
        if bucket_min[index] is None:
            bucket_min[index] = bucket_max[index] = value
        else:
            bucket_min[index] = min(bucket_min[index], value)
            bucket_max[index] = max(bucket_max[index], value)

    answer = 0
    previous_max = minimum
    for index in range(bucket_count):
        if bucket_min[index] is None:
            continue
        answer = max(answer, bucket_min[index] - previous_max)
        previous_max = bucket_max[index]
    return answer


class Solution:
    def maximumGap(self, nums: list[int]) -> int:
        return maximum_gap_bucket(nums)


def run_tests() -> None:
    cases = [([3,6,9,1], 3), ([10], 0), ([1,1,1], 0),
             ([1,10000000], 9999999), ([-10,-3,-1,4], 7), ([3,2,1,0], 1)]
    for nums, expected in cases:
        assert maximum_gap_sorting(nums) == expected
        assert maximum_gap_bucket(nums) == expected
    print("All Maximum Gap test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def maximum_gap_radix(nums: list[int], base: int = 256) -> int:
    """LSD radix sort using an offset; useful for bounded-width integers."""
    if len(nums) < 2:
        return 0
    minimum = min(nums)
    values = [value - minimum for value in nums]
    maximum = max(values)
    exp = 1
    while maximum // exp > 0:
        counts = [0] * base
        output = [0] * len(values)
        for value in values:
            counts[(value // exp) % base] += 1
        for i in range(1, base):
            counts[i] += counts[i - 1]
        for value in reversed(values):
            digit = (value // exp) % base
            counts[digit] -= 1
            output[counts[digit]] = value
        values = output
        exp *= base
    return max(values[i] - values[i - 1] for i in range(1, len(values)))


def run_additional_tests() -> None:
    cases = [([3, 6, 9, 1], 3), ([1, 10000000], 9999999), ([-10, -3, -1, 4], 7), ([1, 1, 1], 0), ([], 0)]
    for nums, expected in cases:
        assert maximum_gap_radix(nums) == expected
    print("Radix-sort Maximum Gap alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
