# Valid Palindrome II

"""
PROBLEM
Given a string s, return True if it can become a palindrome after deleting
at most one character.
Example: "abca" -> True
Explanation: Delete 'b' or 'c' to get "aca" or "aba".

PATTERN
Two Pointers + Greedy Choice.

RECOGNITION TRICKS
- The string is almost a palindrome.
- You are allowed to remove at most one character.
- Compare characters from both ends.
- At the first mismatch, test skipping either the left or right character.

REAL-WORLD ANALOGY
Check whether a mirrored word can be fixed by removing one incorrect letter.

APPROACH 1 — BRUTE FORCE
First check whether s is already a palindrome. If not, try deleting each
character once and check the remaining string.
Time: O(n^2), because up to n palindrome checks each take O(n).
Space: O(n) for sliced strings.

APPROACH 2 — OPTIMAL / STANDARD: TWO POINTERS
Move inward while characters match. At the first mismatch, check the two
possible ranges: skip the left character OR skip the right character.
Time: O(n), because at most two remaining ranges are checked.
Space: O(1) auxiliary space when using index boundaries.

WHY THE OPTIMAL APPROACH WORKS
Before the first mismatch, both ends matched, so those characters must stay.
With only one deletion allowed, the mismatch forces exactly two possibilities:
remove the left character or remove the right character. If either remaining
range is a palindrome, the answer is True.

STEP-BY-STEP THINKING
1. Set left = 0 and right = len(s) - 1.
2. While left < right and s[left] == s[right], move both pointers inward.
3. At the first mismatch, check [left + 1, right].
4. Also check [left, right - 1].
5. Return True if either range is a palindrome.

DRY RUN
s = "abca"
- Compare 'a' and 'a' -> match.
- Compare 'b' and 'c' -> mismatch.
- Skip 'b': "aca" -> palindrome.
- Return True.

EDGE CASES
- Empty or one-character string -> True
- Already a palindrome -> True
- One deletion fixes it -> True
- More than one deletion is needed -> False
- Repeated characters -> handle normally

COMMON INTERVIEW MISTAKES
- Continuing with both pointers after a mismatch without using the deletion.
- Trying only one deletion choice.
- Deleting more than one character.
- Creating sliced strings in the optimal solution and claiming O(1) space.

REUSABLE TEMPLATE
if s[left] != s[right]:
    return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)

SIMILAR PROBLEMS
- Valid Palindrome
- Longest Palindromic Substring
- Palindrome Partitioning
- Remove One Element to Make the Array Strictly Increasing

INTERVIEW TIP
Explain why only two choices are needed at the first mismatch. This greedy
decision is the key insight; no need to try deleting every character.
"""

def is_palindrome_range(s: str, left: int, right: int) -> bool:
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True


def valid_palindrome_brute(s: str) -> bool:
    if s == s[::-1]:
        return True

    for index in range(len(s)):
        candidate = s[:index] + s[index + 1:]
        if candidate == candidate[::-1]:
            return True

    return False


def valid_palindrome_optimal(s: str) -> bool:
    left, right = 0, len(s) - 1

    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            return (
                is_palindrome_range(s, left + 1, right)
                or is_palindrome_range(s, left, right - 1)
            )

    return True


if __name__ == "__main__":
    test_cases = ["abca", "racecar", "abc", "deeee"]

    for value in test_cases:
        print(
            value,
            "->",
            valid_palindrome_brute(value),
            valid_palindrome_optimal(value)
        )
