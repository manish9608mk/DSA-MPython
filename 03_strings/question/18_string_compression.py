# String Compression

"""
PROBLEM
Given a list of characters, compress it in place:
- For a group of consecutive repeating characters, write the character.
- If the group count is greater than 1, write its digits after the character.
Return the new length. Use O(1) extra space.
Example: ["a","a","b","b","c","c","c"]
After compression: ["a","2","b","2","c","3"], return 6.

PATTERN
Two Pointers + In-place Array Modification + Run-Length Encoding.

RECOGNITION TRICKS
- Consecutive duplicates must be grouped.
- Modify the input list in place.
- Return the length of the compressed prefix.
- Counts may have multiple digits, such as 12.

REAL-WORLD ANALOGY
Instead of writing the same symbol repeatedly, write it once followed by
the number of repetitions.

APPROACH 1 — BRUTE FORCE
Build a separate output list by scanning groups and appending each character
and its count.
Time: O(n).
Space: O(n) for the output list.

APPROACH 2 — BETTER: IN-PLACE READ/WRITE POINTERS
Use read to scan each group and write to store compressed characters in the
same list. Convert counts to digits when count > 1.
Time: O(n).
Space: O(1) auxiliary space.

APPROACH 3 — OPTIMAL / STANDARD
The same in-place read/write approach is optimal for the required O(1)
auxiliary space. Each character is scanned once, and each output character
is written once.
Time: O(n).
Space: O(1) auxiliary space.

WHY THE APPROACH WORKS
The read pointer identifies one complete group. The write pointer stores
its compressed representation. Since write never moves ahead of read,
overwriting does not destroy unread characters.

STEP-BY-STEP THINKING
1. Set read = 0, write = 0, n = len(chars).
2. Save the current character.
3. Move read until the character changes or the list ends.
4. Write the saved character at chars[write].
5. If count > 1, write every digit of str(count).
6. Repeat until read reaches n.
7. Return write. Ignore the list contents after this index.

DRY RUN
Input: ["a","a","b","b","c","c","c"]
Group a: write "a", "2"
Group b: write "b", "2"
Group c: write "c", "3"
Compressed prefix: ["a","2","b","2","c","3"]
Return 6.

EDGE CASES
- Empty list -> 0
- One character -> length 1
- No repeated characters -> original length
- One group, e.g. ["x","x","x"] -> ["x","3"]
- Count >= 10 -> write all count digits, e.g. "12"

COMMON INTERVIEW MISTAKES
- Writing the count when it is 1.
- Writing a multi-digit count as one list element.
- Returning len(chars) instead of the write pointer.
- Using extra space in the required in-place solution.
- Counting non-consecutive equal characters as one group.

REUSABLE TEMPLATE
while read < n:
    start = read
    while read < n and chars[read] == chars[start]:
        read += 1
    count = read - start
    chars[write] = chars[start]
    write += 1
    if count > 1:
        for digit in str(count):
            chars[write] = digit
            write += 1

SIMILAR PROBLEMS
- Remove Duplicates from Sorted Array
- Move Zeroes
- Run Length Encoding
- Remove Element

INTERVIEW TIP
Clarify that the returned integer is the length of the valid compressed
prefix. The input list may contain leftover characters after that prefix.
"""

from typing import List


def compress_brute(chars: List[str]) -> int:
    result = []
    read = 0
    n = len(chars)

    while read < n:
        start = read
        current = chars[read]

        while read < n and chars[read] == current:
            read += 1

        count = read - start
        result.append(current)

        if count > 1:
            result.extend(str(count))

    chars[:len(result)] = result
    return len(result)


def compress_in_place(chars: List[str]) -> int:
    read = write = 0
    n = len(chars)

    while read < n:
        start = read
        current = chars[read]

        while read < n and chars[read] == current:
            read += 1

        count = read - start
        chars[write] = current
        write += 1

        if count > 1:
            for digit in str(count):
                chars[write] = digit
                write += 1

    return write


def compress_optimal(chars: List[str]) -> int:
    # The standard in-place read/write solution is already optimal.
    return compress_in_place(chars)


if __name__ == "__main__":
    tests = [
        ["a", "a", "b", "b", "c", "c", "c"],
        ["a"],
        ["a", "b", "c"],
        ["x"] * 12,
        [],
    ]

    for original in tests:
        brute = original.copy()
        optimal = original.copy()

        brute_length = compress_brute(brute)
        optimal_length = compress_optimal(optimal)

        print("Input:", original)
        print("Brute:", brute[:brute_length], "length =", brute_length)
        print("Optimal:", optimal[:optimal_length], "length =", optimal_length)
        print()
