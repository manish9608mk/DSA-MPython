# 506. Relative Ranks

'''
Link:
https://leetcode.com/problems/relative-ranks/

Given an array of unique scores, rank the athletes.

1st → Gold Medal
2nd → Silver Medal
3rd → Bronze Medal
4th onward → "4", "5", ...

Return the answer in the ORIGINAL order.
'''

'''
PATTERN:

Need ranking
    +
Need descending order
    ↓
SORTING

But answer must remain in original order
    ↓
Preserve original index

(score, original_index)
    ↓
Sort by score
    ↓
Sorted position = rank
    ↓
Put result back at original index
'''


'''
APPROACH 1 — BRUTE FORCE:

For every athlete:

Count how many scores are greater.

rank = number of greater scores + 1

Example:

score = [10,3,8,9,4]

For 3:

Greater scores:
10, 8, 9, 4

Count = 4

Rank = 5


CODE:

for i in range(n):

    rank = 1

    for j in range(n):
        if score[j] > score[i]:
            rank += 1

    # convert rank to medal/string


COMPLEXITY:

Time  : O(n²)
Space : O(n)


Why not preferred?

Every athlete scans the entire array.
'''


'''
APPROACH 2 — SORT + HASH MAP:

Create:

score → original index

Example:

10 → 0
3  → 1
8  → 2
9  → 3
4  → 4

Sort the scores in descending order:

[10,9,8,4,3]

Then:

10 → index 0 → rank 1
9  → index 3 → rank 2
8  → index 2 → rank 3
4  → index 4 → rank 4
3  → index 1 → rank 5


COMPLEXITY:

Time  : O(n log n)
Space : O(n)
'''


'''
APPROACH 3 — OPTIMAL / STANDARD:

Store:

(score, original_index)

Example:

[(10,0), (3,1), (8,2), (9,3), (4,4)]

Sort by score descending:

[(10,0), (9,3), (8,2), (4,4), (3,1)]

Now sorted position gives the rank.

position 0 → rank 1
position 1 → rank 2
position 2 → rank 3
position 3 → rank 4
position 4 → rank 5

Put each rank into its original index.

This is the clean standard approach.
'''


class Solution:

    def findRelativeRanks(self, score: list[int]) -> list[str]:

        athletes = [(value, index) for index, value in enumerate(score)]

        athletes.sort(reverse=True)

        answer = [""] * len(score)

        for rank, (value, index) in enumerate(athletes, start=1):

            if rank == 1:
                answer[index] = "Gold Medal"

            elif rank == 2:
                answer[index] = "Silver Medal"

            elif rank == 3:
                answer[index] = "Bronze Medal"

            else:
                answer[index] = str(rank)

        return answer


# Test case
score = [10, 3, 8, 9, 4]

solution = Solution()

result = solution.findRelativeRanks(score)

print("Result =", result)


'''
Output:

Result = ['Gold Medal', '5', 'Bronze Medal', 'Silver Medal', '4']
'''


'''
WHY THE OPTIMAL APPROACH WORKS:

score
    ↓
attach original index
    ↓
sort descending
    ↓
position in sorted array = rank
    ↓
use original index
    ↓
restore original order


Example:

score = [10,3,8,9,4]

Sorted:

10 → index 0 → rank 1
9  → index 3 → rank 2
8  → index 2 → rank 3
4  → index 4 → rank 4
3  → index 1 → rank 5

Final:

index 0 → Gold
index 1 → 5
index 2 → Bronze
index 3 → Silver
index 4 → 4


COMPLEXITY:

Time  : O(n log n)
Space : O(n)


INTERVIEW THINKING:

Need ranking
    ↓
Ranking depends on score order
    ↓
Sort scores descending
    ↓
But original positions are required
    ↓
Store original index
    ↓
(score, index)
    ↓
Sort
    ↓
Sorted position = rank
    ↓
Put result at original index


INTERVIEW EXPLANATION:

"The rank depends on the descending order of the scores,
so I will sort the athletes by score.

Because the output must be in the original order,
I will store each score together with its original index.

After sorting, the position gives the rank.
I then place the corresponding medal or rank string
back at the stored original index.

The time complexity is O(n log n) because of sorting,
and the space complexity is O(n)."
'''


'''
RECOGNITION TRICKS:

1. Need to rank elements
2. Higher/lower values determine position
3. Need sorted order
4. Answer must preserve original positions
5. Need to remember where each element came from

→ Think:

SORT + ORIGINAL INDEX


REUSABLE TEMPLATE:

items = [(value, index) for index, value in enumerate(nums)]

items.sort(reverse=True)

answer = [""] * len(nums)

for rank, (value, index) in enumerate(items, start=1):

    answer[index] = result_for_rank(rank)


GENERAL IDEA:

Sort something
    +
Preserve original index
    ↓
Process in sorted order
    ↓
Restore answer using original index
'''


'''
And this becomes part of your SORTING family.

When you later see:

Relative Ranks
Sort Colors
Kth Largest Element
Top K problems
Meeting scheduling
Activity selection
Ranking problems
Sort + restore original positions

Ask:

"Does sorting determine the answer,
but do I still need the original positions?"

    ↓
SORT + INDEX MAPPING
'''