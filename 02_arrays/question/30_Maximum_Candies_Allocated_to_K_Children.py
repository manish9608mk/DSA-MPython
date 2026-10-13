
# 2226. MAXIMUM CANDIES ALLOCATED TO K CHILDREN

"""
PROBLEM

You are given an array candies.
Each candies[i] represents the number of candies in one pile.

You can split a pile into smaller piles, but you cannot merge piles.
Each child must receive the same number of candies.
Each child can receive candies from only one pile.

Return the maximum number of candies each child can receive.

Example 1:
candies = [5, 8, 6]
k = 3
Output = 5

Example 2:
candies = [2, 5]
k = 11
Output = 0

Important:
- A pile can be split.
- Different piles cannot be merged.
- Each child receives candies from only one pile.
- Some candies can remain unused.
- k can be as large as 10^12.
"""

"""
PATTERN

Maximum Possible Value
→ Binary Search on Answer

We are not searching for a target inside the array.
We are searching for the maximum possible candies per child.

For a candidate x:
- If x is possible, try a larger value.
- If x is impossible, try a smaller value.

Feasibility check:
children = sum(pile // x for pile in candies)

If children >= k:
    x is possible.
Otherwise:
    x is impossible.

Recognition:
Maximum answer + feasibility check
→ Binary Search on Answer
"""

"""
APPROACH 1 — BRUTE FORCE

Try every possible x from 1 to max(candies).

For each x:
1. Count how many children can receive x candies.
2. If at least k children can be served, save x.
3. If x becomes impossible, stop because larger values
   are also impossible.

For a pile of size pile, the number of children it can serve is:
pile // x

TIME: O(n * max(candies)) in the worst case
SPACE: O(1)

This is too slow because candies[i] can reach 10^7.
"""

# BRUTE FORCE CODE

def maximum_candies_brute_force(candies: list[int], k: int) -> int:
    answer = 0

    for x in range(1, max(candies) + 1):
        children = 0

        for pile in candies:
            children += pile // x

        if children >= k:
            answer = x
        else:
            break

    return answer


"""
APPROACH 2 — BINARY SEARCH ON ANSWER

The answer must be between 0 and max(candies).

For a positive candidate x:
children = sum(pile // x for pile in candies)

If children >= k:
- x is feasible.
- Save x.
- Search for a larger answer using left = mid + 1.

Otherwise:
- x is impossible.
- Search for a smaller answer using right = mid - 1.

Use:
left = 1
right = max(candies)
answer = 0

Initialize answer = 0 because no positive allocation may be possible.

TIME: O(n log M), where M = max(candies)
SPACE: O(1)
"""

"""
WHY BINARY SEARCH ON ANSWER?

Feasibility is monotonic.

If x candies per child is possible, every smaller positive value
is also possible.

If x is impossible, every larger value is also impossible.

Example:
x = 1  → possible
x = 2  → possible
x = 3  → possible
x = 4  → possible
x = 5  → possible
x = 6  → impossible
x = 7  → impossible
x = 8  → impossible

Pattern:
True, True, True, ..., False, False

Binary search finds the last True.
That is the maximum feasible answer.
"""

"""
STEP-BY-STEP THINKING

1. What is being asked?
   → Maximize the equal number of candies each child receives.

2. Can we combine piles?
   → No.

3. If each child must receive x candies, how many children
   can one pile serve?
   → pile // x.

4. How many children can all piles serve?
   → Sum pile // x across all piles.

5. When is x feasible?
   → When children >= k.

6. If x is feasible, what should we try?
   → A larger x.

7. If x is impossible, what should we try?
   → A smaller x.

8. Which pattern fits?
   → Binary Search on Answer.

9. What is the search range?
   → 1 to max(candies).

10. Why initialize answer = 0?
    → The answer can be zero if no positive value works.
"""

"""
OPTIMAL CODE
"""

class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left, right = 1, max(candies)
        answer = 0

        while left <= right:
            mid = (left + right) // 2
            children = 0

            for pile in candies:
                children += pile // mid

                if children >= k:
                    break

            if children >= k:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer


"""
TEST CASE
"""

solution = Solution()

candies1 = [5, 8, 6]
k1 = 3
print("Input:", candies1, "k =", k1)
print("Output:", solution.maximumCandies(candies1, k1))

candies2 = [2, 5]
k2 = 11
print("Input:", candies2, "k =", k2)
print("Output:", solution.maximumCandies(candies2, k2))


"""
OUTPUT

Input: [5, 8, 6] k = 3
Output: 5
Input: [2, 5] k = 11
Output: 0
"""

"""
WHY DOES BINARY SEARCH WORK?

For a candidate x, a pile of size c can provide c // x portions
of size x.

Adding these counts gives the maximum number of children who can
receive x candies because piles cannot be merged.

If the total is at least k, x is feasible.

If x is feasible, any smaller positive amount is also feasible.
If x is impossible, any larger amount is also impossible.

Therefore, feasibility changes only once:
from possible to impossible as x increases.

Binary search locates the largest feasible x.

The answer starts at 0 so the algorithm handles cases where
no positive allocation is possible.
"""

