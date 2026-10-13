# 560. SUBARRAY SUM EQUALS K

"""
PROBLEM

Given an integer array nums and an integer k, return the total number
of non-empty contiguous subarrays whose sum equals k.

A subarray must contain consecutive elements.

Example 1:
nums = [1, 1, 1]
k = 2
Output = 2

Valid subarrays:
[1, 1] at indices 0–1
[1, 1] at indices 1–2

Example 2:
nums = [1, 2, 3]
k = 3
Output = 2

Valid subarrays:
[1, 2]
[3]

Important:
- Count subarrays, not distinct sums.
- Subarrays must be contiguous and non-empty.
- Numbers can be negative, zero, or positive.
- The same sum can occur in multiple subarrays.
"""

"""
PATTERN

Array + Contiguous Subarray + Target Sum
→ Prefix Sum + Hash Map

Why?
- A subarray is contiguous.
- We need to count subarrays with a particular sum.
- Negative numbers are allowed, so the usual sliding-window method
  is not reliable.
- Prefix sums let us calculate a subarray sum using two prefix sums.
- A hash map stores how often each prefix sum has appeared.

Main formula:
current_prefix - previous_prefix = k

Rearrange:
previous_prefix = current_prefix - k

Recognition:
Subarray sum equals target + negative values possible
→ Prefix Sum + Frequency Hash Map
"""

"""
APPROACH 1 — BRUTE FORCE

Generate every possible subarray and calculate its sum.
If the sum equals k, increment the answer.

The simplest version repeatedly calls sum() for every subarray.

TIME: O(n^3)
SPACE: O(1) auxiliary space, excluding temporary slices

This is inefficient because sum() repeatedly scans the subarray.
"""

# BRUTE FORCE CODE

def subarray_sum_brute_force(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)

    for start in range(n):
        for end in range(start, n):
            if sum(nums[start:end + 1]) == k:
                count += 1

    return count


"""
APPROACH 2 — BETTER / RUNNING SUM

For every starting index, extend the subarray one element at a time.

Instead of recalculating the sum, maintain a running total:
total += nums[end]

Whenever total == k, increment count.

TIME: O(n^2)
SPACE: O(1)

This avoids repeatedly summing each slice, but still checks every
possible starting and ending index.
"""

# BETTER CODE

def subarray_sum_better(nums: list[int], k: int) -> int:
    count = 0
    n = len(nums)

    for start in range(n):
        total = 0

        for end in range(start, n):
            total += nums[end]

            if total == k:
                count += 1

    return count


"""
APPROACH 3 — OPTIMAL / PREFIX SUM + HASH MAP

Maintain:
prefix_sum = sum of all elements processed so far
count      = number of valid subarrays found
prefix_freq = frequency of previously seen prefix sums

For each num:
1. Add num to prefix_sum.
2. Calculate needed = prefix_sum - k.
3. Every earlier prefix sum equal to needed creates a subarray
   whose sum is k.
4. Add prefix_freq.get(needed, 0) to count.
5. Record the current prefix sum in the map.

Initialize:
prefix_freq = {0: 1}

This represents the empty prefix with sum zero.
It allows subarrays that begin at index 0 to be counted.

TIME: O(n) average
SPACE: O(n)
"""

"""
WHY PREFIX SUM + HASH MAP?

Let:
P[j] = sum of nums[0] through nums[j]

The sum of a subarray from i + 1 through j is:
P[j] - P[i]

We need:
P[j] - P[i] = k

Rearrange:
P[i] = P[j] - k

At the current index, P[j] is prefix_sum.
Therefore, we look for earlier prefix sums equal to:
prefix_sum - k

The map stores frequencies, not just whether a prefix exists,
because several earlier prefixes can have the same value.
Each matching earlier prefix gives a different valid subarray.
"""

"""
STEP-BY-STEP THINKING

1. What is being asked?
   → Count all non-empty contiguous subarrays with sum k.

2. Can I check every subarray?
   → Yes, but the brute-force approaches are slow.

3. What is the subarray sum using prefix sums?
   → Current prefix - previous prefix.

4. What equation do I need?
   → Current prefix - previous prefix = k.

5. What previous prefix am I looking for?
   → Current prefix - k.

6. How do I find it quickly?
   → Store prefix-sum frequencies in a hash map.

7. Why store frequencies?
   → The same prefix sum can appear multiple times, and each occurrence
     represents a different possible subarray.

8. Why start with {0: 1}?
   → It counts a valid subarray that starts at index 0.

9. When should I update the map?
   → After counting matches for the current prefix.

10. What is the complexity?
    → O(n) average time and O(n) space.
"""

