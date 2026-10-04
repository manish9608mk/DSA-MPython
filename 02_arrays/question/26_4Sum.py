# 18. 4Sum


from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # Sort the array to use two pointers and skip duplicates
        nums.sort()
        n = len(nums)
        result = []
        
        # First loop for the first number
        for i in range(n - 3):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Second loop for the second number
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left, right = j + 1, n - 1
                
                # Two pointers for the remaining two numbers
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return result

    
'''
PROBLEM

Given an integer array nums and an integer target, return all
unique quadruplets [a,b,c,d] such that:

a + b + c + d = target

The four elements must come from distinct indices.

Example:

nums = [1,0,-1,0,-2,2]
target = 0

Output:

[[-2,-1,1,2],
 [-2,0,0,2],
 [-1,0,0,1]]

Another example:

nums = [2,2,2,2,2]
target = 8

Output:

[[2,2,2,2]]

Important:

- The answer must contain unique quadruplets.
- Duplicate values are allowed in nums.
- Four indices must be distinct.
- Answer can be returned in any order.
- n <= 200.
'''


'''
PATTERN

Sorting + Two Pointers

4Sum can be reduced to 2Sum.

Think:

4 numbers
→ Fix first number
→ Fix second number
→ Find remaining two numbers
→ Two Pointers

Pattern:

i
j
left
right

After sorting:

nums[i] + nums[j] + nums[left] + nums[right] = target

For fixed i and j:

nums[left] + nums[right]
= target - nums[i] - nums[j]

So the remaining problem becomes a 2Sum problem.

Recognition:

Need 4 elements with a target sum
→ Fix 2 elements
→ Solve remaining 2 with Two Pointers

General pattern:

2Sum
→ Two Pointers

3Sum
→ Fix 1 + Two Pointers

4Sum
→ Fix 2 + Two Pointers

Mental Pattern:

Sort
→ Fix i
→ Fix j
→ Two Pointers
→ Skip duplicates
'''


'''
WHY SORTING?

Sorting gives two important benefits.

1. Two Pointers become possible.

If:

total < target

we need a larger value.

Because the array is sorted:

left += 1

If:

total > target

we need a smaller value.

So:

right -= 1

2. Duplicates become adjacent.

Example:

[2,2,2,2,2]

After sorting, equal values are together.

This makes it easy to skip duplicate values and
return only unique quadruplets.

Therefore:

Sort
→ Ordered values
→ Two Pointer movement
→ Easy duplicate handling
'''


'''
APPROACH 1 — BRUTE FORCE

Use four nested loops.

Choose:

i
j
k
l

For every combination:

if nums[i] + nums[j] + nums[k] + nums[l] == target

add the quadruplet.

To avoid duplicate answers, we can use a Set of tuples.

Why does it work?

Every possible group of four indices is checked.

Why is it inefficient?

There are O(n^4) combinations.

With n = 200, this is too slow.

TIME:

O(n^4)

SPACE:

O(number of unique answers)
'''


# BRUTE FORCE CODE

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        n = len(nums)
        result = set()

        for i in range(n - 3):
            for j in range(i + 1, n - 2):
                for k in range(j + 1, n - 1):
                    for l in range(k + 1, n):
                        total = nums[i] + nums[j] + nums[k] + nums[l]

                        if total == target:
                            result.add(
                                (nums[i], nums[j], nums[k], nums[l])
                            )

        return [list(quadruplet) for quadruplet in result]


'''
APPROACH 2 — HASHING

Fix two numbers:

i
j

Then find two more numbers using a Hash Set.

Required pair:

target - nums[i] - nums[j]

For each remaining value, check whether the required
complement has already been seen.

This reduces the main search to:

i loop
→ j loop
→ linear scan

TIME:

O(n^3)

SPACE:

O(n)

This is better than O(n^4), but duplicate handling is
less natural than the sorted Two Pointer solution.

The standard interview approach is:

Sorting + Two Pointers
'''


'''
APPROACH 3 — OPTIMAL / STANDARD

First sort the array.

Then:

1. Fix nums[i].
2. Fix nums[j].
3. Use left and right pointers for the remaining two values.

Structure:

i → first number
j → second number
left → third number
right → fourth number

Calculate:

total = nums[i] + nums[j] + nums[left] + nums[right]

Three cases:


CASE 1:

total == target

→ Found a valid quadruplet.
→ Add it to result.
→ Skip duplicate left/right values.
→ Move both pointers.


CASE 2:

total < target

The sum is too small.

Because the array is sorted:

left += 1


CASE 3:

total > target

The sum is too large.

Move:

right -= 1


Duplicate handling:

For i:

if i > 0 and nums[i] == nums[i - 1]:
    continue

For j:

if j > i + 1 and nums[j] == nums[j - 1]:
    continue

After finding an answer:

Skip duplicate left values.
Skip duplicate right values.
Then move both pointers.

TIME:

O(n^3)

SPACE:

O(1) extra space

excluding the returned result.
'''


