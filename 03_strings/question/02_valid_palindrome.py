# Valid Palindrome

"""
PROBLEM
Given a string s, return True if it reads the same forward and backward
after ignoring non-alphanumeric characters and letter case.

Examples:
"A man, a plan, a canal: Panama" -> True
"race a car" -> False
" " -> True

PATTERN
Two pointers / string filtering.

RECOGNITION TRICKS
- "Same forward and backward" -> palindrome.
- Ignore spaces or punctuation -> skip non-alphanumeric characters.
- Ignore uppercase/lowercase -> compare lowercase characters.
- Compare opposite ends -> consider two pointers.

REAL-WORLD ANALOGY
Read from both ends toward the middle. Each pair of characters should match.

APPROACH 1 — BRUTE FORCE
Build a cleaned string from lowercase alphanumeric characters, reverse it,
and compare both strings.
Time: O(n); extra space: O(n).
Note: This code uses a list comprehension to avoid repeated string concatenation.

APPROACH 2 — BETTER APPROACH
Build a cleaned list of lowercase alphanumeric characters, then compare
the list with its reverse.
Time: O(n); extra space: O(n).
This is clear, but slicing creates a reversed copy too.

APPROACH 3 — OPTIMAL / STANDARD
Use two pointers on the original string. Skip non-alphanumeric characters,
compare lowercase characters, then move inward.
Time: O(n); auxiliary space: O(1).

WHY THE OPTIMAL APPROACH WORKS
A palindrome must have matching characters at equal distances from both ends.
Each successful comparison confirms one pair. A mismatch proves the string
is not a palindrome. If all pairs match, it is a palindrome.

STEP-BY-STEP THINKING
1. Set left = 0 and right = len(s) - 1.
2. Skip non-alphanumeric characters from the left.
3. Skip non-alphanumeric characters from the right.
4. Compare the lowercase forms of the current characters.
5. Return False if they differ.
6. Move both pointers inward.
7. If the pointers meet or cross, return True.

DRY RUN
s = "A man, a plan, a canal: Panama"

After ignoring punctuation/spaces and letter case:
"amanaplanacanalpanama"

Compare the first and last characters, then the next pair, and continue.
Every pair matches, so the output is True.

EDGE CASES
- Empty string: "" -> True
- Only punctuation/spaces: " , " -> True
- One character: "a" -> True
- Mismatch: "ab" -> False
- Mixed case: "RaceCar" -> True
- Digits count as alphanumeric: "1a1" -> True

COMMON INTERVIEW MISTAKES
- Forgetting case-insensitive comparison.
- Forgetting to skip punctuation and spaces.
- Moving pointers in the wrong direction.
- Accessing invalid indexes after pointers cross.
- Calling an empty string non-palindromic.
- Claiming O(1) space for an approach that builds a cleaned string.

REUSABLE TWO-POINTER TEMPLATE
left, right = 0, len(s) - 1

while left < right:
    while left < right and should_skip(s[left]):
        left += 1
    while left < right and should_skip(s[right]):
        right -= 1
    if not matches(s[left], s[right]):
        return False
    left += 1
    right -= 1

return True

SIMILAR PROBLEMS
- Reverse String (LeetCode 344)
- Valid Palindrome II (LeetCode 680)
- Reverse Vowels of a String (LeetCode 345)

INTERVIEW TIP
Start with the cleaned-string solution because it is easy to explain.
Then optimize to two pointers to avoid storing a second string.
"""


# Approach 1: Brute force — clean, reverse, and compare.
def is_palindrome_brute(s):
    cleaned = "".join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]


# Approach 2: Better — clean into a list and compare from both ends.
def is_palindrome_better(s):
    chars = [char.lower() for char in s if char.isalnum()]
    left, right = 0, len(chars) - 1

    while left < right:
        if chars[left] != chars[right]:
            return False
        left += 1
        right -= 1

    return True


# Approach 3: Optimal / standard — two pointers on the original string.
def is_palindrome_optimal(s):
    left, right = 0, len(s) - 1

    while left < right:
        while left < right and not s[left].isalnum():
            left += 1

        while left < right and not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        " ",
        "",
        " , ",
        "RaceCar",
        "1a1",
        "ab",
    ]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute force:", is_palindrome_brute(s))
        print("Better:", is_palindrome_better(s))
        print("Optimal:", is_palindrome_optimal(s))
        print("-" * 30)
