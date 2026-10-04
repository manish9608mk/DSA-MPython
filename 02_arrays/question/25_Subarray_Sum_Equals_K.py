# 560. Subarray Sum Equals K

'''
PROBLEM

Given an integer array nums and an integer k, return the
number of non-empty contiguous subarrays whose sum is k.

A subarray must contain consecutive elements.


Example:

nums = [1,1,1]
k = 2

Valid subarrays:

[1,1] → 2
[1,1] → 2

Output = 2


Example:

nums = [1,2,3]
k = 3

Valid subarrays:

[1,2] → 3
[3]   → 3

Output = 2


Important:

- Subarray must be contiguous.
- Subarray must be non-empty.
- Negative numbers are allowed.
- We need the number of valid subarrays.
'''


'''
PATTERN

Prefix Sum + Hash Map


The key equation:

current_prefix - previous_prefix = k


Rearrange:

previous_prefix = current_prefix - k


So at every index:

1. Calculate current prefix sum.
2. Find current_prefix - k in the map.
3. Add its frequency to the answer.
4. Store the current prefix sum.


Recognition:

"Count subarrays"
+
"Sum equals K"
+
"Negative numbers"

→ Prefix Sum + Hash Map


Mental pattern:

Current Prefix
→ Need Prefix - K
→ Hash Map Frequency
→ Add Frequency
→ Store Current Prefix
'''


'''
APPROACH 1 — BRUTE FORCE

Try every possible subarray.

For each starting index i:

1. Set current_sum = 0.
2. Extend the subarray to the right.
3. Add nums[j].
4. If current_sum == k, increase the count.


Example:

nums = [1,1,1]
k = 2


i = 0:

[1]   → 1
[1,1] → 2 → count


i = 1:

[1]   → 1
[1,1] → 2 → count


i = 2:

[1] → 1


Answer = 2


Why does it work?

Every possible subarray is considered.


Why is it inefficient?

There are O(n²) possible subarrays.

With nested loops, the total time is:

O(n²)


TIME:

O(n²)


SPACE:

O(1)
'''


# BRUTE FORCE CODE

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        count = 0

        for i in range(len(nums)):
            current_sum = 0

            for j in range(i, len(nums)):
                current_sum += nums[j]

                if current_sum == k:
                    count += 1

        return count


'''
APPROACH 2 — OPTIMAL / PREFIX SUM + HASH MAP

For a subarray from index j + 1 to i:

subarray_sum = current_prefix - previous_prefix


We need:

current_prefix - previous_prefix = k


Therefore:

previous_prefix = current_prefix - k


So for every current prefix sum, we only need to know
how many times current_prefix - k appeared before.


Store:

prefix_sum → frequency


If the needed prefix occurred multiple times,
each occurrence creates a different valid subarray.


This gives:

TIME  = O(n)
SPACE = O(n)
'''


'''
WHY HASH MAP?

We need:

"How many times have I seen current_prefix - k?"


A Hash Map stores:

prefix_sum → number of occurrences


Example:

map = {
    0: 1,
    1: 2,
    3: 1
}


If:

current_prefix - k = 1


then:

map[1] = 2


So there are 2 valid subarrays ending at the
current index.


A Set is not enough because we need frequency,
not just existence.


Therefore:

Need uniqueness
→ Set

Need frequency
→ Hash Map
'''


'''
WHY {0: 1}?

Initialize:

prefix_sum_count = {0: 1}


Meaning:

Before processing any element,
the prefix sum is 0 once.


This handles subarrays that start at index 0.


Example:

nums = [3]
k = 3


current_sum = 3

needed = 3 - 3
        = 0


Since:

map[0] = 1


we count:

[3]


Without {0: 1}, this subarray would be missed.
'''


'''
STEP-BY-STEP THINKING

1. What am I counting?

→ Contiguous subarrays with sum k.


2. Why not brute force?

→ O(n²) is too slow.


3. Can sliding window work?

→ Not reliably because negative numbers are allowed.


4. How can I represent a subarray sum?

→ Prefix sums.


5. What is a subarray sum using prefix sums?

→ Current prefix - previous prefix.


6. Set it equal to k:

current_prefix - previous_prefix = k


7. Rearrange:

previous_prefix = current_prefix - k


8. What do I need?

→ Number of previous prefix sums equal to
  current_prefix - k.


9. Which data structure stores this efficiently?

→ Hash Map.


10. What does the map store?

→ Prefix sum → frequency.


11. What must be initialized?

→ {0: 1}


12. What is the processing order?

→ Update prefix
→ Check needed prefix
→ Add frequency
→ Store current prefix


Final:

Prefix Sum
→ Prefix - K
→ Frequency Lookup
→ Count
→ Store
'''


