# 242. Valid Anagram

"""
PROBLEM

Given two strings s and t, return True if t is an anagram of s.

An anagram uses every character from the first string exactly once,
but the order of the characters may be different.

Examples:
    s = "anagram", t = "nagaram" -> True
    s = "rat", t = "car" -> False

Link:
https://leetcode.com/problems/valid-anagram/


PATTERN

Hashing / Frequency Counting / Sorting

Same characters + same frequency + different order allowed
                         ↓
                FREQUENCY COUNTING
                         ↓
                 HASH MAP / DICTIONARY


RECOGNITION TRICKS

- Same elements or characters with different order -> compare frequencies.
- Need to count occurrences -> Hash Map or Counter.
- A set is not enough when duplicates matter.
- Different lengths immediately mean the strings cannot be anagrams.
- Sorting is a valid alternative, but frequency counting is linear time.


REAL-WORLD ANALOGY

Imagine two bags containing letter tiles.

The bags are anagrams when they contain exactly the same letters
and the same number of each letter, even if the tiles are arranged
differently.


APPROACH 1 — BRUTE FORCE (MATCH EACH CHARACTER)

For every character in s:
    Find one unused matching character in t.
    Mark that position as used.

If a character cannot be matched, return False.

Why it works:
    It tries to match every occurrence exactly once.

Why it is inefficient:
    For each character, we may scan the entire second string.

Time: O(n^2)
Space: O(n) for the used array.


APPROACH 2 — BETTER APPROACH (SORTING)

Sort both strings and compare them.

Why it works:
    Sorting puts the same characters in the same order.
    Anagrams therefore produce identical sorted strings.

Time: O(n log n)
Space: O(n) for sorted copies in Python.


APPROACH 3 — OPTIMAL / STANDARD (FREQUENCY HASH MAP)

Count every character in s.
Then subtract every character in t.

If every character has frequency zero at the end,
both strings contain exactly the same characters in the same quantities.

Time: O(n)
Space: O(k), where k is the number of distinct characters.

For a fixed-size alphabet, auxiliary space can be O(1).


WHY FREQUENCY COUNTING WORKS

Anagrams must contain every character the same number of times.

The dictionary first records how many times each character occurs in s.
Subtracting the characters of t cancels those occurrences.

If all final counts are zero, the frequency of every character matches.
If even one count is non-zero, the strings are not anagrams.


STEP-BY-STEP THINKING

1. If lengths differ, return False.
2. Create an empty frequency dictionary.
3. For every character in s, increase its count.
4. For every character in t:
       - If the character is not in the dictionary, return False.
       - Decrease its count.
       - If its count becomes negative, return False.
5. If all counts are zero, return True.


DRY RUN

s = "anagram"
t = "nagaram"

Count s:

a: 3
n: 1
g: 1
r: 1
m: 1

Subtract t:

n -> 0
a -> 2
g -> 0
a -> 1
r -> 0
a -> 0
m -> 0

All counts are zero.

Output: True


EDGE CASES

- Different lengths: "rat", "cars" -> False
- Same letters with same counts: "aabb", "bbaa" -> True
- Different counts: "aab", "abb" -> False
- Empty strings: "", "" -> True
- Case-sensitive: "A", "a" -> False
- Repeated characters: "listen", "silent" -> True


COMMON INTERVIEW MISTAKES

1. Checking only whether the same distinct characters exist.
   Example: "aab" and "abb" have the same distinct set, but different counts.

2. Using a set.
   A set removes duplicates and loses frequency information.

3. Forgetting the length check.
   Different lengths cannot be anagrams.

4. Ignoring case requirements.
   In this problem, uppercase and lowercase are different characters.

5. Decrementing a character without checking whether it exists.
   A missing character must make the answer False.


REUSABLE TEMPLATE — FREQUENCY COUNTING

counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

for item in other_items:
    counts[item] = counts.get(item, 0) - 1


SIMILAR PROBLEMS

- LeetCode 49: Group Anagrams
- LeetCode 387: First Unique Character in a String
- LeetCode 383: Ransom Note
- LeetCode 438: Find All Anagrams in a String
- LeetCode 451: Sort Characters By Frequency


INTERVIEW TIP

Explain the important property first:

"Two strings are anagrams exactly when every character has the same
frequency in both strings."

Then explain that a dictionary lets us count and compare frequencies
in one pass over each string, giving O(n) time.

Do not say only "I use a dictionary." Explain WHY the dictionary
solves the problem: it preserves duplicate counts.
"""


# APPROACH 1 — BRUTE FORCE
def is_anagram_brute(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    used = [False] * len(t)

    for char in s:
        found = False

        for i in range(len(t)):
            if not used[i] and t[i] == char:
                used[i] = True
                found = True
                break

        if not found:
            return False

    return True


# APPROACH 2 — BETTER: SORTING
def is_anagram_sorting(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)


# APPROACH 3 — OPTIMAL / STANDARD: HASH MAP FREQUENCY COUNTING
def is_anagram_hash_map(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    counts = {}

    for char in s:
        counts[char] = counts.get(char, 0) + 1

    for char in t:
        if char not in counts:
            return False

        counts[char] -= 1

        if counts[char] < 0:
            return False

    return True


# ALTERNATIVE: collections.Counter
from collections import Counter


def is_anagram_counter(s: str, t: str) -> bool:
    return Counter(s) == Counter(t)


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("aabb", "bbaa", True),
        ("aab", "abb", False),
        ("", "", True),
        ("A", "a", False),
        ("listen", "silent", True),
        ("a", "aa", False),
    ]

    for s, t, expected in test_cases:
        brute = is_anagram_brute(s, t)
        sorting = is_anagram_sorting(s, t)
        optimal = is_anagram_hash_map(s, t)
        counter = is_anagram_counter(s, t)

        assert brute == expected
        assert sorting == expected
        assert optimal == expected
        assert counter == expected

        print(f"s={s!r}, t={t!r}")
        print(f"Brute force: {brute}")
        print(f"Sorting:     {sorting}")
        print(f"Hash Map:    {optimal}")
        print(f"Counter:     {counter}")
        print("All approaches passed.\n")


"""
COMPLEXITY SUMMARY

Let n be the length of each string and k be the number of distinct characters.

Approach              Time          Auxiliary Space
Brute force           O(n^2)        O(n)
Sorting               O(n log n)    O(n)
Hash Map              O(n)          O(k)
Counter               O(n)          O(k)


INTERVIEW EXPLANATION (SAY THIS OUT LOUD)

"First, I compare the lengths. If they are different, the strings
cannot be anagrams.

Then I count every character of the first string in a dictionary.
I traverse the second string and decrease the corresponding count.
If a character is missing or a count becomes negative, the strings
cannot be anagrams.

If the traversal finishes successfully, the character frequencies
match, so I return True.

The time complexity is O(n), and the auxiliary space is O(k),
where k is the number of distinct characters."


PATTERN MEMORY

Same characters?
    ↓
Order does not matter?
    ↓
Repeated characters matter?
    ↓
Frequency Counting
    ↓
Hash Map / Dictionary


REVISION CHECKLIST

[ ] Explain why a set is not sufficient.
[ ] Explain why sorting works.
[ ] Write the frequency-map solution without looking.
[ ] Explain why different lengths return False.
[ ] Dry-run "aab" and "abb".
[ ] State time and auxiliary space complexity.
[ ] Explain the solution clearly in under two minutes.
"""