"""
DRY RUN

candies = [5, 8, 6]
k = 3

Initial:
left = 1
right = 8
answer = 0

STEP 1

mid = (1 + 8) // 2 = 4

Children served:
5 // 4 = 1
8 // 4 = 2
6 // 4 = 1

Total = 1 + 2 + 1 = 4

4 >= 3, so x = 4 is feasible.

answer = 4
left = mid + 1 = 5

STEP 2

left = 5
right = 8
mid = (5 + 8) // 2 = 6

Children served:
5 // 6 = 0
8 // 6 = 1
6 // 6 = 1

Total = 2

2 < 3, so x = 6 is impossible.

right = mid - 1 = 5

STEP 3

left = 5
right = 5
mid = 5

Children served:
5 // 5 = 1
8 // 5 = 1
6 // 5 = 1

Total = 3

3 >= 3, so x = 5 is feasible.

answer = 5
left = mid + 1 = 6

Now left > right, so stop.

Final answer = 5.
"""

"""
EDGE CASE 1 — NOT ENOUGH CANDIES

candies = [2, 5]
k = 11

There are only 7 candies in total.
11 children cannot each receive even one candy.

No positive candidate works.

answer remains 0.

Output: 0
"""

"""
EDGE CASE 2 — ONLY ONE CHILD

candies = [5, 8, 6]
k = 1

The largest pile contains 8 candies.
One child cannot combine candies from different piles.

The answer cannot exceed 8.

Output: 8
"""

"""
EDGE CASE 3 — ANSWER IS 1

candies = [1, 1, 1, 1]
k = 4

For x = 1, every pile serves one child.
Total children served = 4.

Output: 1
"""

"""
EDGE CASE 4 — VERY LARGE k

k can reach 10^12.

The number of children we can serve may be smaller than k.
We only need to check whether children >= k.

We can stop counting as soon as children reaches k.

Python integers safely support these values.
"""

"""
TIME & SPACE COMPLEXITY

Let:
n = len(candies)
M = max(candies)

Binary search checks O(log M) candidate values.
Each check scans at most n piles.

TIME: O(n log M)

Since M <= 10^7, binary search takes at most about 24 iterations.

SPACE: O(1)

Only a fixed number of variables are used.
The input array is not modified.
"""

"""
INTERVIEW EXPLANATION

"I will use binary search on the answer.

For a candidate x, each pile can provide pile // x portions
of size x. I sum these portions to count how many children
can receive x candies.

If at least k children can be served, x is feasible.
I save it and search for a larger value.

Otherwise, I search for a smaller value.

Because feasibility is monotonic, binary search finds the
maximum feasible value. I initialize the answer to zero to
handle cases where no positive allocation is possible.

The time complexity is O(n log M), where M is the largest pile,
and extra space is O(1)."
"""

"""
RECOGNITION TRICKS

1. Maximum possible answer + feasibility check
   → Binary Search on Answer

2. If x works, smaller values work too
   → Monotonic feasibility

3. If x works, search higher
   → Save x and move left = mid + 1

4. If x fails, search lower
   → Move right = mid - 1

5. Piles cannot be merged
   → Count portions separately using pile // x

Mental pattern:
Maximum answer
→ Check candidate
→ Feasible?
→ Yes: save and search higher
→ No: search lower
"""

"""
REUSABLE TEMPLATE

def can_make(candidate):
    count = 0

    for value in values:
        count += value // candidate
        if count >= required:
            return True

    return False

left, right = 1, max(values)
answer = 0

while left <= right:
    mid = (left + right) // 2

    if can_make(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

return answer

This is a maximum-feasible-answer template.
For minimum-feasible-answer problems, the search directions differ.
"""

"""
FAMILY

Binary Search
    ↓
Binary Search on Answer
    ↓
Feasibility / Monotonic Predicate

Related problems:
- Koko Eating Bananas
- Capacity To Ship Packages Within D Days
- Minimum Number of Days to Make m Bouquets
- Split Array Largest Sum
- Magnetic Force Between Two Balls
- Minimum Limit of Balls in a Bag

Common idea:
Choose a candidate, check feasibility, and use the monotonic
result to eliminate half of the answer range.
"""

"""
COMMON INTERVIEW MISTAKES

1. Using sum(candies) // k as the answer.
   → This incorrectly treats separate piles as mergeable.

2. Counting total candies instead of portions.
   → Count pile // candidate for every pile.

3. Returning mid immediately when it is feasible.
   → A larger value might still work.

4. Moving left in the wrong direction.
   → For a feasible value, use left = mid + 1.

5. Forgetting answer = 0.
   → No positive allocation may be possible.

6. Using sum(candies) as the upper bound.
   → The answer cannot exceed max(candies).

7. Scanning every possible candidate.
   → Values can reach 10^7; use binary search.

8. Forgetting feasibility-check complexity.
   → Each check scans n piles, giving O(n log M).

9. Dividing by zero.
   → Search only candidates from 1 to max(candies).
"""

"""
MOST IMPORTANT THING TO REMEMBER

Maximum candies per child
→ Binary Search on Answer

For candidate x:
children = sum(pile // x for pile in candies)

If children >= k:
    x is possible
    save x
    search higher

Otherwise:
    x is impossible
    search lower

Answer = largest feasible x, or 0.

TIME: O(n log M)
SPACE: O(1)

Do not try every answer one by one.
Check a candidate and use binary search to find the
maximum feasible value.
"""
