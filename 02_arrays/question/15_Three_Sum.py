# 15. 3Sum

'''
Link:
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets
[nums[i], nums[j], nums[k]] such that:

i != j
i != k
j != k

and:

nums[i] + nums[j] + nums[k] == 0

The solution set must not contain duplicate triplets.

Example:

Input:
[-1, 0, 1, 2, -1, -4]

Output:
[[-1, -1, 2], [-1, 0, 1]]
'''


'''
PATTERN:

3 numbers
    +
Target sum
    ↓
3Sum

Think of 3Sum as an extension of Two Sum:

a + b + c = 0

Fix a
    ↓
b + c = -a
    ↓
Now solve Two Sum

But we need:
    ↓
Unique triplets
    ↓
SORTING helps handle duplicates
    ↓
TWO POINTERS

Final pattern:

SORTING + FIX ONE ELEMENT + TWO POINTERS
'''


'''
APPROACH 1 — BRUTE FORCE:

Try every possible combination of 3 elements.

for i:
    for j:
        for k:
            if nums[i] + nums[j] + nums[k] == 0:
                add triplet

Problem:

The same triplet can appear in different orders:

[-1, 0, 1]
[0, 1, -1]
[1, -1, 0]

So duplicate handling becomes difficult.

TIME:
O(n^3)

SPACE:
O(1) extra
excluding output

This is too slow for n = 3000.
'''


'''
BRUTE FORCE CODE:

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result = []

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    if nums[i] + nums[j] + nums[k] == 0:
                        triplet = [nums[i], nums[j], nums[k]]

                        if triplet not in result:
                            result.append(triplet)

        return result

NOTE:

The duplicate check:

triplet not in result

also takes O(n) in the worst case.

So this approach is mainly useful for understanding
the problem, not for the final solution.
'''


'''
APPROACH 2 — HASH SET:

Fix one number.

a + b + c = 0

For a fixed a:

b + c = -a

Now use a hash set to find the required complement.

For every b:

needed = -a - b

If needed is already seen:
    triplet found

This can achieve approximately:

TIME:
O(n^2)

SPACE:
O(n)

However, duplicate handling is more complicated.

Since 3Sum naturally benefits from a sorted array,
the standard interview solution is:

SORTING + TWO POINTERS
'''


'''
APPROACH 3 — OPTIMAL / STANDARD:

Step 1:
Sort the array.

Example:

[-1, 0, 1, 2, -1, -4]

        ↓

[-4, -1, -1, 0, 1, 2]


Step 2:
Fix one element using i.

Step 3:
Use two pointers:

left = i + 1
right = n - 1

Step 4:
Calculate:

total = nums[i] + nums[left] + nums[right]


If total < 0:

We need a bigger number.

Because the array is sorted:

left += 1


If total > 0:

We need a smaller number.

right -= 1


If total == 0:

We found a valid triplet.

Add it to result.

Then move both pointers.


IMPORTANT:

Skip duplicate values for i.

if i > 0 and nums[i] == nums[i - 1]:
    continue

Also skip duplicate left/right values after finding
a valid triplet.
'''


'''
OPTIMAL CODE:
'''
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif total < 0:
                    left += 1

                else:
                    right -= 1

        return result


# Test Case
nums = [-1, 0, 1, 2, -1, -4]

solution = Solution()
answer = solution.threeSum(nums)

print("Input:", nums)
print("Output:", answer)


'''
STEP-BY-STEP THINKING:

Given:

a + b + c = 0

Think:

1. Can I fix one number?
        ↓
   Yes.

2. After fixing a, what remains?
        ↓
   b + c = -a

3. What problem is this?
        ↓
   Two Sum.

4. How can I solve Two Sum efficiently here?
        ↓
   Two pointers after sorting.

5. Why sort?
        ↓
   To move pointers intelligently
   and handle duplicates easily.

6. What if sum is too small?
        ↓
   Move left forward.

7. What if sum is too large?
        ↓
   Move right backward.

8. What if sum == 0?
        ↓
   Save triplet and move both pointers.

9. How do I avoid duplicate triplets?
        ↓
   Skip duplicate i, left, and right values.
'''


'''
WHY DOES THE TWO-POINTER APPROACH WORK?

Because the array is sorted.

Example:

[-4, -1, -1, 0, 1, 2]
          L        R

If:

nums[i] + nums[L] + nums[R] < 0

The sum is too small.

Moving R left would make the sum even smaller.

So the only useful direction is:

L → right

which increases the sum.

Similarly, if:

sum > 0

Moving L right would make the sum even larger.

So we move:

R → left

which decreases the sum.

Therefore:

sum < 0 → left++
sum > 0 → right--
sum == 0 → found
'''


'''
DUPLICATE HANDLING:

This is one of the most important parts of 3Sum.

Example:

[-1, -1, 0, 1]

If we use the first -1:

[-1, 0, 1]

Then if we use the second -1,
we would find the same triplet again.

So:

if i > 0 and nums[i] == nums[i - 1]:
    continue

This skips duplicate choices for the first number.


After finding a triplet:

[-1, 0, 1]

Move:

left += 1
right -= 1

Then skip repeated values:

while left < right and nums[left] == nums[left - 1]:
    left += 1

while left < right and nums[right] == nums[right + 1]:
    right -= 1

This guarantees unique triplets.
'''


