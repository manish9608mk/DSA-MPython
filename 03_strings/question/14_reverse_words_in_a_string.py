# Reverse Words in a String

"""
PROBLEM
Reverse the order of words in s. Remove leading/trailing spaces and keep
exactly one space between words.
Example: "  the sky  is blue  " -> "blue is sky the"

PATTERN
String manipulation + splitting / two pointers.

RECOGNITION TRICKS
- Reverse word order, not characters inside each word.
- Normalize repeated spaces.
- split() without an argument handles repeated whitespace.

REAL-WORLD ANALOGY
Arrange the words in a sentence from last to first.

APPROACH 1 — BRUTE FORCE
Split into words, then build a reversed result using concatenation.
Time: O(n) overall for this Python implementation in typical analysis;
repeated immutable-string concatenation can be O(n^2) worst case.
Space: O(n).

APPROACH 2 — REVERSE THE WORD LIST
Split, reverse the list in place, then join.
Time: O(n).
Space: O(n).

APPROACH 3 — PYTHONIC / STANDARD
Return " ".join(s.split()[::-1]).
Time: O(n).
Space: O(n), because split creates a list and strings are immutable.

WHY THE APPROACH WORKS
split() removes empty fields caused by repeated whitespace. Reversing the
words changes their order; join() inserts exactly one space.

STEP-BY-STEP THINKING
1. Split s into words.
2. Reverse the word list.
3. Join with one space.
4. Return the result.

DRY RUN
"  the sky  is blue  "
split -> ["the", "sky", "is", "blue"]
reverse -> ["blue", "is", "sky", "the"]
join -> "blue is sky the"

EDGE CASES
- Empty string -> ""
- Only spaces -> ""
- One word -> same word
- Repeated, leading, or trailing spaces -> normalized

COMMON INTERVIEW MISTAKES
- Reversing characters instead of word order.
- Using split(" "), which can create empty strings.
- Forgetting strings are immutable.
- Ignoring the exact whitespace rules in the problem.

REUSABLE TEMPLATE
words = s.split()
words.reverse()
answer = " ".join(words)

SIMILAR PROBLEMS
- Reverse Words in a String III
- Reverse String
- String Compression
- Valid Palindrome

INTERVIEW TIP
In Python, split() without an argument handles runs of whitespace, including
spaces, tabs, and newlines. Follow the problem's exact whitespace definition.
"""

def reverse_words_brute(s: str) -> str:
    words = s.split()
    result = ""

    for word in reversed(words):
        if result:
            result += " "
        result += word

    return result


def reverse_words_list(s: str) -> str:
    words = s.split()
    words.reverse()
    return " ".join(words)


def reverse_words_python(s: str) -> str:
    return " ".join(s.split()[::-1])


if __name__ == "__main__":
    s = "  the sky  is blue  "
    print("Brute force:", reverse_words_brute(s))
    print("Reverse list:", reverse_words_list(s))
    print("Pythonic:", reverse_words_python(s))
