# 09. WORD PATTERN

# LeetCode 290: https://leetcode.com

# PATTERN: Bidirectional Hash Map (Char <-> Word Bijection)

"""
PROBLEM
-------
Given a pattern and a string s, find if s follows the same pattern.
Here follow means a full match, such that there is a bijection between a
letter in pattern and a non-empty word in s.

Example:
pattern = "abba", s = "dog cat cat dog"
Output = True

pattern = "abba", s = "dog cat cat fish"
Output = False

pattern = "aaaa", s = "dog cat cat dog"
Output = False

RECOGNITION
-----------
- "Bijection between letter and word" -> Two-way 1-to-1 mapping.
- Direct extension of Isomorphic Strings (LeetCode 205), replacing target
  characters with space-separated words.
- Must verify both char -> word and word -> char to avoid collisions.

REAL-WORLD ANALOGY
------------------
Assigning secret code letters to action words in a military radio protocol:
'A' stands for "attack", 'B' stands for "retreat". Each letter must represent
only one word, and no two letters can mean the same word.

APPROACH 1: BRUTE FORCE NESTED COMPARISON
-----------------------------------------
Split s into words. If len(pattern) != len(words), return False.
For every pair of indices (i, j), check that pattern[i] == pattern[j]
if and only if words[i] == words[j].
Time: O(n^2 * L), where n is number of words and L is average word length.
Space: O(n * L) to store the split list of words.

APPROACH 2: TWO HASH MAPS (RECOMMENDED)
---------------------------------------
1. Split s by spaces into a list of words.
2. If len(pattern) != len(words), return False immediately.
3. Maintain two dictionaries: char_to_word and word_to_char.
4. Iterate through (ch, word) in zip(pattern, words):
   - If ch in char_to_word and char_to_word[ch] != word -> return False.
   - If word in word_to_char and word_to_char[word] != ch -> return False.
   - Store char_to_word[ch] = word and word_to_char[word] = ch.
5. Return True.

Time: O(n + m), where n = len(pattern) and m = len(s).
Space: O(m) for storing split words and dictionary keys.

APPROACH 3: SINGLE INDEX-MAPPING HASH MAP
-----------------------------------------
Map both ('char', ch) and ('word', word) to their first seen index in a
single dictionary. If their first seen indices ever differ, return False.
Using tagged tuples prevents collisions when a word is a single letter
(e.g., pattern = "ab", s = "b a").
Time: O(n + m).
Space: O(m).

APPROACH 4: ZIP SET CARDINALITY
-------------------------------
After splitting s and checking equal length, verify:
len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words))).
Time: O(n + m).
Space: O(m).

WHY THE RECOMMENDED APPROACH WORKS
----------------------------------
A bijection requires that every character maps to a unique word AND every
word maps back to a unique character. Using two separate dictionaries
prevents both one-to-many mismatches (e.g., 'a' -> "dog" and 'a' -> "cat")
and many-to-one mismatches (e.g., 'a' -> "dog" and 'b' -> "dog").

INTERVIEW THINKING
------------------
1. Split s into words first and check if word count matches pattern length.
2. Just like Isomorphic Strings, one dictionary fails when two different
   pattern letters map to the same word ("ab" vs "dog dog").
3. Maintain char_to_word and word_to_char dictionaries and fail fast on any
   contradiction.

DRY RUN
-------
pattern = "abba", s = "dog cat cat fish"

Split words = ["dog", "cat", "cat", "fish"] (length 4 == len(pattern))

Step 1: ch='a', word="dog" -> char_to_word={'a':"dog"}, word_to_char={"dog":'a'}
Step 2: ch='b', word="cat" -> char_to_word={'a':"dog", 'b':"cat"},
        word_to_char={"dog":'a', "cat":'b'}
Step 3: ch='b', word="cat" -> matches existing mappings.
Step 4: ch='a', word="fish" -> 'a' is in char_to_word, but "dog" != "fish".
        Mismatch! Return False.

EDGE CASES
----------
- Number of words in s does not match length of pattern -> return False.
- Single-letter words matching pattern letters (e.g., pattern="ab", s="b a").
- All pattern characters identical, different words ("aaaa", "dog cat cat dog").
- Different pattern characters, identical words ("abba", "dog dog dog dog").
- Single character pattern and single word ("a", "dog") -> return True.

COMMON MISTAKES
---------------
1. Forgetting to check len(pattern) != len(words) before zipping (zip stops
   at the shorter iterable and can give a false positive).
2. Using only one Hash Map (char_to_word) and failing many-to-one cases.
3. Using a single Hash Map without tagging keys, causing a bug when a word
   equals a pattern letter (e.g., ch='a' and word="a").

REUSABLE TEMPLATE
-----------------
words = s.split()
if len(pattern) != len(words):
    return False
c2w, w2c = {}, {}
for ch, w in zip(pattern, words):
    if (ch in c2w and c2w[ch] != w) or (w in w2c and w2c[w] != ch):
        return False
    c2w[ch] = w
    w2c[w] = ch
return True

PYTHON 3 IMPLEMENTATIONS
========================
"""


