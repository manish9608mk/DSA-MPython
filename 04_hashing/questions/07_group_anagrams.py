# 07. GROUP ANAGRAMS

# LeetCode 49: https://leetcode.com

# PATTERN: Hash Map Grouping + Canonical Key (Sorted String / Char Count Tuple)

"""
PROBLEM
-------
Given an array of strings strs, group the anagrams together. You can return
the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a
different word or phrase, typically using all the original letters exactly once.

Example:
strs = ["eat","tea","tan","ate","nat","bat"]
Output = [["bat"],["nat","tan"],["ate","eat","tea"]]

strs = [""]
Output = [[""]]

RECOGNITION
-----------
- "Group items that share a property" -> Hash Map (defaultdict(list)).
- Anagrams share the exact same character frequencies.
- Need an immutable canonical key to group equivalent words.

REAL-WORLD ANALOGY
------------------
Sorting Scrabble tiles for each word in alphabetical order. Any two words
that produce the exact same sorted sequence of tiles belong in the same pile.

APPROACH 1: BRUTE FORCE PAIRWISE COMPARISON
-------------------------------------------
Keep a visited array. For each unvisited word, scan all remaining words
and compare character counts (or sorted forms) to group them together.
Time: O(n^2 * k), where n is number of strings and k is max string length.
Space: O(n * k) for the output groups and visited tracking.

APPROACH 2: HASH MAP + SORTED STRING KEY
----------------------------------------
1. Create a defaultdict(list).
2. For each word, sort its characters and join them into a tuple or string.
3. Use this sorted form as the dictionary key and append the original word.
4. Return list(groups.values()).

Time: O(n * k log k), sorting each string of length k takes O(k log k).
Space: O(n * k) to store all strings inside the hash map.

APPROACH 3: HASH MAP + CHARACTER COUNT TUPLE KEY (RECOMMENDED / OPTIMAL)
------------------------------------------------------------------------
1. Create a defaultdict(list).
2. For each word, build a 26-element frequency list for 'a'-'z'.
3. Convert the list to an immutable tuple and use it as the Hash Map key.
4. Append the word and return list(groups.values()).

Avoids sorting altogether, reducing per-word key generation to O(k).
Time: O(n * k).
Space: O(n * k).

WHY THE RECOMMENDED APPROACH WORKS
----------------------------------
Two strings are anagrams if and only if their character counts for all 26
lowercase letters are identical. A Python tuple of 26 integers is hashable,
so identical frequency profiles map to the exact same bucket in O(1) average
hash lookup time.

INTERVIEW THINKING
------------------
1. I need to group words that are anagrams of each other, so I need a Hash Map.
2. What makes two words anagrams? Same sorted characters or same letter counts.
3. Lists are unhashable in Python, so I must convert the key to a string or tuple.
4. Sorting is super clean to write; a 26-count tuple avoids the log k factor.

DRY RUN
-------
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Using Sorted Key:
    "eat" -> key "aet" -> groups["aet"] = ["eat"]
    "tea" -> key "aet" -> groups["aet"] = ["eat", "tea"]
    "tan" -> key "ant" -> groups["ant"] = ["tan"]
    "ate" -> key "aet" -> groups["aet"] = ["eat", "tea", "ate"]
    "nat" -> key "ant" -> groups["ant"] = ["tan", "nat"]
    "bat" -> key "abt" -> groups["abt"] = ["bat"]

Answer: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

EDGE CASES
----------
- Empty input list [] -> returns [].
- List containing empty strings ["", ""] -> grouped together as [["", ""]].
- Single character strings ["a"].
- All strings are unique (no anagrams).
- All strings are identical ["aaa", "aaa"].

COMMON MISTAKES
---------------
1. Trying to use a Python list (e.g., [1, 0, 2...]) directly as a dict key
   (raises TypeError: unhashable type: 'list').
2. Mutating the original strings instead of storing original strings in values.
3. Forgetting that anagram groups can be returned in any order.

REUSABLE TEMPLATE
-----------------
from collections import defaultdict
groups = defaultdict(list)
for word in strs:
    key = tuple(sorted(word))
    groups[key].append(word)
return list(groups.values())

PYTHON 3 IMPLEMENTATIONS
========================
"""

from collections import Counter, defaultdict


# APPROACH 1: Brute force pairwise grouping.
def group_anagrams_brute_force(strs):
    n = len(strs)
    visited = [False] * n
    result = []

    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        group = [strs[i]]
        count_i = Counter(strs[i])

        for j in range(i + 1, n):
            if not visited[j] and Counter(strs[j]) == count_i:
                visited[j] = True
                group.append(strs[j])
        result.append(group)

    return result


# APPROACH 2: Hash Map + sorted string key.
def group_anagrams_sorting(strs):
    groups = defaultdict(list)
    for word in strs:
        canonical_key = "".join(sorted(word))
        groups[canonical_key].append(word)
    return list(groups.values())


# APPROACH 3: Hash Map + 26-char frequency tuple key (recommended).
def group_anagrams_count_tuple(strs):
    groups = defaultdict(list)
    for word in strs:
        counts = [0] * 26
        for char in word:
            counts[ord(char) - ord("a")] += 1
        groups[tuple(counts)].append(word)
    return list(groups.values())


def normalize(groups):
    return sorted([sorted(group) for group in groups])


def run_tests():
    tests = [
        (
            ["eat", "tea", "tan", "ate", "nat", "bat"],
            [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
        ),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["", ""], [["", ""]]),
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
    ]

    solutions = [
        group_anagrams_brute_force,
        group_anagrams_sorting,
        group_anagrams_count_tuple,
    ]

    for strs, expected in tests:
        for solution in solutions:
            actual = solution(strs)
            assert normalize(actual) == normalize(expected), (
                f"{solution.__name__}: expected {expected}, got {actual}"
            )

    print("All test cases passed for all 3 approaches.")


if __name__ == "__main__":
    run_tests()


"""
COMPLEXITY SUMMARY
------------------
Let n = number of strings, k = maximum length of a string.

Approach                    Time              Extra space
Brute force pairwise        O(n^2 * k)        O(n * k)
Hash Map + sorted key       O(n * k log k)    O(n * k)
Hash Map + count tuple      O(n * k)          O(n * k)

The count-tuple approach is asymptotically optimal for lowercase English
letters. If Unicode characters are allowed, sorting the string is safer.

INTERVIEWER EXPLANATION
----------------------
"I will use a Hash Map where each key represents a canonical form of an
anagram group, and the value is the list of matching words. For lowercase
English letters, I can build a 26-element character count array for each word
and convert it into an immutable tuple to serve as the dictionary key. This
gives O(n * k) time complexity and O(n * k) space complexity."

RELATED PROBLEMS
----------------
- LeetCode 242: Valid Anagram
- LeetCode 438: Find All Anagrams in a String
- LeetCode 249: Group Shifted Strings
- LeetCode 2273: Find Resultant Array After Removing Anagrams

PATTERN MEMORY
--------------
Group Anagrams:
Hash Map -> canonical key (sorted word or 26-count tuple) -> append word.

REVISION CHECKLIST
------------------
[ ] Explain why a canonical key is needed for grouping.
[ ] Explain why a tuple is used instead of a list as a dict key.
[ ] Compare O(n * k log k) sorting vs O(n * k) counting.
[ ] Handle empty strings and single-element inputs.
[ ] State time and space complexity clearly.
[ ] Explain the solution in 30-60 seconds.
"""
