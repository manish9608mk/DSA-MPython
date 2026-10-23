# Longest Common Prefix

"""
PROBLEM
Given a list of strings strs, return the longest prefix shared by every string.
If no prefix is shared, return "".

Examples:
["flower", "flow", "flight"] -> "fl"
["dog", "racecar", "car"] -> ""
["alone"] -> "alone"

PATTERN
String traversal / prefix comparison.

RECOGNITION TRICKS
- "Shared starting characters" -> common prefix.
- Prefix means characters must match from index 0 without gaps.
- A mismatch ends the common prefix immediately.
- If one string ends first, the prefix cannot be longer than that string.

REAL-WORLD ANALOGY
Compare the labels on several boxes from the first character onward.
Stop as soon as one box has a different character.

APPROACH 1 — BRUTE FORCE
Take the first string as a candidate prefix. Test each prefix length against
every other string, keeping the longest candidate that all strings start with.
Time: O(n * m^2) for this straightforward slicing-based version.
Extra space: O(m) for temporary prefixes.
Here n is the number of strings and m is the length of the shortest string.

APPROACH 2 — BETTER APPROACH (HORIZONTAL SCAN)
Start with the first string as the prefix. Compare it with each next string,
shortening the prefix until that string starts with it.
Time: O(n * m) in the worst case.
Extra space: O(m) for the prefix.

APPROACH 3 — OPTIMAL / STANDARD (VERTICAL SCAN)
Compare characters at the same index across all strings.
Stop at the first mismatch or when any string ends.
Time: O(n * m) in the worst case.
Auxiliary space: O(1), excluding the returned prefix.
This avoids repeatedly creating shorter prefix strings during the scan.

WHY VERTICAL SCAN WORKS
A common prefix must have the same character at every index in every string.
At the first mismatch, no longer prefix can be common. Therefore, returning
the characters before that index gives the longest common prefix.

STEP-BY-STEP THINKING
1. If the list is empty, return "".
2. Use the first string as the reference.
3. Visit each character index in the first string.
4. Compare that character with the character at the same index in every string.
5. If a string ends or a character differs, return the prefix before this index.
6. If every character matches, return the first string.

DRY RUN
strs = ["flower", "flow", "flight"]

Index 0: f == f == f
Index 1: l == l == l
Index 2: o == o, but "flight"[2] is 'i'
Stop before index 2.

Output: "fl"

EDGE CASES
- Empty list: [] -> ""
- Empty first string: ["", "abc"] -> ""
- One string: ["alone"] -> "alone"
- No shared first character: ["dog", "cat"] -> ""
- One string is a prefix of another: ["app", "apple"] -> "app"
- Identical strings: ["abc", "abc"] -> "abc"

COMMON INTERVIEW MISTAKES
- Confusing a prefix with a substring; a prefix must start at index 0.
- Continuing after the first mismatch.
- Forgetting that one string may end before another.
- Assuming the list always has at least one string.
- Returning the longest string instead of the shared prefix.

REUSABLE TEMPLATE
for i in range(len(reference)):
    for word in words:
        if i == len(word) or word[i] != reference[i]:
            return reference[:i]
return reference

SIMILAR PROBLEMS
- Longest Common Prefix (LeetCode 14)
- Longest Common Subsequence (different problem: characters need not be consecutive)
- Find the Index of the First Occurrence in a String (LeetCode 28)

INTERVIEW TIP
Explain that you compare strings from left to right and stop at the first mismatch.
Mention empty inputs and the shortest string as important boundary cases.
"""


# Approach 1: Brute force — test candidate prefixes.
def longest_common_prefix_brute(strs):
    if not strs:
        return ""

    first = strs[0]
    shortest_length = min(len(word) for word in strs)
    answer = ""

    for length in range(1, shortest_length + 1):
        candidate = first[:length]

        if all(word.startswith(candidate) for word in strs):
            answer = candidate
        else:
            break

    return answer


# Approach 2: Better — horizontal scanning.
def longest_common_prefix_better(strs):
    if not strs:
        return ""

    prefix = strs[0]

    for word in strs[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                return ""

    return prefix


# Approach 3: Optimal / standard — vertical scanning.
def longest_common_prefix_optimal(strs):
    if not strs:
        return ""

    reference = strs[0]

    for i in range(len(reference)):
        for word in strs[1:]:
            if i == len(word) or word[i] != reference[i]:
                return reference[:i]

    return reference


if __name__ == "__main__":
    test_cases = [
        ["flower", "flow", "flight"],
        ["dog", "racecar", "car"],
        ["alone"],
        [],
        ["", "abc"],
        ["app", "apple"],
        ["abc", "abc"],
    ]

    for strs in test_cases:
        print("Input:", strs)
        print("Brute force:", longest_common_prefix_brute(strs))
        print("Better:", longest_common_prefix_better(strs))
        print("Optimal:", longest_common_prefix_optimal(strs))
        print("-" * 35)
