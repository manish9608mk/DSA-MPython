# 189. Rotate Array

'''
Link:
https://leetcode.com/problems/rotate-array/

Given an integer array nums, rotate the array to the right
by k steps.

The array must be modified in-place.

Example:

Input:
nums = [1,2,3,4,5,6,7]
k = 3

Output:
[5,6,7,1,2,3,4]
'''

'''
PATTERN:

Array
    +
Rotation
    +
In-place
    +
O(1) extra space
    ↓
REVERSAL TRICK

Right rotation by k:

[ first part | last k elements ]
                    ↓
[ last k elements | first part ]
'''

'''
APPROACH 1 — BRUTE FORCE:

Rotate the array one step at a time.

Example:

[1,2,3,4,5]

Rotate right once:

[5,1,2,3,4]

Repeat this k times.

Code:

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)

TIME:
O(n × k)

SPACE:
O(1)

Why?

One rotation requires O(n) because inserting at the
beginning shifts elements.

With k rotations:

O(n × k)

This can be too slow when n and k are large.
'''

'''
APPROACH 2 — BETTER:

Use an extra array.

For every element at index i:

new_index = (i + k) % n

Example:

nums = [1,2,3,4,5,6,7]
k = 3

For 1:

(0 + 3) % 7 = 3

So 1 goes to index 3.

For 5:

(4 + 3) % 7 = 0

So 5 goes to index 0.

Code:

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        result = [0] * n

        for i in range(n):
            result[(i + k) % n] = nums[i]

        nums[:] = result

TIME:
O(n)

SPACE:
O(n)

This is fast but uses extra memory.
'''

'''
APPROACH 3 — OPTIMAL:

Use the REVERSAL ALGORITHM.

Example:

nums = [1,2,3,4,5,6,7]
k = 3

Original:

[1,2,3,4 | 5,6,7]

We want:

[5,6,7 | 1,2,3,4]

Perform three reversals:

1. Reverse the entire array.

[7,6,5,4,3,2,1]

2. Reverse the first k elements.

[5,6,7,4,3,2,1]

3. Reverse the remaining elements.

[5,6,7,1,2,3,4]

Done.
'''

'''
STEP-BY-STEP THINKING:

Suppose the array is divided into:

A B

where:

A = first n-k elements
B = last k elements

Original:

A B

We need:

B A

Reverse the entire array:

reverse(A B)

= reverse(B) reverse(A)

Then reverse both parts:

reverse(reverse(B)) reverse(reverse(A))

= B A

Therefore:

Reverse ALL
    ↓
Reverse FIRST k
    ↓
Reverse REST
    ↓
RIGHT ROTATION
'''

'''
IMPORTANT:

Always do:

k %= n

Example:

nums = [1,2,3,4,5]
k = 12

Since:

12 % 5 = 2

Rotating 12 times is the same as rotating 2 times.

Every n rotations return the array to its original state.
'''

'''
OPTIMAL CODE:
'''

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


'''
TEST CASE:

Input:

nums = [1,2,3,4,5,6,7]
k = 3
'''

nums = [1,2,3,4,5,6,7]
k = 3

solution = Solution()
solution.rotate(nums, k)

print("Result =", nums)

'''
Output:

Result = [5,6,7,1,2,3,4]
'''

'''
DRY RUN:

nums = [1,2,3,4,5,6,7]
k = 3

Step 1:

Reverse entire array:

[1,2,3,4,5,6,7]
        ↓
[7,6,5,4,3,2,1]


Step 2:

Reverse first 3 elements:

[7,6,5 | 4,3,2,1]
        ↓
[5,6,7 | 4,3,2,1]


Step 3:

Reverse remaining elements:

[5,6,7 | 4,3,2,1]
          ↓
[5,6,7 | 1,2,3,4]


Final:

[5,6,7,1,2,3,4]
'''

'''
WHY THE OPTIMAL APPROACH WORKS:

Suppose:

A = first n-k elements
B = last k elements

Original:

A B

After reversing everything:

reverse(B) reverse(A)

Now reverse each part:

reverse(reverse(B)) reverse(reverse(A))

This becomes:

B A

which is exactly the required right rotation.

Therefore three reversals perform the rotation
without using an extra array.
'''

'''
TIME & SPACE COMPLEXITY:

There are three reversals.

Each reversal takes O(n) at most.

Therefore:

TIME:
O(n)

EXTRA SPACE:
O(1)

The array is modified in-place.
'''

'''
INTERVIEW THINKING:

When you see:

"Rotate an array"

First ask:

1. Is it left or right rotation?
2. Is it required in-place?
3. Is O(1) extra space required?
4. Can k be larger than n?

If the problem says:

Rotate
+
In-place
+
O(1) extra space

Think:

REVERSAL ALGORITHM
'''

'''
INTERVIEW EXPLANATION:

"A right rotation by k means the last k elements
move to the front.

I can achieve this in-place using three reversals.

First, I reverse the entire array.
Then I reverse the first k elements.
Finally, I reverse the remaining n-k elements.

I also use k %= n because rotating n positions
returns the array to its original state.

This gives O(n) time and O(1) extra space."
'''

'''
RECOGNITION TRICKS:

Look for:

- Rotate array
- Shift array
- Rotate left/right
- In-place
- O(1) extra space

Immediately think:

ARRAY ROTATION
      ↓
REVERSAL TRICK
'''

'''
COMMON INTERVIEW MISTAKES:

1. Forgetting:

k %= n


2. Using the wrong reversal order.

For RIGHT rotation:

Reverse ALL
    ↓
Reverse FIRST k
    ↓
Reverse REST


3. Returning nums.

The problem asks for an in-place modification.

So:

return nums

is not required.

The function should modify nums directly.


4. Forgetting k = 0.

After:

k %= n

k can become 0.

The algorithm still works correctly.


5. Not handling k > n.

Example:

n = 5
k = 7

Actual rotation:

7 % 5 = 2
'''

'''
REUSABLE TEMPLATE:

For RIGHT rotation:

n = len(nums)
k %= n

reverse(0, n - 1)
reverse(0, k - 1)
reverse(k, n - 1)

Mental template:

RIGHT ROTATE

ALL
 ↓
FIRST k
 ↓
REST
'''

'''
LEFT ROTATION:

For LEFT rotation by k:

Reverse FIRST k
    ↓
Reverse REST
    ↓
Reverse ALL

Example:

[1,2,3,4,5]
left rotate by 2

First reverse first 2:

[2,1,3,4,5]

Reverse rest:

[2,1,5,4,3]

Reverse all:

[3,4,5,1,2]
'''

'''
FAMILY:

This problem belongs to:

ARRAY
    ↓
ARRAY ROTATION
    ↓
REVERSAL
    ↓
IN-PLACE ARRAY MANIPULATION

Related concepts:

- Left rotation
- Right rotation
- Reversal
- Two pointers
- In-place array manipulation
'''

'''
ONE-LINE MEMORY:

RIGHT ROTATE:

Reverse ALL
    ↓
Reverse FIRST k
    ↓
Reverse REST

B A

is created from:

A B
'''

'''
FINAL PATTERN:

ARRAY
   ↓
ROTATION
   ↓
IN-PLACE?
   ↓
REVERSAL TRICK
   ↓
O(n) TIME
O(1) EXTRA SPACE
'''