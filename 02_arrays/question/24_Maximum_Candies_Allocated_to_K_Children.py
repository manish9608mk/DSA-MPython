# 2226. Maximum Candies Allocated to K Children


# Binary Search approach
from typing import List
class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Find the maximum number of candies in any pile
        left, right = 1, max(candies)
        answer = 0
        
        # Binary search for the maximum possible candies per child
        while left <= right:
            mid = (left + right) // 2
            count = 0
            
            # Count how many children can get 'mid' candies
            for pile in candies:
                count += pile // mid
            
            # If enough children can get 'mid' candies, try for more
            if count >= k:
                answer = mid
                left = mid + 1
            else:
                right = mid - 1
        return answer

# Heap (Priority Queue) approach
import heapq
class Solution2:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Use a max heap to always split the largest pile
        max_pile = max(candies)
        
        # Try all possible pile sizes from largest to smallest
        for size in range(max_pile, 0, -1):
            count = 0
            for pile in candies:
                count += pile // size
            if count >= k:
                return size
        return 0

# Brute Force approach
class Solution3:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Try all possible pile sizes from 1 up to the largest pile
        max_pile = max(candies)
        for size in range(max_pile, 0, -1):
            count = 0
            for pile in candies:
                count += pile // size
            if count >= k:
                return size
        return 0



'''
PROBLEM

You are given an array candies where candies[i] is the size
of the ith pile.

You need to give exactly k children the same number of candies.

Rules:

- Each child must receive the same number of candies.
- Each child can get candies from only one pile.
- A pile can be split into smaller piles.
- Two different piles cannot be merged.
- Some candies/piles may remain unused.

Return the maximum number of candies each child can receive.


Example:

candies = [5,8,6]
k = 3

Try giving each child 5 candies:

5 → 1 child
8 → 1 child
6 → 1 child

Total = 3 children

So 5 candies per child is possible.

Output:

5


Example 2:

candies = [2,5]
k = 11

Total candies = 7.

There are 11 children, so even giving 1 candy to each
child is impossible.

Output:

0
'''


'''
PATTERN

Binary Search on Answer

We are not searching for an element in the array.

We are searching for:

"How many candies can each child receive?"

Suppose we guess:

x = candies per child

One pile of size candies[i] can create:

candies[i] // x

piles of size x.

Each such pile can be given to one child.

Therefore:

children_served = sum(candy // x for candy in candies)

If:

children_served >= k

then x candies per child is possible.

If:

children_served < k

then x is impossible.

The important property:

If x is possible,
every smaller value is also possible.

So the result looks like:

YES YES YES YES NO NO NO
                ↑
              answer

This monotonic structure gives:

→ Binary Search on Answer

Recognition:

"Maximum possible X"
+
"Can I make X?"
+
"Possible values form YES → NO"

→ Think Binary Search on Answer
'''


'''
APPROACH 1 — BRUTE FORCE

Try every possible number of candies per child.

The minimum meaningful value is:

1

The maximum possible value is:

max(candies)

For every x:

1. Calculate how many children can be served.
2. If at least k children can be served,
   update the answer.

Example:

candies = [5,8,6]
k = 3

x = 1:

5//1 + 8//1 + 6//1
= 19

Possible.

x = 2:

2 + 4 + 3
= 9

Possible.

x = 5:

1 + 1 + 1
= 3

Possible.

x = 6:

0 + 1 + 1
= 2

Impossible.

So the answer is 5.

Why does it work?

Every possible value is checked,
so the largest feasible value is found.

Why is it inefficient?

There can be up to max(candies) possible values.

For every value we may scan all n piles.

Therefore:

TIME = O(n * max(candies))

With:

n <= 10^5
max(candies) <= 10^7

this can be too slow.

SPACE:

O(1)
'''


# BRUTE FORCE CODE

class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
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


'''
APPROACH 3 — OPTIMAL / STANDARD

Use Binary Search on the answer.

We search for:

x = candies per child

Search range:

1 ... max(candies)

For a candidate mid:

children = sum(pile // mid for pile in candies)

There are two cases.


CASE 1 — mid is possible

If:

children >= k

then mid candies per child can be achieved.

But we want the maximum possible value.

So try a larger value:

left = mid + 1


CASE 2 — mid is impossible

If:

children < k

then mid is too large.

Any larger value will also be impossible.

So search smaller values:

right = mid - 1

We keep the largest feasible value in answer.

Core algorithm:

1. Binary search on candies per child.
2. Count how many children mid can serve.
3. If enough children can be served:
   - save mid
   - search right
4. Otherwise:
   - search left.

TIME:

O(n log(max(candies)))

SPACE:

O(1)
'''


'''
WHY BINARY SEARCH ON ANSWER?

Normally Binary Search searches an existing sorted array.

Here there is no sorted array of answers.

Instead, we have a monotonic feasibility condition.

Define:

possible(x)

as:

"Can every child receive x candies?"

Example:

candies = [5,8,6]
k = 3

Possible values:

1 → YES
2 → YES
3 → YES
4 → YES
5 → YES
6 → NO
7 → NO
8 → NO

So:

YES YES YES YES YES NO NO NO
                    ↑
                  maximum

We need to find the last YES.

Binary Search is perfect for finding this boundary.
'''


