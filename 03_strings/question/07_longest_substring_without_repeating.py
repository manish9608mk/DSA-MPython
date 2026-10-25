# Longest Substring Without Repeating Characters

"""
PROBLEM
Given a string s, return the length of the longest substring that contains
no repeated characters. A substring is a continuous part of a string.

Examples:
"abcabcbb" -> 3
"bbbbb" -> 1
"pwwkew" -> 3

PATTERN
Sliding window + hashing.

RECOGNITION TRICKS
- "Longest substring" -> consider a sliding window.
- "No repeated characters" -> track characters inside the window.
- A substring must be continuous, unlike a subsequence.
- When a duplicate enters the window, move the left boundary forward.

REAL-WORLD ANALOGY
Imagine a window over a row of characters. Expand it to the right while all
characters are unique. If a duplicate appears, shrink from the left until
the window is valid again.

APPROACH 1 — BRUTE FORCE
Try every substring and check whether its characters are unique.
Time: O(n^3) for this straightforward slicing-and-checking version.
Extra space: O(k) for the set used on one substring.

APPROACH 2 — BETTER
Start at each index and expand right, tracking characters in a set.
Stop when a repeated character appears.
Time: O(n^2) expected; extra space: O(k).

APPROACH 3 — OPTIMAL / STANDARD (SLIDING WINDOW)
Maintain a window with no repeated characters and a set of its characters.
Expand right. If a duplicate appears, remove characters from the left until
the duplicate is gone. Update the maximum window length.
Time: O(n) expected; extra space: O(k).

APPROACH 4 — ALTERNATIVE OPTIMAL (LAST-SEEN INDEX)
Store each character's most recent index. If a repeated character is inside
the current window, jump left to one position after its previous index.
Time: O(n) expected; extra space: O(k).
This avoids removing characters one by one.

WHY SLIDING WINDOW WORKS
The window is kept free of duplicates. For each right endpoint, the left
pointer moves only as far as needed to restore uniqueness. Each pointer moves
forward at most n times, so the total scan is O(n).

STEP-BY-STEP THINKING
1. Set left = 0 and create an empty set.
2. Move right from the beginning to the end.
3. While s[right] is already in the set, remove s[left] and move left forward.
4. Add s[right] to the set.
5. Update best with right - left + 1.
6. Continue until the string ends.

DRY RUN
s = "abcabcbb"

Read a -> window "a", best = 1
Read b -> window "ab", best = 2
Read c -> window "abc", best = 3
Read a -> remove old a; window "bca", best = 3
Continue; no window becomes longer than 3.

Output: 3

EDGE CASES
- Empty string: "" -> 0
- All same characters: "bbbbb" -> 1
- All unique characters: "abc" -> 3
- "pwwkew" -> 3
- Spaces count as characters: "a b" -> 3

COMMON INTERVIEW MISTAKES
- Confusing substring with subsequence.
- Updating best before the window is valid.
- Forgetting to shrink the window while a duplicate remains.
- Moving left backward in the last-seen-index approach.
- Setting left to the previous index instead of previous index + 1.
- Returning a substring when the problem asks for its length.

REUSABLE SLIDING-WINDOW TEMPLATE
left = 0
window = set()
best = 0

for right, char in enumerate(s):
    while char in window:
        window.remove(s[left])
        left += 1
    window.add(char)
    best = max(best, right - left + 1)

SIMILAR PROBLEMS
- Longest Substring Without Repeating Characters (LeetCode 3)
- Longest Repeating Character Replacement (LeetCode 424)
- Permutation in String (LeetCode 567)
- Minimum Window Substring (LeetCode 76)

INTERVIEW TIP
Explain the invariant: the current window always contains unique characters.
Each pointer only moves forward, so the solution runs in O(n) time.
"""


# Approach 1: Brute force — check every substring.
def longest_unique_brute(s):
    best = 0

    for start in range(len(s)):
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if len(set(substring)) == len(substring):
                best = max(best, len(substring))

    return best


# Approach 2: Better — expand from each start with a set.
def longest_unique_better(s):
    best = 0

    for left in range(len(s)):
        seen = set()

        for right in range(left, len(s)):
            if s[right] in seen:
                break

            seen.add(s[right])
            best = max(best, right - left + 1)

    return best


# Approach 3: Optimal / standard — sliding window with a set.
def longest_unique_sliding_window(s):
    left = 0
    window = set()
    best = 0

    for right, char in enumerate(s):
        while char in window:
            window.remove(s[left])
            left += 1

        window.add(char)
        best = max(best, right - left + 1)

    return best


# Approach 4: Alternative optimal — jump using each character's last index.
def longest_unique_last_seen(s):
    last_seen = {}
    left = 0
    best = 0

    for right, char in enumerate(s):
        if char in last_seen and last_seen[char] >= left:
            left = last_seen[char] + 1

        last_seen[char] = right
        best = max(best, right - left + 1)

    return best


if __name__ == "__main__":
    test_cases = ["abcabcbb", "bbbbb", "pwwkew", "", "abc", "a b", "abba"]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute force:", longest_unique_brute(s))
        print("Better:", longest_unique_better(s))
        print("Sliding window:", longest_unique_sliding_window(s))
        print("Last seen index:", longest_unique_last_seen(s))
        print("-" * 35)