"""
OPTIMAL CODE
"""

class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefix_sum = 0
        count = 0
        prefix_freq = {0: 1}

        for num in nums:
            prefix_sum += num

            needed = prefix_sum - k
            count += prefix_freq.get(needed, 0)

            prefix_freq[prefix_sum] = (
                prefix_freq.get(prefix_sum, 0) + 1
            )

        return count


"""
TEST CASE

The following is a runnable Python 3 test using Solution.
"""

solution = Solution()

nums1 = [1, 1, 1]
k1 = 2
print("Input:", nums1, "k =", k1)
print("Output:", solution.subarraySum(nums1, k1))

nums2 = [1, 2, 3]
k2 = 3
print("Input:", nums2, "k =", k2)
print("Output:", solution.subarraySum(nums2, k2))

nums3 = [1, -1, 0]
k3 = 0
print("Input:", nums3, "k =", k3)
print("Output:", solution.subarraySum(nums3, k3))


"""
OUTPUT

Input: [1, 1, 1] k = 2
Output: 2
Input: [1, 2, 3] k = 3
Output: 2
Input: [1, -1, 0] k = 0
Output: 3
"""

"""
WHY DOES THE OPTIMAL APPROACH WORK?

At each index, prefix_sum is the sum of all elements processed so far.

If an earlier prefix sum was prefix_sum - k, then the elements after
that earlier prefix and through the current index have sum k.

Every occurrence of that earlier prefix creates one valid subarray.
The frequency map counts all those occurrences, so adding the frequency
counts every valid subarray ending at the current index.

Every non-empty subarray has an ending index. When that ending index is
processed, its matching earlier prefix is counted.

Therefore, every valid subarray is counted exactly once.

The initial entry {0: 1} represents the empty prefix and handles
valid subarrays beginning at index 0.
"""

"""
DRY RUN

nums = [1, 2, 3]
k = 3

Initial:
prefix_sum = 0
count = 0
prefix_freq = {0: 1}

STEP 1: num = 1

prefix_sum = 1
needed = 1 - 3 = -2
frequency of -2 = 0

count = 0
Record prefix 1:
prefix_freq = {0: 1, 1: 1}

STEP 2: num = 2

prefix_sum = 3
needed = 3 - 3 = 0
frequency of 0 = 1

count = 0 + 1 = 1
This counts subarray [1, 2].

Record prefix 3:
prefix_freq = {0: 1, 1: 1, 3: 1}

STEP 3: num = 3

prefix_sum = 6
needed = 6 - 3 = 3
frequency of 3 = 1

count = 1 + 1 = 2
This counts subarray [3].

Final answer = 2.
"""

"""
EDGE CASE 1 — SUBARRAY STARTS AT INDEX 0

nums = [1, 2]
k = 3

At the second element:
prefix_sum = 3
needed = 3 - 3 = 0

The initial map contains {0: 1}, so the subarray [1, 2] is counted.

Output: 1
"""

"""
EDGE CASE 2 — NEGATIVE NUMBERS

nums = [1, -1, 0]
k = 0

Valid subarrays:
[1, -1]
[0]
[1, -1, 0]

Output: 3

Negative values can make a running sum increase or decrease.
Prefix sum + hash map handles them correctly.
A standard sliding window is not generally reliable here.
"""

"""
EDGE CASE 3 — k = 0

nums = [0, 0]
k = 0

Valid subarrays:
[0] at index 0
[0] at index 1
[0, 0]

Output: 3

Repeated prefix sums must be counted by frequency.
Also, count matches before recording the current prefix so that
the current prefix is not incorrectly used as an empty subarray.
"""

"""
EDGE CASE 4 — REPEATED PREFIX SUMS

nums = [1, -1, 1, -1]
k = 0

The prefix sum returns to zero multiple times.
Each earlier occurrence can create a different valid subarray.

A set would only record whether a prefix exists.
A frequency map counts every occurrence, which is required here.
"""