# APPROACH 1: Brute force pairwise index equivalence.
def word_pattern_brute_force(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    n = len(pattern)
    for i in range(n):
        for j in range(i + 1, n):
            if (pattern[i] == pattern[j]) != (words[i] == words[j]):
                return False
    return True


# APPROACH 2: Two Hash Maps for bidirectional mapping (recommended).
def word_pattern_two_maps(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    char_to_word = {}
    word_to_char = {}

    for ch, word in zip(pattern, words):
        if ch in char_to_word and char_to_word[ch] != word:
            return False
        if word in word_to_char and word_to_char[word] != ch:
            return False

        char_to_word[ch] = word
        word_to_char[word] = ch

    return True


# APPROACH 3: Single Hash Map with tagged first-occurrence indices.
def word_pattern_single_index_map(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False

    first_index = {}
    for idx, (ch, word) in enumerate(zip(pattern, words)):
        char_key = ("c", ch)
        word_key = ("w", word)
        if first_index.setdefault(char_key, idx) != first_index.setdefault(word_key, idx):
            return False
    return True


# APPROACH 4: Set cardinality check.
def word_pattern_set_zip(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    return len(set(pattern)) == len(set(words)) == len(set(zip(pattern, words)))


def run_tests():
    tests = [
        ("abba", "dog cat cat dog", True),
        ("abba", "dog cat cat fish", False),
        ("aaaa", "dog cat cat dog", False),
        ("abba", "dog dog dog dog", False),
        ("aaa", "aa aa aa aa", False),
        ("ab", "b a", True),
        ("a", "dog", True),
    ]

    solutions = [
        word_pattern_brute_force,
        word_pattern_two_maps,
        word_pattern_single_index_map,
        word_pattern_set_zip,
    ]

    for pattern, s, expected in tests:
        for solution in solutions:
            actual = solution(pattern, s)
            assert actual == expected, (
                f"{solution.__name__}: expected {expected}, got {actual}"
            )

    print("All test cases passed for all 4 approaches.")


if __name__ == "__main__":
    run_tests()


"""
COMPLEXITY SUMMARY
------------------
Let n = length of pattern, m = length of string s.

Approach                    Time            Extra space
Brute force pairwise        O(n^2 * L)      O(m)
Two Hash Maps               O(n + m)        O(m)
Single tagged index map     O(n + m)        O(m)
Zip set cardinality         O(n + m)        O(m)

Two Hash Maps is the clearest and easiest to explain in an interview, with
early termination on the first mismatch.

INTERVIEWER EXPLANATION
----------------------
"First, I split the string s into words and check if the word count matches
the pattern length. Because we need a strict bijection, I use two Hash Maps:
one mapping pattern characters to words, and another mapping words back to
characters. If any character or word conflicts with an existing mapping, I
return False immediately. This runs in O(n + m) time and O(m) space."

RELATED PROBLEMS
----------------
- LeetCode 205: Isomorphic Strings
- LeetCode 890: Find and Replace Pattern
- LeetCode 291: Word Pattern II (Backtracking + Hash Map)
- LeetCode 242: Valid Anagram

PATTERN MEMORY
--------------
Word Pattern:
Split s -> check length match -> Two Hash Maps (char <-> word) -> verify 1-to-1.

REVISION CHECKLIST
------------------
[ ] Check len(pattern) == len(words) before zipping.
[ ] Explain why two maps are needed instead of one.
[ ] Explain the single-map collision bug if keys are untagged.
[ ] Walk through a failing example ("abba" vs "dog dog dog dog").
[ ] State O(n + m) time and O(m) space complexity.
[ ] Explain the solution in 30-60 seconds.
"""
