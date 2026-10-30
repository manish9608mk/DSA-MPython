# Group Anagrams

"""
PROBLEM
Group words that are anagrams of each other.
Anagrams contain the same characters with the same frequencies.
Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
Possible output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

PATTERN
Hashing + canonical key (sorting or character-frequency counting).

RECOGNITION TRICKS
- If words should be grouped by the same letters, build a canonical key.
- Sorting each word gives an identical key for anagrams.
- For lowercase English letters, a 26-count tuple is also a key.

REAL-WORLD ANALOGY
Put words into the same box when they contain exactly the same letter counts.

APPROACH 1 — BRUTE FORCE
Compare each word with the representative word of every existing group.
Each comparison sorts both words.
Time: O(m^2 * n log n) worst case.
Space: O(m * n) for the output, excluding temporary sorting.

APPROACH 2 — BETTER: SORTED STRING KEY
Sort each word's characters. Anagrams produce the same key.
Time: O(m * n log n), where m is number of words and n is average word length.
Space: O(m * n) for keys and output.

APPROACH 3 — OPTIMAL / STANDARD: FREQUENCY TUPLE KEY
Count the 26 lowercase English letters and use the tuple as a dictionary key.
Time: O(m * (n + 26)) = O(m * n) for lowercase English letters.
Space: O(m * n), including output and keys.
This approach assumes words contain only lowercase English letters.

WHY THE APPROACH WORKS
Two words are anagrams exactly when every character has the same frequency.
So their sorted keys or frequency tuples match.

STEP-BY-STEP THINKING
1. Create a dictionary from key to list of words.
2. For each word, calculate its key.
3. Append the word to the list for that key.
4. Return the dictionary's groups.

DRY RUN
"eat", "tea", and "ate" share sorted key "aet".
"tan" and "nat" share key "ant".
"bat" has key "abt".
The dictionary creates three groups.

EDGE CASES
- Empty input -> []
- One word -> one group
- Duplicate words -> keep every occurrence
- Empty strings -> grouped together
- Uppercase or other characters -> use sorted keys or normalize first

COMMON INTERVIEW MISTAKES
- Using a set of characters as the key; it loses repeated counts ("aab" vs "abb").
- Dropping duplicate words.
- Using a list as a dictionary key instead of a tuple.
- Assuming the 26-count method supports arbitrary characters.

REUSABLE TEMPLATE
key = tuple(counts)
groups.setdefault(key, []).append(word)

SIMILAR PROBLEMS
- Valid Anagram: compare character counts.
- Find All Anagrams in a String: sliding window + frequency counts.
- Sort Characters By Frequency: counting + hashing.

INTERVIEW TIP
Explain why the key identifies an anagram group. Sorted keys are simple;
frequency tuples run in linear time when the alphabet size is fixed.
"""

from collections import defaultdict
from typing import List


def group_anagrams_brute(words: List[str]) -> List[List[str]]:
    groups = []
    representatives = []

    for word in words:
        placed = False
        for index, representative in enumerate(representatives):
            if sorted(word) == sorted(representative):
                groups[index].append(word)
                placed = True
                break

        if not placed:
            representatives.append(word)
            groups.append([word])

    return groups


def group_anagrams_sorted_key(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for word in words:
        key = "".join(sorted(word))
        groups[key].append(word)

    return list(groups.values())


def group_anagrams_frequency_key(words: List[str]) -> List[List[str]]:
    groups = defaultdict(list)

    for word in words:
        counts = [0] * 26
        for char in word:
            counts[ord(char) - ord("a")] += 1
        groups[tuple(counts)].append(word)

    return list(groups.values())


if __name__ == "__main__":
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    print("Brute force:", group_anagrams_brute(words))
    print("Sorted key:", group_anagrams_sorted_key(words))
    print("Frequency key:", group_anagrams_frequency_key(words))
