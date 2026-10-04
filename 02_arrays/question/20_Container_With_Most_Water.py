# 11. Container With Most Water

'''
PROBLEM

You are given an integer array height.

height[i] represents the height of a vertical line at index i.

Choose two different lines that, together with the x-axis,
form a container.

Return the maximum amount of water the container can store.


Example:

height = [1,8,6,2,5,4,8,3,7]

Choose:

index 1 → height 8
index 8 → height 7


Width:

8 - 1 = 7


Height of water is limited by the shorter line:

min(8,7) = 7


Area:

7 × 7 = 49


Output:

49


Important:

- The container cannot be slanted.
- Width = distance between the two indices.
- Water height = shorter of the two lines.
- We need the maximum area.
'''


'''
PATTERN

Two Pointers


For two indices:

left
right


The area is:

area = (right - left) * min(height[left], height[right])


Start with:

left = 0
right = n - 1


Why?

The two ends give the maximum possible width.

Then, after calculating the current area,
move the pointer at the shorter line.


Recognition:

Choose two elements
→ Distance between them matters
→ Need maximum area
→ Two Pointers


Mental Pattern:

Start at both ends
→ Calculate area
→ Find shorter side
→ Move shorter side
→ Repeat


Most important rule:

Move the shorter pointer.
'''


'''
APPROACH 1 — BRUTE FORCE

Try every possible pair of lines.

For every pair (i, j):

1. Calculate the width.
2. Find the shorter height.
3. Calculate the area.
4. Keep the maximum.


Formula:

area = (j - i) * min(height[i], height[j])


Example:

height = [1,8,6,2]

Pair (1,2):

width = 2 - 1 = 1
height = min(8,6) = 6

area = 1 * 6 = 6


Check every possible pair and return the largest area.


Why does it work?

Every possible pair is checked,
so the maximum pair must be found.


Why is it inefficient?

There are O(n²) possible pairs.

With n = 10^5, this is too slow.


TIME:

O(n²)


SPACE:

O(1)
'''


'''
# BRUTE FORCE CODE
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        max_area = 0
        n = len(height)

        for i in range(n):
            for j in range(i + 1, n):
                width = j - i
                current_height = min(height[i], height[j])

                area = width * current_height
                max_area = max(max_area, area)

        return max_area


'''
APPROACH 2 — OPTIMAL / TWO POINTERS

We do not need to check every pair.

Start with the widest possible container:

left = 0
right = n - 1


At every step:

1. Calculate the current area.
2. Update max_area.
3. Move the pointer at the shorter line.


Why does the shorter line matter?

Suppose:

height[left] = 8
height[right] = 5


The water height is:

min(8,5) = 5


So the right side is the bottleneck.


If we move the left pointer:

- Width becomes smaller.
- The right height is still 5.
- The water height cannot become greater than 5
  as long as this right line remains.

Therefore, keeping the shorter line cannot produce
a better container by moving the taller side.

Instead, discard the shorter side and look for a taller line.


Rule:

if height[left] < height[right]:
    left += 1
else:
    right -= 1


This removes impossible candidates while keeping the
possibility of finding a larger area.


TIME:

O(n)


SPACE:

O(1)
'''


'''
WHY TWO POINTERS?

The area has two important parts:

1. Width
2. Height


Width:

right - left


Height:

min(height[left], height[right])


At the beginning, left and right are at the two ends,
so the width is maximum.


As pointers move inward:

width always decreases.


Therefore, to improve the area,
we need to increase the limiting height.


The limiting height is the shorter line.

So:

Shorter line
→ Bottleneck

Move shorter line
→ Chance to find a taller line

This is the key idea behind the algorithm.
'''


'''
STEP-BY-STEP THINKING

1. What am I trying to maximize?

→ Amount of water.


2. What is the area formula?

→ width × shorter height.


3. What is the width?

→ right - left.


4. What determines the water height?

→ min(height[left], height[right]).


5. What pair gives the maximum initial width?

→ The first and last elements.