"""
TIME & SPACE COMPLEXITY

Let n = len(nums).

Brute force with repeated sum():
TIME: O(n^3)
SPACE: O(1) auxiliary, excluding temporary slices

Running-sum approach:
TIME: O(n^2)
SPACE: O(1)

Prefix sum + hash map:
TIME: O(n) average
SPACE: O(n)

Each element is processed once, with average O(1) hash map operations.
The map may store up to n + 1 distinct prefix sums.
"""

"""
INTERVIEW EXPLANATION

"I will use prefix sums and a hash map to count subarrays efficiently.

Let prefix_sum be the sum up to the current element. A subarray has
sum k when an earlier prefix sum equals prefix_sum - k.

I store the frequency of each prefix sum in a hash map. For every
element, I add the frequency of prefix_sum - k to the answer, then
record the current prefix sum.

I initialize the map with {0: 1} to count subarrays starting at index 0.
The frequency map handles repeated prefix sums, and this method also
works when the array contains negative numbers.

The average time complexity is O(n), and the space complexity is O(n)."
"""

"""
RECOGNITION TRICKS

1. Contiguous subarray + target sum
   → Consider Prefix Sum.

2. Need to count subarrays, not just find one
   → Store prefix-sum frequencies.

3. Negative numbers are allowed
   → A standard sliding window is not reliable.

4. Need subarray sum k
   → Look for previous prefix = current prefix - k.

5. Subarrays may begin at index 0
   → Initialize prefix_freq = {0: 1}.

6. Prefix sums can repeat
   → Use a frequency map, not a set.

Mental pattern:
prefix_sum += num
→ needed = prefix_sum - k
→ count += frequency[needed]
→ record prefix_sum
"""

"""
REUSABLE TEMPLATE

prefix_sum = 0
count = 0
prefix_freq = {0: 1}

for num in nums:
    prefix_sum += num

    needed = prefix_sum - k
    count += prefix_freq.get(needed, 0)

    prefix_freq[prefix_sum] = prefix_freq.get(prefix_sum, 0) + 1

return count

Use this template for counting subarrays with a target sum when
prefix sums and their frequencies are useful.
"""

"""
FAMILY

Arrays
    ↓
Prefix Sum
    ↓
Hash Map / Frequency Counting
    ↓
Count Subarrays With Target Sum

Related problems:
- Range Sum Query
- Continuous Subarray Sum
- Subarray Sums Divisible by K
- Contiguous Array
- Maximum Size Subarray Sum Equals K
- Path Sum III

Common idea:
Use prefix sums to express a range/subarray sum as the difference
between two prefix sums, then use a hash map to find useful prefixes.
"""

"""
COMMON INTERVIEW MISTAKES

1. Using sliding window despite negative values.
   → Negative values break the usual window movement logic.

2. Storing prefix sums in a set.
   → Frequencies are needed because repeated prefixes create multiple
     valid subarrays.

3. Forgetting {0: 1}.
   → Valid subarrays beginning at index 0 may be missed.

4. Updating the map before counting matches.
   → When k = 0, the current prefix could be counted as an empty subarray.

5. Counting only one match.
   → Add the full frequency of prefix_sum - k.

6. Confusing subarray with subsequence.
   → A subarray must be contiguous.

7. Returning the subarrays instead of their count.
   → Return the total count.

8. Recalculating every subarray sum.
   → Use a running sum or prefix sums to avoid repeated work.

9. Claiming O(n) worst-case hash operations in every implementation.
   → Standard Python dictionary operations are O(1) on average.
"""

"""
MOST IMPORTANT THING TO REMEMBER

Subarray Sum Equals K
→ Prefix Sum + Hash Map

Core formula:
current_prefix - previous_prefix = k

Therefore:
previous_prefix = current_prefix - k

For every num:
1. Update prefix_sum.
2. Add the frequency of prefix_sum - k to count.
3. Record the current prefix_sum.

Initialize:
prefix_freq = {0: 1}

TIME: O(n) average
SPACE: O(n)

The key is not to store subarrays.
Store prefix-sum frequencies so every valid subarray can be counted
efficiently.
"""
