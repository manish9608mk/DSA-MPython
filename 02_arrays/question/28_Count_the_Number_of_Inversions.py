# 3193. Count the Number of Inversions

from typing import List

class Solution:
    # Modified merge sort to count inversions
    def countInversions(self, nums: List[int]) -> int:
        def merge_sort(arr, left, right):
            if left >= right:
                return 0
            mid = (left + right) // 2
            count = 0
            
            # Count inversions in left and right halves
            count += merge_sort(arr, left, mid)
            count += merge_sort(arr, mid + 1, right)
            
            # Merge step with inversion counting
            temp = []
            i, j = left, mid + 1
            while i <= mid and j <= right:
                if arr[i] <= arr[j]:
                    temp.append(arr[i])
                    i += 1
                else:
                    # All remaining elements in left half are greater
                    count += (mid - i + 1)
                    temp.append(arr[j])
                    j += 1
            while i <= mid:
                temp.append(arr[i])
                i += 1
            while j <= right:
                temp.append(arr[j])
                j += 1
            
            # Copy back to original array
            arr[left:right+1] = temp
            return count
        
        return merge_sort(nums, 0, len(nums) - 1)

    
'''
PROBLEM

You are given an integer `n` and a 2D array `requirements`.

Each requirement:

requirements[i] = [end_i, cnt_i]

means:

perm[0..end_i] must contain exactly `cnt_i` inversions.

An inversion is a pair:

i < j
AND
perm[i] > perm[j]

Example:

perm = [2,0,1]

Inversions:

(2,0)
(2,1)

Total = 2

Example:

n = 3
requirements = [[2,2],[0,0]]

We need:

perm[0..2] → exactly 2 inversions
perm[0..0] → exactly 0 inversions

Answer = 2

Important:

- We are counting permutations of [0,1,2,...,n-1].
- Requirements are about prefixes.
- `n <= 300`.
- `cnt <= 400`.
- The answer must be modulo 10^9 + 7.
- All requirement end indexes are unique.
- There is always a requirement for `end = n - 1`.
'''


'''
PATTERN

Dynamic Programming + Prefix Sum / Sliding Window

At first:

Permutation
    ↓
n! possibilities
    ↓
Brute force impossible

Key observation:

We do NOT need to construct the actual values.

We only need:

Prefix length
+
Number of inversions

So:

DP[prefix][inversions]

When we add one new element:

It can create:

0,1,2,...,i

new inversions.

Therefore:

Previous inversions
+
New inversions
=
Current inversions

This gives a DP transition.

The transition is a range sum,
so we optimize it with a sliding window.

Final pattern:

Permutation Counting
    ↓
Inversion DP
    ↓
Range Sum Transition
    ↓
Prefix Sum / Sliding Window
    ↓
Exact Prefix Requirements
'''


'''
RECOGNITION TRICKS

Whenever you see:

"Count permutations with exactly K inversions"

Think:

→ DP on inversion count.

Whenever the problem says:

"Prefix must have exactly cnt inversions"

Think:

→ DP by prefix length + inversion count.

When the transition looks like:

dp[j]
+ dp[j-1]
+ dp[j-2]
+ ...

Think:

→ Range Sum
→ Prefix Sum / Sliding Window

Quick recognition:

Permutation
→ Inversions
→ Exact count
→ DP
'''


'''
APPROACH 1 — BRUTE FORCE

Generate every permutation of:

[0,1,2,...,n-1]

There are:

n!

permutations.

For every permutation:

1. Check every requirement.
2. Count inversions inside that prefix.
3. If all requirements are satisfied, increase answer.

For example:

n = 3

Permutations:

[0,1,2]
[0,2,1]
[1,0,2]
[1,2,0]
[2,0,1]
[2,1,0]

Check each one.

WHY DOES IT WORK?

Because we directly examine every possible permutation
and count exactly the valid ones.

WHY IS IT BAD?

`n!` grows extremely quickly.

Even:

10! = 3,628,800

For:

n = 300

Brute force is completely impossible.

TIME:

O(n! × n²)

SPACE:

O(n) excluding the generated permutation storage.
'''


# BRUTE FORCE CODE

from itertools import permutations


class Solution:
    def numberOfPermutations(
        self,
        n: int,
        requirements: list[list[int]]
    ) -> int:
        answer = 0

        for perm in permutations(range(n)):
            valid = True

            for end, required_count in requirements:
                inversions = 0

                for i in range(end + 1):
                    for j in range(i + 1, end + 1):
                        if perm[i] > perm[j]:
                            inversions += 1

                if inversions != required_count:
                    valid = False
                    break

            if valid:
                answer += 1

        return answer


