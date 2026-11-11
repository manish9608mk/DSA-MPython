# 383. Ransom Note

"""
PROBLEM

You are given two strings: ransomNote and magazine.

Return True if ransomNote can be constructed using the characters
from magazine.

Each character in magazine can be used only once.

Examples:

    ransomNote = "a", magazine = "b"       -> False
    ransomNote = "aa", magazine = "ab"     -> False
    ransomNote = "aa", magazine = "aab"    -> True

Link:
https://leetcode.com/problems/ransom-note/


PATTERN

Hashing / Frequency Counting / Resource Availability

Need characters from magazine
              ↓
Count available characters
              ↓
Check required characters
              ↓
Decrease available frequency
              ↓
If any requirement is unavailable -> False


RECOGNITION TRICKS

- Need to construct one string from another -> check character availability.
- Each character can be used only once -> track frequencies.
- Repeated characters matter -> use a Hash Map, not a Set.
- One collection supplies resources and another consumes them.
- If the required frequency is greater than the available frequency, return False.


REAL-WORLD ANALOGY

Imagine you have a box of letter tiles (magazine).
You want to create a message (ransomNote).

You can use each tile only once.
If the message needs three 'a' tiles but the box has only two,
you cannot create the message.


APPROACH 1 — BRUTE FORCE (FIND AND REMOVE)

Convert magazine into a mutable list.

For every character in ransomNote:
    Search for that character in the list.
    If it is missing, return False.
    Otherwise remove that occurrence.

Why it works:
    Removing a used character prevents using it again.

Why it is inefficient:
    Searching and removing from a list can take O(n).

Time: O(m * n), where m = len(ransomNote), n = len(magazine).
Space: O(n) for the list.


APPROACH 2 — BETTER APPROACH (SORTING)

Sort both strings.

Use two pointers to match required characters with available characters.
A required character that cannot be matched means the answer is False.

This approach is possible, but it is more complicated than necessary.

Time: O(m log m + n log n)
Space: O(m + n) for sorted copies.


APPROACH 3 — OPTIMAL / STANDARD (FREQUENCY HASH MAP)

Count every character in magazine.

Then process ransomNote:
    - If the required character has no available count, return False.
    - Otherwise decrease its available count.

If every required character is processed, return True.

Time: O(m + n)
Space: O(k), where k is the number of distinct characters.


WHY FREQUENCY COUNTING WORKS

The magazine tells us how many copies of each character are available.

The ransom note tells us how many copies are required.

For every character:

    available frequency >= required frequency

must be true.

We can check this by counting available characters and decreasing
the count whenever a character is used.

If a count becomes negative or the character is missing,
there are not enough copies.


STEP-BY-STEP THINKING

1. Create an empty frequency dictionary.
2. Count all characters in magazine.
3. Visit every character in ransomNote.
4. If its available count is zero or missing, return False.
5. Otherwise decrease its available count by one.
6. If all required characters are processed, return True.


DRY RUN — TRUE CASE

ransomNote = "aa"
magazine = "aab"

Count magazine:

a: 2
b: 1

Process ransomNote:

First 'a':
    available count = 2
    use one 'a'
    remaining count = 1

Second 'a':
    available count = 1
    use one 'a'
    remaining count = 0

All required characters were available.

Output: True


DRY RUN — FALSE CASE

ransomNote = "aa"
magazine = "ab"

Count magazine:

a: 1
b: 1

Process ransomNote:

First 'a':
    available count = 1
    use one 'a'
    remaining count = 0

Second 'a':
    available count = 0
    no 'a' is available

Output: False


EDGE CASES

- Empty ransom note: "", "abc" -> True
- Empty magazine: "a", "" -> False
- Both empty: "", "" -> True
- Not enough repeated characters: "aa", "a" -> False
- Exact available characters: "abc", "cba" -> True
- Extra unused characters: "a", "abc" -> True
- Same character repeated many times: "aaaa", "aaaaa" -> True


COMMON INTERVIEW MISTAKES

1. Using a Set.
   A set loses duplicate counts. "aa" needs two copies of 'a'.

2. Checking only whether a character exists.
   Existence is not enough; we must know how many copies are available.

3. Forgetting to decrease the count.
   Without decreasing it, the same magazine character could be reused.

4. Reversing the roles.
   magazine provides characters; ransomNote consumes them.

5. Returning False only when a character is absent.
   A character can exist but still have too few copies.


REUSABLE TEMPLATE — AVAILABLE FREQUENCY

available = {}

for item in resources:
    available[item] = available.get(item, 0) + 1

for item in requirements:
    if available.get(item, 0) == 0:
        return False

    available[item] -= 1

return True


SIMILAR PROBLEMS

- LeetCode 242: Valid Anagram
- LeetCode 387: First Unique Character in a String
- LeetCode 49: Group Anagrams
- LeetCode 438: Find All Anagrams in a String
- LeetCode 1160: Find Words That Can Be Formed by Characters


INTERVIEW TIP

Explain the difference between the two strings:

"magazine is the supply; ransomNote is the demand."

I count the supply first. Then each required character consumes
one available copy. This naturally handles duplicates and prevents
reusing a character.

The time complexity is O(m + n), because each string is traversed once.
"""


