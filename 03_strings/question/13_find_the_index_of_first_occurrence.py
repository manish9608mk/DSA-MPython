# Find the Index of the First Occurrence in a String

"""
PROBLEM
Return the first index where needle occurs in haystack. Return -1 if absent.
Example: haystack = "sadbutsad", needle = "sad" -> 0

PATTERN
String Matching: Brute Force and KMP (Knuth-Morris-Pratt).

RECOGNITION TRICKS
- Find one string inside another.
- Simple solution checks every possible starting position.
- KMP avoids repeated comparisons after a mismatch.

REAL-WORLD ANALOGY
Find the first place a short word appears inside a paragraph.

APPROACH 1 — BRUTE FORCE
Try every valid starting index and compare characters.
Time: O((n - m + 1) * m) = O(nm) worst case.
Space: O(1).

APPROACH 2 — PYTHON BUILT-IN
Use haystack.find(needle). This is practical Python, but its exact complexity
is implementation-dependent; do not claim a universal O(n) bound.
Space: Implementation-dependent.

APPROACH 3 — OPTIMAL / STANDARD: KMP
Build the LPS (Longest Proper Prefix which is also Suffix) array for needle.
On mismatch, use LPS to avoid rechecking characters.
Time: O(n + m).
Space: O(m).

WHY KMP WORKS
LPS tells us how much of the pattern is still a valid prefix after mismatch.
The text pointer never moves backward, preventing repeated scanning.

STEP-BY-STEP THINKING
1. Empty needle -> return 0.
2. Build LPS for needle.
3. Compare haystack[i] and needle[j].
4. If equal, move both pointers.
5. If j == m, return i - m.
6. On mismatch, set j = lps[j - 1] if j > 0; otherwise move i forward.
7. If no match is found, return -1.

DRY RUN
haystack = "ababc", needle = "abc".
The first two characters "ab" match, then a mismatch occurs.
KMP uses LPS to continue without restarting the text scan.
It finds "abc" at index 2.

EDGE CASES
- Empty needle -> 0
- Needle longer than haystack -> -1
- No match -> -1
- Match at index 0
- Repeated prefixes, e.g. "aaaaab" and "aaab"

COMMON INTERVIEW MISTAKES
- Returning the ending index instead of the starting index.
- Moving both KMP pointers forward after every mismatch.
- Forgetting the empty-needle case.
- Building LPS for haystack instead of needle.
- Using lps[j] instead of lps[j - 1] on mismatch.

REUSABLE TEMPLATE
if j == len(pattern):
    return i - len(pattern)
if j > 0:
    j = lps[j - 1]
else:
    i += 1

SIMILAR PROBLEMS
- Repeated Substring Pattern
- Longest Happy Prefix
- Shortest Palindrome
- Find All Occurrences of a Pattern

INTERVIEW TIP
Start with O(nm) brute force. Then explain how KMP reaches O(n + m)
using prefix/suffix information stored in LPS.
"""

from typing import List


def str_str_brute(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0

    for start in range(n - m + 1):
        j = 0
        while j < m and haystack[start + j] == needle[j]:
            j += 1
        if j == m:
            return start

    return -1


def str_str_builtin(haystack: str, needle: str) -> int:
    return haystack.find(needle)


def build_lps(pattern: str) -> List[int]:
    lps = [0] * len(pattern)
    length = 0
    i = 1

    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            i += 1

    return lps


def str_str_kmp(haystack: str, needle: str) -> int:
    n, m = len(haystack), len(needle)
    if m == 0:
        return 0

    lps = build_lps(needle)
    i = j = 0

    while i < n:
        if haystack[i] == needle[j]:
            i += 1
            j += 1
            if j == m:
                return i - m
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return -1


if __name__ == "__main__":
    haystack = "ababc"
    needle = "abc"

    print("Brute force:", str_str_brute(haystack, needle))
    print("Built-in find:", str_str_builtin(haystack, needle))
    print("KMP:", str_str_kmp(haystack, needle))