'''
Correct but completely unusable for the constraints.
'''


'''
APPROACH 2 — BETTER APPROACH

Instead of generating permutations,
count them using Dynamic Programming.

Let:

dp[j]

= number of ways to create the current prefix
  with exactly `j` inversions.

Suppose the current prefix has `i` elements.

Now add one new element.

That new element can create:

0,1,2,...,i

new inversions.

Therefore:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ dp[j-2]
+ ...
+ dp[j-i]

In formula:

new_dp[j]
=
Σ dp[j-k]

for:

k = 0 → i

Example:

Suppose:

previous DP:

inversions:
0   1   2

ways:
1   2   1

For the next prefix,
the new element can create `0,1,2` inversions.

To get 2 inversions:

new_dp[2]
= dp[2]
+ dp[1]
+ dp[0]

= 1 + 2 + 1

= 4

This DP is much better than brute force.

TIME:

O(n² × K)

where:

K = maximum required inversion count.

SPACE:

O(K)

WHY IS IT STILL NOT OPTIMAL?

For every `new_dp[j]`,
we calculate a whole range sum again.

So we repeatedly calculate:

dp[j-i]
+
...
+
dp[j]

We can optimize this repeated range sum.
'''


# BETTER CODE

class Solution:
    def numberOfPermutations(
        self,
        n: int,
        requirements: list[list[int]]
    ) -> int:
        MOD = 10**9 + 7

        required = [-1] * n
        max_inv = 0

        for end, cnt in requirements:
            required[end] = cnt
            max_inv = max(max_inv, cnt)

        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for i in range(1, n):
            new_dp = [0] * (max_inv + 1)

            for inv in range(max_inv + 1):
                for added in range(i + 1):
                    if inv - added >= 0:
                        new_dp[inv] += dp[inv - added]

                new_dp[inv] %= MOD

            if required[i] != -1:
                cnt = required[i]

                for inv in range(max_inv + 1):
                    if inv != cnt:
                        new_dp[inv] = 0

            dp = new_dp

        return dp[required[n - 1]]


'''
This is the correct DP idea,
but the transition contains an extra loop.

We can remove that loop using a sliding window.
'''


'''
APPROACH 3 — OPTIMAL / STANDARD

Use:

Dynamic Programming + Sliding Window

Let:

dp[j]

= number of ways for the previous prefix
  to have exactly `j` inversions.

When adding a new element at position `i`,
it can create:

0 → i

new inversions.

Therefore:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ ...
+ dp[j-i]

Notice:

This is a contiguous range in `dp`.

For example:

new_dp[j]
= dp[j-i]
+ ...
+ dp[j-1]
+ dp[j]

Instead of recalculating the entire sum,
maintain a running `window`.

When `j` increases by 1:

Add:

dp[j]

Remove:

dp[j-i-1]

So each state can be calculated in O(1).

This changes:

O(n² × K)

to:

O(n × K)
'''


'''
WHY DP?

The actual permutation contains values,
but inversion requirements only depend on
the ordering.

When we add one element,
we only care how many new inversions it creates.

If the current prefix has `i` elements,
the new element can be inserted in `i + 1`
relative positions.

Therefore it can create:

0,1,2,...,i

new inversions.

So every permutation can be represented by
a sequence of inversion contributions.

Example for positions:

position 0 → can create 0 inversions
position 1 → can create 0 or 1
position 2 → can create 0,1,2
position 3 → can create 0,1,2,3

This gives:

DP[prefix length][inversion count]
'''


'''
WHY SLIDING WINDOW?

Transition:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ ...
+ dp[j-i]

For the next value:

new_dp[j+1]
=
dp[j+1]
+ dp[j]
+ ...
+ dp[j-i+1]

Most of the values overlap.

So instead of recalculating:

dp[j-i] + ... + dp[j]

we maintain:

window

At each step:

window += dp[j]

Remove the value that is now outside the window.

Therefore:

Each DP state = O(1)
'''


'''
HOW DO REQUIREMENTS WORK?

Create:

required[end] = cnt

For example:

requirements = [
    [0,0],
    [1,1],
    [2,2]
]

becomes:

required = [
    0,
    1,
    2
]

If:

required[i] == -1

there is no restriction.

If:

required[i] != -1

only that exact inversion count is allowed.

Example:

required[i] = 2

After calculating `new_dp`:

Only:

new_dp[2]

is kept.

All other inversion counts become invalid.

So:

DP
↓
Calculate all possible counts
↓
Apply requirement
↓
Keep exactly one state
'''


