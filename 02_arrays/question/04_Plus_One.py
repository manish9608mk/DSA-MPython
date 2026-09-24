# 66. Plus One

'''
Link:
https://leetcode.com/problems/plus-one/

You are given a large integer represented as an array of digits.

Increment the integer by one and return the resulting array.

Example:

digits = [1,2,3]
Output: [1,2,4]

digits = [9,9,9]
Output: [1,0,0,0]
'''

'''
PATTERN:

Array represents a number
    +
Add 1
    +
Carry can move from right to left
    ↓
Backward Traversal

Think:
"Addition starts from the last digit."
    ↓
Start from the BACK
    ↓
Handle carry
'''


def plus_one(digits):

    for i in range(len(digits) - 1, -1, -1):

        if digits[i] < 9:
            digits[i] += 1
            return digits

        digits[i] = 0

    return [1] + digits


# Test case
digits = [1, 2, 9]

result = plus_one(digits)

print("Result =", result)


'''
Output:

Result = [1, 3, 0]
'''


'''
BACKWARD TRAVERSAL TEMPLATE:

for i in range(len(nums) - 1, -1, -1):

    if condition:
        # process current element
        return result

    # continue to the left


KEY IDEA:

Start from the last digit.

If digit < 9:
    → add 1
    → return

If digit == 9:
    → make it 0
    → carry moves to the left

If every digit is 9:

[9,9,9]
    ↓
[0,0,0]
    ↓
[1,0,0,0]


Why do we traverse backwards?

Because the rightmost digit is the first digit affected
when we add 1.


COMPLEXITY:

Time  : O(n)
Space : O(1) extra space


RECOGNITION TRICKS:

1. Array represents a number
2. Need to add 1
3. Carry can propagate
4. Carry moves from right to left
5. Need to process digits from the end

→ Think BACKWARD TRAVERSAL + CARRY


INTERVIEW THINKING:

Array represents a number
    ↓
Need to add 1
    ↓
Start from last digit
    ↓
If digit < 9
    → increment and return
    ↓
If digit == 9
    → make it 0
    → continue left
    ↓
All digits were 9
    ↓
Return [1] + digits
'''


'''
And this becomes part of your Array pattern family.

When you later see:

Plus One
Add Binary
Add Strings
Multiply Strings
Add Two Numbers

You should first think:

"Is there a carry?"

If carry moves from right to left:

        BACKWARD TRAVERSAL
                +
              CARRY
'''