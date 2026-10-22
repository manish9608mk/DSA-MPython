# Reverse Vowels of a String

"""
PROBLEM
Given a string s, reverse only its vowels and return the result.
All other characters must stay in their original positions.

Examples:
"hello" -> "holle"
"leetcode" -> "leotcede"
"Python" -> "Python"

PATTERN
Two pointers / selective swapping.

RECOGNITION TRICKS
- Reverse only certain characters -> two pointers with a condition.
- Characters outside the target group must stay in place.
- For vowels, check membership in "aeiouAEIOU".
- The left pointer searches for the next vowel from the left.
- The right pointer searches for the next vowel from the right.

REAL-WORLD ANALOGY
Imagine people standing in a line, but only people wearing red shirts can swap.
Everyone else must stay in the same position.

APPROACH 1 — BRUTE FORCE
Collect all vowels in their original order, reverse that vowel list, and
put the reversed vowels back into the original vowel positions.
Time: O(n); extra space: O(n).

APPROACH 2 — BETTER APPROACH
Use a list of characters and a separate list of vowel positions.
Reverse the vowels by assigning the reversed vowel values to those positions.
Time: O(n); extra space: O(n).
This is clear, but stores both characters and positions.

APPROACH 3 — OPTIMAL / STANDARD
Convert s to a list and use two pointers.
Move left until it finds a vowel. Move right until it finds a vowel.
Swap those vowels, then move both pointers inward.
Time: O(n); extra space: O(n) for the character list.
The two-pointer scan itself uses O(1) extra space after conversion.

WHY THE TWO-POINTER APPROACH WORKS
The left pointer finds the first vowel that must receive a vowel from the
right side. The right pointer finds the last remaining vowel. Swapping them
places both vowels correctly. Repeating inward reverses all vowels while
leaving every non-vowel in its original position.

STEP-BY-STEP THINKING
1. Convert the string to a list because strings are immutable.
2. Set left to the first index and right to the last index.
3. Move left forward while it is not on a vowel.
4. Move right backward while it is not on a vowel.
5. If left is still less than right, swap those vowels.
6. Move both pointers inward.
7. Join the list and return the result.

DRY RUN
s = "hello"
chars = ['h', 'e', 'l', 'l', 'o']

left finds 'e'; right finds 'o'.
Swap them:
['h', 'o', 'l', 'l', 'e']

Output: "holle"

EDGE CASES
- No vowels: "rhythm" -> "rhythm"
- One vowel: "cat" -> "cat"
- All vowels: "aei" -> "iea"
- Uppercase vowels: "A-bE" -> "E-bA"
- Empty string: "" -> ""

COMMON INTERVIEW MISTAKES
- Reversing the entire string instead of only vowels.
- Forgetting uppercase vowels.
- Moving pointers without checking the current character.
- Trying to modify s[i] directly; strings are immutable.
- Forgetting to join the character list at the end.

REUSABLE TEMPLATE
left, right = 0, len(chars) - 1
while left < right:
    while left < right and chars[left] not in TARGET:
        left += 1
    while left < right and chars[right] not in TARGET:
        right -= 1
    if left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

SIMILAR PROBLEMS
- Reverse String (LeetCode 344)
- Valid Palindrome (LeetCode 125)
- Sort Vowels in a String (LeetCode 2785)

INTERVIEW TIP
Explain that this is not ordinary reversal. The two pointers skip all non-vowels
and swap only vowels, preserving every other character's position.
"""


# Approach 1: Brute force — collect vowels, reverse, and replace.
def reverse_vowels_brute(s):
    vowels = [char for char in s if char in "aeiouAEIOU"][::-1]
    result = []
    vowel_index = 0

    for char in s:
        if char in "aeiouAEIOU":
            result.append(vowels[vowel_index])
            vowel_index += 1
        else:
            result.append(char)

    return "".join(result)


# Approach 2: Better — track vowel positions and assign reversed vowels.
def reverse_vowels_better(s):
    chars = list(s)
    positions = [i for i, char in enumerate(chars) if char in "aeiouAEIOU"]
    vowels = [chars[i] for i in positions]

    for i, position in enumerate(positions):
        chars[position] = vowels[len(vowels) - 1 - i]

    return "".join(chars)


# Approach 3: Optimal / standard — two pointers.
def reverse_vowels_optimal(s):
    chars = list(s)
    vowels = "aeiouAEIOU"
    left, right = 0, len(chars) - 1

    while left < right:
        while left < right and chars[left] not in vowels:
            left += 1

        while left < right and chars[right] not in vowels:
            right -= 1

        if left < right:
            chars[left], chars[right] = chars[right], chars[left]
            left += 1
            right -= 1

    return "".join(chars)


if __name__ == "__main__":
    test_cases = [
        "hello",
        "leetcode",
        "Python",
        "rhythm",
        "cat",
        "aei",
        "A-bE",
        "",
    ]

    for s in test_cases:
        print("Input:", repr(s))
        print("Brute force:", reverse_vowels_brute(s))
        print("Better:", reverse_vowels_better(s))
        print("Optimal:", reverse_vowels_optimal(s))
        print("-" * 30)
