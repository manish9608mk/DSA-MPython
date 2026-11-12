# 451. Sort Characters By Frequency

"""
PROBLEM

Given a string s, sort it in decreasing order based on the frequency
of each character.

Return the sorted string. If multiple answers are possible, return any
of them.

Examples:
    s = "tree" -> "eert" or "eetr"
    s = "cccaaa" -> "aaaccc" or "cccaaa"
    s = "Aabb" -> "bbAa" or "bbaA"

Link:
https://leetcode.com/problems/sort-characters-by-frequency/


PATTERN

Hashing / Frequency Counting / Sorting

Need to know how often each character occurs
                    ↓
              HASH MAP
                    ↓
Sort characters by their frequency
                    ↓
       SORT FREQUENCY PAIRS OR BUCKETS


RECOGNITION TRICKS

- "Most frequent", "least frequent", or "sort by occurrence" -> count frequencies.
- If an item must be grouped by its count -> Hash Map.
- If the final answer needs an order based on counts -> sorting or buckets.
- When the output repeats each character count times, use char * count.
- If the required order is based on frequency, a normal set is not enough.


REAL-WORLD ANALOGY

Imagine a classroom where you count how many students have each first name.
You then announce the names from the most common to the least common.

First count each name. Then arrange the name-count pairs by count.
That is exactly what this problem asks us to do with characters.


APPROACH 1 — BRUTE FORCE (REPEATED COUNTING)

For every distinct character:
    Count how many times it appears in the string.
    Store the character and its count.
Sort the stored pairs by count.
Build the output.

Why it works:
    Every character is counted and then placed in descending frequency order.

Why it is inefficient:
    Calling count() for every distinct character scans the whole string
    repeatedly.

Let n be the string length and k the number of distinct characters.
Time: O(n * k + k log k + n), worst case O(n^2).
Space: O(k) for the frequency pairs, excluding output.


APPROACH 2 — OPTIMAL STANDARD (HASH MAP + SORTING)

1. Count each character using a dictionary or Counter.
2. Sort the distinct characters by their frequency in descending order.
3. For each character, append that character frequency times.

Why it works:
    The dictionary stores the exact frequency of every character.
    Sorting by frequency puts higher-frequency characters first.
    Repeating each character by its count uses every occurrence exactly once.

Time:
    O(n) to count.
    O(k log k) to sort k distinct characters.
    O(n) to build the output.
    Total: O(n + k log k).

Space:
    O(k) auxiliary space for the frequency map and sorting,
    excluding the output string.


APPROACH 3 — BUCKET SORT (LINEAR-TIME ALTERNATIVE)

A character can occur between 1 and n times.
Create buckets indexed by frequency.

For every character and its count:
    Put the character into the bucket for that count.

Then traverse buckets from frequency n down to 1.
Append every character in a bucket frequency times.

Why it works:
    The bucket index itself represents the frequency.
    Reading buckets from high to low automatically gives descending order.

Time: O(n + k), which is O(n).
Space: O(n + k) for buckets and frequency data, excluding output.

Interview note:
    Hash Map + Sorting is the simplest standard solution.
    Bucket Sort is a useful optimization when linear time is desired.


WHY HASH MAP + SORTING WORKS

The problem is not asking us to sort individual characters alphabetically.
It asks us to sort groups of equal characters by how frequently they appear.

The dictionary converts the string into character-frequency pairs.
For example:

    "tree" -> {'t': 1, 'r': 1, 'e': 2}

Sorting those pairs by frequency gives:

    [('e', 2), ('t', 1), ('r', 1)]

Repeating each character by its count gives:

    "ee" + "t" + "r" -> "eetr"

Every original character is included exactly as many times as it appeared.


STEP-BY-STEP THINKING

1. What is the sorting key?
       Character frequency, not the character itself.

2. How can we calculate frequency efficiently?
       Use a dictionary or collections.Counter.

3. Do we need to sort all n characters?
       No. We only need to sort k distinct characters.

4. How do we build the answer?
       Repeat each character by its frequency and join the pieces.


DRY RUN

s = "tree"

Step 1 — Count frequencies:

    t -> 1
    r -> 1
    e -> 2

Dictionary:

    {'t': 1, 'r': 1, 'e': 2}

Step 2 — Sort by frequency descending:

    [('e', 2), ('t', 1), ('r', 1)]

Step 3 — Repeat each character:

    'e' * 2 -> 'ee'
    't' * 1 -> 't'
    'r' * 1 -> 'r'

Step 4 — Join:

    "ee" + "t" + "r" = "eetr"

Output: "eetr"

Note:
    The order between characters with equal frequency does not matter.


EDGE CASES

- One character: "a" -> "a"
- All characters equal: "aaaa" -> "aaaa"
- All frequencies equal: "abcd" -> any permutation of "abcd"
- Mixed uppercase and lowercase: "Aabb" -> "bbAa" or another valid order
- Repeated groups: "cccaaa" -> "cccaaa" or "aaaccc"
- Empty string: the helper functions below return "" (the LeetCode constraints
  provide a non-empty string).


COMMON INTERVIEW MISTAKES

1. Sorting characters alphabetically.
   The requirement is descending frequency, not alphabetical order.

2. Sorting all n characters unnecessarily.
   Count first, then sort only k distinct characters.

3. Forgetting to repeat a character by its frequency.
   Adding each distinct character only once loses occurrences.

4. Assuming a unique output.
   Characters with equal frequency can appear in any relative order.

5. Using a set.
   A set removes duplicate occurrences and loses frequency information.

6. Claiming O(n log n) without defining what is sorted.
   The standard solution sorts k distinct characters, so the precise
   complexity is O(n + k log k).


REUSABLE TEMPLATE — FREQUENCY THEN SORT

from collections import Counter

freq = Counter(items)

ordered = sorted(
    freq.items(),
    key=lambda pair: pair[1],
    reverse=True
)

result = []
for item, count in ordered:
    result.append(item * count)

answer = "".join(result)


SIMILAR PROBLEMS

- LeetCode 242: Valid Anagram
- LeetCode 383: Ransom Note
- LeetCode 49: Group Anagrams
- LeetCode 1207: Unique Number of Occurrences
- LeetCode 347: Top K Frequent Elements
- LeetCode 692: Top K Frequent Words

INTERVIEW TIP

Start by saying:

"I need to arrange characters by their occurrence count, so I will
first build a frequency map. I only need to sort the distinct characters,
not every character in the input. Then I will append each character
frequency times."

For the standard solution, state:
    Time: O(n + k log k)
    Auxiliary space: O(k), excluding the output.

If the interviewer asks whether we can improve the sorting step,
explain the bucket-sort solution in O(n) time.


PYTHON DETAILS

- Counter(s) creates a frequency map.
- sorted(..., key=..., reverse=True) sorts by frequency descending.
- char * count repeats a string.
- "".join(parts) combines strings efficiently.
- Python sorting is stable, but equal-frequency order is not required here.
"""


