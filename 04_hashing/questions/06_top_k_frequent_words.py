"""
06. TOP K FREQUENT WORDS
LeetCode 692: https://leetcode.com/problems/top-k-frequent-words/

PATTERN: Hash Map frequency counting + Sorting / Heap

PROBLEM
-------
Return the k most frequent words.
1. Higher frequency comes first.
2. If frequencies tie, lexicographically smaller word comes first.

Example:
words = ["i","love","leetcode","i","love","coding"], k = 2
Output = ["i","love"]

words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
Output = ["the","is","sunny","day"]

RECOGNITION
-----------
- "Most frequent" -> Hash Map / Counter.
- "Top K" -> sorting or heap.
- A tie-break rule must be part of the ordering.

REAL-WORLD ANALOGY
------------------
Find the most-used search terms on a website. Higher counts come
first; equal counts are ordered alphabetically.

APPROACH 1: BRUTE FORCE RECOUNT
-------------------------------
Find distinct words, count each by scanning the full list, sort by
(-frequency, word), and take k.
Time: O(n*d + d log d), where n is input size and d is distinct words.
Space: O(d).

APPROACH 2: HASH MAP + SORTING (RECOMMENDED)
--------------------------------------------
1. Count words with Counter.
2. Sort distinct words using key (-frequency, word).
3. Return the first k.

Python sorts ascending, so negative frequency puts larger counts
first. The word key sorts ties alphabetically.
Time: O(n + d log d) comparisons.
Space: O(d). String comparison cost can depend on word length.

APPROACH 3: HASH MAP + SIZE-K HEAP
----------------------------------
Use heapq.nsmallest(k, frequency.items(), key=lambda item:
(-item[1], item[0])). This selects the k best items using the
same complete ordering.
Time: O(n + d log k) typically.
Space: O(d + k), including map and selection heap.

APPROACH 4: FREQUENCY BUCKETS
-----------------------------
Group words by frequency, visit frequencies from high to low,
sort words alphabetically inside each bucket, and stop at k.
Time: O(n + d log d) worst case.
Space: O(n + d).

WHY THE RECOMMENDED APPROACH WORKS
----------------------------------
Counter stores every word's exact frequency. Sorting by
(-count, word) orders higher counts first. When counts are equal,
the second key orders words alphabetically. Thus, the first k
words satisfy both rules.

INTERVIEW THINKING
------------------
1. I need each word's count, so I will use a Hash Map.
2. I need the top k, so I will sort distinct words.
3. Ties must be alphabetical.
4. I will sort by (-count, word) and return the first k.

DRY RUN
-------
words = ["i","love","leetcode","i","love","coding"], k = 2

Frequency:
    i: 2, love: 2, leetcode: 1, coding: 1

Sorted by (-frequency, word):
    i: 2, love: 2, coding: 1, leetcode: 1

"i" comes before "love" because both occur twice and i is
alphabetically smaller.
Answer: ["i", "love"]

EDGE CASES
----------
- Only one distinct word.
- All words have equal frequency.
- k equals the number of distinct words.
- Many repeated words.
- Equal frequencies requiring alphabetical ordering.

COMMON MISTAKES
---------------
1. Sorting only by frequency and forgetting the tie-break.
2. Using positive frequency, which sorts ascending.
3. Returning k words before applying the complete ordering.
4. Building a heap with incorrect tie-breaking.

REUSABLE TEMPLATE
-----------------
from collections import Counter
freq = Counter(items)
answer = sorted(freq, key=lambda x: (-freq[x], x))[:k]

PYTHON 3 IMPLEMENTATIONS
========================
"""

from collections import Counter, defaultdict
import heapq


# APPROACH 1: Brute force - recount every distinct word.
def top_k_frequent_brute_force(words, k):
    pairs = []
    for word in set(words):
        count = sum(1 for current in words if current == word)
        pairs.append((word, count))

    pairs.sort(key=lambda pair: (-pair[1], pair[0]))
    return [word for word, count in pairs[:k]]


# APPROACH 2: Hash Map + sorting (recommended).
def top_k_frequent_sorting(words, k):
    frequency = Counter(words)
    return sorted(
        frequency,
        key=lambda word: (-frequency[word], word)
    )[:k]


# APPROACH 3: Hash Map + size-k heap.
def top_k_frequent_heap(words, k):
    frequency = Counter(words)
    selected = heapq.nsmallest(
        k,
        frequency.items(),
        key=lambda item: (-item[1], item[0])
    )
    return [word for word, count in selected]


# APPROACH 4: Frequency buckets.
def top_k_frequent_bucket(words, k):
    frequency = Counter(words)
    buckets = defaultdict(list)

    for word, count in frequency.items():
        buckets[count].append(word)

    answer = []
    for count in range(len(words), 0, -1):
        for word in sorted(buckets[count]):
            answer.append(word)
            if len(answer) == k:
                return answer
    return answer


def run_tests():
    tests = [
        (["i", "love", "leetcode", "i", "love", "coding"], 2,
         ["i", "love"]),
        (["the", "day", "is", "sunny", "the", "the", "the",
          "sunny", "is", "is"], 4, ["the", "is", "sunny", "day"]),
        (["b", "a", "c"], 2, ["a", "b"]),
        (["hello", "hello"], 1, ["hello"]),
        (["a", "b", "a", "b", "c"], 2, ["a", "b"]),
        (["z", "x", "y"], 3, ["x", "y", "z"]),
    ]

    solutions = [
        top_k_frequent_brute_force,
        top_k_frequent_sorting,
        top_k_frequent_heap,
        top_k_frequent_bucket,
    ]

    for words, k, expected in tests:
        for solution in solutions:
            actual = solution(words, k)
            assert actual == expected, (
                f"{solution.__name__}: expected {expected}, got {actual}"
            )

    print("All test cases passed for all 4 approaches.")


if __name__ == "__main__":
    run_tests()


"""
COMPLEXITY SUMMARY
------------------
Let n = total words, d = distinct words.

Approach                    Time                  Extra space
Brute force + sorting       O(n*d + d log d)      O(d)
Hash Map + sorting          O(n + d log d)        O(d)
Hash Map + size-k heap      O(n + d log k)        O(d + k)
Frequency buckets           O(n + d log d)        O(n + d)

String comparisons can depend on word length. The heap is useful
when k is much smaller than d. Sorting is the clearest solution.

INTERVIEWER EXPLANATION
----------------------
"I will count each word using a Hash Map. Then I will sort the
distinct words using negative frequency and the word itself.
Negative frequency puts higher counts first, while the word
provides alphabetical order for ties. Finally, I return the first
k words. The time complexity is O(n + d log d), and the extra
space complexity is O(d)."

RELATED PROBLEMS
----------------
- LeetCode 347: Top K Frequent Elements
- LeetCode 451: Sort Characters By Frequency
- LeetCode 973: K Closest Points to Origin
- LeetCode 703: Kth Largest Element in a Stream

PATTERN MEMORY
--------------
Top K Frequent Words:
Hash Map -> (-frequency, word) -> sorting / heap -> first k.

REVISION CHECKLIST
------------------
[ ] Explain why a Hash Map is needed.
[ ] Explain the key (-frequency, word).
[ ] Handle equal frequencies correctly.
[ ] Implement sorting without looking.
[ ] Explain when a size-k heap is useful.
[ ] State time and space complexity.
[ ] Explain the solution in 30-60 seconds.
"""
