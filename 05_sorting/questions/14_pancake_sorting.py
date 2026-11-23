"""
969. PANCAKE SORTING
LeetCode: https://leetcode.com/problems/pancake-sorting/

PROBLEM
Sort arr using prefix reversals (pancake flips). A flip with k reverses
arr[0:k]. Return the sequence of k values used.

Example: [3,2,4,1] -> one valid sequence of flips sorts the array.

PATTERN
Selection Sort Idea + Prefix Reversal

KEY OBSERVATION
For each active prefix, move its largest value to index 0 using one
flip, then flip the whole active prefix to put it in its final place.

APPROACH
For size from n down to 2:
1. Find maximum index in arr[0:size].
2. If already at size-1, continue.
3. If not at index 0, flip max_index+1.
4. Flip size.

DRY RUN
[3,2,4,1], size=4: flip 3 -> [4,2,3,1], flip 4 -> [1,3,2,4].
Then place the largest of the first three, then the first two.

EDGE CASES
- One element; already sorted; reverse sorted; maximum already last.

COMPLEXITY
O(n^2) time, at most 2(n-1) flips, O(1) working space.

INTERVIEW EXPLANATION
"I place the largest value of the unsorted prefix into its final
position. A first prefix flip moves it to the front; a second flip
moves it to the end of the active prefix."

COMMON MISTAKES
- Recording an index instead of prefix length.
- Using arr[:k+1] when k already represents prefix length.
- Forgetting the maximum may already be in place.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

Only prefix reversals are allowed. The greedy strategy fixes the largest element of the active prefix at the end using at most two flips.


APPROACH ANALYSIS

APPROACH 1 — NORMAL SORT (NOT ALLOWED)
A normal sort gives the answer but does not produce a valid sequence of prefix flips.

APPROACH 2 — PANCAKE SELECTION (GREEDY)
For active prefix length size, find the maximum. If already at size-1, no flip is needed. Otherwise flip max_index+1 to move it to index 0, then flip size to move it to the last index of the active prefix. Reduce size and repeat. At most 2(n-1) flips are used.
Time O(n²) because finding each maximum scans the active prefix; O(1) auxiliary space apart from the flip list.


WHY THE RECOMMENDED APPROACH WORKS

A prefix reversal can move the chosen maximum to the front without disturbing elements beyond the active prefix. A second reversal of the entire active prefix moves that maximum to the final active position. Once placed, later operations use a shorter prefix and never touch the fixed suffix. Repeating this fixes positions from right to left.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

arr=[3,2,4,1]
size=4: max 4 at index 2. Flip k=3 -> [4,2,3,1]. Flip k=4 -> [1,3,2,4].
size=3: max 3 at index 1. Flip k=2 -> [3,1,2,4]. Flip k=3 -> [2,1,3,4].
size=2: max 2 at index 0. Flip k=2 -> [1,2,3,4].
The recorded k values are prefix lengths, not zero-based indices.


EDGE CASES TO TEST

- Already sorted array: no flips may be needed.
- Reverse sorted array.
- One element: empty flip list.
- Largest value already at active prefix end.
- Duplicate values are allowed by the general greedy idea, although original problem constraints provide a permutation.


COMMON INTERVIEW MISTAKES

1. Recording max_index rather than max_index+1 as the flip length.
2. Treating k as an inclusive Python slice endpoint; arr[:k] is the prefix.
3. Forgetting the second flip.
4. Flipping the entire array rather than only the active prefix.
5. Continuing after the active prefix has length 1.


REUSABLE PATTERN TEMPLATE

for size in range(n, 1, -1):
    max_index = max(range(size), key=arr.__getitem__)
    if max_index == size-1: continue
    if max_index > 0:
        flip(max_index+1)
    flip(size)


COMPLEXITY ANALYSIS

At active length m, finding the maximum costs O(m). Summing n+(n-1)+...+1 gives O(n²) time. At most 2(n-1) flips are returned. Working memory is O(1), excluding the output flip list.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I place the maximum of the current unsorted prefix into its final position. If it is not already at the end, I first flip the prefix ending at the maximum to bring it to index zero, then flip the entire active prefix to move it to the end. I shrink the active prefix and repeat. This is similar to selection sort and takes O(n²) time."


PATTERN MEMORY

Only prefix reversals are allowed. The greedy strategy fixes the largest element of the active prefix at the end using at most two flips.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why two flips place the maximum at the end.
[ ] Remember flip values are prefix lengths.
[ ] Use arr[:k] for the first k elements.
[ ] Skip a flip when the maximum is already at the end.
[ ] Verify the returned flips actually sort a copy.
[ ] State O(n²) time and at most 2(n-1) flips.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Use the greedy pancake-selection construction. Unlike ordinary sorting questions, the task requires returning prefix flips, so comparison sort, heap sort, or Quick Sort do not satisfy the operation model. The standard practical construction uses at most 2(n-1) flips and O(n²) time. There is no commonly expected simpler alternative algorithm with better general bounds for this exact interface.

IMPLEMENTATION NOTE: The max-search step can be written with max(range(...), key=...) or an explicit scan; both are the same O(n²) greedy strategy. The implementation below includes a manual-scan variant so the flip construction is fully visible.

"""

def pancake_sort(arr: list[int]) -> list[int]:
    flips = []
    for size in range(len(arr), 1, -1):
        max_index = max(range(size), key=arr.__getitem__)
        if max_index == size - 1:
            continue
        if max_index != 0:
            k = max_index + 1
            arr[:k] = reversed(arr[:k])
            flips.append(k)
        arr[:size] = reversed(arr[:size])
        flips.append(size)
    return flips


def apply_flips(values: list[int], flips: list[int]) -> list[int]:
    result = values[:]
    for k in flips:
        result[:k] = reversed(result[:k])
    return result


class Solution:
    def pancakeSort(self, arr: list[int]) -> list[int]:
        return pancake_sort(arr)


def run_tests() -> None:
    for original in ([3,2,4,1], [1,2,3,4], [4,3,2,1], [1], [2,1], [5,1,4,2,3]):
        working = list(original)
        flips = pancake_sort(working)
        assert working == sorted(original)
        assert apply_flips(list(original), flips) == sorted(original)
        assert all(1 <= k <= len(original) for k in flips)
    print("All Pancake Sorting test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def pancake_sort_manual_scan(arr: list[int]) -> list[int]:
    """Same greedy construction, with the maximum search written explicitly."""
    flips = []
    for size in range(len(arr), 1, -1):
        max_index = 0
        for i in range(1, size):
            if arr[i] > arr[max_index]:
                max_index = i
        if max_index == size - 1:
            continue
        if max_index > 0:
            k = max_index + 1
            arr[:k] = reversed(arr[:k])
            flips.append(k)
        arr[:size] = reversed(arr[:size])
        flips.append(size)
    return flips


def run_additional_tests() -> None:
    cases = [[3, 2, 4, 1], [1, 2, 3, 4], [4, 3, 2, 1], [1], [2, 1], [5, 1, 4, 2, 3]]
    for original in cases:
        a = original[:]
        flips_a = pancake_sort(a)
        b = original[:]
        flips_b = pancake_sort_manual_scan(b)
        assert a == sorted(original) and b == sorted(original)
        assert apply_flips(original, flips_a) == sorted(original)
        assert apply_flips(original, flips_b) == sorted(original)
        assert len(flips_a) <= 2 * max(0, len(original) - 1)
    print("Both pancake-selection implementations passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
