# 347. Top K Frequent Elements

"""
PROBLEM

Given an integer array nums and an integer k, return the k most frequent
elements.

You may return the answer in any order.

Examples:

    nums = [1, 1, 1, 2, 2, 3], k = 2
    Output = [1, 2]

    nums = [1], k = 1
    Output = [1]

Link:
https://leetcode.com/problems/top-k-frequent-elements/


PATTERN

Hashing / Frequency Counting / Top K / Heap / Bucket Sort

Need the most frequent elements
              ↓
      Count frequencies
              ↓
         HASH MAP
              ↓
   Select the largest k counts
              ↓
       HEAP or BUCKET SORT


RECOGNITION TRICKS

- "Top K frequent" -> frequency map + selection.
- Need only k largest/smallest items -> consider a heap.
- Need all items ordered by frequency -> sorting is straightforward.
- Frequency is bounded by n -> bucket sort may give linear time.
- Do not sort the original array just to count duplicates.
- The output order does not matter in this problem.


REAL-WORLD ANALOGY

Imagine a website tracking the number of visits to each page.
You are asked to report the k most visited pages.

First count visits per page. Then select the k pages with the largest
visit counts. You do not need to arrange every page if only the top k
are required.


APPROACH 1 — BRUTE FORCE (COUNT EACH DISTINCT NUMBER)

1. Find the distinct numbers.
2. For each distinct number, count how many times it appears in nums.
3. Store (number, frequency) pairs.
4. Sort the pairs by frequency in descending order.
5. Return the first k numbers.

Why it works:
    Every distinct number gets its exact frequency.
    Sorting by frequency puts the most frequent numbers first.

Why it is inefficient:
    Counting each distinct number scans the array again.

Time:
    O(n * d + d log d), where d is the number of distinct values.
    Worst case: O(n^2).

Space:
    O(d) for the distinct values and frequency pairs.


APPROACH 2 — BETTER / SIMPLE (HASH MAP + SORTING)

1. Count every number using a dictionary.
2. Sort the dictionary items by frequency, descending.
3. Return the first k numbers.

Why it works:
    The dictionary calculates all frequencies in one pass.
    Sorting arranges the distinct numbers from highest frequency to lowest.

Time:
    O(n) to count + O(d log d) to sort.
    Total: O(n + d log d).

Space:
    O(d) for the frequency map and sorted pairs.

Interview note:
    This is usually the easiest optimized solution to explain.
    However, it sorts all d distinct values even though we only need k.


APPROACH 3 — OPTIMAL FOR TOP K (HASH MAP + MIN HEAP)

1. Count frequencies using a dictionary.
2. Keep a min heap containing at most k (frequency, number) pairs.
3. For each distinct number:
       Push its (frequency, number) pair.
       If heap size becomes greater than k, remove the smallest pair.
4. The heap now contains the k most frequent numbers.

Why a min heap?
    The smallest frequency among the selected elements stays at the root.
    When a new candidate arrives, we can remove the weakest candidate.

Why it works:
    At every step, the heap retains the k largest frequencies seen so far.
    Removing the smallest whenever the heap grows beyond k maintains
    exactly the best k candidates.

Time:
    O(n) to count.
    O(d log k) to maintain the heap.
    Total: O(n + d log k).

Space:
    O(d) for the frequency map + O(k) for the heap.

Python:
    Use heapq.heappush() and heapq.heappop().


APPROACH 4 — LINEAR TIME (HASH MAP + BUCKET SORT)

A number can occur from 1 to n times.

1. Count frequencies using a dictionary.
2. Create buckets indexed by frequency.
3. Put each number into the bucket matching its frequency.
4. Traverse buckets from frequency n down to 1.
5. Collect numbers until k elements have been selected.

Why it works:
    The bucket index represents the frequency.
    Reading buckets from high frequency to low frequency visits the
    most frequent numbers first.

Time:
    O(n) to count + O(n) to create/traverse buckets.
    Total: O(n).

Space:
    O(n + d) for buckets and the frequency map.

Interview note:
    Bucket sort is an excellent solution when the interviewer asks
    for linear time. It uses the fact that no frequency can exceed n.


WHY HASH MAP + MIN HEAP WORKS

The hash map answers:
    "How many times does each number appear?"

The min heap answers:
    "Among the k candidates currently selected, which has the
     smallest frequency?"

Keeping only k elements is enough because every element removed from
the heap has a frequency no greater than the k elements retained at
that moment.

After processing all distinct numbers, the heap contains the k
largest frequency candidates.


STEP-BY-STEP THINKING

1. Do duplicates matter?
       Yes. We need their counts.

2. What data structure stores counts?
       A dictionary / Hash Map.

3. Do we need all distinct numbers sorted?
       No. We only need k numbers.

4. Which structure can maintain the best k candidates?
       A min heap of size k.

5. Can we do linear time?
       Yes. Frequencies are between 1 and n, so use buckets.


DRY RUN — HASH MAP + MIN HEAP

nums = [1, 1, 1, 2, 2, 3]
k = 2

Step 1 — Count:

    1 -> 3
    2 -> 2
    3 -> 1

Frequency map:

    {1: 3, 2: 2, 3: 1}

Step 2 — Process (frequency, number) pairs:

    (3, 1) -> heap = [(3, 1)]
    (2, 2) -> heap = [(2, 2), (3, 1)]
    (1, 3) -> push, heap size becomes 3

Since heap size is greater than k = 2, pop the smallest:

    remove (1, 3)

Remaining heap contains:

    (2, 2), (3, 1)

Step 3 — Return the numbers:

    [2, 1]

Output: [2, 1]

The order does not matter.


DRY RUN — BUCKET SORT

nums = [1, 1, 1, 2, 2, 3]
k = 2

Frequency map:

    {1: 3, 2: 2, 3: 1}

Buckets:

    frequency 1 -> [3]
    frequency 2 -> [2]
    frequency 3 -> [1]

Traverse from frequency 3 downwards:

    frequency 3 -> take 1
    frequency 2 -> take 2

We have selected k = 2 elements.

Output: [1, 2]


EDGE CASES

- One distinct value: nums = [5, 5, 5], k = 1 -> [5]
- Every value is distinct: nums = [1, 2, 3], k = 2 -> any two values
- k equals number of distinct values.
- Negative values: nums = [-1, -1, 2], k = 1 -> [-1]
- Multiple values have the same frequency.
  Any valid k elements according to the problem's constraints are acceptable.
- Large input: avoid repeated nums.count() calls.


COMMON INTERVIEW MISTAKES

1. Sorting the original array and returning k values.
   This does not directly select by frequency.

2. Using a set.
   A set removes duplicates, so frequency information is lost.

3. Building a heap with all n input elements.
   We only need one entry per distinct number, and the heap can stay
   at size k.

4. Using a max heap without understanding Python's heapq.
   Python heapq is a min heap by default.

5. Forgetting to remove an element when heap size exceeds k.
   The heap must contain at most k candidates.

6. Claiming the heap solution is O(n log k) without explaining d.
   The precise complexity is O(n + d log k), where d is the number
   of distinct values.

7. Assuming one exact output order.
   The problem allows any order.


REUSABLE TEMPLATE — TOP K USING A MIN HEAP

from collections import Counter
import heapq

freq = Counter(nums)
heap = []

for num, count in freq.items():
    heapq.heappush(heap, (count, num))

    if len(heap) > k:
        heapq.heappop(heap)

answer = [num for count, num in heap]


REUSABLE TEMPLATE — FREQUENCY BUCKETS

from collections import Counter

freq = Counter(nums)
buckets = [[] for _ in range(len(nums) + 1)]

for num, count in freq.items():
    buckets[count].append(num)

answer = []

for count in range(len(nums), 0, -1):
    for num in buckets[count]:
        answer.append(num)

        if len(answer) == k:
            return answer


SIMILAR PROBLEMS

- LeetCode 451: Sort Characters By Frequency
- LeetCode 692: Top K Frequent Words
- LeetCode 703: Kth Largest Element in a Stream
- LeetCode 215: Kth Largest Element in an Array
- LeetCode 973: K Closest Points to Origin
- LeetCode 1207: Unique Number of Occurrences


INTERVIEW TIP

Start with the key observation:

"Because the answer depends on how frequently each number occurs,
I will first build a frequency map."

Then explain the selection requirement:

"We only need the k most frequent values, not a complete ordering.
I can maintain a min heap of size k. Its root is the weakest selected
candidate, so whenever the heap grows beyond k, I remove that root."

Finish with complexity:

"Counting takes O(n), and processing d distinct values in a heap of
size k takes O(d log k). Total time is O(n + d log k), with O(d + k)
auxiliary space."

If asked for linear time, explain frequency buckets.


PYTHON DETAILS

- Counter(nums) counts each number.
- heapq is a min heap in Python.
- heappush(heap, item) inserts an item.
- heappop(heap) removes the smallest item.
- A tuple is compared lexicographically: first frequency, then number.
- The problem accepts any valid answer order.


COMPLEXITY SUMMARY

Let:
    n = length of nums
    d = number of distinct values
    k = number of requested elements

Approach                       Time                  Auxiliary Space
Repeated counting + sorting    O(n*d + d log d)      O(d)
Hash Map + sorting             O(n + d log d)        O(d)
Hash Map + min heap            O(n + d log k)        O(d + k)
Hash Map + bucket sort         O(n)                  O(n + d)

The returned answer is not counted as auxiliary space.


INTERVIEW EXPLANATION (SAY THIS OUT LOUD)

"I first count the frequency of each number using a dictionary.
Then I use a min heap to keep only k candidates.

For every distinct number, I push its frequency and value into the heap.
If the heap contains more than k elements, I remove the smallest
frequency. This ensures that the heap always stores the k most frequent
candidates processed so far.

At the end, I return the values from the heap.

The time complexity is O(n + d log k), where d is the number of
distinct values. The auxiliary space is O(d + k)."

If asked for a linear-time solution:

"Since each frequency is at most n, I can use buckets indexed by
frequency. I traverse the buckets from n down to 1 and stop after
collecting k values. This takes O(n) time."


PATTERN MEMORY

Top K frequent?
       ↓
Count occurrences
       ↓
Hash Map / Counter
       ↓
Need only k best candidates?
       ↓
Min Heap of size k

Need linear time and frequency is bounded by n?
       ↓
Bucket Sort


REVISION CHECKLIST

[ ] Explain why frequency counting is necessary.
[ ] Write the Hash Map + sorting solution without looking.
[ ] Explain why a min heap is used for Top K.
[ ] Explain why heap size must never exceed k.
[ ] Dry-run nums = [1, 1, 1, 2, 2, 3], k = 2.
[ ] Write the bucket-sort solution.
[ ] State O(n + d log k) for the heap approach.
[ ] State O(n) for bucket sort.
[ ] Explain the solution clearly in under two minutes.
"""