'''
WHY pile // x?

Suppose:

pile = 13
x = 5

We can split:

13 → 5 + 5 + 3

So this pile can serve:

13 // 5 = 2 children

The remaining 3 candies are not enough for another
child to receive 5.

Another example:

pile = 20
x = 6

20 // 6 = 3

because:

6 + 6 + 6 = 18

So one pile of 20 can serve 3 children.

Important:

We do this independently for every pile because
piles cannot be merged.
'''


'''
WHY CAN'T WE USE sum(candies) // k?

Because piles cannot be merged.

The total number of candies alone does not tell us
whether the children can actually receive them.

For every candidate x, we must calculate:

sum(pile // x)

This respects the rule that each child gets candies
from only one pile.

So feasibility must be checked pile by pile.
'''


'''
STEP-BY-STEP THINKING

1. What are we maximizing?

→ Candies per child.

2. Can I guess a possible answer?

→ Yes. Let it be x.

3. How can one pile help?

→ pile // x children.

4. How many children can all piles serve?

→ sum(pile // x)

5. When is x possible?

→ When total children served >= k.

6. What happens if x is possible?

→ Every smaller value is also possible.

7. What happens if x is impossible?

→ Every larger value is also impossible.

8. What pattern is this?

→ Monotonic YES/NO.

9. Which algorithm finds the maximum feasible value?

→ Binary Search.

10. What is the search range?

→ 1 to max(candies).

11. If mid is feasible?

→ Save it and search right.

12. If mid is not feasible?

→ Search left.

13. What do we return?

→ The largest feasible value.

Final thinking:

Guess candies per child
→ Check feasibility
→ Possible → go right
→ Impossible → go left
→ Maximum feasible value
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        left = 1
        right = max(candies)
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

# TEST CASE

candies = [5,8,6]
k = 3

solution = Solution()

answer = solution.maximumCandies(candies, k)

print("Input:", candies)
print("K:", k)
print("Output:", answer)


'''
OUTPUT

Input: [5,8,6]
K: 3
Output: 5
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

For a chosen value x, each pile of size pile can create:

pile // x

groups of x candies.

Therefore:

sum(pile // x)

is exactly the maximum number of children that can
receive x candies.

So:

sum(pile // x) >= k

means x is feasible.

Now consider monotonicity.

If x candies per child is feasible,
then any smaller value is also feasible because
we can give each child fewer candies.

If x is impossible,
any larger value is also impossible because
larger groups require even more candies from every pile.

Therefore feasible values always have the form:

YES YES YES ... YES NO NO NO ... NO

Binary Search finds the last YES.

When mid is feasible:

answer = mid
left = mid + 1

When mid is impossible:

right = mid - 1

At the end, answer is the maximum number of candies
that can be given to every child.
'''


'''
DRY RUN

candies = [5,8,6]
k = 3

We search for the maximum candies per child.

Initial range:

left = 1
right = 8
answer = 0


STEP 1:

mid = (1 + 8) // 2
    = 4

Check 4 candies per child:

5 // 4 = 1
8 // 4 = 2
6 // 4 = 1

Total:

1 + 2 + 1 = 4

Need:

3 children

4 >= 3

So 4 is possible.

Update:

answer = 4
left = 5

Now:

left = 5
right = 8


STEP 2:

mid = (5 + 8) // 2
    = 6

Check:

5 // 6 = 0
8 // 6 = 1
6 // 6 = 1

Total:

2

2 < 3

So 6 is impossible.

Update:

right = 5

Now:

left = 5
right = 5


STEP 3:

mid = 5

Check:

5 // 5 = 1
8 // 5 = 1
6 // 5 = 1

Total:

3

3 >= 3

So 5 is possible.

Update:

answer = 5
left = 6

Now:

left = 6
right = 5

Stop.

Final answer:

5
'''


'''
DRY RUN — IMPOSSIBLE FROM THE START

candies = [2,5]
k = 11

Search:

1 ... 5

Try:

mid = 3

2 // 3 = 0
5 // 3 = 1

Total = 1

1 < 11

So 3 is impossible.

Try smaller values.

Eventually:

mid = 1

2 // 1 = 2
5 // 1 = 5

Total = 7

7 < 11

Even 1 candy per child is impossible.

Therefore:

answer = 0
'''


'''
DRY RUN — PILES CANNOT BE MERGED

candies = [4,4]
k = 2

Try:

x = 5

4 // 5 = 0
4 // 5 = 0

Total = 0

We cannot combine:

4 + 4 = 8

because different piles cannot be merged.

Therefore 5 candies per child is impossible.
'''


'''
EDGE CASE 1 — ANSWER IS 0

candies = [2,5]
k = 11

Even 1 candy per child is impossible.

Answer:

0
'''


'''
EDGE CASE 2 — ONLY ONE PILE

candies = [10]
k = 3

Possible values:

10 // 1 = 10 children
10 // 2 = 5 children
10 // 3 = 3 children
10 // 4 = 2 children

Therefore:

answer = 3
'''


'''
EDGE CASE 3 — LARGE k

k can be as large as 10^12.

Do not assume k fits in a small integer.

The child count should be allowed to grow large enough
for comparison with k.

In Python, integers handle this automatically.
'''


'''
EDGE CASE 4 — ALL PILES ARE SMALL

candies = [1,1,1,1]
k = 4

Try x = 1:

1 + 1 + 1 + 1 = 4 children

Therefore:

answer = 1
'''


'''
EDGE CASE 5 — ONE VERY LARGE PILE

candies = [100]
k = 1

One child can receive the entire pile.

Therefore:

answer = 100
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = len(candies)
M = max(candies)

Binary Search performs:

O(log M)

iterations.

Each iteration scans the piles:

O(n)

Therefore:

TIME = O(n log M)

where:

M = max(candies)

Only a few variables are used.

Therefore:

SPACE = O(1)

Final:

Time  = O(n log(max(candies)))
Space = O(1)
'''


'''
INTERVIEW EXPLANATION

"I binary search the number of candies each child can
receive.

For a candidate x, a pile of size pile can produce
pile // x groups of x candies. Therefore the total number
of children we can serve is:

sum(pile // x)

If this is at least k, then x is feasible, and I try
a larger value.

Otherwise x is too large, so I search smaller values.

Because feasibility is monotonic, Binary Search finds
the maximum feasible x.

The time complexity is O(n log(max(candies))) and the
space complexity is O(1)."
'''


'''
RECOGNITION TRICKS

1. "Maximum possible X"

→ Think Binary Search on Answer.

2. Ask:

"Can I check whether X is possible?"

3. If the answer has this structure:

YES YES YES NO NO NO

→ Binary Search.

4. Here:

X = candies per child

5. Feasibility:

sum(pile // X) >= k

Quick pattern:

Maximum X
→ Feasibility Check
→ Monotonic condition
→ Binary Search
'''


'''
REUSABLE TEMPLATE

left = minimum_possible
right = maximum_possible
answer = default_answer

while left <= right:

    mid = (left + right) // 2

    if is_possible(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

return answer

For this problem:

left = 1
right = max(candies)

is_possible(x):

    children = sum(pile // x for pile in candies)

    return children >= k
'''


'''
FAMILY

Binary Search on Answer

Common signals:

- Maximum minimum value
- Minimum maximum value
- Allocate resources
- Divide into groups
- Capacity problems
- "Can we make X?"
- "Can we finish within X?"
- "Is X feasible?"

Related ideas:

- Koko Eating Bananas
- Capacity To Ship Packages Within D Days
- Split Array Largest Sum
- Minimum Days to Make m Bouquets
- Aggressive Cows
- Allocate Books

Common structure:

Search for an answer
→ Check feasibility
→ Monotonic YES/NO
→ Binary Search
'''


'''
COMMON INTERVIEW MISTAKES

1. Binary-searching the array instead of the answer.

We are searching:

candies per child

not an array index.

2. Using:

sum(candies) // k

This ignores the rule that children cannot combine
candies from multiple piles.

3. Merging different piles.

Not allowed.

4. Using:

pile / mid

instead of:

pile // mid

We need the number of complete groups.

5. Returning the first feasible value.

We need the maximum feasible value.

So:

answer = mid
left = mid + 1

6. Forgetting the impossible case.

If even 1 candy per child is impossible:

answer = 0

7. Starting with mid = 0.

This causes division by zero.

Use:

left = 1

8. Forgetting the monotonic property.

Once x is impossible,
every larger value is also impossible.

9. Not breaking early when enough children are already
   counted.

This is optional, but:

if children >= k:
    break

can avoid unnecessary work.
'''


'''
MOST IMPORTANT THING TO REMEMBER

The complete pattern:

Maximum candies per child
→ Binary Search on Answer

For a candidate x:

pile // x
→ children served by one pile

sum(pile // x)
→ total children served

If:

total >= k

→ x is possible
→ Search right

If:

total < k

→ x is impossible
→ Search left

One-line rule:

Maximum X
→ Can I achieve X?
→ YES → go right
→ NO → go left
→ Find maximum feasible X

For this problem:

Candies per child
→ Binary Search
→ sum(pile // mid)
→ compare with k

Final Mental Model:

          Search Answer
                ↓
       candies per child = mid
                ↓
        Count children served
                ↓
         sum(pile // mid)
                ↓
         Is total >= k?
          /          \
        YES           NO
         ↓             ↓
      go RIGHT       go LEFT
         ↓
    maximize answer

Most important sentence:

"I am binary-searching the number of candies
each child can receive, and the feasibility check
tells me whether that value can serve at least k children."
'''
