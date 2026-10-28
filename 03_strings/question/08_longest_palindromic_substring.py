# Longest Palindromic Substring

"""
PROBLEM
Given a string s, return the longest substring of s that is a palindrome.
A substring must be continuous.

Examples:
"babad" -> "bab" or "aba"
"cbbd" -> "bb"
"racecar" -> "racecar"

PATTERN
Two pointers / expand around center.

RECOGNITION TRICKS
- "Longest palindromic substring" -> try expanding around a center.
- A palindrome mirrors around its center.
- Odd-length palindrome: one center character, e.g. "racecar".
- Even-length palindrome: a center between two characters, e.g. "abba".
- If asked for a substring, characters must be continuous.

REAL-WORLD ANALOGY
Imagine a mirror placed at the center of a word. Characters equally far
from the mirror must match. Expand outward while they match.

APPROACH 1 — BRUTE FORCE
Generate every substring and check whether it is a palindrome.
There are O(n^2) substrings, and checking each can take O(n).
Time: O(n^3); extra space: O(n) for a substring/checking operation.

APPROACH 2 — BETTER APPROACH (EXPAND AROUND CENTER)
Try every index as an odd-length center and every gap as an even-length center.
Expand left and right while characters match, keeping the longest result.
Time: O(n^2); auxiliary space: O(1), excluding the returned substring.

APPROACH 3 — OPTIMAL (MANACHER'S ALGORITHM)
Manacher's algorithm reuses information about previously found palindromes
to avoid checking the same regions repeatedly.
Time: O(n); auxiliary space: O(n).
It is more complex and usually not needed unless linear time is required.

WHY EXPAND AROUND CENTER WORKS
Every palindrome has either one middle character or a middle gap between
two characters. Trying both center types at every position covers every
possible palindrome. Expanding while matching finds the longest palindrome
for each center.

STEP-BY-STEP THINKING
1. Start with the first character as the current best.
2. For each index, expand around (i, i) for odd-length palindromes.
3. Expand around (i, i + 1) for even-length palindromes.
4. While both indexes are valid and characters match, expand outward.
5. Keep the longer palindrome found.
6. Return the best substring.

DRY RUN
s = "cbbd"

Center between the two b characters:
left = 1, right = 2 -> 'b' == 'b'
Expand outward: 'c' != 'd', so stop.

Longest palindrome: "bb"

EDGE CASES
- Empty string: "" -> ""
- One character: "a" -> "a"
- All same characters: "aaaa" -> "aaaa"
- Even-length palindrome: "cbbd" -> "bb"
- Multiple valid answers: "babad" -> "bab" or "aba"

COMMON INTERVIEW MISTAKES
- Checking only odd-length centers and missing even-length palindromes.
- Confusing substring with subsequence.
- Updating the best boundaries incorrectly.
- Assuming "babad" has only one correct answer.
- Using a greedy method that stops at the first mismatch without trying other centers.

REUSABLE TEMPLATE
def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return left + 1, right - 1

SIMILAR PROBLEMS
- Longest Palindromic Substring (LeetCode 5)
- Palindromic Substrings (LeetCode 647)
- Valid Palindrome (LeetCode 125)
- Longest Palindromic Subsequence (LeetCode 516; subsequence, not substring)

INTERVIEW TIP
Start with brute force, then explain that every palindrome has a center.
Expand around both odd and even centers for an O(n^2) solution. Mention
Manacher's algorithm as the linear-time alternative if required.
"""


# Approach 1: Brute force — generate and check every substring.
def longest_palindrome_brute(s):
    best = ""

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            candidate = s[start:end]

            if candidate == candidate[::-1] and len(candidate) > len(best):
                best = candidate

    return best


# Helper used by the center-expansion approach.
def expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    # The last expansion went one step too far on both sides.
    return left + 1, right - 1


# Approach 2: Better / standard — expand around every center.
def longest_palindrome_center(s):
    if not s:
        return ""

    best_start = 0
    best_end = 0

    for center in range(len(s)):
        # Odd-length palindrome.
        left1, right1 = expand_around_center(s, center, center)

        # Even-length palindrome.
        left2, right2 = expand_around_center(s, center, center + 1)

        if right1 - left1 > best_end - best_start:
            best_start, best_end = left1, right1

        if right2 - left2 > best_end - best_start:
            best_start, best_end = left2, right2

    return s[best_start:best_end + 1]


# Approach 3: Optimal linear-time alternative — Manacher's algorithm.
def longest_palindrome_manacher(s):
    if not s:
        return ""

    # Transform "abba" into "^#a#b#b#a#$" to unify odd/even centers.
    transformed = "^#" + "#".join(s) + "#$"
    radii = [0] * len(transformed)
    center = right_boundary = 0

    for i in range(1, len(transformed) - 1):
        mirror = 2 * center - i

        if i < right_boundary:
            radii[i] = min(right_boundary - i, radii[mirror])

        while transformed[i + 1 + radii[i]] == transformed[i - 1 - radii[i]]:
            radii[i] += 1

        if i + radii[i] > right_boundary:
            center = i
            right_boundary = i + radii[i]

    max_length = max(radii)
    best_center = radii.index(max_length)
    start = (best_center - max_length) // 2

    return s[start:start + max_length]


if __name__ == "__main__":
    test_cases = ["babad", "cbbd", "racecar", "", "a", "aaaa", "abc"]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute force:", longest_palindrome_brute(s))
        print("Expand around center:", longest_palindrome_center(s))
        print("Manacher:", longest_palindrome_manacher(s))
        print("-" * 35)
