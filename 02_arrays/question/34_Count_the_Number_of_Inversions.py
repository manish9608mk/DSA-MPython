# 3193. COUNT THE NUMBER OF INVERSIONS

"""
PROBLEM

Given an integer n and requirements, count permutations of
[0, 1, 2, ..., n - 1] satisfying every prefix inversion requirement.

requirements[i] = [end, cnt]

It means the prefix perm[0:end + 1] must contain exactly cnt inversions.

An inversion is a pair (i, j) such that:
i < j and perm[i] > perm[j]

Return the number of valid permutations modulo 10**9 + 7.

Example:
Input:
n = 3
requirements = [[2, 2], [0, 0]]

Output:
2

Valid permutations:
[2, 0, 1] -> 2 inversions
[1, 2, 0] -> 2 inversions

The prefix of length 1 has zero inversions in both cases.
"""

"""
PATTERN

Dynamic Programming + Inversion Counting + Prefix Constraints

Main idea:
Count permutations by their length and inversion count.

dp[j] = number of permutations of the current length
        having exactly j inversions.

When a prefix has a fixed requirement, discard all DP states
that do not have the required inversion count.

Recognition tricks:
- Count permutations satisfying conditions.
- Conditions apply to prefixes.
- Exact inversion counts are required.
- n is too large for generating every permutation.
- The answer must be calculated modulo 10**9 + 7.
"""

"""
APPROACH 1 — BRUTE FORCE

Generate all n! permutations.

For each permutation:
1. Count inversions in every required prefix.
2. Check whether every requirement is satisfied.
3. Count the valid permutations.

Why it is inefficient:
There are n! permutations, and checking each permutation
can require additional time.

For n = 300, generating all permutations is impossible.
"""

# BRUTE FORCE IDEA

from itertools import permutations

def number_of_permutations_brute(n, requirements):
    required = dict(requirements)
    answer = 0

    for perm in permutations(range(n)):
        valid = True

        for end, cnt in requirements:
            inversions = 0

            for i in range(end + 1):
                for j in range(i + 1, end + 1):
                    if perm[i] > perm[j]:
                        inversions += 1

            if inversions != cnt:
                valid = False
                break

        if valid:
            answer += 1

    return answer


"""
Complexity:
Time: At least O(n!); checking all required prefixes adds more work.
Space: O(n) for each generated permutation, excluding iterator internals.

This approach is only for understanding, not for the constraints.
"""

"""
APPROACH 2 — DYNAMIC PROGRAMMING

Define:

dp[i][j] = number of permutations of length i
           having exactly j inversions.

Base case:
dp[0][0] = 1

There is one empty permutation and it has zero inversions.

Transition:

dp[i][j] = sum(dp[i - 1][j - x])
           for x from 0 to min(j, i - 1)

Why?

Insert the new largest element into a permutation of length i - 1.

The new element can create:
0, 1, 2, ..., i - 1 inversions.

Therefore, every previous inversion count can contribute
to the current inversion count.

A direct transition loops over all possible x, making it
O(n * K * n) time.

We can optimize it using a sliding window.
"""

"""
APPROACH 3 — OPTIMAL / STANDARD

Use one-dimensional DP with a sliding window.

Let K be the inversion count required for the complete array.

We only need inversion counts from 0 to K.

For each length i:
1. Build the next DP array.
2. Maintain a running window sum.
3. Remove states that exceed the allowed insertion range.
4. Apply the requirement for prefix length i.
5. Keep only the required inversion count when a constraint exists.

Sliding-window transition:

new_dp[j] = dp[j] + dp[j - 1] + ... + dp[j - (i - 1)]

Only valid indices are included.

This reduces the transition to O(K) per length.
"""

"""
IMPORTANT OPTIMIZATION

A prefix requirement [end, cnt] means that the prefix of length
end + 1 must have exactly cnt inversions.

After processing that prefix:
- Keep dp[cnt].
- Set every other DP state to zero.

Future prefixes must be built only from these valid states.

The input guarantees a requirement for end = n - 1.
Therefore, the final required inversion count is available.
"""

# OPTIMAL CODE

from typing import List

class Solution:
    def numberOfPermutations(
        self, n: int, requirements: List[List[int]]
    ) -> int:
        MOD = 10**9 + 7

        req = [-1] * n

        for end, cnt in requirements:
            req[end] = cnt

        max_inv = req[n - 1]

        dp = [0] * (max_inv + 1)
        dp[0] = 1

        for length in range(1, n + 1):
            new_dp = [0] * (max_inv + 1)
            window = 0

            for inv in range(max_inv + 1):
                window += dp[inv]

                if inv >= length:
                    window -= dp[inv - length]

                new_dp[inv] = window % MOD

            dp = new_dp

            required = req[length - 1]

            if required != -1:
                value = dp[required]
                dp = [0] * (max_inv + 1)
                dp[required] = value

        return dp[max_inv]


