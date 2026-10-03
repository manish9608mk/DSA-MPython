# 1985. Find the Kth Largest Integer in the Array

'''
PROBLEM

Given an array nums of strings representing integers and an integer k,
return the kth largest integer in the array as a string.

Example:
nums = ["3", "6", "7", "10"]
k = 2

Output:
"7"

Important:
- nums contains strings.
- We must compare the values numerically.
- The answer must be returned as a string.
'''


'''
PATTERN

Kth Largest
→ Keep K largest elements
→ Remove the smallest when size > K
→ Min Heap
→ heap[0] = Kth largest

Why?

If we keep the K largest elements, the smallest among them is
the Kth largest.

Example:
K = 3

K largest = [20, 30, 50]
Smallest among them = 20

Therefore:
20 = 3rd largest

Recognition:
Kth Largest  → Min Heap
Kth Smallest → Max Heap
'''


'''
APPROACH 1 — BRUTE FORCE

For every number, count how many numbers are greater than it.

If:
greater_count == k - 1

then that number is the kth largest.

Example:
nums = ["3", "6", "7", "10"]
k = 2

For 7:
Only 10 is greater.

greater_count = 1
k - 1 = 1

Therefore, 7 is the 2nd largest.

TIME: O(n²)
SPACE: O(1)

This works, but it is inefficient.
'''


# BRUTE FORCE CODE

class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        n = len(nums)

        for i in range(n):
            count = 0

            for j in range(n):
                if int(nums[j]) > int(nums[i]):
                    count += 1

            if count == k - 1:
                return nums[i]


'''
APPROACH 2 — SORTING

Sort all numbers in descending numerical order.

Example:
["3", "6", "7", "10"]
→ ["10", "7", "6", "3"]

Then:
kth largest → index k - 1

Important:
nums contains strings, so normal string sorting is wrong.

Wrong:
nums.sort(reverse=True)

Correct:
nums.sort(key=int, reverse=True)

Why key=int?

Because:
"10" and "3" are strings.

String comparison and numerical comparison are different.

TIME: O(n log n)
SPACE: O(log n)

Sorting is simple, but we do not actually need to sort
the complete array.
'''


# SORTING CODE

class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        nums.sort(key=int, reverse=True)
        return nums[k - 1]


'''
APPROACH 3 — OPTIMAL / MIN HEAP

We only need the K largest elements, not the complete sorted array.

Maintain a Min Heap of size at most K.

For every number:
1. Convert the string to an integer.
2. Push it into the heap.
3. If heap size > K, remove the smallest element.

After processing all elements:
- The heap contains the K largest elements.
- The smallest among them is the Kth largest.
- In a Min Heap, the smallest element is at heap[0].

Therefore:
heap[0] = Kth largest

TIME: O(n log k)
SPACE: O(k)
'''


'''
WHY MIN HEAP?

Suppose K = 3.

Current K largest candidates:

[10, 20, 30]

Now 50 arrives.

Temporarily:

[10, 20, 30, 50]

We only want 3 elements.

Which one can we remove safely?

10, because it is the smallest.

After removing 10:

[20, 30, 50]

These are the 3 largest elements.

The smallest among them is 20.

Therefore:
20 = 3rd largest

So the logic is:

Kth Largest
→ Keep K largest
→ Remove smallest
→ Min Heap
'''


'''
STEP-BY-STEP THINKING

1. What is being asked?
   → Find the Kth largest.

2. Do I need the entire array sorted?
   → No.

3. How many elements actually matter?
   → K.

4. Which data structure can keep only K elements?
   → Heap.

5. Which heap should I use?
   → Min Heap.

6. Why?
   → I need to remove the smallest element when I have more than K.

7. When do I remove?
   → When len(heap) > k.

8. What remains?
   → The K largest elements.

9. Which element is the answer?
   → The smallest among those K elements.

10. Where is the smallest element in a Min Heap?
    → heap[0].

11. Input is a string, so what should I do?
    → Convert num to int before putting it into the heap.

12. Output must be a string, so:
    → return str(min_heap[0])
'''


# OPTIMAL CODE

import heapq

class Solution:
    def kthLargestNumber(self, nums: list[str], k: int) -> str:
        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, int(num))

            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return str(min_heap[0])


'''
TEST CASE

nums = ["3", "2", "1", "5", "6", "4"]
k = 2
'''

nums = ["3", "2", "1", "5", "6", "4"]
k = 2

solution = Solution()
answer = solution.kthLargestNumber(nums, k)

print("Input:", nums)
print("K:", k)
print("Output:", answer)


'''
OUTPUT

Input: ['3', '2', '1', '5', '6', '4']
K: 2
Output: 5
'''


'''
WHY DOES THE MIN HEAP APPROACH WORK?

The heap always contains the K largest elements seen so far.

Whenever the heap size becomes K + 1,
we remove the smallest element.

Therefore, smaller elements are continuously removed
and only the K largest candidates remain.

At the end:

Heap = K largest elements

The smallest element among them = Kth largest

Therefore:

heap[0] = Kth largest
'''


