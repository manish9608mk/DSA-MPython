"""
1331. RANK TRANSFORM OF AN ARRAY
LeetCode: https://leetcode.com/problems/rank-transform-of-an-array/

PROBLEM
Replace every value with its rank. Rank starts at 1; equal values get
the same rank; larger values get larger ranks.

Example: [40,10,20,30] -> [4,1,2,3]

PATTERN
Sorting + Hash Map / Coordinate Compression

APPROACH 1 — SORT UNIQUE VALUES
1. Get distinct values.
2. Sort ascending.
3. Assign ranks starting at 1.
4. Map original array through the rank dictionary.
Time O(n log n), space O(n).

DRY RUN
Sorted unique values: [10,20,30,40].
Ranks: 10->1, 20->2, 30->3, 40->4.
Original order [40,10,20,30] becomes [4,1,2,3].

EDGE CASES
- Empty array; all equal; negative values; duplicate values.

COMPLEXITY
O(n log n) time and O(n) space.

INTERVIEW EXPLANATION
"I use coordinate compression: sort unique values and assign each a
consecutive rank. A dictionary maps each original value to its rank."

COMMON MISTAKES
- Giving duplicates different ranks.
- Starting at rank zero.
- Returning sorted ranks rather than preserving original order.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

Rank is determined by relative order among distinct values, not by the raw numeric distance. This is coordinate compression.


APPROACH ANALYSIS

APPROACH 1 — SORT UNIQUE VALUES + MAP (OPTIMAL STANDARD)
Create sorted(set(arr)). Assign ranks 1,2,... to those values. Build a dictionary value->rank and map each original element through it. Time O(n log n), space O(n).

APPROACH 2 — SORT PAIRS WITH ORIGINAL INDICES
Sort (value,index) pairs and assign a new rank only when the value changes. Write the rank into answer[index]. This makes index restoration explicit but requires more bookkeeping.

APPROACH 3 — DIRECT VALUE RANGE
If values occupy a tiny bounded range, a direct-address array can map values to rank. For arbitrary large or negative values, the hash map is more flexible.


WHY THE RECOMMENDED APPROACH WORKS

All occurrences of the same value must share a rank. Sorting distinct values gives their exact relative order. Assigning consecutive integers in that order preserves all comparisons: a<b if and only if rank[a]<rank[b]. The dictionary maps those ranks back into the original sequence without changing element positions.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

arr=[40,10,20,30]
Unique sorted values=[10,20,30,40]
Rank map:
10->1, 20->2, 30->3, 40->4
Apply to original order:
40,10,20,30 -> 4,1,2,3.

With duplicates arr=[100,100,100], the unique list is [100], so every rank is 1.


EDGE CASES TO TEST

- Empty array.
- All values equal.
- Duplicate values.
- Negative values.
- Very large values; do not allocate an array indexed by the value.
- Already sorted or reverse sorted input.


COMMON INTERVIEW MISTAKES

1. Giving duplicate values different ranks.
2. Starting rank from 0 rather than 1.
3. Returning sorted ranks instead of preserving the original positions.
4. Allocating a huge direct-address array for arbitrary values.
5. Using numeric differences as rank differences; only order matters.


REUSABLE PATTERN TEMPLATE

ordered = sorted(set(arr))
rank = {value: i+1 for i, value in enumerate(ordered)}
return [rank[value] for value in arr]


COMPLEXITY ANALYSIS

Building the set O(n) expected. Sorting d distinct values O(d log d), where d<=n. Building the map and answer O(n) expected. Total O(n log n) time and O(n) space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"Only relative order matters, so I use coordinate compression. I sort the distinct values and assign consecutive ranks starting at 1. A hash map stores value-to-rank, and I traverse the original array to produce the transformed result. Equal values get the same rank and original order is preserved."


PATTERN MEMORY

Rank is determined by relative order among distinct values, not by the raw numeric distance. This is coordinate compression.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain coordinate compression.
[ ] Sort distinct values, not only the entire array.
[ ] Assign ranks starting at 1.
[ ] Preserve original order when constructing the answer.
[ ] Test duplicates, negatives, and empty input.
[ ] State O(n log n) time and O(n) space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Sort the unique values, build a value-to-rank dictionary, then map the original array. This is the clearest coordinate-compression explanation and runs in O(n log n). Sort-pairs-with-indices is useful if the interviewer asks you to avoid a hash map.

ADDITIONAL IMPLEMENTATIONS: A sorted-pairs variant writes ranks directly to original positions. A direct-address/counting array can be used only if the numeric range is small; it is not suitable for arbitrary large or negative values without an offset and range check.

"""

def array_rank_transform(arr: list[int]) -> list[int]:
    ordered = sorted(set(arr))
    rank = {value: index + 1 for index, value in enumerate(ordered)}
    return [rank[value] for value in arr]


class Solution:
    def arrayRankTransform(self, arr: list[int]) -> list[int]:
        return array_rank_transform(arr)


def run_tests() -> None:
    cases = [([40,10,20,30], [4,1,2,3]), ([100,100,100], [1,1,1]),
             ([37,12,28,9,100,56,80,5,12], [5,3,4,2,8,6,7,1,3]),
             ([], []), ([-5,-10,-5,0], [2,1,2,3])]
    for arr, expected in cases:
        assert array_rank_transform(arr) == expected
    print("All Rank Transform test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def array_rank_transform_pairs(arr: list[int]) -> list[int]:
    """Sort (value,index) pairs and assign equal values the same rank."""
    ordered = sorted((value, index) for index, value in enumerate(arr))
    result = [0] * len(arr)
    rank = 0
    previous = None
    for value, index in ordered:
        if previous is None or value != previous:
            rank += 1
            previous = value
        result[index] = rank
    return result


def array_rank_transform_bounded(arr: list[int], max_range: int = 100_000) -> list[int]:
    """Direct-address rank map for a reasonably small value range."""
    if not arr:
        return []
    low, high = min(arr), max(arr)
    if high - low + 1 > max_range:
        raise ValueError("value range is too large for direct addressing")
    present = [False] * (high - low + 1)
    for value in arr:
        present[value - low] = True
    rank_at = [0] * len(present)
    rank = 0
    for offset, exists in enumerate(present):
        if exists:
            rank += 1
            rank_at[offset] = rank
    return [rank_at[value - low] for value in arr]


def run_additional_tests() -> None:
    cases = [([40, 10, 20, 30], [4, 1, 2, 3]), ([100, 100, 100], [1, 1, 1]),
             ([37, 12, 28, 9, 100, 56, 80, 5, 12], [5, 3, 4, 2, 8, 6, 7, 1, 3]),
             ([-5, -10, -5, 0], [2, 1, 2, 3]), ([], [])]
    for arr, expected in cases:
        assert array_rank_transform_pairs(arr) == expected
        assert array_rank_transform_bounded(arr) == expected
    print("Sorted-pair and direct-address Rank Transform alternatives passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
