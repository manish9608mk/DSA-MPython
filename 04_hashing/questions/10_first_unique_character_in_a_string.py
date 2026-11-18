# 10. FIRST UNIQUE CHARACTER IN A STRING

# LeetCode 387: https://leetcode.com

# PATTERN: Hash Map Frequency Counting + Order-Preserving Scan

"""
PROBLEM
-------
Given a string s, find the first non-repeating character in it and return
its index. If it does not exist, return -1.

Example:
s = "leetcode"
Output = 0

s = "loveleetcode"
Output = 2

s = "aabb"
Output = -1

RECOGNITION
-----------
- "Non-repeating / unique element" -> Frequency counting via Hash Map / Counter.
- "First in order" -> Iterate through original string indices after counting,
  or leverage Python 3.7+ insertion-ordered dictionaries.

REAL-WORLD ANALOGY
------------------
Scanning a guest check-in log from top to bottom to find the very first
visitor whose name appears only once on the entire list.

APPROACH 1: BRUTE FORCE NESTED SCAN
-----------------------------------
For each index i in s, scan every index j in s. If s[i] != s[j] for all
j != i, return i. If no such index exists, return -1.
Time: O(n^2), where n is the length of s.
Space: O(1) extra space.

APPROACH 2: TWO-PASS HASH MAP / COUNTER (RECOMMENDED)
-----------------------------------------------------
1. Pass 1: Build a frequency map of all characters in s using Counter(s).
2. Pass 2: Loop over enumerate(s) from left to right.
3. Return the first index idx where freq[char] == 1.
4. If the loop completes without finding one, return -1.

Time: O(n) (two linear passes over s).
Space: O(1) (at most 26 lowercase English letters).

APPROACH 3: FIXED-SIZE ARRAY OF 26 COUNTERS
-------------------------------------------
Instead of a dictionary, use an array counts = * 26 indexed by
ord(char) - ord('a'). Pass 1 increments counts; Pass 2 finds the first
character with count == 1.
Time: O(n).
Space: O(1) (strictly 26 integers, zero hash overhead).

APPROACH 4: SINGLE-PASS INDEX TRACKING MAP
------------------------------------------
Store each character's first index if seen once, or mark it as invalid (-1 /
float('inf')) if seen more than once. At the end, return the minimum valid
index across the 26 keys in the map.
Time: O(n) (only iterates over string once, then scans at most 26 map entries).
Space: O(1) (at most 26 entries).

WHY THE RECOMMENDED APPROACH WORKS
----------------------------------
You cannot know whether a character is unique until you have seen the entire
string (a duplicate could appear at the very last index). Counting frequencies
first gives global knowledge in O(n), and a second pass in index order
guarantees we return the earliest unique character.

INTERVIEW THINKING
------------------
1. To know if a character never repeats, I must inspect all characters first.
2. A Hash Map (Counter) counts every character's frequency in O(n) time.
3. Then I scan the string from index 0 to n - 1 and return the first index
   whose frequency is 1.
4. Since the alphabet has only 26 lowercase letters, extra space is O(1).

DRY RUN
-------
s = "loveleetcode"

Pass 1 (Frequency Map):
    {'l': 2, 'o': 2, 'v': 1, 'e': 4, 't': 1, 'c': 1, 'd': 1}

Pass 2 (Left-to-Right Scan):
    idx 0: 'l' -> freq['l'] == 2 (skip)
    idx 1: 'o' -> freq['o'] == 2 (skip)
    idx 2: 'v' -> freq['v'] == 1 -> Return 2!

EDGE CASES
----------
- Single character string "z" -> returns 0.
- All characters repeated "aabbcc" -> returns -1.
- First character is unique "abcdef" -> returns 0.
- Only the very last character is unique "aabbccd" -> returns 6.
- Long string with all 26 characters appearing multiple times.

COMMON MISTAKES
---------------
1. Returning the character itself instead of its integer index.
2. Returning 0 instead of -1 when no unique character exists.
3. Using s.count(char) inside a loop, which looks concise in Python but
   turns the algorithm into O(n^2).

REUSABLE TEMPLATE
-----------------
from collections import Counter
freq = Counter(s)
for idx, char in enumerate(s):
    if freq[char] == 1:
        return idx
return -1

PYTHON 3 IMPLEMENTATIONS
========================
"""

