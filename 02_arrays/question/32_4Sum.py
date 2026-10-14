# 18. 4SUM

"""
PROBLEM

Given an integer array nums and an integer target, return all unique
quadruplets [a, b, c, d] such that:

a + b + c + d == target

Rules:
- All four elements must come from different indices.
- The answer must not contain duplicate quadruplets.
- The order of quadruplets does not matter.

Example:
Input: nums = [1, 0, -1, 0, -2, 2], target = 0

Output:
[[-2, -1, 1, 2],
 [-2, 0, 0, 2],
 [-1, 0, 0, 1]]

"""

"""
PATTERN

Sorting + Two Pointers + Nested Loops

3Sum:
Fix 1 element + Two Pointers

4Sum:
Fix 2 elements + Two Pointers

Main idea:
Sort the array, fix nums[i] and nums[j], then use left and right
pointers to find the remaining two elements.
"""

"""
RECOGNITION TRICKS

Look for these clues:
- Find four numbers whose sum equals target.
- Return all unique combinations.
- Duplicate answers are not allowed.
- The array can contain negative numbers.
- Brute force with four loops is too slow.

Think:
Sorting -> Fix two elements -> Two Pointers -> Skip duplicates
"""

"""
APPROACH 1 — BRUTE FORCE

Use four nested loops to select four different indices.

Check whether their sum equals target.
Sort each valid quadruplet and store it only if it is unique.

Why not optimal?
Four nested loops take O(n^4) time.
Checking duplicates can add extra overhead.
"""

# BRUTE FORCE CODE

def four_sum_brute(nums, target):
    n = len(nums)
    result = []

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            for k in range(j + 1, n - 1):
                for l in range(k + 1, n):
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        quadruplet = sorted([
                            nums[i], nums[j], nums[k], nums[l]
                        ])

                        if quadruplet not in result:
                            result.append(quadruplet)

    return result


"""
Complexity:
Time: O(n^4) or worse with duplicate-list checks
Space: O(1) auxiliary, excluding the result
"""

"""
APPROACH 2 — BETTER APPROACH

Fix two elements and use a hash set to find pairs among the remaining
elements.

For each fixed pair:
1. Calculate the remaining required sum.
2. Scan the remaining elements.
3. Check whether the required complement has already been seen.
4. Store valid quadruplets in a set to remove duplicates.

This avoids four nested loops, but handling duplicates is more complex.
The overall time complexity is O(n^3) on average, with extra space
for the hash set and stored answers.

The sorting + two-pointer approach is generally preferred because
its duplicate handling is easier to understand.
"""

# BETTER APPROACH CODE

def four_sum_better(nums, target):
    n = len(nums)
    result = set()

    for i in range(n - 3):
        for j in range(i + 1, n - 2):
            seen = set()
            required = target - nums[i] - nums[j]

            for k in range(j + 1, n):
                complement = required - nums[k]

                if complement in seen:
                    quadruplet = tuple(sorted([
                        nums[i], nums[j], complement, nums[k]
                    ]))
                    result.add(quadruplet)

                seen.add(nums[k])

    return [list(q) for q in result]


"""
Complexity:
Time: O(n^3) average, excluding output conversion details
Space: O(n) auxiliary hash set per fixed pair, plus result storage

Note:
The hash set stores values, while the loops ensure that the selected
elements come from different indices.
"""

"""
APPROACH 3 — OPTIMAL / STANDARD

Use sorting, two nested loops, and two pointers.

Steps:
1. Sort nums.
2. Fix the first element using i.
3. Fix the second element using j.
4. Set left = j + 1 and right = n - 1.
5. Calculate the sum of all four selected elements.
6. If sum == target:
   - Store the quadruplet.
   - Move both pointers.
   - Skip duplicate values.
7. If sum < target, move left forward.
8. If sum > target, move right backward.
9. Skip duplicate values for i and j.

Why sorting?
After sorting, moving left increases the sum and moving right
decreases the sum.
"""

# OPTIMAL CODE

class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 3):
            # Skip duplicate first elements.
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            for j in range(i + 1, n - 2):
                # Skip duplicate second elements.
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue

                left = j + 1
                right = n - 1

                while left < right:
                    total = (
                        nums[i] + nums[j] +
                        nums[left] + nums[right]
                    )

                    if total == target:
                        result.append([
                            nums[i], nums[j],
                            nums[left], nums[right]
                        ])

                        left += 1
                        right -= 1

                        # Skip duplicate left values.
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1

                        # Skip duplicate right values.
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1

                    elif total < target:
                        left += 1

                    else:
                        right -= 1

        return result


