# 33. Search in Rotated Sorted Array
    
'''
PROBLEM

You are given an ascending sorted array with distinct values.

The array may have been rotated at an unknown index.

Example:

Original:

[0,1,2,4,5,6,7]

After rotation:

[4,5,6,7,0,1,2]


Given nums and target, return the index of target.

If target does not exist, return -1.


Example:

nums = [4,5,6,7,0,1,2]
target = 0

Output = 4


Important:

- Values are distinct.
- The original array is sorted.
- The array may be rotated.
- Required time complexity = O(log n).
'''


'''
PATTERN

Modified Binary Search


A rotated sorted array is not completely sorted,
but it has an important property:

At least one half is always sorted.


Example:

[4,5,6,7,0,1,2]
 L     M       R


At any mid:

Either:

Left half is sorted

or:

Right half is sorted


Then:

1. Identify the sorted half.
2. Check whether target is inside that half.
3. Search that half if yes.
4. Otherwise search the other half.


Recognition:

Sorted array
→ Rotated
→ Distinct values
→ O(log n)

Think:

Modified Binary Search
'''


'''
APPROACH 1 — BRUTE FORCE

Scan the array from left to right.

For every index:

if nums[i] == target:
    return i

If the loop finishes:

return -1


Why does it work?

We directly check every element.


Example:

nums = [4,5,6,7,0,1,2]
target = 0

Scan:

4 → no
5 → no
6 → no
7 → no
0 → found at index 4


TIME:

O(n)


SPACE:

O(1)


Why is it not enough?

The problem requires O(log n).
'''


'''
# BRUTE FORCE CODE
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1


'''
APPROACH 2 — BETTER APPROACH

Find the rotation point first, then perform Binary Search
on the two sorted parts.


Example:

[4,5,6,7,0,1,2]

Rotation point:

index 4


Two sorted parts:

[4,5,6,7]
[0,1,2]


Step 1:

Find the smallest element / rotation point.


Step 2:

Check which sorted part can contain target.


Step 3:

Perform normal Binary Search in that part.


Complexity:

Finding rotation point = O(log n)
Binary Search = O(log n)

Overall:

O(log n) time


Space:

O(1)


This works, but it uses two separate phases.

We can solve the problem in one Binary Search pass,
which is the standard interview solution.
'''


'''
# BETTER CODE
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)

        # Find rotation point.
        left = 0
        right = n - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        pivot = left

        # Binary search helper.
        def binary_search(left: int, right: int) -> int:
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] == target:
                    return mid

                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return -1

        if nums[pivot] <= target <= nums[n - 1]:
            return binary_search(pivot, n - 1)

        return binary_search(0, pivot - 1)


'''
APPROACH 3 — OPTIMAL / STANDARD

Use one modified Binary Search.


Start:

left = 0
right = n - 1


At every step:

mid = (left + right) // 2


First check:

nums[mid] == target

If yes:

return mid


Otherwise, determine which half is sorted.


CASE 1 — LEFT HALF IS SORTED

Condition:

nums[left] <= nums[mid]


Example:

[4,5,6,7,0,1,2]
 L     M


The left half:

[4,5,6,7]

is sorted.


Now ask:

Is target inside this sorted range?


Condition:

nums[left] <= target < nums[mid]


If yes:

right = mid - 1


Otherwise:

left = mid + 1


CASE 2 — RIGHT HALF IS SORTED

If the left half is not sorted,
the right half must be sorted.


Example:

[6,7,0,1,2,4,5]
 L     M     R


Right half:

[1,2,4,5]

is sorted.


Check whether target lies there:

nums[mid] < target <= nums[right]


If yes:

left = mid + 1


Otherwise:

right = mid - 1


TIME:

O(log n)


SPACE:

O(1)
'''


'''
WHY MODIFIED BINARY SEARCH?

Normal Binary Search needs the whole array to be sorted.

A rotated array is not fully sorted.

Example:

[4,5,6,7,0,1,2]


But at every mid, at least one half is sorted.


That is enough.

Once we identify the sorted half,
we can determine whether target belongs there.


So:

Rotated array
→ Find sorted half
→ Check target range
→ Discard the impossible half


This allows us to remove about half of the
search space every iteration.
'''