'''
# OPTIMAL CODE
'''

# from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Dictionary to store prefix sum frequencies
        prefix_sum_count = defaultdict(int)
        prefix_sum_count[0] = 1
        
        current_sum = 0
        count = 0
        
        # Iterate through the array
        for num in nums:
            # Update the running prefix sum
            current_sum += num
            
            # Check if there is a prefix sum that matches current_sum - k
            count += prefix_sum_count[current_sum - k]
            
            # Update the frequency of the current prefix sum
            prefix_sum_count[current_sum] += 1
        
        return count

# TEST CASE

nums = [1,2,3]
k = 3

solution = Solution()

answer = solution.subarraySum(nums, k)

print("Input:", nums)
print("K:", k)
print("Output:", answer)

'''
OUTPUT

Input: [1,2,3]
K: 3
Output: 2
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

Let the current prefix sum be S.

Suppose an earlier prefix sum is P.

The elements between those two prefix positions
have sum:

S - P


For the subarray sum to equal k:

S - P = k


Therefore:

P = S - k


So whenever the map contains S - k,
there is a subarray ending at the current index
with sum k.


If S - k appeared multiple times,
each occurrence represents a different starting
position and therefore a different subarray.


The map stores those frequencies, so:

count += prefix_sum_count[S - k]


counts every valid subarray ending at the current index.


Every subarray has exactly one ending index,
so every valid subarray is counted exactly once.


The initial:

{0: 1}

handles subarrays that start at index 0.
'''


'''
DRY RUN

nums = [1,2,3]
k = 3


Start:

prefix_sum_count = {0:1}
current_sum = 0
count = 0


STEP 1:

num = 1

current_sum = 1

needed = 1 - 3
        = -2

-2 is not in the map.

count = 0

Store 1:

{0:1, 1:1}


STEP 2:

num = 2

current_sum = 3

needed = 3 - 3
        = 0

0 occurred once.

count += 1

count = 1


This counts:

[1,2]


Store 3:

{0:1, 1:1, 3:1}


STEP 3:

num = 3

current_sum = 6

needed = 6 - 3
        = 3

3 occurred once.

count += 1

count = 2


This counts:

[3]


Final:

count = 2


Answer = 2
'''


'''
DRY RUN — REPEATED PREFIX SUM

nums = [1,-1,1]
k = 1


Start:

map = {0:1}
current_sum = 0
count = 0


num = 1:

current_sum = 1
needed = 0

map[0] = 1

count = 1

map = {0:1, 1:1}


This counts:

[1]


num = -1:

current_sum = 0
needed = -1

Not found.

count = 1

Current prefix 0 appears again:

map[0] = 2


num = 1:

current_sum = 1
needed = 0

map[0] = 2

count += 2

count = 3


The two new subarrays are:

[1,-1,1]
[1]


Final answer:

3


Important lesson:

The map must store frequencies,
not just whether a prefix exists.
'''


'''
DRY RUN — ZERO AND NEGATIVE VALUES

nums = [1,-1,1]
k = 0


Start:

map = {0:1}


num = 1:

current_sum = 1
needed = 1

not found

map = {0:1, 1:1}


num = -1:

current_sum = 0
needed = 0

map[0] = 1

count = 1

map[0] = 2


Valid subarray:

[1,-1]


num = 1:

current_sum = 1
needed = 1

map[1] = 1

count = 2


Valid subarray:

[-1,1]


Final:

2
'''


'''
EDGE CASE 1 — SUBARRAY STARTS AT INDEX 0

nums = [3]
k = 3


current_sum = 3

needed = 0

map[0] = 1


So:

count = 1


Answer:

1
'''


'''
EDGE CASE 2 — NO VALID SUBARRAY

nums = [1,2,3]
k = 10


No subarray has sum 10.

Answer:

0
'''


'''
EDGE CASE 3 — SINGLE ELEMENT

nums = [5]
k = 5


The subarray [5] has sum 5.

Answer:

1
'''


'''
EDGE CASE 4 — k = 0

nums = [1,-1,1,-1]
k = 0


Positive and negative values can cancel each other.

Prefix Sum + Hash Map handles this naturally.
'''


