"""
2418. SORT THE PEOPLE
LeetCode: https://leetcode.com/problems/sort-the-people/

PROBLEM
names[i] belongs to the person whose height is heights[i]. Return names
sorted by height in descending order.

Example:
names=["Mary","John","Emma"], heights=[180,165,170]
Output=["Mary","Emma","John"]

PATTERN
Custom Sort Key / Pair Sorting / Zip

APPROACH 1 — ZIP + SORT
Pair every height with its name, sort by height descending, then extract
names. Time O(n log n), space O(n).

APPROACH 2 — SORT INDICES
Sort indices by their corresponding heights, then map to names.
This is useful when the original arrays must remain unchanged.

DRY RUN
Pairs: (180,Mary), (165,John), (170,Emma).
Descending order: Mary, Emma, John.

EDGE CASES
- One person; empty arrays; already sorted; reverse sorted.
- The original problem guarantees unique heights.

COMPLEXITY
O(n log n) time and O(n) additional space.

INTERVIEW EXPLANATION
"I keep each name attached to its height by sorting pairs, then return
the names in descending height order."

COMMON MISTAKES
- Sorting names independently from heights.
- Sorting heights without applying the same permutation to names.
- Sorting ascending instead of descending.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

The two arrays are parallel: each name must stay attached to its height. Sorting the pairs or sorting indices preserves this relationship.


APPROACH ANALYSIS

APPROACH 1 — ZIP PAIRS + SORT (RECOMMENDED)
Create (height,name) pairs with zip, sort descending by height, and extract names. Time O(n log n), space O(n).

APPROACH 2 — SORT INDICES
Sort indices by heights[index] descending, then return names[index] in that order. This avoids manually constructing pairs but still stores an index order.

APPROACH 3 — DECORATE-SORT-UNDECORATE
This is the same principle in a general form: attach the sort key to each object, sort the decorated entries, and remove the decoration afterward.


WHY THE RECOMMENDED APPROACH WORKS

Pairing each name with its height ensures the same permutation is applied to both arrays. Sorting only names or only heights would break the association. Since heights are unique in the original problem, sorting tuples in descending order is sufficient; sorting by a key makes the intended primary criterion explicit.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

names=["Mary","John","Emma"]
heights=[180,165,170]
zip pairs:
(180,"Mary"), (165,"John"), (170,"Emma")
Sort by height descending:
(180,"Mary"), (170,"Emma"), (165,"John")
Extract names:
["Mary","Emma","John"].


EDGE CASES TO TEST

- One person.
- Already descending heights.
- Ascending heights.
- Empty arrays.
- Duplicate heights: the original problem guarantees unique values; for generalized input, add a tie-break rule if required.


COMMON INTERVIEW MISTAKES

1. Sorting names independently from heights.
2. Sorting heights but forgetting to apply the same permutation to names.
3. Sorting ascending instead of descending.
4. Depending on tuple reverse ordering when a custom tie-break is required; use key= explicitly.


REUSABLE PATTERN TEMPLATE

pairs = sorted(zip(heights, names), key=lambda p: p[0], reverse=True)
return [name for height, name in pairs]

# Or sort index positions:
order = sorted(range(len(names)), key=heights.__getitem__, reverse=True)
return [names[i] for i in order]


COMPLEXITY ANALYSIS

Pair construction O(n), sorting O(n log n), extraction O(n). Total O(n log n) time and O(n) space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I must keep each name attached to its height. I zip the two arrays into pairs, sort those pairs by height in descending order, and then extract the names. This applies the same permutation to both pieces of data and takes O(n log n) time with O(n) extra space."


PATTERN MEMORY

The two arrays are parallel: each name must stay attached to its height. Sorting the pairs or sorting indices preserves this relationship.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why parallel arrays must stay synchronized.
[ ] Implement zip-and-sort.
[ ] Implement index sorting as an alternative.
[ ] Sort descending by height.
[ ] Explain tie handling if heights are not unique.
[ ] State O(n log n) time and O(n) space.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: ZIP + SORT BY HEIGHT DESCENDING is the cleanest interview answer: it keeps the name and height together and takes O(n log n) time. Sorting indices is a good alternative when you want to leave the parallel arrays untouched. A heap version is useful for streaming/top-order variants, but not needed here.

ADDITIONAL IMPLEMENTATIONS: A heap-based version gives O(n log n) time and O(n) space. A manual selection-sort version is an educational O(n²) baseline. The input guarantees unique heights; if not, define an explicit tie-break.

"""

def sort_people_zip(names: list[str], heights: list[int]) -> list[str]:
    if len(names) != len(heights):
        raise ValueError("names and heights must have equal lengths")
    return [name for height, name in sorted(zip(heights, names), reverse=True)]


def sort_people_indices(names: list[str], heights: list[int]) -> list[str]:
    if len(names) != len(heights):
        raise ValueError("names and heights must have equal lengths")
    order = sorted(range(len(names)), key=heights.__getitem__, reverse=True)
    return [names[index] for index in order]


class Solution:
    def sortPeople(self, names: list[str], heights: list[int]) -> list[str]:
        return sort_people_zip(names, heights)


def run_tests() -> None:
    cases = [(["Mary","John","Emma"], [180,165,170], ["Mary","Emma","John"]),
             (["Alice","Bob"], [155,185], ["Bob","Alice"]), (["A"], [170], ["A"]),
             ([], [], [])]
    for names, heights, expected in cases:
        assert sort_people_zip(names, heights) == expected
        assert sort_people_indices(names, heights) == expected
    print("All Sort the People test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def sort_people_heap(names: list[str], heights: list[int]) -> list[str]:
    """Heap alternative; height is the priority, max first."""
    import heapq
    if len(names) != len(heights):
        raise ValueError("names and heights must have equal lengths")
    heap = [(-height, index, name) for index, (height, name) in enumerate(zip(heights, names))]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[2] for _ in range(len(heap))]


def sort_people_selection(names: list[str], heights: list[int]) -> list[str]:
    """O(n^2) educational baseline, preserving name-height pairs."""
    pairs = list(zip(heights, names))
    for i in range(len(pairs)):
        best = i
        for j in range(i + 1, len(pairs)):
            if pairs[j][0] > pairs[best][0]:
                best = j
        pairs[i], pairs[best] = pairs[best], pairs[i]
    return [name for height, name in pairs]


def run_additional_tests() -> None:
    cases = [(["Mary", "John", "Emma"], [180, 165, 170], ["Mary", "Emma", "John"]),
             (["Alice", "Bob"], [155, 185], ["Bob", "Alice"]), (["A"], [170], ["A"]), ([], [], [])]
    for names, heights, expected in cases:
        assert sort_people_heap(names, heights) == expected
        assert sort_people_selection(names, heights) == expected
    print("Heap and selection-sort Sort the People alternatives passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
