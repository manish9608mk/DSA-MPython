# 08. ISOMORPHIC STRINGS

# LeetCode 205: https://leetcode.com

# PATTERN: Bidirectional Hash Map (One-to-One Character Bijection)

"""
PROBLEM
-------
Given two strings s and t, determine if they are isomorphic.
Two strings s and t are isomorphic if the characters in s can be replaced
to get t.
All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same
character, but a character may map to itself.

Example:
s = "egg", t = "add"
Output = True

s = "foo", t = "bar"
Output = False

s = "paper", t = "title"
Output = True

RECOGNITION
-----------
- "One-to-one character replacement" -> Bijection between two sets.
- Checking s -> t alone fails when two characters in s map to the same char in t.
- Requires two Hash Maps (s -> t and t -> s) or first-occurrence index encoding.

REAL-WORLD ANALOGY
------------------
A simple substitution cipher where every letter is replaced by a unique
code letter. You cannot assign two different plain letters to the same cipher
letter, or decoding becomes ambiguous.

APPROACH 1: BRUTE FORCE NESTED INDEX CHECK
------------------------------------------
For every pair of indices (i, j), verify that s[i] == s[j] if and only if
t[i] == t[j].
Time: O(n^2), where n is the length of the strings.
Space: O(1) extra space.

APPROACH 2: TWO HASH MAPS (RECOMMENDED)
---------------------------------------
1. If len(s) != len(t), return False immediately.
2. Maintain two dictionaries: s_to_t and t_to_s.
3. Iterate through pairs (c1, c2) in zip(s, t):
   - If c1 in s_to_t and s_to_t[c1] != c2 -> return False.
   - If c2 in t_to_s and t_to_s[c2] != c1 -> return False.
   - Record s_to_t[c1] = c2 and t_to_s[c2] = c1.
4. Return True if all pairs succeed.

Time: O(n).
Space: O(1) (bounded by character set size, at most 256 ASCII characters).

APPROACH 3: FIRST-OCCURRENCE INDEX PATTERN TRANSFORMATION
---------------------------------------------------------
Map every character in a string to the index of its first appearance.
For example, "egg" -> [0, 1, 1] and "add" ->.
Compare the transformed index sequences for s and t.
Time: O(n).
Space: O(n) to build the transformed index lists.

APPROACH 4: ZIP SET CARDINALITY TRICK
-------------------------------------
Check if len(set(s)) == len(set(t)) == len(set(zip(s, t))) (after checking
equal lengths).
Time: O(n).
Space: O(n) for storing pairs in a set.

WHY THE RECOMMENDED APPROACH WORKS
----------------------------------
A valid isomorphism requires a bijection (both injective and surjective on the
characters present). Checking s_to_t guarantees each char in s maps to only
one char in t. Checking t_to_s guarantees no two chars in s claim the same
target char in t.

INTERVIEW THINKING
------------------
1. First check if lengths match; different lengths can never be isomorphic.
2. One dictionary (s -> t) is a trap because "badc" and "baba" would pass
   if we don't block both 'b' and 'd' from mapping to 'b'.
3. Using two maps (s_to_t and t_to_s) enforces strict 1-to-1 mapping in O(n).

DRY RUN
-------
s = "badc", t = "baba"

Step 1: c1='b', c2='b' -> s_to_t={'b':'b'}, t_to_s={'b':'b'}
Step 2: c1='a', c2='a' -> s_to_t={'b':'b', 'a':'a'}, t_to_s={'b':'b', 'a':'a'}
Step 3: c1='d', c2='b' -> 'd' not in s_to_t, BUT 'b' IS in t_to_s and
        t_to_s['b'] == 'b' != 'd' -> Conflict! Return False.

EDGE CASES
----------
- Different string lengths -> return False.
- Empty strings "" and "" -> return True.
- Character mapping to itself ("abc", "abc") -> valid, return True.
- Many-to-one violation ("ab", "aa") -> return False.
- One-to-many violation ("aa", "ab") -> return False.
- Non-letter ASCII characters like spaces, digits, or symbols.

COMMON MISTAKES
---------------
1. Using only ONE hash map (s_to_t) and failing cases like s="ab", t="aa".
2. Assuming characters cannot map to themselves (the problem explicitly allows it).
3. Assuming input only contains lowercase 'a'-'z' (LeetCode 205 allows any
   valid ASCII character).

REUSABLE TEMPLATE
-----------------
s_to_t, t_to_s = {}, {}
for c1, c2 in zip(s, t):
    if (c1 in s_to_t and s_to_t[c1] != c2) or (c2 in t_to_s and t_to_s[c2] != c1):
        return False
    s_to_t[c1] = c2
    t_to_s[c2] = c1
return True

PYTHON 3 IMPLEMENTATIONS
========================
"""