"""
WHY DOES THE SLIDING WINDOW WORK?

For a new permutation of length i, inserting the largest element
can add at most i - 1 inversions.

For inversion count j, valid previous counts are:

j, j - 1, ..., j - (i - 1)

The running window adds the newest DP value and removes the value
that is now outside this range.

Thus, every valid previous state is counted exactly once.

Modulo arithmetic keeps values within manageable bounds.
"""

"""
STEP-BY-STEP THINKING

1. Read every requirement into req[end].
2. Find the final required inversion count K.
3. Initialize dp[0] = 1.
4. Process permutation lengths from 1 to n.
5. For each length, calculate all inversion-count states.
6. Use the sliding window to calculate each new state.
7. If the current prefix has a requirement, remove all states
   except the required inversion count.
8. Return dp[K].
"""

"""
DRY RUN

Input:
n = 3
requirements = [[2, 2], [0, 0]]

Required prefix inversion counts:
Length 1 -> 0
Length 3 -> 2

There is no requirement for length 2.

Length 0:
dp = [1, 0, 0]

Length 1:
Only zero inversions are possible.
dp = [1, 0, 0]

Requirement for length 1 is 0.
Keep only dp[0].

Length 2:
Possible inversion counts are 0 and 1.
dp = [1, 1, 0]

No requirement for length 2, so keep all states.

Length 3:
Possible inversion counts are 0, 1, 2, 3.
But K = 2, so track only 0, 1, 2.

Before applying the final requirement:
dp = [1, 2, 2]

The requirement for length 3 is 2.
Answer = dp[2] = 2.

Output:
2
"""

"""
WHY DOES THE APPROACH WORK?

1. Every permutation of length i can be created by inserting
   the largest element into a permutation of length i - 1.

2. The insertion creates between 0 and i - 1 new inversions.

3. The DP transition counts every valid construction.

4. Applying a prefix requirement removes every state that violates it.

5. The final requirement fixes the inversion count of the complete
   permutation, so dp[max_inv] is the required answer.
"""

"""
EDGE CASES

1. n = 2, requirements = [[0, 0], [1, 0]]
   Output: 1

2. Final required inversion count is 0.
   Only the increasing permutation can satisfy it.

3. A requirement allows fewer inversions than a previous prefix.
   The resulting DP state becomes zero if impossible.

4. Multiple requirements:
   Each required prefix must be enforced at its corresponding length.

5. Large answer:
   Apply modulo 10**9 + 7 during DP calculations.

6. Impossible combination of requirements:
   The DP count becomes zero.
"""

"""
TIME & SPACE COMPLEXITY

Let:
n = number of elements
K = required inversion count for the complete permutation

Time Complexity:
O(n * K)

Space Complexity:
O(K)

The algorithm stores two DP arrays of length K + 1.
"""

"""
INTERVIEW EXPLANATION

"I use dynamic programming where dp[j] represents the number
of permutations of the current length with exactly j inversions.

When adding the next largest element, it can create between
zero and length minus one new inversions. I calculate the new
states with a sliding window, reducing the transition to O(K)
per length.

Whenever a prefix requirement exists, I keep only its required
inversion-count state. Finally, I return the count for the
required inversion count of the complete permutation.

The time complexity is O(nK), and the auxiliary space is O(K)."
"""

"""
RECOGNITION TRICKS

When a problem asks you to count arrangements:
Think about Dynamic Programming.

When the number of inversions matters:
Track inversion counts as DP states.

When conditions apply to prefixes:
Apply constraints after processing each prefix length.

When a transition sums a continuous range of previous states:
Look for a sliding-window or prefix-sum optimization.

When n! is too large:
Avoid generating every permutation.
"""

"""
REUSABLE DP TEMPLATE

dp = [0] * (K + 1)
dp[0] = 1

for length in range(1, n + 1):
    new_dp = [0] * (K + 1)
    window = 0

    for inv in range(K + 1):
        window += dp[inv]

        if inv >= length:
            window -= dp[inv - length]

        new_dp[inv] = window % MOD

    dp = new_dp

    # Apply the requirement for this prefix, if present.
"""

"""
COMMON INTERVIEW MISTAKES

1. Generating all permutations for large n.
2. Confusing an inversion with an increasing pair.
3. Forgetting that end is a zero-based index.
4. Forgetting that prefix length equals end + 1.
5. Allowing the largest element to create more than length - 1
   new inversions.
6. Forgetting to apply a prefix requirement immediately.
7. Keeping DP states that violate a fixed requirement.
8. Forgetting modulo arithmetic.
9. Returning the sum of all final states instead of dp[max_inv].
10. Using O(n * K * n) DP when a sliding window is available.
"""

"""
MOST IMPORTANT THING TO REMEMBER

DP state:
dp[j] = number of permutations with j inversions.

Transition:
Insert the new largest element.

Optimization:
Sliding window over the previous DP states.

Constraint:
Keep only the required inversion count at each constrained prefix.

Time: O(n * K)
Space: O(K)
"""