# String to Integer (atoi)

"""
PROBLEM
Implement myAtoi(s), converting a string to a 32-bit signed integer.

Rules:
1. Ignore leading whitespace.
2. Read an optional '+' or '-' sign.
3. Read digits until a non-digit character appears.
4. If no digit is read, return 0.
5. Clamp the result to [-2**31, 2**31 - 1].

Examples:
"42" -> 42
"   -42" -> -42
"4193 with words" -> 4193
"words and 987" -> 0
"-91283472332" -> -2147483648

PATTERN
String traversal / parsing / boundary checking.

RECOGNITION TRICKS
- Convert text according to strict step-by-step rules -> parsing.
- Stop at the first invalid character after digits begin.
- A sign is valid only before digits.
- Clamp the answer to a fixed numeric range.

REAL-WORLD ANALOGY
Read a number from a line of text. Ignore spaces at the start, accept one sign,
then read digits until the first character that cannot belong to the number.

APPROACH 1 — BRUTE FORCE / BUILT-IN CONVERSION
Extract the leading signed digit sequence with a regular expression, then use
int(). This is concise, but still needs prefix extraction and clamping.
Time: O(n); extra space: O(n).

APPROACH 2 — BETTER APPROACH
Use strip() and a regular expression to extract a leading signed digit sequence,
then convert it and clamp the value.
Time: O(n); extra space: O(n).
This is concise but relies on regular expressions and integer conversion.

APPROACH 3 — OPTIMAL / STANDARD (MANUAL PARSING)
Scan the original string directly: skip leading whitespace, read the sign,
and accumulate digits. Clamp the result to the 32-bit signed range.
Time: O(n); auxiliary space: O(1).

WHY MANUAL PARSING WORKS
The rules specify which characters are valid at each stage. Processing them
in order prevents accepting signs in the middle or digits after an invalid
character. Each digit updates value = value * 10 + digit.

STEP-BY-STEP THINKING
1. Skip leading whitespace.
2. If the next character is '+' or '-', record the sign and move forward.
3. Read digits while the current character is a digit.
4. Update value = value * 10 + digit.
5. Stop at the first non-digit.
6. Apply the sign.
7. Clamp the result to the 32-bit signed range.

DRY RUN
s = "   -42xyz"
Skip spaces -> "-42xyz"
Read '-' -> sign = -1
Read '4' -> value = 4
Read '2' -> value = 42
Read 'x' -> stop
Apply sign -> -42

Output: -42

EDGE CASES
- Leading spaces: "   42" -> 42
- Sign only: "+" -> 0
- No digits: "words 12" -> 0
- Digits then words: "12abc" -> 12
- Decimal point: "3.14" -> 3
- Positive overflow -> 2147483647
- Negative overflow -> -2147483648

COMMON INTERVIEW MISTAKES
- Calling int(s) on the entire input.
- Accepting a sign after digits have started.
- Continuing after the first non-digit.
- Forgetting the 32-bit clamp.
- Forgetting that a sign without digits returns 0.

REUSABLE TEMPLATE
i = 0
while i < len(s) and s[i].isspace():
    i += 1

sign = 1
if i < len(s) and s[i] in "+-":
    sign = -1 if s[i] == "-" else 1
    i += 1

value = 0
while i < len(s) and s[i].isdigit():
    value = value * 10 + int(s[i])
    i += 1

SIMILAR PROBLEMS
- String to Integer (atoi) (LeetCode 8)
- Valid Number (LeetCode 65)
- Basic Calculator II (LeetCode 227)

INTERVIEW TIP
Follow the parsing rules in order. Mention stopping at the first non-digit
and clamping to the 32-bit signed integer range.
"""

import re


def clamp_32_bit(value):
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1
    return max(INT_MIN, min(value, INT_MAX))


# Approach 1: Extract a valid prefix, then use int().
def my_atoi_brute(s):
    match = re.match(r"\\s*[+-]?\\d+", s)
    if not match:
        return 0
    return clamp_32_bit(int(match.group().strip()))


# Approach 2: Regex with a capture group.
def my_atoi_better(s):
    match = re.match(r"\\s*([+-]?\\d+)", s)
    if not match:
        return 0
    return clamp_32_bit(int(match.group(1)))


# Approach 3: Optimal / standard — manual parsing.
def my_atoi_optimal(s):
    INT_MIN = -(2**31)
    INT_MAX = 2**31 - 1
    i = 0
    n = len(s)

    while i < n and s[i].isspace():
        i += 1

    sign = 1
    if i < n and s[i] in "+-":
        if s[i] == "-":
            sign = -1
        i += 1

    value = 0

    while i < n and s[i].isdigit():
        digit = int(s[i])
        value = value * 10 + digit
        i += 1

        if sign == 1 and value > INT_MAX:
            return INT_MAX
        if sign == -1 and -value < INT_MIN:
            return INT_MIN

    return sign * value


if __name__ == "__main__":
    test_cases = [
        "42", "   -42", "4193 with words", "words and 987",
        "-91283472332", "+", "12abc", "3.14",
        "99999999999", "-99999999999",
    ]

    for s in test_cases:
        print("Input:", repr(s))
        print("Prefix + int:", my_atoi_brute(s))
        print("Regex:", my_atoi_better(s))
        print("Manual parsing:", my_atoi_optimal(s))
        print("-" * 35)