"""
WHY SORTING + TWO POINTERS?

The array is sorted in ascending order.

If the sum is smaller than target:
Move left forward to increase the sum.

If the sum is larger than target:
Move right backward to decrease the sum.

If the sum equals target:
Store the quadruplet and move both pointers.

Sorting also places duplicate values next to each other,
making it easy to skip duplicate quadruplets.
"""

"""
STEP-BY-STEP THINKING PROCESS

When you see a 4Sum problem, ask:

1. Do I need four nested loops?
   Brute force uses O(n^4), so look for an improvement.

2. Can sorting help?
   Yes. Sorting enables two-pointer movement and duplicate skipping.

3. How many elements should I fix?
   Fix two elements with i and j.

4. How do I find the remaining two?
   Use left and right pointers.

5. How do I avoid duplicates?
   Skip repeated values at i, j, left, and right.

6. When should pointers move?
   Sum too small -> left += 1
   Sum too large -> right -= 1
   Sum correct -> save answer and move both.
"""

"""
DRY RUN

Input:
nums = [1, 0, -1, 0, -2, 2]
target = 0

After sorting:
nums = [-2, -1, 0, 0, 1, 2]

First valid quadruplet:
-2 + -1 + 1 + 2 = 0

Second valid quadruplet:
-2 + 0 + 0 + 2 = 0

Third valid quadruplet:
-1 + 0 + 0 + 1 = 0

Output:
[[-2, -1, 1, 2],
 [-2, 0, 0, 2],
 [-1, 0, 0, 1]]

Repeated values are skipped, so each quadruplet appears only once.
"""

"""
WHY DOES THE OPTIMAL APPROACH WORK?

1. Every possible answer can be represented by two fixed elements
   and a pair searched using two pointers.

2. Sorting makes pointer movement predictable.

3. If the sum is too small, moving left is the useful direction.
   Moving right would make the sum even smaller.

4. If the sum is too large, moving right is the useful direction.
   Moving left would make the sum even larger.

5. Duplicate skipping prevents repeated quadruplets without
   removing any distinct value combinations.

Therefore, the algorithm finds all unique quadruplets.
"""

"""
EDGE CASES

1. Empty or very small array:
   Fewer than four elements -> [].

2. No valid quadruplet:
   Return [].

3. All elements are equal:
   Return one quadruplet if four copies reach the target;
   otherwise return [].

4. Negative numbers:
   Supported because Python handles negative integer sums.

5. Duplicate values:
   Skip duplicates at all four selection positions.

6. Large positive or negative values:
   Python integers do not overflow.
"""

"""
TIME & SPACE COMPLEXITY

Let n be the number of elements.

Sorting:
O(n log n)

Two fixed loops and the two-pointer scan:
O(n^3)

Total time:
O(n^3)

Auxiliary space:
O(log n) typically for Python's sorting implementation,
excluding the output and considering the in-place sort.

Output space:
Depends on the number of valid quadruplets.
"""

"""
INTERVIEW EXPLANATION

"I sort the array first so that I can use two pointers and handle
duplicates easily.

Then I fix two elements using nested loops. For the remaining
two elements, I use left and right pointers.

If the sum is smaller than the target, I move the left pointer
forward. If it is larger, I move the right pointer backward.
When the sum matches, I save the quadruplet and move both pointers.

I skip duplicate values at each selection position to ensure
that every quadruplet is unique.

The time complexity is O(n^3)."
"""

"""
RECOGNITION TRICKS

2Sum:
Hash map or two pointers after sorting.

3Sum:
Sort + fix one element + two pointers.

4Sum:
Sort + fix two elements + two pointers.

General k-Sum:
Fix elements recursively or with loops, then reduce to a smaller
sum problem.

Remember:
More fixed elements usually mean more outer loops.
The final pair can often be solved using two pointers.
"""

"""
REUSABLE TWO-POINTER TEMPLATE

left = start
right = end

while left < right:
    total = nums[left] + nums[right]

    if total == target:
        # Save the answer
        left += 1
        right -= 1

    elif total < target:
        left += 1

    else:
        right -= 1
"""

"""
COMMON INTERVIEW MISTAKES

1. Forgetting to sort before using two pointers.
2. Using <= instead of < in the pointer loop.
3. Forgetting to skip duplicate i or j values.
4. Forgetting to skip duplicates after finding a valid quadruplet.
5. Moving only one pointer after finding a valid pair.
6. Using four nested loops in the final solution.
7. Accidentally selecting the same index more than once.
8. Claiming O(n^2) time for the standard 4Sum solution.
9. Returning duplicate quadruplets.
"""

"""
MOST IMPORTANT THING TO REMEMBER

4Sum = Sorting + Fix Two Elements + Two Pointers

Brute force: O(n^4)
Optimal standard approach: O(n^3)

Always skip duplicates at i, j, left, and right.
"""