'''
STEP-BY-STEP THINKING

1. What is impossible?

→ Generating all n! permutations.

2. What actually matters?

→ Number of inversions in each prefix.

3. What should the DP store?

→ Number of ways for each inversion count.

4. Define:

dp[j]

→ Ways for current prefix with exactly `j`
  inversions.

5. When adding the next element?

→ It can create `0..i` new inversions.

6. Therefore:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ ...
+ dp[j-i]

7. What is the problem with this transition?

→ It is a range sum.

8. How do we optimize it?

→ Sliding window / prefix sum.

9. How do we apply requirements?

→ Keep only the required inversion count.

10. What is the final answer?

→ The DP value at the required inversion count
  for the full array.

Final thinking:

Permutation
    ↓
Inversion Count
    ↓
Prefix DP
    ↓
Range Sum
    ↓
Sliding Window
    ↓
Apply Requirements
    ↓
Answer
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def numberOfPermutations(
        self,
        n: int,
        requirements: list[list[int]]
    ) -> int:
        MOD = 10**9 + 7

        # required[i] = exact inversion count required
        # for prefix perm[0..i].
        required = [-1] * n
        max_inv = 0

        for end, cnt in requirements:
            required[end] = cnt
            max_inv = max(max_inv, cnt)

        # A prefix containing one element
        # always has 0 inversions.
        if required[0] not in (-1, 0):
            return 0

        # dp[j] = ways for the current prefix
        # with exactly j inversions.
        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for i in range(1, n):
            new_dp = [0] * (max_inv + 1)
            window = 0

            for j in range(max_inv + 1):
                window += dp[j]

                # The new element can create at most i inversions.
                # Remove the value that is outside the window.
                if j - i - 1 >= 0:
                    window -= dp[j - i - 1]

                window %= MOD
                new_dp[j] = window

            # Apply exact prefix requirement.
            if required[i] != -1:
                cnt = required[i]

                # A prefix of length i+1 can have at most
                # i * (i+1) / 2 inversions.
                if cnt > i * (i + 1) // 2:
                    return 0

                ways = new_dp[cnt]

                new_dp = [0] * (max_inv + 1)
                new_dp[cnt] = ways

            dp = new_dp

        # The problem guarantees a requirement at n-1.
        return dp[required[n - 1]] % MOD

# TEST CASE

n = 3

requirements = [
    [2,2],
    [0,0]
]

solution = Solution()

answer = solution.numberOfPermutations(
    n,
    requirements
)

print("Input:", n, requirements)
print("Output:", answer)

'''
OUTPUT

Input:

3 [[2,2],[0,0]]

Output:

2
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

Consider a prefix containing `i` elements.

When we add one new element,
its position relative to the existing elements
determines how many inversions it creates.

It can create:

0,1,2,...,i

new inversions.

Therefore, to obtain exactly `j` inversions,
the previous prefix must have:

j
j-1
j-2
...
j-i

inversions.

So:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ ...
+ dp[j-i]

The sliding window calculates exactly this sum.

Then requirements remove all states that do not
match the required inversion count.

Therefore every valid inversion sequence is counted,
and every invalid sequence is removed.

Because inversion contributions uniquely determine
a permutation, counting these DP states counts
the required permutations exactly.
'''


'''
DRY RUN

EXAMPLE 1

n = 3

requirements = [
    [2,2],
    [0,0]
]

Requirements:

required[0] = 0
required[2] = 2

MAX REQUIRED INVERSIONS:

max_inv = 2


INITIAL

Prefix length = 1

Only:

[0]

So:

dp = [1,0,0]

Meaning:

0 inversions → 1 way
1 inversion  → 0 ways
2 inversions  → 0 ways

Requirement at index 0:

required[0] = 0

Correct.
'''


'''
DRY RUN — BUILD PREFIX LENGTH 2

i = 1

The new element can create:

0 or 1 inversion.

For inversion count 0:

new_dp[0]
= dp[0]
= 1

For inversion count 1:

new_dp[1]
= dp[1] + dp[0]
= 0 + 1
= 1

For inversion count 2:

new_dp[2]
= dp[2] + dp[1]
= 0

Therefore:

new_dp = [1,1,0]

There is no requirement at index 1.

So:

dp = [1,1,0]

Meaning:

0 inversions → 1 way
1 inversion  → 1 way
2 inversions  → 0 ways
'''


'''
DRY RUN — BUILD PREFIX LENGTH 3

i = 2

The new element can create:

0,1,2 inversions.

For inversion count 0:

new_dp[0]
= dp[0]
= 1

For inversion count 1:

new_dp[1]
= dp[1] + dp[0]
= 1 + 1
= 2

For inversion count 2:

new_dp[2]
= dp[2] + dp[1] + dp[0]
= 0 + 1 + 1
= 2

Therefore:

new_dp = [1,2,2]

Requirement:

required[2] = 2

So keep only:

new_dp[2] = 2

Result:

dp = [0,0,2]

Final answer:

dp[2] = 2

Answer:

2

The two permutations are:

[2,0,1]
[1,2,0]
'''


'''
DRY RUN — WHY SLIDING WINDOW WORKS

Suppose:

dp = [1,1,0]

For i = 2,
the window size is:

i + 1 = 3

For j = 0:

window = dp[0]
= 1

new_dp[0] = 1

For j = 1:

window += dp[1]
= 1 + 1
= 2

new_dp[1] = 2

For j = 2:

window += dp[2]
= 2 + 0
= 2

new_dp[2] = 2

Now imagine a larger j.

The window would contain:

dp[j-2] + dp[j-1] + dp[j]

When moving to `j+1`:

Add:

dp[j+1]

Remove:

dp[j-2]

So we never recalculate the entire sum.
'''


'''
DRY RUN — EXAMPLE 2

n = 3

requirements = [
    [2,2],
    [1,1],
    [0,0]
]

Requirements:

Prefix 0 → 0 inversions
Prefix 1 → 1 inversion
Prefix 2 → 2 inversions

Start:

dp = [1]

After prefix length 2:

dp = [1,1]

Requirement at index 1:

required[1] = 1

Keep only:

dp[1] = 1

So:

dp = [0,1]

Now build prefix length 3.

To get 2 inversions:

new_dp[2]
= dp[2]
+ dp[1]
+ dp[0]
= 0 + 1 + 0
= 1

Requirement says:

2 inversions

Keep:

dp[2] = 1

Answer:

1
'''


'''
DRY RUN — EXAMPLE 3

n = 2

requirements = [
    [0,0],
    [1,0]
]

Prefix 1:

0 inversions

Start:

dp = [1]

Add second element.

To have 0 inversions:

new_dp[0] = dp[0]
= 1

Requirement at index 1:

0 inversions

Keep:

dp = [1]

Final answer:

1

Permutation:

[0,1]
'''


'''
EDGE CASE 1 — REQUIREMENT AT INDEX 0

A prefix containing one element can never
have an inversion.

Therefore:

required[0] must be:

0

If:

required[0] > 0

answer = 0

That is why:

if required[0] not in (-1, 0):
    return 0
'''


'''
EDGE CASE 2 — REQUIRED COUNT TOO LARGE

A prefix containing `i + 1` elements can have
at most:

(i + 1) * i / 2

inversions.

Example:

Prefix length = 4

Maximum:

4 * 3 / 2 = 6

So requirement:

[3,7]

is impossible.

Return:

0
'''


'''
EDGE CASE 3 — REQUIREMENT WITH 0 INVERSIONS

If a prefix must have:

0 inversions

then that prefix must be strictly increasing.

The DP automatically keeps only:

dp[0]
'''


'''
EDGE CASE 4 — REQUIREMENT WITH MAXIMUM INVERSIONS

For a prefix of length `L`,
maximum inversions are:

L * (L - 1) / 2

That happens when the prefix is completely decreasing.

Example:

Length = 4

Maximum = 6

Permutation pattern:

[3,2,1,0]

The DP handles this automatically.
'''


'''
EDGE CASE 5 — NO REQUIREMENT AT A POSITION

`required[i] = -1`

means:

No restriction.

Keep every valid inversion count.
'''


'''
EDGE CASE 6 — LARGE ANSWER

The number of permutations can be as large as:

n!

which is enormous.

Therefore every DP state is stored modulo:

10^9 + 7

Use:

MOD = 10**9 + 7
'''


'''
EDGE CASE 7 — MAXIMUM CONSTRAINTS

n <= 300

cnt <= 400

We only need inversion states:

0 → 400

Therefore:

O(300 × 400)

is easily manageable.
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = number of elements
K = maximum required inversion count

Given:

K <= 400

For every prefix:

We process all `K + 1` inversion states.

The sliding window calculates every state in O(1).

Therefore:

TIME:

O(n × K)

SPACE:

O(K)

We use:

dp
new_dp

Each has size:

K + 1

Therefore:

TIME  = O(n × K)
SPACE = O(K)

With constraints:

n <= 300
K <= 400

