# 454. 4Sum II
"""
PROBLEM
Given four integer arrays nums1, nums2, nums3, nums4 of equal length n,
count tuples (i, j, k, l) such that:
nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0.

Example:
    nums1 = [1, 2]
    nums2 = [-2, -1]
    nums3 = [-1, 2]
    nums4 = [0, 2]
    Output = 2

PATTERN
Hash Map / Pair Sums / Meet in the Middle

APPROACH 1 — BRUTE FORCE
Check all n^4 combinations.
Time O(n^4), Space O(1).

APPROACH 2 — OPTIMAL: HASH MAP + SPLIT INTO PAIRS
Instead of four nested loops, split the equation:
    (a + b) + (c + d) = 0
For each pair from nums1 and nums2, count each sum in a dictionary.
Then for each pair from nums3 and nums4, look for -(c + d).
If that complement is in the map, add its frequency (not just 1),
because multiple pairs may produce the same sum.
Time O(n^2) average, Space O(n^2).

DRY RUN (small example)
A=[1], B=[-1], C=[0], D=[0]
A+B sum = 0 -> map {0: 1}
C+D sum = 0 -> need 0; frequency is 1
Answer = 1

EDGE CASES
- Repeated values / repeated pair sums: add frequency, not just boolean.
- Negative and zero values: dictionary handles them.
- Empty arrays: answer 0.

INTERVIEW NOTE
This is a meet-in-the-middle trick: turn four choices into two pair-sum
collections, and use a hash map to match complements.
"""

# APPROACH 1 — BRUTE FORCE (FOUR LOOPS)
def four_sum_count_brute(a: list[int], b: list[int],
                         c: list[int], d: list[int]) -> int:
    count = 0
    for x in a:
        for y in b:
            for z in c:
                for w in d:
                    if x + y + z + w == 0:
                        count += 1
    return count


# APPROACH 2 — OPTIMAL: HASH MAP OF PAIR SUMS
def four_sum_count_hashmap(a: list[int], b: list[int],
                           c: list[int], d: list[int]) -> int:
    pair_frequency = {}

    for x in a:
        for y in b:
            total = x + y
            pair_frequency[total] = pair_frequency.get(total, 0) + 1

    answer = 0
    for z in c:
        for w in d:
            needed = -(z + w)
            answer += pair_frequency.get(needed, 0)

    return answer


class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int],
                     nums3: list[int], nums4: list[int]) -> int:
        return four_sum_count_hashmap(nums1, nums2, nums3, nums4)


if __name__ == "__main__":
    tests = [
        ([1, 2], [-2, -1], [-1, 2], [0, 2], 2),
        ([0], [0], [0], [0], 1),
        ([1], [1], [1], [1], 0),
        ([1, 1], [-1, -1], [0, 0], [0, 0], 8),
    ]

    for a, b, c, d, expected in tests:
        result = four_sum_count_hashmap(a, b, c, d)
        assert result == expected
        print(f"Result={result} | expected={expected} | passed")

"""
COMPLEXITY
Brute force: O(n^4) time, O(1) extra space.
Pair-sum map: O(n^2) average time, O(n^2) space.

Pattern memory:
Four values sum to target
-> Split into two pairs
-> Store first pair sums with counts
-> Search complement for second pair
"""