'''
DRY RUN:

Input:

[-1, 0, 1, 2, -1, -4]


After sorting:

[-4, -1, -1, 0, 1, 2]


i = 0

nums[i] = -4

left = 1 → -1
right = 5 → 2

sum:

-4 + (-1) + 2 = -3

sum < 0

Move:

left++


Continue moving left until no valid
triplet is possible for -4.


i = 1

nums[i] = -1

left = 2 → -1
right = 5 → 2

sum:

-1 + (-1) + 2 = 0

Found:

[-1, -1, 2]


Move:

left++
right--

Now:

left = 3 → 0
right = 4 → 1

sum:

-1 + 0 + 1 = 0

Found:

[-1, 0, 1]


Move both pointers again.


i = 2

nums[2] == nums[1]

Both are:

-1

So skip i = 2.

Final result:

[[-1, -1, 2], [-1, 0, 1]]
'''


'''
TEST CASE:

nums = [-1, 0, 1, 2, -1, -4]

Solution:

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        result = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i + 1
            right = len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1

                else:
                    result.append([
                        nums[i],
                        nums[left],
                        nums[right]
                    ])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return result


Output:

[[-1, -1, 2], [-1, 0, 1]]
'''


'''
EDGE CASE 1:

Input:

[0, 1, 1]

No three numbers sum to 0.

Output:

[]
'''


'''
EDGE CASE 2:

Input:

[0, 0, 0]

Output:

[[0, 0, 0]]

Even though all values are duplicates,
we return the triplet only once.
'''


'''
EDGE CASE 3:

Input:

[1, 2, 3, 4]

All numbers are positive.

No triplet can sum to 0.

Output:

[]
'''


'''
EDGE CASE 4:

Input:

[-3, -2, -1]

All numbers are negative.

No triplet can sum to 0.

Output:

[]
'''


'''
TIME & SPACE COMPLEXITY:

Sorting:

O(n log n)

Outer loop:

O(n)

Two pointers for each i:

O(n)

Therefore:

O(n log n) + O(n^2)

= O(n^2)


Extra space:

O(1)

excluding the output array.

Python's sort uses internal memory, but the
algorithm's auxiliary working space is generally
considered O(1) for this problem.
'''


'''
INTERVIEW EXPLANATION:

"I'll first sort the array so that I can use two
pointers and handle duplicates easily.

For every index i, I'll treat nums[i] as the first
number of the triplet.

Then I'll use left = i + 1 and right = n - 1 to find
two numbers whose sum is -nums[i].

If the total is smaller than zero, I'll move left
forward because the array is sorted and I need a
larger value.

If the total is greater than zero, I'll move right
backward to get a smaller value.

When the total is zero, I'll add the triplet and move
both pointers.

Finally, I'll skip duplicate values for i, left, and
right so that the result contains only unique triplets.

The time complexity is O(n^2) and the extra space is
O(1), excluding the output."
'''


'''
RECOGNITION TRICKS:

When you see:

"Find three numbers..."
        +
"sum equals target / zero"
        ↓
Think 3Sum.

Immediately convert:

a + b + c = target

Fix a:

b + c = target - a

Now you have Two Sum.

If:
    duplicates matter
    +
    array can be sorted

Think:

SORT
  ↓
FIX ONE
  ↓
TWO POINTERS
  ↓
SKIP DUPLICATES


Quick mental rule:

2 numbers → Two Sum
3 numbers → Fix one + Two Sum
4 numbers → Fix two + Two Sum

This idea becomes useful for 4Sum and kSum too.
'''


'''
REUSABLE TEMPLATE:

3Sum / sorted two-pointer family:

nums.sort()
result = []

for i in range(n - 2):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    left = i + 1
    right = n - 1

    while left < right:

        total = nums[i] + nums[left] + nums[right]

        if total < target:
            left += 1

        elif total > target:
            right -= 1

        else:
            result.append([
                nums[i],
                nums[left],
                nums[right]
            ])

            left += 1
            right -= 1

            # Skip duplicates
            while left < right and nums[left] == nums[left - 1]:
                left += 1

            while left < right and nums[right] == nums[right + 1]:
                right -= 1
'''


'''
FAMILY:

3Sum
    ↓
4Sum
    ↓
kSum

Also related to:

Two Sum
Two Sum II
3Sum Closest
3Sum Smaller
4Sum

Core idea:

FIX SOME ELEMENTS
        ↓
REDUCE THE PROBLEM
        ↓
TWO POINTERS / HASHING
'''


'''
COMMON INTERVIEW MISTAKES:

1. Forgetting to sort.

2. Using three nested loops unnecessarily.

3. Not skipping duplicate i values.

4. Not skipping duplicate left/right values.

5. Moving only one pointer after finding a valid
   triplet.

6. Moving left when sum > 0.

7. Moving right when sum < 0.

Correct:

sum < 0 → left++
sum > 0 → right--

8. Forgetting that [0,0,0] should return only:

[[0,0,0]]

9. Returning duplicate triplets.

10. Using a set without understanding how duplicate
    triplets will be handled.
'''


'''
MOST IMPORTANT THING TO REMEMBER:

Don't memorize the 3Sum code.

Memorize the thinking:

3Sum
  ↓
Fix one number
  ↓
Remaining two numbers
  ↓
Two Sum
  ↓
Sort the array
  ↓
Two pointers
  ↓
sum < 0 → left++
sum > 0 → right--
sum == 0 → save
  ↓
Skip duplicates


This is the real pattern.
'''