'''
EDGE CASE 5 — NEGATIVE k

nums = [-1,-1,1]
k = -2


The subarray:

[-1,-1]

has sum -2.

The same prefix-sum formula works.
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = len(nums)


Each element is processed once.

For every element:

1. Update prefix sum.
2. Check Hash Map.
3. Update Hash Map.


Hash Map operations are O(1) average.


Therefore:

TIME = O(n)


The map can store O(n) prefix sums.

Therefore:

SPACE = O(n)


Final:

Time  = O(n)
Space = O(n)
'''


'''
INTERVIEW EXPLANATION

"I use Prefix Sum with a Hash Map.

Let the current prefix sum be S.

For a subarray to have sum k, we need an earlier
prefix sum P such that:

S - P = k

which means:

P = S - k

So for each element, I update the running prefix sum,
check how many times prefix_sum - k has appeared,
and add that frequency to the answer.

Then I store the current prefix sum in the map.

I initialize the map with {0: 1} so subarrays starting
at index 0 are counted.

The time complexity is O(n) and the space complexity
is O(n)."
'''


'''
RECOGNITION TRICKS

1. "Subarray Sum Equals K"

→ Prefix Sum + Hash Map


2. Negative numbers are allowed.

→ Sliding Window is not generally reliable.


3. Need to count subarrays.

→ Store prefix sum frequencies.


4. Remember the equation:

current_prefix - previous_prefix = k


Therefore:

previous_prefix = current_prefix - k


5. Same prefix can occur many times.

→ Store frequency, not just existence.


Quick pattern:

Subarray
→ Prefix Sum

Equals K
→ Need Prefix - K

Count matches
→ Hash Map Frequency
'''


'''
REUSABLE TEMPLATE

from collections import defaultdict

prefix_sum_count = defaultdict(int)
prefix_sum_count[0] = 1

current_sum = 0
count = 0

for num in nums:
    current_sum += num

    count += prefix_sum_count[current_sum - k]

    prefix_sum_count[current_sum] += 1

return count


Core equation:

current_prefix - previous_prefix = k

→ previous_prefix = current_prefix - k


Core line:

count += prefix_sum_count[current_sum - k]
'''


'''
FAMILY

Prefix Sum + Hash Map


Related problem types:

- Count subarrays with target sum
- Longest subarray with target sum
- Subarray sum divisible by K
- Binary subarray sum
- Prefix-sum frequency problems


Useful distinction:

Need cumulative value
→ Prefix Sum


Need previous matching values
→ Hash Map


Need their number of occurrences
→ Hash Map Frequency
'''


'''
COMMON INTERVIEW MISTAKES

1. Using Sliding Window.

Negative numbers are allowed, so the sum is not
monotonic.


2. Using a Set.

A Set tells whether a prefix exists,
but we need how many times it exists.


3. Forgetting:

prefix_sum_count[0] = 1


This misses subarrays starting at index 0.


4. Looking for:

k - current_sum


The correct value is:

current_sum - k


5. Storing the current prefix before checking.

Correct order:

current_sum += num

count += prefix_sum_count[current_sum - k]

prefix_sum_count[current_sum] += 1


6. Adding only 1 when a prefix is found.

The prefix may have appeared multiple times,
so add its entire frequency.


7. Confusing subarray with subsequence.

Subarray must be contiguous.


8. Using O(n²) nested loops when O(n) is possible.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Complete Pattern:

Subarray Sum Equals K
→ Prefix Sum
→ Current Prefix = S
→ Need Previous Prefix = S - K
→ Hash Map stores frequencies
→ Add frequency to answer
→ Store current prefix


One-line rule:

Subarray Sum K
→ Prefix Sum
→ Need Prefix - K
→ Hash Map Frequency
→ Count Matches


Most important equation:

current_prefix - previous_prefix = k


Rearrange:

previous_prefix = current_prefix - k


Most important initialization:

prefix_sum_count[0] = 1


Most important code:

current_sum += num

count += prefix_sum_count[current_sum - k]

prefix_sum_count[current_sum] += 1


Final Mental Model:

Current Prefix
→ Subtract K
→ Find matching previous Prefix
→ Frequency tells number of valid subarrays
→ Add to count
→ Store current Prefix


Think:

"Find the earlier prefix that would make the
current subarray sum exactly K."
'''