from collections import Counter
import heapq


# APPROACH 1 — BRUTE FORCE: REPEATED COUNTING + SORTING
def top_k_frequent_brute(nums: list[int], k: int) -> list[int]:
    distinct = set(nums)
    pairs = []

    for num in distinct:
        pairs.append((num, nums.count(num)))

    pairs.sort(key=lambda pair: pair[1], reverse=True)

    return [num for num, count in pairs[:k]]


# APPROACH 2 — BETTER: HASH MAP + SORTING
def top_k_frequent_sorting(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)

    ordered = sorted(
        freq.items(),
        key=lambda pair: pair[1],
        reverse=True
    )

    return [num for num, count in ordered[:k]]


# APPROACH 3 — OPTIMAL TOP K: HASH MAP + MIN HEAP
def top_k_frequent_heap(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)

    return [num for count, num in heap]


# APPROACH 4 — LINEAR TIME: HASH MAP + BUCKET SORT
def top_k_frequent_bucket(nums: list[int], k: int) -> list[int]:
    freq = Counter(nums)

    # A number can occur at most len(nums) times.
    buckets = [[] for _ in range(len(nums) + 1)]

    for num, count in freq.items():
        buckets[count].append(num)

    result = []

    for count in range(len(nums), 0, -1):
        for num in buckets[count]:
            result.append(num)

            if len(result) == k:
                return result

    return result


