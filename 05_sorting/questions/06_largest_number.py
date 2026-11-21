"""
179. LARGEST NUMBER
LeetCode: https://leetcode.com/problems/largest-number/

PROBLEM
Arrange non-negative integers so their concatenation forms the largest
possible number. Return the result as a string.

Example: [3,30,34,5,9] -> "9534330"

PATTERN
Custom Comparator + Sorting + Greedy Ordering

KEY OBSERVATION
For strings a and b, compare a+b with b+a. Put a first when a+b is
larger. Ordinary numerical or lexicographical sorting is not enough.

APPROACH
1. Convert numbers to strings.
2. Sort using cmp_to_key with the concatenation comparator.
3. Join the strings.
4. If the result starts with zero, return "0".

DRY RUN
[3,30,34,5,9] is ordered as [9,5,34,3,30].
Join -> "9534330".

EDGE CASES
- [0,0] -> "0", not "00".
- One value; numbers with different digit lengths.
- Values such as 3 and 30.

COMPLEXITY
O(n log n) comparisons, with string concatenation/comparison work
proportional to the number of digits. O(total digits) output space.

INTERVIEW EXPLANATION
"The goal is to maximize concatenation, so for two values a and b I
compare a+b against b+a. This comparator gives the correct relative
order. After sorting I join and normalize leading zeroes."

COMMON MISTAKES
- Sorting integers numerically descending.
- Forgetting the all-zero case.
- Returning an integer instead of a string.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The desired order is not numeric order or ordinary string order. The correct relative order of two tokens is determined by which concatenation is larger.


APPROACH ANALYSIS

APPROACH 1 — NUMERIC DESCENDING SORT (INCORRECT)
For [3,30], numeric descending produces [30,3] -> "303", but [3,30] -> "330" is larger. So individual numeric magnitude does not determine the best concatenation.

APPROACH 2 — ORDINARY STRING SORT (INCORRECT)
Lexicographically sorting each token alone also does not directly compare the two possible concatenations.

APPROACH 3 — CUSTOM COMPARATOR (CORRECT)
Convert numbers to strings. For a and b, compare a+b with b+a. If a+b is larger, a must precede b; otherwise b precedes a. Use cmp_to_key to adapt a comparator to Python sorting. Join the ordered tokens. If the result starts with zero, return exactly "0".
Time O(n log n) comparisons; each comparison costs time proportional to token lengths. Extra space O(total digits).


WHY THE RECOMMENDED APPROACH WORKS

For two adjacent tokens, the only local decision is whether their order should be a,b or b,a. The comparator picks the order giving the larger concatenation. Sorting by this relation arranges tokens in the order that maximizes the combined number. The all-zero normalization is necessary because joining zero tokens otherwise returns multiple zero characters even though the numeric result is just zero.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

nums=[3,30,34,5,9]
Compare 3 and 30:
    "330" > "303" -> 3 before 30.
Compare 34 and 3:
    "343" > "334" -> 34 before 3.
Compare 9 and 5:
    "95" > "59" -> 9 before 5.

Sorted token order = ["9","5","34","3","30"]
Join = "9534330".


EDGE CASES TO TEST

- [0] -> "0".
- [0,0,0] -> "0", not "000".
- Prefix-related tokens: 12 and 121.
- Different digit lengths: 3 and 30.
- Large values: return a string.
- Empty list is not part of the usual constraints.


COMMON INTERVIEW MISTAKES

1. Numeric descending sort.
2. Ordinary reverse lexicographic string sort.
3. Reversing the comparator result.
4. Returning int instead of str.
5. Forgetting all-zero normalization.
6. Stating O(n log n) without acknowledging string comparison cost.


REUSABLE PATTERN TEMPLATE

def compare(a, b):
    if a+b > b+a: return -1
    if a+b < b+a: return 1
    return 0
values.sort(key=cmp_to_key(compare))
answer = "".join(values)
if answer.startswith("0"): answer = "0"


COMPLEXITY ANALYSIS

Let n be number of items and m the maximum digits per item. Sorting performs O(n log n) comparisons, each requiring O(m) character work in the simple bound. Total O(n log n * m); conversion/join uses O(total digits) space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"Sorting by numeric value is not correct because the output is a concatenation. For two strings a and b, I compare a+b with b+a. If a+b is larger, a should come first. I apply this custom comparator with cmp_to_key, join the strings, and normalize the all-zero case to a single zero."


PATTERN MEMORY

The desired order is not numeric order or ordinary string order. The correct relative order of two tokens is determined by which concatenation is larger.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Demonstrate why 3 and 30 break normal numeric sorting.
[ ] Derive a+b versus b+a.
[ ] Use cmp_to_key correctly.
[ ] Handle all-zero input.
[ ] Return a string.
[ ] Include digit-length work in complexity.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Custom comparator with cmp_to_key is the correct interview solution. First show why numeric sorting fails on [3,30], then compare a+b with b+a. A brute-force permutation solution is only a tiny-input baseline; there is no ordinary numeric sort key that replaces the comparator.

ADDITIONAL IMPLEMENTATION: Brute-force permutations enumerate all possible orders and choose the largest concatenated string. This is useful for proving small examples, but factorial time makes it unsuitable beyond tiny n.

"""

from functools import cmp_to_key


def largest_number(nums: list[int]) -> str:
    if not nums:
        return ""
    if any(value < 0 for value in nums):
        raise ValueError("nums must contain non-negative integers")
    values = [str(value) for value in nums]

    def compare(a: str, b: str) -> int:
        if a + b > b + a:
            return -1
        if a + b < b + a:
            return 1
        return 0

    values.sort(key=cmp_to_key(compare))
    result = "".join(values)
    return "0" if result and result[0] == "0" else result


class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        return largest_number(nums)


def run_tests() -> None:
    cases = [([10,2], "210"), ([3,30,34,5,9], "9534330"),
             ([0,0], "0"), ([12,121], "12121"), ([1], "1"),
             ([8308,830], "8308830")]
    for nums, expected in cases:
        assert largest_number(nums) == expected
    print("All Largest Number test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def largest_number_bruteforce(nums: list[int]) -> str:
    """Exponential reference: only use for very small arrays (about n<=8)."""
    from itertools import permutations
    if not nums:
        return ""
    if any(value < 0 for value in nums):
        raise ValueError("nums must be non-negative")
    best = max("".join(map(str, order)) for order in permutations(nums))
    return "0" if best and best[0] == "0" else best


def run_additional_tests() -> None:
    cases = [([10, 2], "210"), ([3, 30, 34, 5, 9], "9534330"), ([0, 0], "0"), ([12, 121], "12121")]
    for nums, expected in cases:
        assert largest_number_bruteforce(nums) == expected
        assert largest_number(nums) == expected
    print("Brute-force permutation reference and comparator solution passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
