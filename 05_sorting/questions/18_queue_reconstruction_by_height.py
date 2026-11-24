"""
406. QUEUE RECONSTRUCTION BY HEIGHT
LeetCode: https://leetcode.com/problems/queue-reconstruction-by-height/

PROBLEM
people[i]=[h,k] means exactly k people in front have height >= h.
Reconstruct the queue.

PATTERN
Sorting + Greedy + Insertion

KEY OBSERVATION
Place taller people first. When inserting [h,k], all already placed
people are at least as tall, so inserting at index k fixes its count.

APPROACH
1. Sort by height descending.
2. For equal heights, sort k ascending.
3. Insert each person at index k.

DRY RUN
Input [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Sorted order [[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]].
Insert each at its own k position to build the valid queue.

EDGE CASES
- One person; same heights; k=0; large k.

COMPLEXITY
Sorting O(n log n), list insertion O(n) each -> O(n^2) total.
Space O(n) output.

INTERVIEW EXPLANATION
"I process taller people first and insert each person at index k.
Shorter people inserted later cannot change the number of taller or
equal-height people before an already placed person."

COMMON MISTAKES
- Sorting height ascending.
- Sorting equal heights by k descending.
- Appending instead of inserting at index k.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

Sort taller people first, then insert each person at index k. Once the taller/equal people are placed, that insertion position establishes the required count in front.


APPROACH ANALYSIS

APPROACH 1 — BRUTE FORCE PERMUTATION
Try different orders and validate the k condition. This is factorial and infeasible.

APPROACH 2 — GREEDY SORT + INSERTION (STANDARD)
Sort by height descending. For equal heights, sort k ascending. Insert each [h,k] at index k in the current queue. The already placed people are all at least as tall as the current person, so index k gives exactly k qualifying people ahead.
Time O(n²) due to Python list insert shifting elements; sorting is O(n log n). Space O(n).

The equal-height tie-break is essential: among equally tall people, the person requiring fewer qualifying people ahead must be placed first.


WHY THE RECOMMENDED APPROACH WORKS

When a person of height h is processed, every person already in the queue has height at least h because the input was sorted descending. Inserting [h,k] at index k puts exactly k existing people before them. Later insertions are shorter or equal-height people ordered by k; they do not invalidate the already established count for taller people. Sorting equal heights by increasing k preserves the constraint among peers.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

people=[[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
Sort by (-height,k):
[[7,0],[7,1],[6,1],[5,0],[5,2],[4,4]]

Insert each at its k index:
[7,0] -> [[7,0]]
[7,1] -> [[7,0],[7,1]]
[6,1] -> [[7,0],[6,1],[7,1]]
Then continue inserting [5,0], [5,2], [4,4].
Final queue = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]].


EDGE CASES TO TEST

- One person.
- All people have equal height.
- Several k=0 people.
- People with large k.
- Equal height with different k.
- Validate final queue by counting previous heights >= current height.


COMMON INTERVIEW MISTAKES

1. Sorting height ascending.
2. Sorting equal heights by k descending.
3. Appending instead of inserting at index k.
4. Claiming list insertion is O(1); it is O(n).
5. Forgetting that the count includes people with equal height, not only strictly taller people.


REUSABLE PATTERN TEMPLATE

people.sort(key=lambda p: (-p[0], p[1]))
queue = []
for person in people:
    queue.insert(person[1], person)
return queue


COMPLEXITY ANALYSIS

Sorting O(n log n). Each list insertion can shift O(n) elements, so all insertions cost O(n²). Total O(n²) time and O(n) queue space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"I sort people by descending height and, for equal heights, ascending k. Then I insert each person at index k. At that moment, everyone already placed is at least as tall as the current person, so exactly k of those people are placed ahead. This greedy order yields a valid queue. The list insertion makes the total time O(n²)."


PATTERN MEMORY

Sort taller people first, then insert each person at index k. Once the taller/equal people are placed, that insertion position establishes the required count in front.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why taller people are inserted first.
[ ] Sort equal heights by ascending k.
[ ] Insert at index k.
[ ] Explain why later shorter people do not break previous constraints.
[ ] Validate the output.
[ ] State O(n²) due to list insertion.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: The descending-height sort + insert-at-k greedy solution is the best first interview answer because its invariant is simple, but Python list insertion makes it O(n²). For an advanced O(n log n) follow-up, process shortest people first and use a Fenwick tree to select the (k+1)-th empty slot.

ADDITIONAL IMPLEMENTATION: Fenwick Tree order-statistic placement achieves O(n log n). Sort by height ascending and, for equal heights, k descending. Empty positions represent places that will be occupied by people at least as tall; choose the (k+1)-th empty position.

"""

def reconstruct_queue(people: list[list[int]]) -> list[list[int]]:
    ordered = sorted(people, key=lambda person: (-person[0], person[1]))
    queue = []
    for person in ordered:
        queue.insert(person[1], person[:])
    return queue


def is_valid_queue(queue: list[list[int]]) -> bool:
    for index, (height, k) in enumerate(queue):
        actual = sum(previous_height >= height for previous_height, _ in queue[:index])
        if actual != k:
            return False
    return True


class Solution:
    def reconstructQueue(self, people: list[list[int]]) -> list[list[int]]:
        return reconstruct_queue(people)


def run_tests() -> None:
    people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
    expected = [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
    result = reconstruct_queue(people)
    assert result == expected
    assert is_valid_queue(result)
    assert reconstruct_queue([[5,0]]) == [[5,0]]
    print("All Queue Reconstruction test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def reconstruct_queue_fenwick(people: list[list[int]]) -> list[list[int]]:
    """O(n log n) order-statistic solution using a Fenwick tree of empty slots."""
    n = len(people)
    if n == 0:
        return []

    # A Fenwick tree initially containing 1 at every position.
    tree = [0] * (n + 1)
    for i in range(1, n + 1):
        tree[i] = i & -i

    def add(index: int, delta: int) -> None:
        while index <= n:
            tree[index] += delta
            index += index & -index

    def kth_empty(k: int) -> int:
        """Return the 1-based index of the k-th still-empty position."""
        index = 0
        bit = 1 << (n.bit_length() - 1)
        while bit:
            nxt = index + bit
            if nxt <= n and tree[nxt] < k:
                index = nxt
                k -= tree[nxt]
            bit >>= 1
        return index + 1

    # Shortest first; among equal heights, larger k is placed first.
    ordered = sorted(people, key=lambda person: (person[0], -person[1]))
    result = [None] * n

    for height, k in ordered:
        position = kth_empty(k + 1)
        result[position - 1] = [height, k]
        add(position, -1)

    return result


def run_additional_tests() -> None:
    cases = [
        [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]],
        [[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]],
        [[5, 0]],
        [],
    ]
    for people in cases:
        result = reconstruct_queue_fenwick(people)
        assert is_valid_queue(result), (people, result)
    print("Fenwick order-statistic Queue Reconstruction alternative passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
