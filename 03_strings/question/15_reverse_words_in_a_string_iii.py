# Reverse Words in a String III

"""
PROBLEM
Reverse the characters of each word, keeping word order and spaces unchanged.
Example: "Let's take LeetCode contest" -> "s'teL ekat edoCteeL tsetnoc"

PATTERN
String manipulation + two pointers.

RECOGNITION TRICKS
- Reverse each word independently.
- Word order remains unchanged.
- Spaces stay in their original positions.

REAL-WORLD ANALOGY
Keep each word in place, but write its letters backward.

APPROACH 1 — BRUTE FORCE
Split using the exact space separator, reverse each word with slicing, join.
Time: O(n). Space: O(n).

APPROACH 2 — TWO POINTERS
Convert to a character list. Find each word's boundaries and reverse that
range in place using left and right pointers.
Time: O(n). Space: O(n) for the character list; O(1) auxiliary per reversal.

APPROACH 3 — PYTHONIC / STANDARD
Use split(" "), reverse each part with slicing, and join with " ".
Time: O(n). Space: O(n).
This has the same core operation as approach 1; it is the concise Python form.

WHY THE APPROACH WORKS
A word is a continuous range between spaces. Reversing only that range
preserves the order of words and the original spaces.

STEP-BY-STEP THINKING
1. Convert s to a list of characters.
2. Scan until a space or the end.
3. Reverse the current word using two pointers.
4. Continue with the next word.
5. Join the character list.

DRY RUN
"Let's take"
"Let's" -> "s'teL"
"take" -> "ekat"
Result -> "s'teL ekat"

EDGE CASES
- Empty string -> ""
- One word -> reverse it
- Multiple spaces -> preserve them
- Leading/trailing spaces -> preserve them
- One-character words -> unchanged

COMMON INTERVIEW MISTAKES
- Reversing the order of words instead of each word's characters.
- Collapsing repeated spaces.
- Letting a pointer cross a space.
- Forgetting the final word when no trailing space exists.

REUSABLE TEMPLATE
while left < right:
    chars[left], chars[right] = chars[right], chars[left]
    left += 1
    right -= 1

SIMILAR PROBLEMS
- Reverse Words in a String
- Reverse String
- Reverse Vowels of a String
- String Compression

INTERVIEW TIP
In this problem, word order stays the same. Only characters inside each word
are reversed. Use split(" ") if exact spaces must be preserved.
"""

def reverse_words_brute(s: str) -> str:
    return " ".join(word[::-1] for word in s.split(" "))


def reverse_words_two_pointers(s: str) -> str:
    chars = list(s)
    start = 0

    for end in range(len(chars) + 1):
        if end == len(chars) or chars[end] == " ":
            left, right = start, end - 1

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

            start = end + 1

    return "".join(chars)


def reverse_words_python(s: str) -> str:
    return " ".join(word[::-1] for word in s.split(" "))


if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print("Brute force:", reverse_words_brute(s))
    print("Two pointers:", reverse_words_two_pointers(s))
    print("Pythonic:", reverse_words_python(s))
