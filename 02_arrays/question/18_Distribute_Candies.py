# 575. Distribute Candies

'''
PROBLEM

Alice has n candies.

The ith candy has a type represented by candyType[i].

She can eat only:

n / 2

candies.

She wants to eat the maximum number of different
candy types.

We need to return the maximum number of different
types she can eat.


Example:

candyType = [1,1,2,2,3,3]

n = 6

Alice can eat:

6 / 2 = 3 candies

Different types:

{1,2,3}

She can take one candy from each type.

Output:

3


Important:

- We care about different types, not total candies.
- Duplicate candies of the same type do not add a new type.
- Alice can eat only n / 2 candies.
'''


'''
PATTERN

Unique Elements
→ Set
→ Count different types
→ Compare with n / 2
→ Take minimum


Why?

There are two limits on the answer:

1. Number of different types available.
2. Number of candies Alice is allowed to eat.


If there are:

unique_types = 3
n / 2 = 5

then the answer is 3.


If there are:

unique_types = 10
n / 2 = 5

then the answer is 5.


Therefore:

answer = min(unique_types, n / 2)


Recognition:

"Different"
"Distinct"
"Unique"
→ Think Set


Mental pattern:

Count unique
→ Find selection limit
→ Take minimum
'''


'''
APPROACH 1 — BRUTE FORCE

Try every possible selection of n / 2 candies.

For each selection:

1. Count its different candy types.
2. Keep the maximum count.


Example:

candyType = [1,1,2,3]

Alice can eat 2 candies.

Possible selections:

[1,1] → 1 type
[1,2] → 2 types
[1,3] → 2 types
[2,3] → 2 types


Maximum = 2


Why does it work?

Every valid selection is considered, so the best
possible selection will be found.


Why is it inefficient?

The number of possible selections is:

C(n, n/2)

This grows extremely fast.

For example:

C(10,5) = 252

For n up to 10^4, this is not practical.


TIME:

O(C(n, n/2) * n)


SPACE:

O(n)


This approach is useful for understanding the problem,
but it is not suitable for the constraints.
'''


# BRUTE FORCE CODE

from itertools import combinations


class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        limit = len(candyType) // 2
        answer = 0

        for candies in combinations(candyType, limit):
            answer = max(answer, len(set(candies)))

        return answer


'''
APPROACH 2 — BETTER APPROACH

Instead of trying every possible selection, first find
how many different candy types exist.

Sorting can be used to count unique values.

Example:

[1,1,2,2,3,3]

After sorting:

[1,1,2,2,3,3]

Scan the array and count whenever the current value
is different from the previous value.

unique_types = 3


Alice can eat:

n / 2 = 3


Therefore:

answer = min(3,3)

= 3


This is much better than checking every combination.


TIME:

O(n log n)


SPACE:

O(n) worst case in Python's sorting implementation
'''


