"""
148. SORT LIST
LeetCode: https://leetcode.com/problems/sort-list/

PROBLEM
Sort a singly linked list in ascending order. Target O(n log n) time.

Example: 4 -> 2 -> 1 -> 3 becomes 1 -> 2 -> 3 -> 4.

PATTERN
Linked List + Merge Sort + Divide and Conquer

WHY MERGE SORT?
Linked lists do not provide efficient random access. Splitting via
slow/fast pointers and merging via next pointers is natural.

APPROACH 1 — ARRAY + SORT
Copy values to an array, sort, and write back. O(n log n) time,
O(n) extra space.

APPROACH 2 — TOP-DOWN MERGE SORT
1. Find midpoint with slow/fast pointers.
2. Disconnect the halves.
3. Recursively sort both halves.
4. Merge with a dummy node.
Time O(n log n), recursion O(log n) space.

APPROACH 3 — BOTTOM-UP MERGE SORT
Merge runs of size 1, 2, 4, ... to avoid recursion and achieve O(1)
auxiliary space; it is more involved to implement.

DRY RUN
4 -> 2 -> 1 -> 3
Split into 4->2 and 1->3; split to single nodes; merge to
2->4 and 1->3; final merge 1->2->3->4.

EDGE CASES
- Empty list; one node; duplicates; negative values; reverse order.

COMPLEXITY
Top-down: O(n log n) time, O(log n) recursion space.

INTERVIEW EXPLANATION
"I use merge sort because linked lists can be split and merged by
changing pointers. Slow and fast pointers find the midpoint; I sort
each half and merge them."

COMMON MISTAKES
- Forgetting to disconnect the two halves.
- Losing the head during merge.
- Failing to advance the chosen pointer.


DETAILED STUDY NOTES — READ THIS BEFORE CODING

CORE IDEA

Linked lists do not support efficient random access, so Merge Sort is a natural fit: split with slow/fast pointers and merge by relinking nodes.


APPROACH ANALYSIS

APPROACH 1 — COPY VALUES TO ARRAY
Traverse the list, collect values, sort them, then write values back. Time O(n log n), extra space O(n). Simple, but does not meet the O(1) auxiliary-space follow-up.

APPROACH 2 — TOP-DOWN LINKED-LIST MERGE SORT
1. Base case: zero or one node is already sorted.
2. Find the middle using slow and fast pointers.
3. Disconnect the list into two halves.
4. Recursively sort each half.
5. Merge the sorted lists using a dummy node and next pointers.
Time O(n log n); recursion stack O(log n).

APPROACH 3 — BOTTOM-UP MERGE SORT
Merge runs of size 1, then 2, 4, 8, etc. This avoids recursion and can achieve O(1) auxiliary space, but pointer management is more involved.


WHY THE RECOMMENDED APPROACH WORKS

Splitting a list into halves gives the same recurrence as array Merge Sort: T(n)=2T(n/2)+O(n), which solves to O(n log n). During merge, the smallest remaining node must be at one of the two list heads, so choosing that node maintains ascending order. Relinking nodes avoids creating a new node for every value.


STEP-BY-STEP THINKING

1. Read the constraints and required output carefully.\n2. Identify what ordering rule the problem asks for.\n3. Decide whether general sorting is sufficient or whether the task needs a custom key, greedy ordering, a heap, or a merge-sort counting technique.\n4. State the invariant before writing the loop.\n5. Check duplicates and equality boundaries.\n6. Test the smallest input and a case that exercises the main pattern.


DRY RUN — DETAILED WALKTHROUGH

4 -> 2 -> 1 -> 3

Split with slow/fast pointers:
Left: 4 -> 2
Right: 1 -> 3

Split again:
4 | 2
1 | 3

Merge pairs:
2 -> 4
1 -> 3

Final merge compares 2 and 1, then 2 and 3, then 4 and 3:
1 -> 2 -> 3 -> 4.


EDGE CASES TO TEST

- Empty list.
- One node.
- Two nodes.
- Already sorted or reverse sorted.
- Duplicate values.
- Negative values.
- Long list where recursive stack depth matters.


COMMON INTERVIEW MISTAKES

1. Forgetting to split by setting slow.next=None.
2. Using fast=head rather than fast=head.next without adjusting the loop, causing an unbalanced or non-terminating split on small lists.
3. Losing the head of the merged list.
4. Forgetting to advance the selected list pointer.
5. Rebuilding all nodes when the task asks to sort the linked list itself.
6. Claiming top-down recursive Merge Sort uses O(1) total auxiliary space; its recursion stack is O(log n).


REUSABLE PATTERN TEMPLATE

if not head or not head.next:
    return head
slow, fast = head, head.next
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
right = slow.next
slow.next = None
left = sortList(head)
right = sortList(right)
return merge(left, right)


COMPLEXITY ANALYSIS

Array-copy sorting: O(n log n) time and O(n) extra space. Top-down linked-list Merge Sort: O(n log n) time and O(log n) recursion stack; nodes are relinked. Bottom-up variant: O(n log n) time and O(1) auxiliary space.


INTERVIEW EXPLANATION — SAY THIS OUT LOUD

"Merge Sort suits linked lists because I can split with slow and fast pointers and merge by changing next pointers. I find the midpoint, disconnect the two halves, recursively sort them, and merge them with a dummy node. The time is O(n log n). This top-down version uses O(log n) recursion space; a bottom-up variant can achieve O(1) auxiliary space."


PATTERN MEMORY

Linked lists do not support efficient random access, so Merge Sort is a natural fit: split with slow/fast pointers and merge by relinking nodes.\n\nRecognize the constraint -> choose the right sorting pattern -> maintain its invariant -> verify edge cases.


REVISION CHECKLIST

[ ] Explain why Merge Sort is preferred for linked lists.
[ ] Find the midpoint with slow/fast pointers.
[ ] Disconnect the two halves.
[ ] Merge with a dummy node.
[ ] Test empty, one-node, and two-node lists.
[ ] State recursion space separately from node storage.
[ ] Explain bottom-up as the constant-space follow-up.


INTERVIEW SOLUTION SELECTION

INTERVIEW BEST SOLUTION: Top-down linked-list Merge Sort is the best first answer: slow/fast split + recursive sort + pointer merge, O(n log n) time and O(log n) recursion space. If the interviewer insists on O(1) auxiliary space, use bottom-up iterative Merge Sort. Copy-to-array is the simplest but uses O(n) extra space.

ADDITIONAL IMPLEMENTATIONS: Array conversion + Python sort is the easy baseline. Bottom-up Merge Sort merges runs of size 1,2,4,..., avoids recursion, and achieves O(1) auxiliary node storage.

"""