'''
WHY TWO POINTERS?

After fixing i and j, only two numbers remain.

We need:

nums[left] + nums[right]
= target - nums[i] - nums[j]

Because nums is sorted:

If:

total < target

the sum is too small.

Moving left forward gives a larger or equal value.

So:

left += 1

If:

total > target

the sum is too large.

Moving right backward gives a smaller or equal value.

So:

right -= 1

If:

total == target

we found the required pair.

This works because sorting gives us the direction
in which the sum changes.
'''


'''
STEP-BY-STEP THINKING

1. What am I looking for?

→ Four numbers whose sum equals target.

2. What makes the problem harder?

→ Need unique quadruplets.

3. Can I use four loops?

→ Yes, but O(n^4) is too slow.

4. Can I reduce the number of loops?

→ Fix two numbers and solve the remaining two.

5. What technique solves the remaining two efficiently?

→ Two Pointers.

6. Why do I sort first?

→ It enables pointer movement and duplicate skipping.

7. How do I initialize the pointers?

left = j + 1
right = n - 1

8. What if total is too small?

→ left += 1

9. What if total is too large?

→ right -= 1

10. What if total equals target?

→ Add quadruplet.

11. How do I avoid duplicate quadruplets?

→ Skip duplicate i, j, left, and right values.

12. What is the complexity?

→ O(n^3) time.

Final thinking:

Sort
→ Fix first 2
→ Solve last 2
→ Two Pointers
→ Skip duplicates
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = (
                        nums[i]
                        + nums[j]
                        + nums[left]
                        + nums[right]
                    )

                    if total == target:
                        result.append([
                            nums[i],
                            nums[j],
                            nums[left],
                            nums[right]
                        ])

                        while left < right and nums[left] == nums[left + 1]:
                            left += 1

                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1

                        left += 1
                        right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result

# TEST CASE

nums = [1,0,-1,0,-2,2]
target = 0

solution = Solution()

answer = solution.fourSum(nums, target)

print("Input:", nums)
print("Target:", target)
print("Output:", answer)


'''
OUTPUT

Input: [1,0,-1,0,-2,2]
Target: 0

Output:

[[-2,-1,1,2],
 [-2,0,0,2],
 [-1,0,0,1]]
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

After sorting, we fix the first two values.

For those fixed values, the remaining problem is:

Find two numbers whose sum is:

target - nums[i] - nums[j]

The two-pointer method checks all relevant pairs
in the remaining sorted portion.

If the current sum is too small,
moving left increases the sum.

If the current sum is too large,
moving right decreases the sum.

Therefore every pointer movement moves toward the
required target without needing to check the discarded
pair again.

Sorting also places duplicates together.

Skipping equal values at each level prevents the same
value quadruplet from being added more than once.

Because i, j, left, and right always represent different
positions, the four indices are distinct.

Therefore the algorithm finds every valid unique
quadruplet exactly once.
'''


'''
DRY RUN

nums = [1,0,-1,0,-2,2]
target = 0

STEP 1 — SORT

nums:

[-2,-1,0,0,1,2]


STEP 2 — i = 0

nums[i] = -2

j = 1

nums[j] = -1

left = 2 → 0
right = 5 → 2

Calculate:

-2 + (-1) + 0 + 2
= -1

Too small.

Move left:

left = 3

Calculate:

-2 + (-1) + 0 + 2
= -1

Still too small.

Move left:

left = 4

Calculate:

-2 + (-1) + 1 + 2
= 0

Found:

[-2,-1,1,2]

Add it.

Move both pointers.

Now the pointers cross.

Next j:

j = 2

nums[j] = 0

left = 3
right = 5

Calculate:

-2 + 0 + 0 + 2
= 0

Found:

[-2,0,0,2]

Add it.

Next j would also point to another 0,
but it is a duplicate of the previous j value.

Skip it.


STEP 3 — i = 1

nums[i] = -1

j = 2

nums[j] = 0

left = 3
right = 5

Calculate:

-1 + 0 + 0 + 2
= 1

Too large.

Move right:

right = 4

Calculate:

-1 + 0 + 0 + 1
= 0

Found:

[-1,0,0,1]

Add it.

Final result:

[
    [-2,-1,1,2],
    [-2,0,0,2],
    [-1,0,0,1]
]
'''


'''
DRY RUN — ALL DUPLICATES

nums = [2,2,2,2,2]
target = 8

After sorting:

[2,2,2,2,2]

i = 0

nums[i] = 2

j = 1

nums[j] = 2

left = 2
right = 4

total:

2 + 2 + 2 + 2
= 8

Found:

[2,2,2,2]

Add it.

Skip duplicate left values.
Skip duplicate right values.

Move:

left
right

The remaining values do not generate another unique
quadruplet.

Final:

[[2,2,2,2]]
'''


'''
EDGE CASE 1 — NOT ENOUGH ELEMENTS

nums = [1,2,3]

There are fewer than 4 elements.

No quadruplet is possible.

The loops naturally return:

[]
'''


'''
EDGE CASE 2 — ALL VALUES ARE THE SAME

nums = [2,2,2,2,2]
target = 8