6. Which data structure/pattern fits?

→ Two Pointers.


7. What should I calculate at every step?

→ Current area.


8. Which pointer should move?

→ The pointer at the shorter line.


9. Why?

→ The shorter line limits the water.
  Moving the taller line only decreases width while
  keeping the same limiting height.


10. When do I stop?

→ When left >= right.


11. What must I keep?

→ The maximum area seen so far.


Final Thinking:

Start from both ends
→ Calculate area
→ Move shorter side
→ Repeat
→ Return maximum
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1

        max_area = 0

        while left < right:
            width = right - left
            current_height = min(height[left], height[right])

            area = width * current_height
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


'''
TEST CASE

height = [1,8,6,2,5,4,8,3,7]

solution = Solution()

answer = solution.maxArea(height)

print("Input:", height)
print("Output:", answer)
'''


'''
OUTPUT

Input: [1,8,6,2,5,4,8,3,7]

Output: 49
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

At any step, we have two lines:

left
right


Suppose:

height[left] <= height[right]


Then the current container height is:

height[left]


Now keep left fixed and move right inward.

The width becomes smaller.

The new height is:

min(height[left], height[new_right])


This can never be greater than height[left].


So:

width decreases
height cannot increase


Therefore, moving right cannot produce a better
container while left remains fixed.

The current left line can safely be discarded.

So we move:

left += 1


The same reasoning applies when the right line is shorter.

If:

height[right] < height[left]

then right is the bottleneck,
so we move:

right -= 1


Therefore, every pointer movement discards only a side
that cannot lead to a better answer with the current
opposite side.

Since every possible useful candidate is preserved,
the maximum area is found.


Key idea:

Shorter side is the bottleneck
→ Discard shorter side
→ Search for a taller side
'''


'''
DRY RUN

height = [1,8,6,2,5,4,8,3,7]


Start:

left = 0
right = 8

height[left] = 1
height[right] = 7


Width:

8 - 0 = 8


Height:

min(1,7) = 1


Area:

8 × 1 = 8


max_area = 8


1 is shorter:

left += 1


Now:

left = 1
right = 8

heights:

8 and 7


Width:

8 - 1 = 7


Height:

min(8,7) = 7


Area:

7 × 7 = 49


max_area = 49


7 is shorter:

right -= 1


Now:

left = 1
right = 7

heights:

8 and 3


Width:

7 - 1 = 6


Height:

3


Area:

6 × 3 = 18


max_area remains 49


3 is shorter:

right -= 1


Continue the same process.

No later pair produces an area greater than 49.


Final:

max_area = 49


Answer:

49
'''


'''
DRY RUN — IMPORTANT POINTER DECISION

Suppose:

height[left] = 8
height[right] = 5


Current height:

min(8,5) = 5


The right side is the bottleneck.


If we move left:

width decreases

but the height is still limited by 5.


So this cannot improve the current area.


Instead:

move right


Now we search for a new right line that may be
taller than 5.


This is why:

shorter side → move
'''


'''
DRY RUN — EQUAL HEIGHTS

Suppose:

height[left] = 5
height[right] = 5


Current height:

5


Either pointer can be moved.

For example:

right -= 1


The common implementation is:

if height[left] < height[right]:
    left += 1
else:
    right -= 1


So equal heights move the right pointer.

The important rule is only:

When the heights are different,
move the shorter side.
'''


'''
EDGE CASE 1 — TWO ELEMENTS

height = [1,1]


left = 0
right = 1


width = 1
height = 1

area = 1


Answer:

1
'''


'''
EDGE CASE 2 — ONE VERY TALL LINE

height = [1,10,1]


Possible container:

index 0 and index 2

width = 2
height = min(1,1) = 1

area = 2


The tall middle line cannot form a container with itself.

Two different lines are always required.
'''


'''
EDGE CASE 3 — ALL HEIGHTS ARE THE SAME

height = [5,5,5,5]


Start:

left = 0
right = 3

width = 3
height = 5

area = 15


The maximum is created by the two outermost lines.

The algorithm handles equal heights naturally.
'''