# APPROACH 1 — BRUTE FORCE
def can_construct_brute(ransom_note: str, magazine: str) -> bool:
    available = list(magazine)

    for char in ransom_note:
        if char not in available:
            return False

        available.remove(char)

    return True


# APPROACH 2 — BETTER: SORTING + TWO POINTERS
def can_construct_sorting(ransom_note: str, magazine: str) -> bool:
    required = sorted(ransom_note)
    available = sorted(magazine)

    i = 0
    j = 0

    while i < len(required) and j < len(available):
        if required[i] == available[j]:
            i += 1
            j += 1
        elif required[i] > available[j]:
            j += 1
        else:
            return False

    return i == len(required)


# APPROACH 3 — OPTIMAL: HASH MAP FREQUENCY COUNTING
def can_construct_hash_map(ransom_note: str, magazine: str) -> bool:
    available = {}

    for char in magazine:
        available[char] = available.get(char, 0) + 1

    for char in ransom_note:
        if available.get(char, 0) == 0:
            return False

        available[char] -= 1

    return True


# ALTERNATIVE — collections.Counter
from collections import Counter


def can_construct_counter(ransom_note: str, magazine: str) -> bool:
    required = Counter(ransom_note)
    available = Counter(magazine)

    for char, needed_count in required.items():
        if available[char] < needed_count:
            return False

    return True


if __name__ == "__main__":
    test_cases = [
        ("a", "b", False),
        ("aa", "ab", False),
        ("aa", "aab", True),
        ("", "abc", True),
        ("a", "", False),
        ("", "", True),
        ("abc", "cba", True),
        ("a", "abc", True),
        ("aaaa", "aaaaa", True),
        ("aaa", "aa", False),
    ]

    for ransom_note, magazine, expected in test_cases:
        brute = can_construct_brute(ransom_note, magazine)
        sorting = can_construct_sorting(ransom_note, magazine)
        optimal = can_construct_hash_map(ransom_note, magazine)
        counter = can_construct_counter(ransom_note, magazine)

        assert brute == expected
        assert sorting == expected
        assert optimal == expected
        assert counter == expected

        print(f"ransomNote={ransom_note!r}, magazine={magazine!r}")
        print(f"Brute force: {brute}")
        print(f"Sorting:     {sorting}")
        print(f"Hash Map:    {optimal}")
        print(f"Counter:     {counter}")
        print("All approaches passed.\n")


"""
COMPLEXITY SUMMARY

Let:
    m = len(ransomNote)
    n = len(magazine)
    k = number of distinct characters

Approach              Time              Auxiliary Space
Brute force           O(m * n)          O(n)
Sorting               O(m log m +       O(m + n)
                      n log n)
Hash Map              O(m + n)          O(k)
Counter               O(m + n)          O(k)


INTERVIEW EXPLANATION (SAY THIS OUT LOUD)

"I treat magazine as the available supply of characters.

First, I build a frequency map of magazine. Then I traverse
ransomNote. For each required character, I check whether at least
one copy is available. If not, I return False. Otherwise, I consume
one copy by decreasing its frequency.

If I process the entire ransomNote, I return True.

This handles repeated characters correctly because every use
decreases the available count.

The time complexity is O(m + n), and the auxiliary space is O(k),
where k is the number of distinct characters."


PATTERN MEMORY

One collection provides resources
              +
Another collection consumes resources
              ↓
       FREQUENCY HASH MAP
              ↓
       Count available items
              ↓
       Decrease when used
              ↓
       Missing / zero count -> False


IMPORTANT DIFFERENCE

Valid Anagram:
    Count one string and compare against another.
    Both strings must have exactly equal frequencies.

Ransom Note:
    Count the available magazine characters.
    The ransom note may use only some of them.
    Extra magazine characters are allowed.


REVISION CHECKLIST

[ ] Explain why a Set is not enough.
[ ] Explain why each used character must decrease the count.
[ ] Write the Hash Map solution without looking.
[ ] Dry-run "aa" with "aab".
[ ] Dry-run "aa" with "ab".
[ ] Explain the difference from Valid Anagram.
[ ] State time and auxiliary space complexity.
[ ] Explain the solution clearly in under two minutes.
"""
