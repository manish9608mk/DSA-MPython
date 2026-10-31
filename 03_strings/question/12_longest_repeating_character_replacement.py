# Longest Repeating Character Replacement

"""
PROBLEM
Given a string s and an integer k, replace at most k characters so the
longest substring can contain only one repeated character.
Return the maximum possible length.

Example:
s = "AABABBA", k = 1
Output: 4
Explanation: Replace one character in "AABA" to make "AAAA".

PATTERN
Sliding Window + Frequency Counting.

RECOGNITION TRICKS
- The question asks for the longest substring.
- You may change at most k characters inside that substring.
- For a window of length L, changes needed = L - highest character frequency.
- A window is valid when L - max_frequency <= k.

REAL-WORLD ANALOGY
Find the longest section of a banner that can be made one colour by repainting
at most k tiles.

APPROACH 1 — BRUTE FORCE
Try every substring and count its character frequencies.
For each substring, calculate length - maximum frequency.
Time: O(n^2 * A), where A is the alphabet size; for uppercase English letters,
A = 26, so this is O(n^2).
Space: O(A) = O(1) for the frequency counts.

APPROACH 2 — BETTER
For every left boundary, extend the right boundary and update frequencies.
Track the maximum frequency as the window grows; check whether the current
window can be fixed using at most k replacements.
Time: O(n^2) for a fixed-size alphabet.
Space: O(A) = O(1).

APPROACH 3 — OPTIMAL / STANDARD
Use a sliding window. Expand right and update counts. Track the highest
frequency seen in the current expansion. If window_length - max_frequency > k,
move left forward and decrease the outgoing character count.
Time: O(n), because each pointer moves forward at most n times.
Space: O(A) = O(1) for uppercase English letters.

WHY THE OPTIMAL APPROACH WORKS
To make a window contain one character, keep its most frequent character and
replace every other character. Therefore, required replacements are
window_length - maximum_frequency. If this exceeds k, shrink the window.

STEP-BY-STEP THINKING
1. Keep left = 0, counts, max_frequency = 0, and answer = 0.
2. Add s[right] to the frequency map.
3. Update max_frequency.
4. While window length - max_frequency > k, remove s[left] and advance left.
5. Update the answer with the valid window length.

DRY RUN
s = "AABABBA", k = 1
A window such as "AABA" has length 4 and max frequency 3.
Required replacements = 4 - 3 = 1, so length 4 is possible.
No valid answer longer than 4 exists for this input.

EDGE CASES
- Empty string -> 0
- k = 0 -> longest run of the same character
- k >= len(s) -> len(s)
- All characters equal -> len(s)

COMMON INTERVIEW MISTAKES
- Using window length - max_frequency as the replacement count.
- Forgetting to remove the outgoing character from the frequency map.
- Moving left when the window is still valid.
- Recomputing the maximum frequency from scratch every time unnecessarily.

REUSABLE TEMPLATE
for right, char in enumerate(s):
    counts[char] = counts.get(char, 0) + 1
    max_frequency = max(max_frequency, counts[char])
    while (right - left + 1) - max_frequency > k:
        counts[s[left]] -= 1
        left += 1
    answer = max(answer, right - left + 1)

SIMILAR PROBLEMS
- Longest Substring Without Repeating Characters
- Minimum Window Substring
- Find All Anagrams in a String
- Max Consecutive Ones III

INTERVIEW TIP
State the validity formula clearly: window length minus the most frequent
character count must be at most k. The standard solution keeps max_frequency
as the highest value seen during expansion; it does not decrease it when
shrinking. This is safe for finding the maximum length, though the count may
not equal the exact current-window maximum at every moment.
"""

from collections import defaultdict


def character_replacement_brute(s: str, k: int) -> int:
    n = len(s)
    answer = 0

    for left in range(n):
        counts = defaultdict(int)

        for right in range(left, n):
            counts[s[right]] += 1
            max_frequency = max(counts.values())
            window_length = right - left + 1

            if window_length - max_frequency <= k:
                answer = max(answer, window_length)

    return answer


def character_replacement_better(s: str, k: int) -> int:
    n = len(s)
    answer = 0

    for left in range(n):
        counts = defaultdict(int)
        max_frequency = 0

        for right in range(left, n):
            counts[s[right]] += 1
            max_frequency = max(max_frequency, counts[s[right]])
            window_length = right - left + 1

            if window_length - max_frequency <= k:
                answer = max(answer, window_length)

    return answer


def character_replacement_optimal(s: str, k: int) -> int:
    counts = defaultdict(int)
    left = 0
    max_frequency = 0
    answer = 0

    for right, char in enumerate(s):
        counts[char] += 1
        max_frequency = max(max_frequency, counts[char])

        while (right - left + 1) - max_frequency > k:
            counts[s[left]] -= 1
            left += 1

        answer = max(answer, right - left + 1)

    return answer


if __name__ == "__main__":
    s = "AABABBA"
    k = 1

    print("Brute force:", character_replacement_brute(s, k))
    print("Better:", character_replacement_better(s, k))
    print("Optimal:", character_replacement_optimal(s, k))
