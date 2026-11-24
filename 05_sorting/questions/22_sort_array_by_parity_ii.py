"""
922. SORT ARRAY BY PARITY II
LeetCode: https://leetcode.com/problems/sort-array-by-parity-ii/

PROBLEM
Sort the array so every even index contains an even number and every
odd index contains an odd number. The input has equal counts of even
and odd values.

Example: [4,2,5,7] -> [4,5,2,7]

PATTERN
Two Pointers + In-place Swapping

APPROACH 1 — EXTRA ARRAY
Place even values at even positions and odd values at odd positions.
Time O(n), space O(n).

APPROACH 2 — TWO POINTERS (IN-PLACE)
Use one pointer on even indices and one on odd indices. Advance the
pointer while its slot already has the correct parity. When both point
to incorrect slots, swap the values.
Time O(n), auxiliary space O(1).

DRY RUN
[4,2,5,7]: even pointer reaches index 2 containing 5; odd pointer
checks index 1 containing 2. Swap -> [4,5,2,7].

EDGE CASES
- Already valid; one pair; negatives; all even values at front.

COMPLEXITY
O(n) time and O(1) auxiliary space for the two-pointer method.

INTERVIEW EXPLANATION
"I scan even and odd positions independently. When both point to a
misplaced value, I swap them. Each pointer only moves forward."

COMMON MISTAKES
- Checking the value at the wrong pointer.
- Incrementing both pointers before swapping.
- Forgetting the problem guarantees equal parity counts.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

Every even index needs an even value and every odd index needs an odd value. The input guarantees equal counts, so misplaced even and odd values can be exchanged using two pointers.


APPROACH ANALYSIS

APPROACH 1 — EXTRA ARRAY
Create an answer array. Fill even indices with even values and odd indices with odd values using separate pointers. Time O(n), space O(n).

APPROACH 2 — IN-PLACE TWO-POINTER SWAPS (OPTIMAL SPACE)
Use even_index=0 and odd_index=1. If nums[even_index] is already even, advance by 2. If nums[odd_index] is already odd, advance by 2. When both point to misplaced values, swap them. Each index advances in steps of two.
Time O(n), auxiliary space O(1).

The input promise of equal even/odd counts guarantees that every misplaced value has a counterpart.


WHY THE RECOMMENDED APPROACH WORKS

The only invalid positions are even indices containing odd numbers and odd indices containing even numbers. A swap between one position of each type fixes both mismatches at once. Since each pointer visits indices of only its parity, each location is examined at most once or a constant number of times. Equal counts guarantee the process can finish without an unmatched category.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[4,2,5,7]
Even index scan: index 0 has 4 (correct), move to 2.
Odd index scan: index 1 has 2 (wrong), stay.
Swap nums[2]=5 with nums[1]=2 -> [4,5,2,7].
Now index 2 has 2 (correct), index 1 has 5 (correct).
Output=[4,5,2,7].


EDGE CASES TO TEST

- Empty array.
- Already valid layout.
- Alternating wrong parity.
- Negative values: Python modulo 2 still identifies parity.
- Input with equal counts is guaranteed; without this promise, validate counts first.


COMMON INTERVIEW MISTAKES

1. Incrementing pointers by 1 rather than 2, which mixes index parity.
2. Swapping when only one of the two selected values is misplaced.
3. Forgetting the input count guarantee.
4. Using value parity instead of index parity to decide which pointer moves.
5. Creating an extra array while claiming O(1) space.


REUSABLE PATTERN TEMPLATE

even_i = 0
odd_i = 1
while even_i < n and odd_i < n:
    if nums[even_i] % 2 == 0:
        even_i += 2
    elif nums[odd_i] % 2 == 1:
        odd_i += 2
    else:
        nums[even_i], nums[odd_i] = nums[odd_i], nums[even_i]
        even_i += 2
        odd_i += 2


COMPLEXITY ANALYSIS

Extra-array method: O(n) time and O(n) space. Two-pointer in-place method: O(n) time and O(1) auxiliary space because each pointer advances by two and never moves backward.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I need even values at even indices and odd values at odd indices. I use one pointer over even indices and another over odd indices. A pointer advances when its current value is already correct. When both pointers identify misplaced values, I swap them; that fixes both positions. Equal parity counts are guaranteed, and the algorithm takes O(n) time and O(1) extra space."


PATTERN MEMORY

Every even index needs an even value and every odd index needs an odd value. The input guarantees equal counts, so misplaced even and odd values can be exchanged using two pointers.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain the two kinds of misplaced positions.
[ ] Move pointers by two.
[ ] Swap only when both positions are wrong.
[ ] Test negative numbers.
[ ] Explain the equal-count guarantee.
[ ] State O(n) time and O(1) auxiliary space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Use the two-pointer in-place swap method when O(1) extra space is desired. The extra-array approach is easier to explain and also O(n) time, but uses O(n) space. Advance pointers by two so each visits only its own parity of indices.

ADDITIONAL IMPLEMENTATION: An extra-array solution distributes even values to even indices and odd values to odd indices. It is often the easiest first implementation; the in-place version is the follow-up optimization.

"""

def sort_array_by_parity_ii(nums: list[int]) -> list[int]:
    even = 0
    odd = 1
    n = len(nums)
    while even < n and odd < n:
        while even < n and nums[even] % 2 == 0:
            even += 2
        while odd < n and nums[odd] % 2 == 1:
            odd += 2
        if even < n and odd < n:
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2
    return nums


class Solution:
    def sortArrayByParityII(self, nums: list[int]) -> list[int]:
        return sort_array_by_parity_ii(nums)


def is_valid_parity_order(nums: list[int]) -> bool:
    return all(value % 2 == index % 2 for index, value in enumerate(nums))


def run_tests() -> None:
    for original in ([4,2,5,7], [2,3], [3,2,4,5], [5,4,7,6]):
        result = sort_array_by_parity_ii(list(original))
        assert sorted(result) == sorted(original)
        assert is_valid_parity_order(result)
    print("All Sort Array By Parity II test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def sort_array_by_parity_ii_extra_space(nums: list[int]) -> list[int]:
    """O(n) time and O(n) additional space."""
    if len(nums) % 2:
        raise ValueError("array length must be even")
    evens = [value for value in nums if value % 2 == 0]
    odds = [value for value in nums if value % 2 != 0]
    if len(evens) != len(odds):
        raise ValueError("input must contain equal even and odd counts")
    result = [0] * len(nums)
    result[::2] = evens
    result[1::2] = odds
    return result


def run_additional_tests() -> None:
    cases = [[4, 2, 5, 7], [2, 3], [3, 2, 4, 5], [5, 4, 7, 6], [-2, -3, 4, 5]]
    for original in cases:
        expected_multiset = sorted(original)
        extra = sort_array_by_parity_ii_extra_space(original)
        in_place = sort_array_by_parity_ii(original[:])
        assert sorted(extra) == expected_multiset and is_valid_parity_order(extra)
        assert sorted(in_place) == expected_multiset and is_valid_parity_order(in_place)
    print("Extra-array and in-place Sort Array By Parity II approaches passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
