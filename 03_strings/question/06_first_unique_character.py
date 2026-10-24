# First Unique Character in a String

"""
PROBLEM
Given a string s, return the index of the first character that appears
exactly once. If no such character exists, return -1.

Examples:
"leetcode" -> 0
"loveleetcode" -> 2
"aabb" -> -1

PATTERN
Hashing / frequency counting / string traversal.

RECOGNITION TRICKS
- "First character that appears once" -> count frequencies, then scan in order.
- Need both occurrence counts and original order -> dictionary + second pass.
- Return an index, not the character itself.
- A set alone is not enough because it does not store occurrence counts.

REAL-WORLD ANALOGY
In a queue, find the first person with a name that appears only once.
First count each name, then walk through the queue from the beginning.

APPROACH 1 — BRUTE FORCE
For each character, count how many times it appears in the whole string.
Return the first index whose character count is one.
Time: O(n^2); extra space: O(1) auxiliary space.
Python's count() scans the string each time.

APPROACH 2 — BETTER APPROACH (FREQUENCY DICTIONARY)
Count every character in one pass, then scan the string again and return
the first index whose count is one.
Time: O(n); extra space: O(k), where k is the number of distinct characters.

APPROACH 3 — ALTERNATIVE (COUNTER)
Use collections.Counter to build the frequency map, then scan the string.
Time: O(n); extra space: O(k).
This is concise Python, but understanding the dictionary version is important.

WHY FREQUENCY COUNTING WORKS
The frequency map tells us exactly how often each character appears.
Scanning the original string from left to right preserves the required order.
The first character with frequency one is therefore the answer.

STEP-BY-STEP THINKING
1. Count every character in s.
2. Visit each character by index from left to right.
3. If its frequency is one, return its index immediately.
4. If the scan finishes, return -1.

DRY RUN
s = "loveleetcode"

Frequencies include:
l: 2, o: 2, v: 1, e: 4, t: 1, c: 1, d: 1

Scan in order:
index 0: 'l' -> count 2
index 1: 'o' -> count 2
index 2: 'v' -> count 1

Output: 2

EDGE CASES
- Empty string: "" -> -1
- All repeated: "aabb" -> -1
- First character is unique: "abc" -> 0
- Unique character later: "aabbc" -> 4
- Case-sensitive: "aA" -> 0 because 'a' and 'A' are different characters.

COMMON INTERVIEW MISTAKES
- Returning the character instead of its index.
- Returning the first character that appears once without checking earlier positions.
- Using a set and losing frequency information.
- Returning 0 or None when no unique character exists; the required result is -1.
- Scanning only the frequency dictionary, which does not express the original string order.

REUSABLE TEMPLATE
counts = {}
for char in s:
    counts[char] = counts.get(char, 0) + 1

for i, char in enumerate(s):
    if counts[char] == 1:
        return i

return -1

SIMILAR PROBLEMS
- First Unique Character in a String (LeetCode 387)
- Ransom Note (LeetCode 383)
- Valid Anagram (LeetCode 242)
- Find All Anagrams in a String (LeetCode 438)

INTERVIEW TIP
The key is to separate counting from choosing. The first pass counts characters;
the second pass finds the earliest character whose count is one.
"""


# Approach 1: Brute force — count each character repeatedly.
def first_unique_brute(s):
    for i, char in enumerate(s):
        if s.count(char) == 1:
            return i
    return -1


# Approach 2: Better — frequency dictionary.
def first_unique_better(s):
    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for i, char in enumerate(s):
        if counts[char] == 1:
            return i

    return -1


# Approach 3: Alternative — collections.Counter.
from collections import Counter


def first_unique_counter(s):
    counts = Counter(s)

    for i, char in enumerate(s):
        if counts[char] == 1:
            return i

    return -1


if __name__ == "__main__":
    test_cases = [
        "leetcode",
        "loveleetcode",
        "aabb",
        "",
        "abc",
        "aabbc",
        "aA",
    ]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute force:", first_unique_brute(s))
        print("Frequency map:", first_unique_better(s))
        print("Counter:", first_unique_counter(s))
        print("-" * 30)