# LEETCODE SUBMISSION CLASS
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        return top_k_frequent_heap(nums, k)


def validate_answer(nums: list[int], k: int, answer: list[int]) -> bool:
    """
    Validate the answer without assuming a particular output order.

    Checks:
    - Exactly k elements are returned.
    - No returned element is repeated.
    - Every returned element exists in nums.
    - No excluded element has a strictly greater frequency
      than the least frequent selected element.
    """
    if len(answer) != k or len(set(answer)) != k:
        return False

    freq = Counter(nums)

    if any(num not in freq for num in answer):
        return False

    if k == len(freq):
        return True

    selected_min_frequency = min(freq[num] for num in answer)
    excluded = [count for num, count in freq.items() if num not in answer]

    return not excluded or max(excluded) <= selected_min_frequency


if __name__ == "__main__":
    test_cases = [
        ([1, 1, 1, 2, 2, 3], 2),
        ([1], 1),
        ([1, 2, 3, 4], 2),
        ([-1, -1, 2, 2, 2, 3], 2),
        ([4, 4, 4, 5, 5, 6], 1),
        ([1, 1, 2, 2, 3, 3], 2),
    ]

    solution = Solution()

    for nums, k in test_cases:
        brute = top_k_frequent_brute(nums, k)
        sorting = top_k_frequent_sorting(nums, k)
        heap = solution.topKFrequent(nums, k)
        bucket = top_k_frequent_bucket(nums, k)

        assert validate_answer(nums, k, brute)
        assert validate_answer(nums, k, sorting)
        assert validate_answer(nums, k, heap)
        assert validate_answer(nums, k, bucket)

        print(f"nums={nums}, k={k}")
        print(f"Brute force: {brute}")
        print(f"Sorting:     {sorting}")
        print(f"Min heap:    {heap}")
        print(f"Bucket sort: {bucket}")
        print("All approaches passed.\n")
