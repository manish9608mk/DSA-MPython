# 128. Longest Consecutive Sequence
"""
PROBLEM
Given an unsorted array of integers nums, return the length of the longest
sequence of consecutive values. Values in the sequence need not be adjacent
in the original array.

Example:
    nums = [100, 4, 200, 1, 3, 2]
    Output = 4
    Longest sequence: 1, 2, 3, 4

PATTERN
Hash Set / Sequence Expansion

APPROACH 1 — BRUTE FORCE
For every number, repeatedly check whether the next number exists in nums.
Using list membership takes O(n), and we may do it for each number:
Time O(n^2) worst case, Space O(1) extra (ignoring sequence storage).

APPROACH 2 — SORTING
Sort nums. Walk through the sorted list, counting consecutive values.
Duplicates should not break the sequence.
Time O(n log n), Space depends on sorting (Python sorted creates O(n) copy).

APPROACH 3 — OPTIMAL HASH SET
Put values in a set for O(1) average membership.
Only begin extending from a number if its predecessor (num - 1) is absent.
That means num is the beginning of a sequence; each sequence is expanded once.
Time O(n) average, Space O(n).

DRY RUN
nums = [100, 4, 200, 1, 3, 2]
set = {100, 4, 200, 1, 3, 2}

100: predecessor 99 absent -> sequence length 1
4: predecessor 3 present -> skip (not a start)
200: predecessor 199 absent -> length 1
1: predecessor 0 absent -> expand 1,2,3,4 -> length 4
3,2: predecessors present -> skip
Answer = 4

EDGE CASES
- Empty array -> 0
- Duplicates -> ignore duplicates
- Negative values -> works
- One value -> 1

INTERVIEW NOTE
The key optimization is not to expand every number. Start only at sequence
beginnings, identified by the absence of num - 1.
"""

# APPROACH 1 — BRUTE FORCE
def longest_consecutive_brute(nums: list[int]) -> int:
    best = 0
    for num in nums:
        length = 1
        current = num
        while current + 1 in nums:
            current += 1
            length += 1
        best = max(best, length)
    return best


# APPROACH 2 — SORTING
def longest_consecutive_sorting(nums: list[int]) -> int:
    if not nums:
        return 0

    arr = sorted(nums)
    best = current = 1

    for i in range(1, len(arr)):
        if arr[i] == arr[i - 1]:       # duplicate: ignore
            continue
        if arr[i] == arr[i - 1] + 1:   # consecutive
            current += 1
        else:
            current = 1
        best = max(best, current)

    return best


# APPROACH 3 — OPTIMAL: HASH SET
def longest_consecutive_hashset(nums: list[int]) -> int:
    values = set(nums)
    best = 0

    for num in values:
        if num - 1 not in values:      # sequence start
            current = num
            length = 1

            while current + 1 in values:
                current += 1
                length += 1

            best = max(best, length)

    return best


class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        return longest_consecutive_hashset(nums)


if __name__ == "__main__":
    tests = [
        ([100, 4, 200, 1, 3, 2], 4),
        ([], 0),
        ([1, 1, 2, 2, 3], 3),
        ([-3, -2, -1, 0, 2], 4),
        ([7], 1),
    ]

    for nums, expected in tests:
        results = [
            longest_consecutive_brute(nums),
            longest_consecutive_sorting(nums),
            longest_consecutive_hashset(nums),
        ]
        assert results == [expected] * 3
        print(f"nums={nums} -> {results[2]} | all approaches passed")

"""
COMPLEXITY
Approach             Time               Extra Space
Brute force         O(n^2) worst       O(1)
Sorting             O(n log n)          O(n) for sorted copy
Hash Set           O(n) average        O(n)

Pattern memory:
Unsorted values + consecutive sequence + fast membership
-> Hash Set
-> Expand only from sequence starts
"""