# BETTER CODE

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        candyType.sort()

        unique_types = 1

        for i in range(1, len(candyType)):
            if candyType[i] != candyType[i - 1]:
                unique_types += 1

        return min(unique_types, len(candyType) // 2)


'''
APPROACH 3 — OPTIMAL / STANDARD

We do not need to sort the array.

The only thing we need to know is:

How many different candy types exist?


A Set gives the answer directly.


Example:

candyType = [1,1,2,2,3,3]

set(candyType)

→ {1,2,3}


Therefore:

unique_types = len(set(candyType))


Alice can eat only:

n / 2

candies.

Since every different type needs at least one candy,
she can eat at most n / 2 different types.


So:

answer = min(unique_types, n / 2)


Core idea:

Count unique types
→ Find how many candies can be eaten
→ Return the smaller value


TIME:

O(n) average


SPACE:

O(n)
'''


'''
WHY SET?

The problem asks for different candy types.

A Set automatically removes duplicates.

Example:

[1,1,1,2,2,3]

→ {1,2,3}

Therefore:

len(set(candyType))

gives the number of different types.


Why not Counter?

Counter gives frequencies:

{1:3, 2:2, 3:1}

But frequency is not needed.

We only need the number of unique types.


So:

Need uniqueness
→ Set


Need frequency
→ Hash Map / Counter


Why not sorting?

Sorting also works, but costs O(n log n).

A Set gives O(n) average time for this problem.
'''


'''
STEP-BY-STEP THINKING

1. What is being asked?

→ Maximum number of different candy types.


2. How many candies can Alice eat?

→ n / 2.


3. What does one different type require?

→ At least one candy.


4. So what is the maximum number of different types
   Alice can eat because of the candy limit?

→ n / 2.


5. What is the other limit?

→ Number of different types available.


6. How do I find that?

→ Use a Set.


7. How do I count them?

→ len(set(candyType))


8. Now I have two limits:

→ unique_types
→ n / 2


9. Which one controls the answer?

→ The smaller one.


10. Final formula:

answer = min(unique_types, n / 2)


11. Do I need to know which candies Alice chooses?

→ No.


12. Do I need frequencies?

→ No.


13. Do I need sorting?

→ No.


14. Do I need a heap?

→ No.


Final thinking:

Unique types + limited number of candies
→ Set
→ Count unique
→ Take minimum
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        unique_types = len(set(candyType))

        return min(unique_types, len(candyType) // 2)


'''
TEST CASE

candyType = [1,1,2,2,3,3]

solution = Solution()

answer = solution.distributeCandies(candyType)

print("Input:", candyType)
print("Output:", answer)
'''


'''
OUTPUT

Input: [1,1,2,2,3,3]

Output: 3
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

Let:

D = number of different candy types

K = n / 2


Alice can eat only K candies.


To eat x different types, she needs at least
x candies because each type needs one candy.

Therefore:

x <= K


She also cannot eat more types than actually exist:

x <= D


So:

x <= min(D, K)


Now check both cases.


CASE 1:

D <= K

Alice has enough candy slots to take one candy
from every different type.

So:

answer = D


CASE 2:

D > K

There are more types than available candy slots.

Alice can choose one candy from any K different types.

So:

answer = K


Therefore, in both cases:

answer = min(D, K)


Where:

D = len(set(candyType))
K = n / 2


Hence the algorithm always returns the maximum
possible number of different candy types.
'''


'''
DRY RUN

candyType = [1,1,2,2,3,3]

n = 6


Step 1:

Alice can eat:

6 / 2 = 3


Step 2:

Find unique types:

set(candyType)

→ {1,2,3}


Step 3:

unique_types = 3


Step 4:

Compare:

unique_types = 3
limit = 3


Step 5:

answer = min(3,3)

= 3


Final answer:

3


One possible choice:

[1,2,3]

3 candies
3 different types
'''


'''
DRY RUN — UNIQUE TYPES > LIMIT

candyType = [1,2,3,4,5,6]

n = 6


Alice can eat:

6 / 2 = 3


Unique types:

{1,2,3,4,5,6}

unique_types = 6


Therefore:

answer = min(6,3)

= 3


Why?

There are 6 types, but only 3 candy slots.

So Alice can choose any 3 different types.
'''


'''
DRY RUN — UNIQUE TYPES < LIMIT

candyType = [6,6,6,6]

n = 4


Alice can eat:

4 / 2 = 2


Unique types:

{6}

unique_types = 1


Therefore:

answer = min(1,2)

= 1


Why?

Alice can eat 2 candies, but only one type exists.
'''


'''
EDGE CASE 1 — ONLY ONE TYPE

candyType = [5,5,5,5]

unique_types = 1
n / 2 = 2

answer = min(1,2)

= 1
'''


'''
EDGE CASE 2 — ALL TYPES ARE UNIQUE

candyType = [1,2,3,4,5,6]

unique_types = 6
n / 2 = 3

answer = min(6,3)

= 3
'''


'''
EDGE CASE 3 — EXACTLY n / 2 DIFFERENT TYPES

candyType = [1,1,2,2,3,3]

unique_types = 3
n / 2 = 3

answer = 3

Alice can take one candy from each type.
'''


'''
EDGE CASE 4 — MANY DUPLICATES

candyType = [1,1,1,1,2,2,2,3]

unique_types = 3
n / 2 = 4

answer = min(3,4)

= 3
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = len(candyType)


Creating the Set:

O(n) average


The Set stores at most n unique values.

SPACE:

O(n)


Final:

TIME  = O(n) average
SPACE = O(n)


Comparison:

Brute Force
→ O(C(n,n/2) * n)

Sorting
→ O(n log n)

Set
→ O(n) average
'''


'''
INTERVIEW EXPLANATION

"I need to maximize the number of different candy types.

Alice can eat only n/2 candies, so she can eat at most
n/2 different types because each type requires at least
one candy.

I use a Set to count the unique candy types.

The answer is the minimum of the unique type count
and n/2.

So:

min(len(set(candyType)), len(candyType) // 2)

The time complexity is O(n) on average and the space
complexity is O(n)."
'''


'''
RECOGNITION TRICKS

1. "Different", "Distinct", or "Unique"

→ Set


2. Maximum number of categories with a selection limit

→ Count unique values and compare with the limit.


3. One selected element can represent one new type

→ Number of different types cannot exceed the
  number of selected elements.


General pattern:

Unique values + selection limit
→ min(unique_count, limit)
'''


'''
REUSABLE TEMPLATE

unique_count = len(set(nums))

limit = K

answer = min(unique_count, limit)


For this problem:

unique_count = len(set(candyType))

limit = len(candyType) // 2

answer = min(unique_count, limit)
'''


'''
FAMILY

Set / Hashing

Related patterns:

- Count distinct elements
- Remove duplicates
- Find unique values
- Maximum distinct elements
- Distinct values with a selection limit
- Frequency problems


Important distinction:

Uniqueness
→ Set


Frequency
→ Hash Map / Counter


Kth / Top K
→ Heap


Ordering
→ Sorting
'''


'''
COMMON INTERVIEW MISTAKES

1. Returning only the unique count.

Wrong:

return len(set(candyType))


Why?

It ignores the n / 2 restriction.


Correct:

return min(len(set(candyType)), len(candyType) // 2)


2. Counting candies instead of types.

Example:

[1,1,1,2,2,3]

6 candies
3 different types


3. Using Counter when frequency is unnecessary.

Use Set.


4. Sorting unnecessarily.

Sorting works, but the Set solution is simpler
and gives O(n) average time.


5. Using a Heap.

This is not a Kth Largest, Kth Smallest, or Top K problem.


6. Constructing Alice's actual selection.

The problem asks only for the maximum count.


7. Memorizing the formula without understanding it.

Remember the two limits:

Unique types
+
Candy slots

→ Take minimum.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Complete pattern:

Different types
→ Duplicates do not matter
→ Use Set
→ Count unique types
→ Alice can eat n / 2 candies
→ Each type needs one candy
→ Compare the two limits
→ Take minimum


One-line rule:

Different Types + Limited Selection
→ Set
→ Count Unique
→ min(unique_count, limit)


For this problem:

candyType
→ set(candyType)
→ len(set(candyType))
→ compare with n / 2
→ min()
→ answer


Final mental model:

"D I F F E R E N T"
→ SET


"ONLY HALF CAN BE EATEN"
→ n / 2


"WHICH LIMITS THE ANSWER?"
→ MIN


Set
→ Unique Count
→ n / 2
→ Minimum
→ Answer
'''