'''
STEP-BY-STEP THINKING

1. What is being asked?

→ Find the index of target.


2. What is special about nums?

→ It was sorted, then possibly rotated.


3. Can I use normal Binary Search?

→ Not directly, because the whole array is not sorted.


4. What useful property remains?

→ At least one half is always sorted.


5. How do I identify the sorted half?

→ Compare nums[left] and nums[mid].


6. If:

nums[left] <= nums[mid]

→ Left half is sorted.


7. Is target inside that sorted range?

nums[left] <= target < nums[mid]


If yes:

→ Search left.


Otherwise:

→ Search right.


8. If left half is not sorted:

→ Right half is sorted.


9. Is target inside the right sorted range?

nums[mid] < target <= nums[right]


If yes:

→ Search right.


Otherwise:

→ Search left.


10. When do I stop?

→ When left > right.


11. If target was never found:

→ return -1.


Final Thinking:

Binary Search
→ Identify sorted half
→ Check target range
→ Eliminate one half
→ Repeat
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # Binary search in rotated sorted array
        while left <= right:
            mid = (left + right) // 2

            # Check if mid is the target
            if nums[mid] == target:
                return mid

            # Determine which half is sorted or, Left half is sorted.
            if nums[left] <= nums[mid]:

                # Left half is sorted
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

            # Right half is sorted.
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        # Target not found            
        return -1


# TEST CASE

nums = [4,5,6,7,0,1,2]
target = 0

solution = Solution()

answer = solution.search(nums, target)

print("Input:", nums)
print("Target:", target)
print("Output:", answer)



'''
OUTPUT

Input: [4,5,6,7,0,1,2]
Target: 0
Output: 4
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

At every iteration, we know that at least one half
is sorted.


CASE 1:

nums[left] <= nums[mid]

The left half is sorted.


If:

nums[left] <= target < nums[mid]

then target must be inside the left sorted half.

So:

right = mid - 1


Otherwise, target cannot be in that half,
so we search the right half:

left = mid + 1


CASE 2:

The left half is not sorted.

Therefore the right half is sorted.


If:

nums[mid] < target <= nums[right]

then target lies in the right sorted half.

So:

left = mid + 1


Otherwise:

right = mid - 1


Every step removes a half that cannot contain target.

Therefore the search space shrinks logarithmically.

Because all values are distinct, there is no ambiguity
when deciding which half is sorted.


Hence:

TIME = O(log n)
SPACE = O(1)
'''


'''
DRY RUN

nums = [4,5,6,7,0,1,2]
target = 0


Start:

left = 0
right = 6


STEP 1:

mid = (0 + 6) // 2
    = 3


Values:

nums[left] = 4
nums[mid] = 7
nums[right] = 2


Check:

4 <= 7

So left half is sorted:

[4,5,6,7]


Is target 0 inside:

4 <= 0 < 7

No.


Therefore target must be in the right half.

left = mid + 1

left = 4


Now:

left = 4
right = 6


STEP 2:

mid = (4 + 6) // 2
    = 5


Values:

nums[left] = 0
nums[mid] = 1
nums[right] = 2


Check:

0 <= 1

So left half is sorted:

[0,1]


Is target 0 inside:

0 <= 0 < 1

Yes.


Therefore:

right = mid - 1

right = 4


Now:

left = 4
right = 4


STEP 3:

mid = 4


nums[4] = 0


Target found.


Return:

4
'''


'''
DRY RUN — TARGET NOT FOUND

nums = [4,5,6,7,0,1,2]
target = 3


Start:

left = 0
right = 6
mid = 3


nums[mid] = 7

Left half is sorted:

[4,5,6,7]


Target 3 is not in:

[4,7)


So:

left = 4


Now search:

[0,1,2]


None of these is 3.

Eventually:

left > right


Therefore:

return -1
'''


'''
DRY RUN — ROTATION IN A DIFFERENT POSITION

nums = [6,7,0,1,2,4,5]
target = 4


Start:

left = 0
right = 6
mid = 3


nums[mid] = 1


Left half:

[6,7,0,1]

is not sorted.


Therefore right half is sorted:

[1,2,4,5]


Check:

1 < 4 <= 5

Yes.


So:

left = mid + 1

left = 4


Continue Binary Search.

Eventually:

nums[5] = 4


Answer:

5
'''


'''
EDGE CASE 1 — SINGLE ELEMENT

nums = [1]
target = 1


left = 0
right = 0
mid = 0


nums[mid] == target

Return:

0
'''


'''
EDGE CASE 2 — SINGLE ELEMENT, NOT FOUND

nums = [1]
target = 0


nums[0] != 0


Search ends immediately.

Return:

-1
'''


'''
EDGE CASE 3 — ALREADY SORTED

nums = [1,2,3,4,5]
target = 3


Even without rotation,
the algorithm works normally.