from collections import Counter


# APPROACH 1 — BRUTE FORCE: REPEATED COUNTING + SORTING
def frequency_sort_brute(s: str) -> str:
    distinct_chars = set(s)
    pairs = []

    for char in distinct_chars:
        count = s.count(char)
        pairs.append((char, count))

    pairs.sort(key=lambda pair: pair[1], reverse=True)

    result = []
    for char, count in pairs:
        result.append(char * count)

    return "".join(result)


# APPROACH 2 — OPTIMAL STANDARD: HASH MAP / COUNTER + SORTING
def frequency_sort_hash_map(s: str) -> str:
    freq = Counter(s)

    ordered = sorted(
        freq.items(),
        key=lambda pair: pair[1],
        reverse=True
    )

    result = []
    for char, count in ordered:
        result.append(char * count)

    return "".join(result)


# APPROACH 3 — BUCKET SORT: O(n) TIME
def frequency_sort_bucket(s: str) -> str:
    if not s:
        return ""

    freq = Counter(s)

    # buckets[count] stores all characters that occur 'count' times.
    buckets = [[] for _ in range(len(s) + 1)]

    for char, count in freq.items():
        buckets[count].append(char)

    result = []

    # Read frequencies from highest to lowest.
    for count in range(len(s), 0, -1):
        for char in buckets[count]:
            result.append(char * count)

    return "".join(result)