class ListNode:
    def __init__(self, val: int = 0, next: "ListNode | None" = None):
        self.val = val
        self.next = next


def build_linked_list(values: list[int]) -> ListNode | None:
    dummy = ListNode()
    current = dummy
    for value in values:
        current.next = ListNode(value)
        current = current.next
    return dummy.next


def linked_list_to_list(head: ListNode | None) -> list[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


def merge_two_lists(left: ListNode | None, right: ListNode | None) -> ListNode | None:
    dummy = ListNode()
    tail = dummy
    while left and right:
        if left.val <= right.val:
            tail.next = left
            left = left.next
        else:
            tail.next = right
            right = right.next
        tail = tail.next
    tail.next = left if left else right
    return dummy.next


def sort_list(head: ListNode | None) -> ListNode | None:
    if head is None or head.next is None:
        return head
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    right_head = slow.next
    slow.next = None
    return merge_two_lists(sort_list(head), sort_list(right_head))


class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        return sort_list(head)


def run_tests() -> None:
    cases = [([4,2,1,3], [1,2,3,4]), ([-1,5,3,4,0], [-1,0,3,4,5]),
             ([], []), ([1], [1]), ([3,3,1,2,1], [1,1,2,3,3])]
    for values, expected in cases:
        assert linked_list_to_list(sort_list(build_linked_list(values))) == expected
    print("All Sort List test cases passed.")



# ADDITIONAL APPROACH IMPLEMENTATIONS
def sort_list_array(head: ListNode | None) -> ListNode | None:
    """Simple baseline: copy values to an array, sort, write values back."""
    values = linked_list_to_list(head)
    values.sort()
    current = head
    for value in values:
        current.val = value
        current = current.next
    return head


def sort_list_bottom_up(head: ListNode | None) -> ListNode | None:
    """Bottom-up linked-list Merge Sort: O(n log n), O(1) auxiliary space."""
    if head is None or head.next is None:
        return head

    n = 0
    node = head
    while node:
        n += 1
        node = node.next

    dummy = ListNode(0, head)

    def split(start: ListNode | None, size: int) -> ListNode | None:
        if start is None:
            return None
        for _ in range(size - 1):
            if start.next is None:
                break
            start = start.next
        rest = start.next
        start.next = None
        return rest

    def merge_runs(left: ListNode | None, right: ListNode | None):
        tail_dummy = ListNode()
        tail = tail_dummy
        while left and right:
            if left.val <= right.val:
                tail.next = left
                left = left.next
            else:
                tail.next = right
                right = right.next
            tail = tail.next
        tail.next = left if left else right
        while tail.next:
            tail = tail.next
        return tail_dummy.next, tail

    size = 1
    while size < n:
        previous = dummy
        current = dummy.next
        while current:
            left = current
            right = split(left, size)
            current = split(right, size)
            merged_head, merged_tail = merge_runs(left, right)
            previous.next = merged_head
            merged_tail.next = current
            previous = merged_tail
        size *= 2

    return dummy.next


def run_additional_tests() -> None:
    cases = [[4, 2, 1, 3], [-1, 5, 3, 4, 0], [], [1], [2, 1], [3, 3, 1, 2, 1], list(range(20, -1, -1))]
    for values in cases:
        expected = sorted(values)
        for implementation in (sort_list_array, sort_list_bottom_up, sort_list):
            head = build_linked_list(values)
            result = implementation(head)
            assert linked_list_to_list(result) == expected, implementation.__name__
    print("Array, top-down, and bottom-up Sort List approaches passed.")

if __name__ == "__main__":
    run_tests()
    run_additional_tests()