'''
DRY RUN

nums = [3, 2, 1, 5, 6, 4]
k = 2

We need the 2nd largest.

Start:
heap = []

3 → [3]

2 → [2, 3]

1 → [1, 2, 3]
     size > 2
     remove 1
     → [2, 3]

5 → [2, 3, 5]
     remove 2
     → [3, 5]

6 → [3, 5, 6]
     remove 3
     → [5, 6]

4 → [4, 5, 6]
     remove 4
     → [5, 6]

Final heap:
[5, 6]

Smallest = 5

Therefore:
2nd largest = 5
'''


'''
EDGE CASE 1 — K = 1

nums = ["3", "6", "7", "10"]
k = 1

We only keep one element.

Final heap:
[10]

Answer:
"10"
'''


'''
EDGE CASE 2 — K = N

nums = ["3", "6", "7", "10"]
k = 4

The heap can contain all elements.

Smallest element = 3

Therefore:
4th largest = "3"
'''


'''
EDGE CASE 3 — DUPLICATES

nums = ["2", "2", "3", "1"]
k = 2

Sorted:
3, 2, 2, 1

Therefore:
2nd largest = 2

The heap handles duplicates naturally.
No special duplicate handling is required.
'''


'''
EDGE CASE 4 — VERY LARGE NUMBERS

The input values are strings because they can be very large.

Convert for numerical comparison:

int(num)

After finding the answer, convert it back:

str(min_heap[0])

Flow:

String
→ int
→ Heap
→ Find answer
→ str
'''


'''
TIME & SPACE COMPLEXITY

There are n elements.

For every element, we perform a heap operation.

The heap contains at most K elements.

One heap operation:
O(log k)

For n elements:

TIME: O(n log k)

Heap stores at most K elements:

SPACE: O(k)

Compared with sorting:

Sorting:
O(n log n)

Min Heap:
O(n log k)

So the heap approach is especially useful when K is much smaller than N.
'''


'''
INTERVIEW EXPLANATION

"I need to find the Kth largest integer.

Instead of sorting the entire array, I can maintain a Min Heap
containing only the K largest values.

For every number, I push it into the heap.
If the heap size becomes greater than K, I remove the smallest value.

This guarantees that the heap always contains the K largest
elements seen so far.

At the end, the smallest element in the heap is the Kth largest.

Since the input values are strings, I convert them to integers
for comparison and return the final answer as a string.

The time complexity is O(n log k) and the space complexity is O(k)."
'''


'''
RECOGNITION TRICKS

1. Kth Largest
   → Min Heap

2. Kth Smallest
   → Max Heap

3. Top K Largest
   → Min Heap of size K

4. Top K Smallest
   → Max Heap of size K

General pattern:

Only K elements matter
→ Use a Heap

For Kth Largest:

Kth Largest
→ Keep K largest
→ Remove smallest
→ Min Heap
→ heap[0] = answer

Main question to ask in a new problem:

"Do I really need all elements sorted,
or do I only need K important elements?"

If only K elements matter:
→ Think Heap.
'''


'''
REUSABLE TEMPLATE

Kth Largest:

import heapq

heap = []

for value in nums:
    heapq.heappush(heap, value)

    if len(heap) > k:
        heapq.heappop(heap)

answer = heap[0]

Remember:

Kth Largest
→ Min Heap
→ Keep K
→ Pop smallest
→ heap[0] = answer
'''


'''
FAMILY

Kth Largest
Kth Smallest
Top K Largest
Top K Smallest
Top K Frequent
K Closest Elements
K Closest Points
Priority Queue problems

Common idea:

Need only K important elements
→ Heap
'''


'''
COMMON INTERVIEW MISTAKES

1. Using normal string sorting.

Wrong:
nums.sort(reverse=True)

Correct:
nums.sort(key=int, reverse=True)


2. Using Max Heap for Kth Largest.

Remember:
Kth Largest → Min Heap
Kth Smallest → Max Heap


3. Forgetting to remove when heap size > K.

Need:

if len(heap) > k:
    heapq.heappop(heap)


4. Forgetting that Python's heapq is a Min Heap.


5. Returning an integer instead of a string.

Correct:
return str(min_heap[0])


6. Thinking heap[0] is the largest.

In a Min Heap:
heap[0] = smallest

But here the heap contains only the K largest elements,
so the smallest among them is exactly the Kth largest.


7. Memorizing the code instead of understanding the pattern.

Remember:

Kth Largest
→ Keep K largest
→ Remove smallest
→ Min Heap
'''


'''
MOST IMPORTANT THING TO REMEMBER

The complete pattern:

Kth Largest
→ Keep K largest elements
→ Need to remove the smallest
→ Use Min Heap
→ If size > K, pop smallest
→ Heap contains K largest
→ heap[0] = Kth largest

One-line rule:

Kth Largest → Min Heap → Keep K → Pop smallest → heap[0]

For this problem:

String input
→ Convert to int
→ Min Heap
→ Find Kth Largest
→ Convert answer back to string

When you see a new problem asking for:

"Kth Largest"

your first thought should be:

MIN HEAP

Then ask:

"Can I keep only K elements?"

If yes, use a Min Heap of size K.
''' 