# LEETCODE SUBMISSION CLASS
class Solution:
    def frequencySort(self, s: str) -> str:
        return frequency_sort_hash_map(s)


def is_valid_frequency_sort(original: str, result: str) -> bool:
    """
    Validate an answer without requiring one exact order.
    It checks:
    1. The output contains exactly the original characters.
    2. Output character frequencies are in non-increasing order.
    """
    if Counter(original) != Counter(result):
        return False

    output_freq = Counter(result)
    counts_in_output = [output_freq[char] for char in result]

    return all(
        counts_in_output[i] >= counts_in_output[i + 1]
        for i in range(len(counts_in_output) - 1)
    )


if __name__ == "__main__":
    test_cases = [
        "tree",
        "cccaaa",
        "Aabb",
        "a",
        "aaaa",
        "abcd",
        "mississippi",
        "",  # Empty input is supported by these helper implementations.
    ]

    solution = Solution()

    for s in test_cases:
        brute = frequency_sort_brute(s)
        optimal = solution.frequencySort(s)
        bucket = frequency_sort_bucket(s)

        assert is_valid_frequency_sort(s, brute)
        assert is_valid_frequency_sort(s, optimal)
        assert is_valid_frequency_sort(s, bucket)

        print(f"Input:       {s!r}")
        print(f"Brute force: {brute!r}")
        print(f"Hash Map:    {optimal!r}")
        print(f"Bucket sort: {bucket!r}")
        print("All approaches passed.\n")


"""
COMPLEXITY SUMMARY

Let:
    n = length of the string
    k = number of distinct characters

Approach                         Time                  Auxiliary Space
Repeated count + sorting         O(n*k + k log k)      O(k)
Counter + sorting                O(n + k log k)        O(k)
Bucket sort                      O(n)                  O(n + k)

The output string is not included in auxiliary-space figures.


INTERVIEW EXPLANATION (SAY THIS OUT LOUD)

"First, I count the frequency of every character using a Counter,
which is a hash map.

Then I sort the distinct character-frequency pairs in descending
order of frequency. I do not need to sort all characters individually;
I only sort the k distinct characters.

After sorting, I repeat each character according to its frequency
and join all pieces into the final string.

Counting takes O(n), sorting takes O(k log k), and building the result
takes O(n). Therefore, the total time complexity is O(n + k log k).
The auxiliary space is O(k), excluding the output."

If asked for a linear-time alternative:

"Since a character frequency can only range from 1 to n, I can use
bucket sort. I place each character into the bucket matching its
frequency and traverse buckets from n down to 1. This gives O(n)
time, with O(n + k) auxiliary space."


PATTERN MEMORY

Sort by how often an item appears?
            ↓
      Count frequencies
            ↓
       Hash Map / Counter
            ↓
Sort distinct items by their counts
            ↓
     Build the required output


REVISION CHECKLIST

[ ] Explain why frequency counting is needed.
[ ] Explain why sorting all n characters is unnecessary.
[ ] Write the Counter + sorting solution without looking.
[ ] Explain why equal-frequency order does not matter.
[ ] Dry-run "tree".
[ ] Explain the bucket-sort alternative.
[ ] State O(n + k log k) time for the standard solution.
[ ] State O(n) time for the bucket solution.
[ ] Explain the solution clearly in under two minutes.
"""