'''
EDGE CASE 4 — ZERO HEIGHT

height = [0,5,0]


Any container using a zero-height line
stores zero water.

The algorithm still works because:

min(0,5) = 0
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = len(height)


At every iteration, at least one pointer moves.


Each pointer can move only toward the other pointer,
so the total number of iterations is O(n).


Therefore:

TIME = O(n)


Only a few variables are used:

left
right
max_area


No extra data structure is required.

Therefore:

SPACE = O(1)


Final:

Time  → O(n)
Space → O(1)
'''


'''
INTERVIEW EXPLANATION

"I use two pointers, one at the beginning and one at
the end of the array.

For any two lines, the area is:

(right - left) * min(height[left], height[right])

I calculate the area and update the maximum.

The shorter line limits the water height. If I move the
taller side inward, the width decreases while the shorter
side still limits the height, so that move cannot improve
the area for the current pair.

Therefore, I always move the pointer at the shorter line.

This gives O(n) time and O(1) extra space."
'''


'''
RECOGNITION TRICKS

1. Choose two elements

→ Think Two Pointers.


2. Distance between indices affects the answer

→ Width = right - left.


3. The answer depends on the smaller of two values

→ min(height[left], height[right]).


4. Starting from opposite ends gives maximum width.


5. When one side is the bottleneck:

→ Move the shorter side.


Quick recognition:

Two lines
→ Width between them
→ Height limited by shorter line
→ Maximize area
→ Two Pointers
'''


'''
REUSABLE TEMPLATE

left = 0
right = len(nums) - 1
answer = 0

while left < right:

    current = ...
    answer = max(answer, current)

    if nums[left] < nums[right]:
        left += 1
    else:
        right -= 1


For Container With Most Water:

width = right - left
current_height = min(nums[left], nums[right])

area = width * current_height

answer = max(answer, area)
'''


'''
FAMILY

Two Pointer Problems


Related patterns:

- Two Sum II
- 3Sum
- Trapping Rain Water
- Remove Duplicates from Sorted Array
- Move Zeroes
- Pair-based problems
- Problems involving opposite ends


Important distinction:

Opposite ends + pair condition
→ Two Pointers


Sliding range/window
→ Sliding Window


Need target in sorted array
→ Often Two Pointers / Binary Search
'''


'''
COMMON INTERVIEW MISTAKES

1. Using max() instead of min() for height.

Wrong:

max(height[left], height[right])


Correct:

min(height[left], height[right])


The shorter line limits the water.


2. Moving the taller pointer.

Wrong idea:

"Keep the shorter side and move the taller side."


Correct:

Move the shorter side.


3. Moving both pointers.

Only one pointer should move at each step.

Otherwise, valid candidates can be skipped.


4. Forgetting width.

The area is:

(right - left) * shorter_height


5. Starting with adjacent elements.

The best starting width is obtained by:

left = 0
right = n - 1


6. Using O(n²) nested loops when an O(n) solution exists.


7. Returning the last calculated area instead of
   the maximum area.

Always maintain:

max_area
'''


'''
MOST IMPORTANT THING TO REMEMBER

The complete pattern:

Container With Most Water
→ Two Pointers
→ Start at both ends
→ Width is maximum initially
→ Calculate area
→ Shorter line is the bottleneck
→ Move shorter pointer
→ Keep maximum area


One-line rule:

Two Pointers
→ Area = width × shorter height
→ Move shorter side
→ Keep maximum


Formula:

area = (right - left) * min(height[left], height[right])


Pointer rule:

if height[left] < height[right]:
    left += 1
else:
    right -= 1


Final Mental Model:

Start wide
→ Check area
→ Identify bottleneck
→ Discard shorter side
→ Look for a taller side
→ Repeat


Most important sentence:

"The shorter line controls the water, so move the
shorter pointer to have a chance of increasing the
height while accepting the smaller width."
'''