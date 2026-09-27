# 169. Majority Element

'''
Link:
https://leetcode.com/problems/majority-element/

Given an array nums of size n, return the majority element.

The majority element appears more than n / 2 times.

You may assume that a majority element always exists.

Example:

nums = [2,2,1,1,1,2,2]
Output: 2
'''

'''
PATTERN:

Majority element
    +
Must solve in O(n) time
    +
O(1) extra space
    ↓
Boyer-Moore Voting Algorithm

Think:
"Different elements can cancel each other."

The majority element appears more than n / 2 times,
so it will survive all the cancellations.
'''


def majority_element(nums):

    candidate = None
    count = 0

    for num in nums:

        if count == 0:
            candidate = num

        if num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


# Test case
nums = [2, 2, 1, 1, 1, 2, 2]

result = majority_element(nums)

print("Majority Element =", result)


'''
Output:

Majority Element = 2
'''


'''
BOYER-MOORE VOTING TEMPLATE:

candidate = None
count = 0

for num in nums:

    if count == 0:
        candidate = num

    if num == candidate:
        count += 1
    else:
        count -= 1

return candidate


KEY IDEA:

candidate
    → current possible majority element

count
    → current vote count

If count == 0:
    → choose current number as candidate

If num == candidate:
    → count += 1

If num != candidate:
    → count -= 1


Why does cancellation work?

Suppose:

[2,2,1,1,1,2,2]

The majority element appears more than n / 2 times.

So the majority element has more occurrences than
all other elements combined.

One majority element can be cancelled by one
different element.

Even after all possible cancellations,
the majority element will still remain.


Important:

This solution works because the problem guarantees
that a majority element always exists.


COMPLEXITY:

Time  : O(n)
Space : O(1)


RECOGNITION TRICKS:

1. Find the element appearing more than n / 2 times
2. Majority element is guaranteed to exist
3. Need O(n) time
4. Need O(1) extra space

→ Think BOYER-MOORE VOTING


INTERVIEW THINKING:

Need majority element
    ↓
Majority appears > n/2
    ↓
Can cancel different elements
    ↓
Track candidate + count
    ↓
Same as candidate → +1
Different → -1
    ↓
count becomes 0
    → choose new candidate
    ↓
Return candidate
    ↓
O(n) time
O(1) space
'''


'''
And this becomes part of your Array pattern family.

When you later see:

Majority Element
Majority Element II
Find element occurring most frequently
Find element with more than n/2 occurrences

You should ask:

"Is there a guaranteed majority?"

If yes:

        BOYER-MOORE VOTING
                ↓
        candidate + count
                ↓
        O(n) time
        O(1) space
'''