Maximum DP states are roughly:

300 × 400 = 120,000

which is efficient.
'''


'''
INTERVIEW EXPLANATION

"I use Dynamic Programming where `dp[j]` represents the
number of ways for the current prefix to have exactly `j`
inversions.

When I add the next element at position `i`, it can create
anywhere from `0` to `i` new inversions. Therefore,
`new_dp[j]` is the sum of `dp[j], dp[j-1], ..., dp[j-i]`.

This is a sliding range sum, so I maintain a running window
instead of recalculating it for every state.

Whenever a prefix has a requirement, I keep only the exact
required inversion count.

The complexity is O(n × K) time and O(K) space, where K is the
maximum required inversion count."
'''


'''
RECOGNITION TRICKS

1. Permutations + inversion count

→ Think DP.

2. Exact inversion count

→ DP state should include inversion count.

3. Prefix inversion requirements

→ Process positions from left to right.

4. Adding one element

→ It can create 0..i new inversions.

5. Transition:

dp[j] + dp[j-1] + ... + dp[j-i]

→ Range Sum.

6. Repeated range sums

→ Prefix Sum / Sliding Window.

7. Requirement:

prefix has exactly cnt inversions

→ Keep only dp[cnt].

Quick pattern:

Permutation
→ Inversion Count
→ Prefix DP
→ Range Sum
→ Sliding Window
'''


'''
REUSABLE TEMPLATE

MOD = 10**9 + 7

required = [-1] * n

for end, cnt in requirements:
    required[end] = cnt

dp = [0] * (max_inv + 1)
dp[0] = 1

for i in range(1, n):

    new_dp = [0] * (max_inv + 1)

    window = 0

    for j in range(max_inv + 1):

        window += dp[j]

        if j - i - 1 >= 0:
            window -= dp[j - i - 1]

        window %= MOD

        new_dp[j] = window

    if required[i] != -1:

        cnt = required[i]
        ways = new_dp[cnt]

        new_dp = [0] * (max_inv + 1)
        new_dp[cnt] = ways

    dp = new_dp

return dp[required[n - 1]]
'''


'''
FAMILY

Permutation + Inversion DP

Related concepts:

- Counting permutations by inversion count
- Inversion sequence
- Dynamic Programming on prefix length
- Prefix sum optimization
- Sliding window DP
- Exact-state filtering

Common DP structure:

Previous State
    ↓
Generate Current States
    ↓
Optimize Range Transition
    ↓
Apply Constraint
    ↓
Continue
'''


'''
COMMON INTERVIEW MISTAKES

1. Trying to generate all permutations.

n! is impossible for n = 300.

2. Trying to track the actual permutation.

The actual values are unnecessary.

Track:

prefix length + inversion count

instead.

3. Forgetting how many inversions a new element can add.

For a prefix of size `i`,
the new element can add:

0..i

inversions.

4. Using the wrong transition.

Correct:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ ...
+ dp[j-i]

5. Recalculating the range every time.

That gives:

O(n² × K)

Use a sliding window instead.

6. Forgetting to apply requirements immediately.

When:

required[i] != -1

only that inversion count should survive.

7. Forgetting the base case.

A one-element prefix has:

0 inversions

Therefore:

dp[0] = 1

8. Forgetting modulo.

The number of permutations becomes enormous.

9. Tracking more inversion states than necessary.

Only counts up to the maximum required inversion count
are needed.

10. Forgetting that inversion count is non-decreasing
when the prefix is extended.

Adding a new element can only add inversions,
never remove existing ones.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Do NOT think:

"How do I generate all permutations?"

Think:

Permutation
    ↓
Represent by inversion contributions
    ↓
Each new element adds 0..i inversions
    ↓
DP by prefix length + inversion count
    ↓
Transition is a range sum
    ↓
Sliding Window optimizes the range
    ↓
Requirements keep one exact state

Core DP:

new_dp[j]
=
dp[j]
+ dp[j-1]
+ ...
+ dp[j-i]

Core optimization:

window += dp[j]

if j - i - 1 >= 0:
    window -= dp[j-i-1]

Core requirement handling:

if required[i] != -1:

    cnt = required[i]

    keep only new_dp[cnt]

Core state meaning:

dp[j]

=

Number of ways for the current prefix
to have exactly `j` inversions.

One-line mental model:

Prefix
→ Count Inversions
→ DP
→ Sliding Window
→ Enforce Requirement

The most important idea:

"When adding the next element, it can contribute
any number of new inversions from 0 to i."

Once you understand that,
the entire DP transition becomes natural.
'''