# APPROACH 1: Brute force pairwise index equivalence.
def is_isomorphic_brute_force(s, t):
    if len(s) != len(t):
        return False
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n):
            if (s[i] == s[j]) != (t[i] == t[j]):
                return False
    return True


# APPROACH 2: Two Hash Maps for bidirectional mapping (recommended).
def is_isomorphic_two_maps(s, t):
    if len(s) != len(t):
        return False

    s_to_t = {}
    t_to_s = {}

    for c1, c2 in zip(s, t):
        if c1 in s_to_t and s_to_t[c1] != c2:
            return False
        if c2 in t_to_s and t_to_s[c2] != c1:
            return False

        s_to_t[c1] = c2
        t_to_s[c2] = c1

    return True


# APPROACH 3: First-occurrence index normalization.
def is_isomorphic_first_index(s, t):
    if len(s) != len(t):
        return False

    def encode(word):
        first_seen = {}
        pattern = []
        for idx, char in enumerate(word):
            if char not in first_seen:
                first_seen[char] = idx
            pattern.append(first_seen[char])
        return pattern

    return encode(s) == encode(t)


# APPROACH 4: Set cardinality check.
def is_isomorphic_set_zip(s, t):
    if len(s) != len(t):
        return False
    return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


def run_tests():
    tests = [
        ("egg", "add", True),
        ("foo", "bar", False),
        ("paper", "title", True),
        ("badc", "baba", False),
        ("ab", "aa", False),
        ("aa", "ab", False),
        ("", "", True),
        ("a", "b", True),
        ("13", "42", True),
    ]

    solutions = [
        is_isomorphic_brute_force,
        is_isomorphic_two_maps,
        is_isomorphic_first_index,
        is_isomorphic_set_zip,
    ]

    for s, t, expected in tests:
        for solution in solutions:
            actual = solution(s, t)
            assert actual == expected, (
                f"{solution.__name__}: expected {expected}, got {actual}"
            )

    print("All test cases passed for all 4 approaches.")


if __name__ == "__main__":
    run_tests()


"""
COMPLEXITY SUMMARY
------------------
Let n = length of strings s and t, k = size of character set (<= 256 ASCII).

Approach                    Time        Extra space
Brute force pairwise        O(n^2)      O(1)
Two Hash Maps               O(n)        O(k) -> O(1) for ASCII
First-index encoding        O(n)        O(n)
Zip set cardinality         O(n)        O(n)

Two Hash Maps is the cleanest and most space-efficient linear solution because
it stops early on the first mismatch without allocating O(n) auxiliary arrays.

INTERVIEWER EXPLANATION
----------------------
"To check if two strings are isomorphic, I need a one-to-one mapping between
characters in s and characters in t. A single dictionary isn't enough because
two different characters in s might try to map to the same character in t.
So I maintain two Hash Maps—one from s to t and one from t to s—checking for
conflicts at each index. This runs in O(n) time and O(1) space for fixed ASCII."

RELATED PROBLEMS
----------------
- LeetCode 290: Word Pattern
- LeetCode 890: Find and Replace Pattern
- LeetCode 242: Valid Anagram
- LeetCode 1153: String Transforms Into Another String

PATTERN MEMORY
--------------
Isomorphic Strings:
Two Hash Maps (s -> t and t -> s) -> verify bijection -> no collisions.

REVISION CHECKLIST
------------------
[ ] Explain why one Hash Map fails (many-to-one collision).
[ ] Implement the two-map bijection check cleanly.
[ ] Explain the first-occurrence index encoding alternative.
[ ] Handle unequal string lengths and ASCII characters.
[ ] State O(n) time and O(1) character-set space complexity.
[ ] Explain the solution in 30-60 seconds.
"""
