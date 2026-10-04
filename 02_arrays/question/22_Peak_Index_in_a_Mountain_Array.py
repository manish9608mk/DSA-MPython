# 852. Peak Index in a Mountain Array

'''
PROBLEM

You are given a mountain array arr.

A mountain array has this structure:

increasing → peak → decreasing

Example:

arr = [0,2,5,3,1]

0 < 2 < 5 > 3 > 1

Peak value = 5
Peak index = 2


We need to return the index of the peak element.


Important:

- arr is guaranteed to be a mountain array.
- The array has at least 3 elements.
- The required time complexity is O(log n).
- We need to return the index, not the value.
'''


'''
PATTERN

Binary Search


A mountain array has two phases:

Increasing
→ Peak
→ Decreasing


At index mid, compare:

arr[mid]
arr[mid + 1]


Two possibilities:


1. arr[mid] < arr[mid + 1]

→ We are going uphill.
→ Peak must be to the right.

left = mid + 1


2. arr[mid] > arr[mid + 1]

→ We are going downhill.
→ Peak is at mid or to the left.

right = mid


Recognition:

Increasing → Peak → Decreasing
→ Think Binary Search


Mental pattern:

mid < mid + 1
→ Go right

mid > mid + 1
→ Go left, but keep mid
'''


'''
APPROACH 1 — BRUTE FORCE

Scan the array from left to right.

The peak is the element that is greater than
both its neighbors.

Example:

arr = [0,2,5,3,1]

At index 2:

5 > 2
5 > 3

Therefore:

peak index = 2


Since the array is guaranteed to be a mountain,
the peak is also the maximum element.


So we can simply find the maximum element
and return its index.


TIME:

O(n)


SPACE:

O(1)


Why is it not enough?

The problem requires:

O(log n)

So we need a Binary Search solution.
'''


'''
# BRUTE FORCE CODE
'''

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        peak_index = 0

        for i in range(1, len(arr)):
            if arr[i] > arr[peak_index]:
                peak_index = i

        return peak_index


'''
APPROACH 2 — OPTIMAL / STANDARD

Use Binary Search based on the direction of the array.


Start:

left = 0
right = len(arr) - 1


At every step:

mid = (left + right) // 2


Compare:

arr[mid]
arr[mid + 1]


CASE 1:

arr[mid] < arr[mid + 1]


The array is still increasing.

Example:

[1,3,5,8,6,2]
     ↑ ↑
    mid next


Since the next value is larger,
mid cannot be the peak.

Therefore:

left = mid + 1


CASE 2:

arr[mid] > arr[mid + 1]


The array is decreasing.

Example:

[1,3,8,6,2]
     ↑ ↑
    mid next


The peak could be mid itself.

Therefore we cannot remove mid.

So:

right = mid


Continue until:

left == right


That index is the peak.


TIME:

O(log n)


SPACE:

O(1)
'''


'''
WHY BINARY SEARCH?

Normally Binary Search is used on a sorted array.

Here the entire array is not sorted.

But it has a useful structure:

increasing → decreasing


At any mid, we can determine which side
contains the peak.


If:

arr[mid] < arr[mid + 1]

we are climbing.

→ Peak is on the right.


If:

arr[mid] > arr[mid + 1]

we are descending.

→ Peak is on the left or at mid.


So each comparison allows us to discard
part of the search space.

That is why Binary Search works.
'''


'''
STEP-BY-STEP THINKING

1. What am I looking for?

→ The index of the peak.


2. What is special about the array?

→ It increases and then decreases.


3. Can I use the direction of the array?

→ Yes.


4. What comparison tells me the direction?

→ Compare arr[mid] and arr[mid + 1].


5. If arr[mid] < arr[mid + 1], what does it mean?

→ We are still increasing.


6. Where is the peak?

→ To the right.


7. Update:

left = mid + 1


8. Otherwise:

arr[mid] > arr[mid + 1]


→ We are decreasing.


9. Where can the peak be?

→ At mid or to the left.


10. Update:

right = mid


11. When do we stop?

→ left == right


12. What is the answer?

→ left


Final thinking:

Mountain shape
→ Check direction at mid
→ Eliminate one side
→ Binary Search
→ left == right = peak
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def peakIndexInMountainArray(self, arr: list[int]) -> int:
        left = 0
        right = len(arr) - 1

        while left < right:
            mid = (left + right) // 2

            if arr[mid] < arr[mid + 1]:
                left = mid + 1
            else:
                right = mid

        return left


# TEST CASE

arr = [0,1,0]

solution = Solution()

answer = solution.peakIndexInMountainArray(arr)

print("Input:", arr)
print("Output:", answer)



'''
OUTPUT

Input: [0,1,0]

Output: 1
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

At every mid, exactly one of these conditions is true.


CASE 1:

arr[mid] < arr[mid + 1]


This means the array is still going upward.

Therefore mid is not the peak.

The peak must occur somewhere after mid.

So:

left = mid + 1


CASE 2:

arr[mid] > arr[mid + 1]


This means the array is going downward.

Therefore the peak is either:

- mid itself
- somewhere before mid


So mid must remain in the search space.

Therefore:

right = mid


Each step removes only a portion that cannot
contain the peak.

Eventually:

left == right

Only one candidate remains.

Because the input is guaranteed to be a mountain array,
that remaining index is the peak.

Therefore the algorithm always returns the correct index.
'''


'''
DRY RUN

arr = [0,1,5,3,2]


Start:

left = 0
right = 4


Step 1:

mid = (0 + 4) // 2
    = 2


Compare:

arr[2] = 5
arr[3] = 3


5 > 3

→ We are going downhill.

The peak can be mid.

Therefore:

right = 2


Now:

left = 0
right = 2


Step 2:

mid = (0 + 2) // 2
    = 1


Compare:

arr[1] = 1
arr[2] = 5


1 < 5

→ We are going uphill.

The peak must be to the right.

Therefore:

left = mid + 1
     = 2


Now:

left = 2
right = 2


Stop.


Peak index:

2


Peak value:

arr[2] = 5


Answer:

2
'''


'''
DRY RUN — EXAMPLE 2

arr = [0,2,1,0]


Start:

left = 0
right = 3


mid = 1


Compare:

arr[1] = 2
arr[2] = 1


2 > 1

→ Going downhill.

right = 1


Now:

left = 0
right = 1


mid = 0


Compare:

arr[0] = 0
arr[1] = 2


0 < 2

→ Going uphill.

left = 1


Now:

left = 1
right = 1


Peak index = 1
'''


'''
EDGE CASE 1 — PEAK AT INDEX 1

arr = [0,10,5,2]

The first element cannot be the peak because
the array must first increase.

The algorithm finds:

peak index = 1
'''


'''
EDGE CASE 2 — PEAK NEAR THE END

arr = [0,1,2,3,10,7]

The algorithm can still detect the transition
from increasing to decreasing.

Peak index = 4
'''


'''
EDGE CASE 3 — MINIMUM ARRAY SIZE

arr = [0,1,0]

Only three elements.

The middle element is the peak.

Answer:

1
'''


'''
EDGE CASE 4 — STRICTLY INCREASING BEFORE PEAK

arr = [1,3,5,7,4,2]

The algorithm keeps moving right while it is
still climbing.

Once it detects the decreasing side,
it keeps the current mid as a possible peak.
'''


'''
TIME & SPACE COMPLEXITY

At every iteration, the search space is reduced.


Therefore:

TIME = O(log n)


Only a few variables are used:

left
right
mid


Therefore:

SPACE = O(1)


Final:

Time  = O(log n)
Space = O(1)
'''


'''
INTERVIEW EXPLANATION

"I use Binary Search because the array has a mountain
structure: it first increases and then decreases.

At mid, I compare arr[mid] with arr[mid + 1].

If arr[mid] < arr[mid + 1], we are still climbing,
so the peak must be to the right and I set
left = mid + 1.

Otherwise, we are descending, so the peak is at mid
or somewhere to the left. I set right = mid because
mid itself can be the peak.

When left equals right, that index is the peak.

The time complexity is O(log n) and the space complexity
is O(1)."
'''


'''
RECOGNITION TRICKS

1. Mountain array

→ Increasing → Peak → Decreasing
→ Think Binary Search


2. Compare neighboring elements

arr[mid] and arr[mid + 1]

→ Tells whether we are climbing or descending.


3. Going uphill

arr[mid] < arr[mid + 1]

→ Peak is right.


4. Going downhill

arr[mid] > arr[mid + 1]

→ Peak is left or mid.


Quick rule:

UP
→ left = mid + 1


DOWN
→ right = mid
'''


'''
REUSABLE TEMPLATE

left = 0
right = len(arr) - 1

while left < right:

    mid = (left + right) // 2

    if arr[mid] < arr[mid + 1]:
        left = mid + 1
    else:
        right = mid

return left


General pattern:

Increasing
→ Move right


Decreasing
→ Keep mid and move left
'''


'''
FAMILY

Binary Search on Specially Structured Arrays


Related patterns:

- Find Peak Element
- Search in Rotated Sorted Array
- Find Minimum in Rotated Sorted Array
- Binary Search on Bitonic/Mountain Arrays
- Search on monotonic conditions


Important distinction:

Normal sorted array
→ Compare target with mid


Mountain / Peak problem
→ Compare mid with mid + 1
→ Determine direction
'''


'''
COMMON INTERVIEW MISTAKES

1. Using O(n) linear search.

It works, but violates the required O(log n) time.


2. Writing:

right = mid - 1


This is dangerous because mid itself can be the peak.

Correct:

right = mid


3. Forgetting:

left = mid + 1


When arr[mid] < arr[mid + 1],
mid is definitely not the peak.


4. Returning the peak value instead of its index.

Wrong:

return arr[left]


Correct:

return left


5. Using while left <= right without a clear boundary plan.

The clean version is:

while left < right:


6. Checking both neighbors unnecessarily.

You only need:

arr[mid] < arr[mid + 1]


because the mountain structure gives the rest
of the information.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Complete pattern:

Mountain Array
→ Increasing → Peak → Decreasing
→ Binary Search
→ Compare mid and mid + 1


If:

arr[mid] < arr[mid + 1]

→ Going UP
→ Peak is RIGHT
→ left = mid + 1


If:

arr[mid] > arr[mid + 1]

→ Going DOWN
→ Peak is LEFT or MID
→ right = mid


Stop:

left == right

→ Peak index


One-line rule:

UP → Go Right
DOWN → Keep Mid and Go Left


Final Mental Model:

          PEAK
           / /
          /  /
       UP/   / DOWN

mid < mid+1
→ climbing
→ move left pointer


mid > mid+1
→ descending
→ move right pointer


Most important code:

if arr[mid] < arr[mid + 1]:
    left = mid + 1
else:
    right = mid
'''