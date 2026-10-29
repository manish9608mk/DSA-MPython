# Longest Common Subsequence (LCS)

"""
PROBLEM
Given two strings text1 and text2, return the length of their longest
common subsequence.

A subsequence keeps the relative order of characters, but characters do not
need to be next to each other.

Examples:
"abcde", "ace" -> 3
"abc", "abc" -> 3
"abc", "def" -> 0

PATTERN
Dynamic programming / two strings.

RECOGNITION TRICKS
- "Longest common subsequence" -> usually dynamic programming.
- Characters must stay in order, but gaps are allowed.
- If characters match, use both and move diagonally.
- If they do not match, skip one character from either string and take the
  better result.
- Do not confuse subsequence with substring; a substring must be continuous.

REAL-WORLD ANALOGY
Compare two messages and find the longest sequence of letters that appears
in both messages in the same order, even if other letters occur between them.

APPROACH 1 — BRUTE FORCE
Generate all subsequences of the first string and check which also appears
as a subsequence in the second string. There can be 2^m subsequences.
Time: exponential, approximately O(2^m * n) for a straightforward method.
Extra space: O(m) for recursion or a generated subsequence.
This is too slow for large inputs.

APPROACH 2 — BETTER APPROACH (RECURSION + MEMOIZATION)
Let solve(i, j) be the LCS length using text1[i:] and text2[j:].
If characters match, add 1 and move both indexes.
Otherwise, take the maximum of skipping one character from either string.
Memoization prevents solving the same state repeatedly.
Time: O(m * n); extra space: O(m * n).

APPROACH 3 — OPTIMAL / STANDARD (BOTTOM-UP DP)
Build a table dp where dp[i][j] is the LCS length of the first i characters
of text1 and the first j characters of text2.
If characters match: dp[i][j] = 1 + dp[i - 1][j - 1].
Otherwise: dp[i][j] = max(dp[i - 1][j], dp[i][j - 1]).
Time: O(m * n); extra space: O(m * n).

APPROACH 4 — SPACE-OPTIMIZED DP
Only the previous row and current row are needed.
Time: O(m * n); extra space: O(min(m, n)).
This gives the same answer while storing much less memory.

WHY THE DP TRANSITION WORKS
If the current characters match, they can extend a common subsequence from
the two prefixes before them. If they differ, they cannot both be the final
matched character, so at least one of them must be skipped. Taking the maximum
of those two choices considers the best possible result.

STEP-BY-STEP THINKING
1. Define dp[i][j] for prefixes of lengths i and j.
2. Initialize row 0 and column 0 to zero because an empty string has LCS 0
   with any string.
3. Compare text1[i - 1] and text2[j - 1].
4. If equal, use diagonal + 1.
5. Otherwise, take max(top, left).
6. Return dp[m][n].

DRY RUN
text1 = "abcde", text2 = "ace"

Common characters in order:
a -> c -> e

LCS = "ace"
Length = 3

EDGE CASES
- One string empty: "", "abc" -> 0
- Identical strings: "abc", "abc" -> 3
- No common characters: "abc", "def" -> 0
- One string is a subsequence of the other: "abcde", "ace" -> 3
- Repeated characters: "aab", "azb" -> 2

COMMON INTERVIEW MISTAKES
- Confusing subsequence with substring.
- Forgetting the zero row and zero column.
- Using dp[i][j] = diagonal + 1 when characters do not match.
- Returning a subsequence instead of its length when only length is requested.
- Using exponential recursion without memoization.
- Mixing string indexes with DP prefix lengths.

REUSABLE DP TEMPLATE
for i in range(1, m + 1):
    for j in range(1, n + 1):
        if text1[i - 1] == text2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

SIMILAR PROBLEMS
- Longest Common Subsequence (LeetCode 1143)
- Longest Palindromic Subsequence (LeetCode 516)
- Delete Operation for Two Strings (LeetCode 583)
- Shortest Common Supersequence (LeetCode 1092)

INTERVIEW TIP
Define the DP state clearly before coding. Explain why matching characters use
the diagonal state and why a mismatch takes the maximum of top and left.
"""


# Approach 1: Brute force — generate subsequences of text1.
def lcs_brute(text1, text2):
    best = 0

    def is_subsequence(candidate, text):
        i = 0
        for char in text:
            if i < len(candidate) and candidate[i] == char:
                i += 1
        return i == len(candidate)

    def generate(index, current):
        nonlocal best

        if index == len(text1):
            if len(current) > best and is_subsequence(current, text2):
                best = len(current)
            return

        generate(index + 1, current)
        generate(index + 1, current + text1[index])

    generate(0, "")
    return best


# Approach 2: Recursion + memoization.
from functools import lru_cache


def lcs_memo(text1, text2):
    @lru_cache(maxsize=None)
    def solve(i, j):
        if i == len(text1) or j == len(text2):
            return 0

        if text1[i] == text2[j]:
            return 1 + solve(i + 1, j + 1)

        return max(solve(i + 1, j), solve(i, j + 1))

    return solve(0, 0)


# Approach 3: Bottom-up DP table.
def lcs_dp(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]


# Approach 4: Space-optimized DP.
def lcs_space_optimized(text1, text2):
    # Keep the second string shorter to minimize row size.
    if len(text2) > len(text1):
        text1, text2 = text2, text1

    m, n = len(text1), len(text2)
    previous = [0] * (n + 1)

    for i in range(1, m + 1):
        current = [0] * (n + 1)

        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                current[j] = previous[j - 1] + 1
            else:
                current[j] = max(previous[j], current[j - 1])

        previous = current

    return previous[n]


if __name__ == "__main__":
    test_cases = [
        ("abcde", "ace"),
        ("abc", "abc"),
        ("abc", "def"),
        ("", "abc"),
        ("aab", "azb"),
    ]

    for text1, text2 in test_cases:
        print("Input:", repr(text1), repr(text2))
        print("Brute force:", lcs_brute(text1, text2))
        print("Memoization:", lcs_memo(text1, text2))
        print("Bottom-up DP:", lcs_dp(text1, text2))
        print("Space optimized:", lcs_space_optimized(text1, text2))
        print("-" * 35)
