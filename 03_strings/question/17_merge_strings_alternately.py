# Merge Strings Alternately

"""
PROBLEM
Merge word1 and word2 by taking one character from each, starting with word1.
If one string is longer, append its remaining characters.
Example: "abc", "pqr" -> "apbqcr"
Example: "ab", "pqrs" -> "apbqrs"

PATTERN
Two Pointers + String Construction.

RECOGNITION TRICKS
- Take characters alternately from two strings.
- Input strings may have different lengths.
- Append the remaining suffix after one string ends.

REAL-WORLD ANALOGY
Take one item alternately from two queues, then take the remaining items.

APPROACH 1 — BRUTE FORCE
Build the result with repeated string concatenation.
Time: O((n + m)^2) worst case due to immutable-string copying.
Space: O(n + m) for the output.

APPROACH 2 — BETTER: BUILD A LIST
Append alternating characters to a list, then join once.
Time: O(n + m).
Space: O(n + m) for output storage.

APPROACH 3 — OPTIMAL / STANDARD: TWO POINTERS
Use i and j to read both strings. Append one character from each while both
have characters, then append the remaining suffixes.
Time: O(n + m).
Space: O(n + m) for output; O(1) auxiliary space excluding output.

WHY THE APPROACH WORKS
Every character is copied exactly once and in the required order.
Both pointers only move forward, so the work is linear.

STEP-BY-STEP THINKING
1. Initialize i = 0, j = 0, and an output list.
2. While both strings have characters, append word1[i], then word2[j].
3. Advance both pointers.
4. Append any remaining characters from word1 and word2.
5. Join the list.

DRY RUN
word1 = "ab", word2 = "pqrs"
Take a,p -> "ap"; take b,q -> "apbq".
word1 ends; append "rs" -> "apbqrs".

EDGE CASES
- Both empty -> ""
- One empty -> return the other
- Equal lengths -> fully alternating
- Different lengths -> append the remaining suffix
- One-character strings -> alternate once

COMMON INTERVIEW MISTAKES
- Forgetting the remaining suffix.
- Taking two characters from one string in a turn.
- Claiming repeated concatenation is O(n + m).
- Starting with the wrong string.

REUSABLE TEMPLATE
while i < len(a) and j < len(b):
    result.append(a[i])
    result.append(b[j])
    i += 1
    j += 1
result.extend(a[i:])
result.extend(b[j:])

SIMILAR PROBLEMS
- Zigzag Conversion
- Interleaving String
- Merge Two Sorted Lists
- Shuffle String

INTERVIEW TIP
Each character is processed once: O(n + m) time. Output storage is O(n + m);
auxiliary working space is O(1) if output is excluded.
"""

def merge_alternately_brute(word1: str, word2: str) -> str:
    result = ""
    limit = min(len(word1), len(word2))

    for i in range(limit):
        result += word1[i] + word2[i]

    return result + word1[limit:] + word2[limit:]


def merge_alternately_list(word1: str, word2: str) -> str:
    result = []
    limit = min(len(word1), len(word2))

    for i in range(limit):
        result.append(word1[i])
        result.append(word2[i])

    result.extend(word1[limit:])
    result.extend(word2[limit:])
    return "".join(result)


def merge_alternately_two_pointers(word1: str, word2: str) -> str:
    result = []
    i = j = 0

    while i < len(word1) and j < len(word2):
        result.append(word1[i])
        result.append(word2[j])
        i += 1
        j += 1

    result.extend(word1[i:])
    result.extend(word2[j:])
    return "".join(result)


if __name__ == "__main__":
    tests = [("abc", "pqr"), ("ab", "pqrs"), ("abcd", "pq"), ("", "xyz")]
    for first, second in tests:
        print(first, second, "->", merge_alternately_brute(first, second),
              merge_alternately_list(first, second),
              merge_alternately_two_pointers(first, second))