Only one unique quadruplet exists:

[2,2,2,2]

Duplicate skipping prevents repeated answers.
'''


'''
EDGE CASE 3 — NO VALID QUADRUPLET

nums = [1,2,3,4]
target = 100

No combination sums to 100.

Answer:

[]
'''


'''
EDGE CASE 4 — NEGATIVE VALUES

nums = [-3,-1,0,2,4,5]
target = 2

Negative values work normally because the comparison
is based on the total sum after sorting.
'''


'''
EDGE CASE 5 — TARGET CAN BE NEGATIVE

The target can be negative.

The same two-pointer logic still works.

No special handling is required.
'''


'''
EDGE CASE 6 — DUPLICATE VALUES ARE VALID

Duplicate values are allowed.

The goal is not:

"Use every value only once."

The goal is:

"Return each value quadruplet only once."

For example:

[2,2,2,2]

is a valid answer.
'''


'''
TIME & SPACE COMPLEXITY

Sorting:

O(n log n)

First fixed element:

O(n)

Second fixed element:

O(n)

Two pointers:

O(n)

Overall:

O(n^3)

Since n <= 200, this is suitable.

Extra space:

O(1)

The returned result itself requires space depending
on the number of quadruplets.
'''


'''
INTERVIEW EXPLANATION

"I first sort the array so I can use two pointers and
handle duplicates easily.

Then I fix the first two numbers using two loops.
For each pair, I use left and right pointers to find
the remaining two numbers.

If the total is smaller than target, I move left forward
to increase the sum. If it is larger, I move right
backward to decrease the sum.

When the total equals target, I add the quadruplet and
skip duplicate values before moving both pointers.

The overall time complexity is O(n^3), and the extra
space is O(1), excluding the output."
'''


'''
RECOGNITION TRICKS

1. Four numbers + target sum

→ Think 4Sum.

2. 4Sum can be reduced to:

→ Fix 2 + solve 2.

3. Sorted array + pair sum

→ Two Pointers.

4. Unique combinations required

→ Sort + skip duplicates.

5. Sum too small

→ Move left.

6. Sum too large

→ Move right.

Quick recognition:

4Sum
→ Sort
→ Fix i
→ Fix j
→ Two Pointers
→ Skip duplicates
'''


'''
REUSABLE TEMPLATE

nums.sort()

for i in range(n - 3):

    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, n - 2):

        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total == target:
                # Save answer
                # Skip duplicate left/right
                # Move both

            elif total < target:
                left += 1

            else:
                right -= 1

Core pattern:

Fix
→ Fix
→ Two Pointers
→ Skip duplicates
'''


'''
FAMILY

Sum + Two Pointer Problems

2Sum:

Two Pointers

3Sum:

Fix one
→ Two Pointers

4Sum:

Fix two
→ Two Pointers

General idea:

kSum
→ Fix elements
→ Reduce to a smaller Sum problem

Related problems:

- 1. Two Sum
- 15. 3Sum
- 16. 3Sum Closest
- 18. 4Sum
- kSum-style problems
'''


'''
COMMON INTERVIEW MISTAKES

1. Not sorting the array.

Two-pointer movement and duplicate skipping depend
on sorting.

2. Using four loops.

This gives O(n^4).

Use:

2 loops + Two Pointers

for O(n^3).

3. Forgetting duplicate i values.

Use:

if i > 0 and nums[i] == nums[i - 1]:
    continue

4. Forgetting duplicate j values.

Use:

if j > i + 1 and nums[j] == nums[j - 1]:
    continue

5. Forgetting duplicate left/right values after
   finding an answer.

6. Moving the wrong pointer.

Remember:

total < target
→ left++

total > target
→ right--

7. Thinking duplicate values are not allowed.

They are allowed.

Only duplicate quadruplets are not allowed.

8. Using a Set as the main solution unnecessarily.

Sorting + pointer duplicate skipping gives the
standard clean solution.

9. Forgetting that the four indices must be distinct.

Using:

i < j < left < right

ensures distinct positions.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Complete pattern:

4Sum
→ Sort
→ Fix first number
→ Fix second number
→ Two Pointers for last two
→ Skip duplicates


Pointer rule:

total < target
→ left++

total > target
→ right--

total == target
→ Add quadruplet
→ Skip duplicate left/right
→ Move both


Duplicate rule:

Duplicate i
→ Skip

Duplicate j
→ Skip

Duplicate left/right
→ Skip after finding a valid answer


One-line rule:

4Sum
→ Fix 2
→ Two Pointers
→ Sort
→ Skip Duplicates


Final Mental Model:

         i       j       left       right
         ↓       ↓        ↓           ↓
[-2, -1,  0,      0,       1,          2]

Fix i
→ Fix j
→ Search remaining pair

If sum is small:

→ left++

If sum is large:

→ right--

If sum matches:

→ Save
→ Skip duplicates
→ Move both


Most important sentence:

"4Sum is 2Sum after fixing two numbers, and sorting
lets me solve the remaining pair with Two Pointers
while also removing duplicate quadruplets."
'''