from collections import Counter


# APPROACH 1: Brute force nested scan.
def first_uniq_char_brute_force(s):
    n = len(s)
    for i in range(n):
        is_unique = True
        for j in range(n):
            if i != j and s[i] == s[j]:
                is_unique = False
                break
        if is_unique:
            return i
    return -1


# APPROACH 2: Two-pass Hash Map / Counter (recommended).
def first_uniq_char_counter(s):
    freq = Counter(s)
    for idx, char in enumerate(s):
        if freq[char] == 1:
            return idx
    return -1


# APPROACH 3: Fixed 26-element frequency array.
def first_uniq_char_array(s):
    counts = [0] * 26
    for char in s:
        counts[ord(char) - ord("a")] += 1

    for idx, char in enumerate(s):
        if counts[ord(char) - ord("a")] == 1:
            return idx
    return -1


# APPROACH 4: Single-pass first-index tracking map.
def first_uniq_char_single_pass(s):
    first_pos = {}
    for idx, char in enumerate(s):
        if char not in first_pos:
            first_pos[char] = idx
        else:
            first_pos[char] = -1

    earliest = float("inf")
    for pos in first_pos.values():
        if pos != -1 and pos < earliest:
            earliest = pos

    return earliest if earliest != float("inf") else -1


def run_tests():
    tests = [
        ("leetcode", 0),
        ("loveleetcode", 2),
        ("aabb", -1),
        ("z", 0),
        ("aabbccd", 6),
        ("aadadaad", -1),
    ]

    solutions = [
        first_uniq_char_brute_force,
        first_uniq_char_counter,
        first_uniq_char_array,
        first_uniq_char_single_pass,
    ]

    for s, expected in tests:
        for solution in solutions:
            actual = solution(s)
            assert actual == expected, (
                f"{solution.__name__}: expected {expected}, got {actual}"
            )

    print("All test cases passed for all 4 approaches.")


if __name__ == "__main__":
    run_tests()


"""
COMPLEXITY SUMMARY
------------------
Let n = length of string s.

Approach                    Time        Extra space
Brute force nested          O(n^2)      O(1)
Two-pass Counter            O(n)        O(1) (<= 26 chars)
Fixed 26-char array         O(n)        O(1) (26 ints)
Single-pass index map       O(n)        O(1) (<= 26 chars)

Two-pass Counter is the cleanest and most idiomatic Python solution, while
single-pass index tracking is great if the input is a huge data stream.

INTERVIEWER EXPLANATION
----------------------
"Because a duplicate can appear at the very end of the string, we must count
all character frequencies first. I will build a frequency Hash Map in one
O(n) pass, then scan the string from left to right and return the first
index whose frequency equals 1. Since the string contains lowercase English
letters, the map holds at most 26 keys, giving O(n) time and O(1) space."

RELATED PROBLEMS
----------------
- LeetCode 242: Valid Anagram
- LeetCode 383: Ransom Note
- LeetCode 451: Sort Characters By Frequency
- LeetCode 2351: First Letter to Appear Twice

PATTERN MEMORY
--------------
First Unique Character:
Count all frequencies -> scan left to right -> return first index with count == 1.

REVISION CHECKLIST
------------------
[ ] Explain why two passes (or a tracking map) are required.
[ ] Avoid calling s.count(char) inside a loop (O(n^2) trap).
[ ] Explain why extra space is O(1) for fixed alphabet size.
[ ] Return -1 when all characters repeat.
[ ] Explain the single-pass stream optimization as a follow-up.
[ ] Explain the solution in 30-60 seconds.
"""
