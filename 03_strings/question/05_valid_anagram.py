# Valid Anagram

"""
PROBLEM
Given two strings s and t, return True if t is an anagram of s.
An anagram uses every character from the first string exactly once,
but the character order may be different.

Examples:
"anagram", "nagaram" -> True
"rat", "car" -> False

PATTERN
Hashing / frequency counting / sorting.

RECOGNITION TRICKS
- Same characters with the same counts, but possibly different order -> anagram.
- Need to count occurrences -> dictionary or Counter.
- If sorting is allowed, compare sorted strings.
- Different lengths immediately mean the strings cannot be anagrams.

REAL-WORLD ANALOGY
Two bags contain letter tiles. They are anagrams if both bags contain
exactly the same letters in the same quantities, regardless of order.

APPROACH 1 — BRUTE FORCE
For each character in s, find one matching unused character in t.
Mark that character as used so it cannot be matched twice.
Time: O(n^2); extra space: O(n) for the used markers.

APPROACH 2 — BETTER APPROACH (SORTING)
Sort both strings and compare the sorted results.
Time: O(n log n); extra space: O(n) for sorted copies.

APPROACH 3 — OPTIMAL / STANDARD (FREQUENCY COUNTING)
Count each character in s and subtract each character in t.
If every count ends at zero, the strings are anagrams.
Time: O(n); extra space: O(k), where k is the number of distinct characters.
For a fixed-size alphabet, auxiliary space can be O(1).

WHY FREQUENCY COUNTING WORKS
Anagrams must contain every character the same number of times.
Adding counts from s and subtracting counts from t leaves zero for each
character exactly when their frequencies match.

STEP-BY-STEP THINKING
1. If lengths differ, return False.
2. Create an empty frequency dictionary.
3. Add 1 for every character in s.
4. Subtract 1 for every character in t.
5. If any count becomes negative or the final counts are nonzero, return False.
6. Otherwise, return True.

DRY RUN
s = "anagram", t = "nagaram"

After counting s:
a: 3, n: 1, g: 1, r: 1, m: 1

Subtract characters from t:
Each count becomes zero.

Output: True

EDGE CASES
- Different lengths: "rat", "cars" -> False
- Same characters: "aabb", "bbaa" -> True
- Different counts: "aab", "abb" -> False
- Empty strings: "", "" -> True
- Case matters in this version: "A", "a" -> False

COMMON INTERVIEW MISTAKES
- Checking only distinct characters instead of their counts.
- Forgetting repeated character counts or the length check.
- Assuming uppercase and lowercase are equal when the problem says otherwise.
- Using a set instead of counts; sets lose duplicate information.

REUSABLE TEMPLATE
counts = {}

for char in s:
    counts[char] = counts.get(char, 0) + 1

for char in t:
    counts[char] = counts.get(char, 0) - 1

return all(count == 0 for count in counts.values())

SIMILAR PROBLEMS
- Valid Anagram (LeetCode 242)
- Group Anagrams (LeetCode 49)
- Find All Anagrams in a String (LeetCode 438)

INTERVIEW TIP
Explain that anagrams require equal character frequencies, not just equal
sets of characters. Frequency counting gives linear time without sorting.
"""


# Approach 1: Brute force — match each character once.
def is_anagram_brute(s, t):
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


# Approach 2: Better — sort both strings.
def is_anagram_better(s, t):
    return sorted(s) == sorted(t)


# Approach 3: Optimal / standard — frequency counting.
def is_anagram_optimal(s, t):
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

    return all(count == 0 for count in counts.values())


if __name__ == "__main__":
    test_cases = [
        ("anagram", "nagaram"),
        ("rat", "car"),
        ("aabb", "bbaa"),
        ("aab", "abb"),
        ("", ""),
        ("A", "a"),
        ("rat", "cars"),
    ]

    for s, t in test_cases:
        print("Input:", repr(s), repr(t))
        print("Brute force:", is_anagram_brute(s, t))
        print("Better:", is_anagram_better(s, t))
        print("Optimal:", is_anagram_optimal(s, t))
        print("-" * 30)