At each step, the left half is sorted.

Answer:

2
'''


'''
EDGE CASE 4 — TARGET AT ROTATION POINT

nums = [4,5,6,7,0,1,2]
target = 0


The rotation point is index 4.

The algorithm can find it directly.


Answer:

4
'''


'''
EDGE CASE 5 — TARGET AT FIRST POSITION

nums = [4,5,6,7,0,1,2]
target = 4


The target is at index 0.


Answer:

0
'''


'''
EDGE CASE 6 — TARGET AT LAST POSITION

nums = [4,5,6,7,0,1,2]
target = 2


The target is at index 6.


Answer:

6
'''


'''
TIME & SPACE COMPLEXITY

Each Binary Search iteration eliminates roughly half
of the remaining search space.


Therefore:

TIME = O(log n)


Only three variables are used:

left
right
mid


No extra array or data structure is required.


Therefore:

SPACE = O(1)


Final:

Time  = O(log n)
Space = O(1)
'''


'''
INTERVIEW EXPLANATION

"I use a modified Binary Search.

Because the original array was sorted and then rotated,
at least one half of the current search range is always
sorted.

At each step, I determine which half is sorted.

If the left half is sorted, I check whether the target
lies within its value range. If it does, I search left;
otherwise I search right.

If the right half is sorted, I perform the symmetric
check.

Since one half is eliminated at every step, the time
complexity is O(log n), with O(1) extra space."
'''


'''
RECOGNITION TRICKS

1. Sorted array + rotation

→ Modified Binary Search


2. Distinct values

→ At least one half is clearly sorted.


3. Compare:

nums[left] <= nums[mid]

→ Left half sorted.


4. Otherwise:

→ Right half sorted.


5. Then ask:

"Can target exist inside the sorted half?"


Quick pattern:

Rotated Sorted Array
→ Find sorted half
→ Check target range
→ Discard other half
'''


'''
REUSABLE TEMPLATE

left = 0
right = len(nums) - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        return mid

    if nums[left] <= nums[mid]:

        # Left half is sorted.
        if nums[left] <= target < nums[mid]:
            right = mid - 1
        else:
            left = mid + 1

    else:

        # Right half is sorted.
        if nums[mid] < target <= nums[right]:
            left = mid + 1
        else:
            right = mid - 1

return -1


Remember:

Left sorted
→ target in left range?
→ left or right


Right sorted
→ target in right range?
→ right or left
'''


'''
FAMILY

Binary Search on Modified / Special Arrays


Related problems:

- 81. Search in Rotated Sorted Array II
- 153. Find Minimum in Rotated Sorted Array
- 154. Find Minimum in Rotated Sorted Array II
- 162. Find Peak Element
- 852. Peak Index in a Mountain Array


Common idea:

Use the structure of the array
→ Determine which direction/half is useful
→ Eliminate part of the search space
→ O(log n)
'''


'''
COMMON INTERVIEW MISTAKES

1. Treating the whole rotated array as sorted.

It is not.

At least one half is sorted.


2. Forgetting to check which half is sorted.

This is the main idea of the problem.


3. Using the wrong left-half condition.

Correct:

nums[left] <= nums[mid]


4. Using the wrong target range.

Left sorted:

nums[left] <= target < nums[mid]


Right sorted:

nums[mid] < target <= nums[right]


5. Using:

right = mid

after deciding the target is on the left.

Correct:

right = mid - 1

because nums[mid] was already checked.


6. Using:

left = mid

instead of:

left = mid + 1

when searching right.

Again, nums[mid] was already checked.


7. Forgetting the distinct-values condition.

This solution relies on the fact that values are unique.


8. Returning -1 too early.

Only return -1 after:

left > right
'''


'''
MOST IMPORTANT THING TO REMEMBER

Complete pattern:

Rotated Sorted Array
→ Modified Binary Search


At every mid:

1. Check target.


2. Find sorted half.

nums[left] <= nums[mid]
→ Left half sorted

Otherwise
→ Right half sorted


3. Check whether target belongs to
   the sorted half.


4. Search that half or discard it.


One-line rule:

Rotated Array
→ Find Sorted Half
→ Check Target Range
→ Eliminate One Half
→ Repeat


Final Mental Model:

[ sorted part | rotated part ]
        ↓
       MID
        ↓
Which side is sorted?
        ↓
Can target be there?
        ↓
YES → search there
NO  → search other side


The most important interview sentence:

"I don't need the whole array to be sorted.
I only need to identify which half is sorted,
then use that sorted half to decide where the
target can exist."
'''