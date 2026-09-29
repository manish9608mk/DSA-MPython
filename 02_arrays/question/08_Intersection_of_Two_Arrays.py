# 349. Intersection of Two Arrays

'''
Link:
https://leetcode.com/problems/intersection-of-two-arrays/

Given two integer arrays nums1 and nums2,
return their intersection.

Each element in the result must be unique.
Order does not matter.

Example:

nums1 = [1,2,2,1]
nums2 = [2,2]

Output: [2]
'''

'''
PATTERN:

Two arrays
    +
Find common elements
    +
Result must be unique
    +
Need fast lookup
    ↓
HASH SET

Think:

"Do I need to quickly check
whether an element exists?"

    ↓
SET
'''


class Solution:

    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:

        seen = set(nums1)
        result = []

        for num in nums2:

            if num in seen:
                result.append(num)
                seen.remove(num)

        return result


# Test case
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

solution = Solution()

result = solution.intersection(nums1, nums2)

print("Result =", result)


'''
HASH SET TEMPLATE:

seen = set(nums1)

for num in nums2:

    if num in seen:
        # common element
        # process it

        seen.remove(num)


KEY IDEA:

set()
    → removes duplicates

num in set
    → average O(1) lookup

remove()
    → prevents duplicate result


COMPLEXITY:

Time  : O(n + m) average
Space : O(n)


RECOGNITION TRICKS:

1. Find common elements
2. Unique result
3. Fast membership checking
4. Duplicate detection
5. "Have I seen this before?"

→ Think HASH SET


INTERVIEW THINKING:

Need common elements
    ↓
Need fast lookup
    ↓
Need uniqueness
    ↓
Use SET
    ↓
Store one array
    ↓
Scan the other
    ↓
Found → process it
    ↓
Remove if duplicate result is not allowed
'''


'''
HASHING FAMILY:

SET:

Contains Duplicate
Intersection of Two Arrays
Longest Consecutive Sequence
Unique elements


HASH MAP / DICTIONARY:

Two Sum
Valid Anagram
Group Anagrams
Frequency problems


Quick rule:

Existence / uniqueness
    → SET

Frequency / counting / mapping
    → HASH MAP
'''