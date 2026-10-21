# Reverse String

"""
PROBLEM
Given a string s, return its characters in reverse order.
Example: "hello" -> "olleh"

PATTERN
String traversal / two pointers.

RECOGNITION TRICKS
- "Reverse a string" -> consider slicing first.
- If asked to reverse in place or avoid a separate result string -> two pointers.
- Python strings are immutable; list(s) is needed for character swaps.

REAL-WORLD ANALOGY
Read a word from its last character to its first character.
For the two-pointer method, swap the first and last cards, then move inward.

APPROACH 1 — BRUTE FORCE
Build the answer by visiting characters from right to left.
Repeated string concatenation can take O(n^2) time in the worst case.
Time: O(n^2) worst case; extra space: O(n).

APPROACH 2 — PYTHON SHORTCUT
Use s[::-1].
Time: O(n); extra space: O(n) for the new string.

APPROACH 3 — TWO POINTERS
Convert the string to a list, then swap the leftmost and rightmost characters.
Move both pointers inward until they meet or cross.
Time: O(n); extra space: O(n) for list(s).
The swap process itself uses O(1) extra space after conversion.

WHY THE TWO-POINTER APPROACH WORKS
Each swap puts two characters into their final reversed positions.
Move inward after each swap. When pointers meet or cross, every pair is correct.

STEP-BY-STEP THINKING
1. The first character must become the last.
2. The last character must become the first.
3. Swap them.
4. Repeat for the next pair toward the center.
5. Join the list into a string and return it.

DRY RUN
s = "code"
chars = ['c', 'o', 'd', 'e']
Swap c and e -> ['e', 'o', 'd', 'c']
Swap o and d -> ['e', 'd', 'o', 'c']
Answer: "edoc"

EDGE CASES
- Empty string: "" -> ""
- One character: "a" -> "a"
- Repeated characters: "aaaa" -> "aaaa"
- Spaces and letter case are preserved; only character order changes.

COMMON INTERVIEW MISTAKES
- Trying to assign s[0] = ...; strings are immutable.
- Forgetting that right starts at len(chars) - 1.
- Using while left <= right; the middle character does not need a swap.
- Claiming repeated concatenation is always O(n).
- Claiming O(1) extra space for list(s); converting to a list takes O(n).

REUSABLE TEMPLATE
left, right = 0, len(items) - 1
while left < right:
    items[left], items[right] = items[right], items[left]
    left += 1
    right -= 1

SIMILAR PROBLEMS
- Reverse String (LeetCode 344: mutable character array)
- Reverse Vowels of a String (LeetCode 345)
- Valid Palindrome (LeetCode 125)

INTERVIEW TIP
For a Python string, explain slicing first. If asked to show the algorithm,
explain two pointers and why each swap puts a pair in its final position.
"""


# Approach 1: Brute force — build from right to left.
def reverse_brute(s):
    result = ""
    for i in range(len(s) - 1, -1, -1):
        result += s[i]
    return result


# Approach 2: Python slicing.
def reverse_slicing(s):
    return s[::-1]


# Approach 3: Two pointers on a mutable list.
def reverse_two_pointers(s):
    chars = list(s)
    left, right = 0, len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1

    return "".join(chars)


if __name__ == "__main__":
    s = "code"

    print("Input:", s)
    print("Brute force:", reverse_brute(s))
    print("Slicing:", reverse_slicing(s))
    print("Two pointers:", reverse_two_pointers(s))

    # Edge cases
    print("Empty string:", repr(reverse_two_pointers("")))
    print("One character:", reverse_two_pointers("a"))
