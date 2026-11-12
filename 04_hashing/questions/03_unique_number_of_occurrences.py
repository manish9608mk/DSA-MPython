# 1207. Unique Number of Occurrences

"""
PROBLEM

Given an array of integers arr, return True if the number of occurrences
of each value in the array is unique. Otherwise, return False.

Examples:

    arr = [1, 2, 2, 1, 1, 3] -> True
    Explanation:
        1 appears 3 times.
        2 appears 2 times.
        3 appears 1 time.
        Frequencies [3, 2, 1] are all unique.

    arr = [1, 2] -> False
    Explanation:
        1 appears once and 2 appears once.
        Frequency 1 is repeated.

    arr = [-3, 0, 1, -3, 1, 1, -3, 10, 0] -> True

Link:
https://leetcode.com/problems/unique-number-of-occurrences/


PATTERN

Hashing / Frequency Counting + Hash Set

Count occurrences
       ↓
Collect frequencies
       ↓
Check whether frequencies repeat
       ↓
Hash Set


RECOGNITION TRICKS

- "How many times does each value appear?" -> Frequency Map.
- "Are all frequencies different?" -> Compare list length with set length.
- Need to detect duplicate counts -> Hash Set.
- Values may be negative -> Dictionary handles them directly.
- Do not confuse unique values with unique frequencies.


REAL-WORLD ANALOGY

Imagine a classroom where students have different numbers of books.

You first count how many books each student has.
Then check whether every student has a different count.

If two students have the same number of books, the condition is false.


APPROACH 1 — BRUTE FORCE

For every distinct value:
    Count how many times it appears in arr.
    Compare this frequency with frequencies of previously checked values.

If a frequency is repeated, return False.

Time: O(n^2) in a straightforward implementation.
Space: O(n) for tracking checked values and frequencies.


APPROACH 2 — BETTER APPROACH (SORTING)

1. Sort the array.
2. Count the length of each group of equal values.
3. Store the frequencies.
4. Sort the frequency list.
5. Check adjacent frequencies for duplicates.

Why it works:
    Equal values become adjacent after sorting.
    We can count each value's frequency in one scan.

Time: O(n log n)
Space: O(n) for the frequency list and sorting storage.


APPROACH 3 — OPTIMAL / STANDARD (HASH MAP + HASH SET)

1. Use a dictionary to count each number's frequency.
2. Create a set from the dictionary's frequency values.
3. If the number of frequencies equals the number of unique frequencies,
   every frequency is unique.

Core condition:

    len(frequencies) == len(set(frequencies))

Time: O(n) average
Space: O(n)


WHY HASH MAP + HASH SET WORKS

The dictionary maps each distinct number to its occurrence count.

For example:

    arr = [1, 2, 2, 1, 1, 3]

    counts = {
        1: 3,
        2: 2,
        3: 1
    }

The frequency values are:

    [3, 2, 1]

A set removes duplicate values:

    set([3, 2, 1]) = {1, 2, 3}

If the list and set have equal lengths, no frequency was repeated.

If their lengths differ, at least one frequency appeared more than once.


STEP-BY-STEP THINKING

1. What must be counted?
       The occurrences of every distinct number.

2. Which data structure stores value -> count?
       Hash Map / Dictionary.

3. What must be checked after counting?
       Whether two different values have the same frequency.

4. Which data structure detects duplicate frequencies?
       Hash Set.

5. How can we check uniqueness quickly?
       Compare the length of the frequency list with the length of its set.


DRY RUN — TRUE CASE

arr = [1, 2, 2, 1, 1, 3]

Count frequencies:

    1 -> 3
    2 -> 2
    3 -> 1

Frequency list:

    [3, 2, 1]

Unique frequency set:

    {1, 2, 3}

Compare:

    len([3, 2, 1]) = 3
    len({1, 2, 3}) = 3

Both lengths are equal.

Output: True


DRY RUN — FALSE CASE

arr = [1, 2]

Count frequencies:

    1 -> 1
    2 -> 1

Frequency list:

    [1, 1]

Unique frequency set:

    {1}

Compare:

    len([1, 1]) = 2
    len({1}) = 1

Lengths are different.

Output: False


EDGE CASES

- One element: [5] -> True
- Empty array: [] -> True
- Every value appears once: [1, 2, 3] -> False
- All values equal: [7, 7, 7] -> True
- Negative values: [-1, -1, 2, 2, 2] -> True
- Repeated frequencies: [1, 1, 2, 2, 3] -> False


COMMON INTERVIEW MISTAKES

1. Checking whether array values are unique.
   The problem asks whether their occurrence counts are unique.

2. Using only a set of array values.
   That removes duplicates and loses frequency information.

3. Checking only the number of distinct array values.
   We must compare their frequencies.

4. Forgetting that two different values can have the same frequency.

5. Sorting the original array unnecessarily in the optimal approach.
   A dictionary counts values directly.


REUSABLE TEMPLATE — FREQUENCY UNIQUENESS

counts = {}

for item in items:
    counts[item] = counts.get(item, 0) + 1

frequencies = list(counts.values())

return len(frequencies) == len(set(frequencies))


SIMILAR PROBLEMS

- LeetCode 242: Valid Anagram
- LeetCode 383: Ransom Note
- LeetCode 387: First Unique Character in a String
- LeetCode 451: Sort Characters By Frequency
- LeetCode 1647: Minimum Deletions to Make Character Frequencies Unique


INTERVIEW TIP

Explain the two data structures separately:

"The dictionary counts how often each number appears.
The set checks whether any two numbers have the same frequency.

If converting the frequency list to a set does not reduce its length,
all frequencies are unique."

This clearly explains why both Hash Map and Hash Set are used.
"""


# APPROACH 1 — BRUTE FORCE
def unique_occurrences_brute(arr: list[int]) -> bool:
    checked_values = set()
    seen_frequencies = []

    for num in arr:
        if num in checked_values:
            continue

        checked_values.add(num)
        frequency = arr.count(num)

        if frequency in seen_frequencies:
            return False

        seen_frequencies.append(frequency)

    return True


# APPROACH 2 — BETTER: SORTING
def unique_occurrences_sorting(arr: list[int]) -> bool:
    if not arr:
        return True

    nums = sorted(arr)
    frequencies = []

    count = 1

    for i in range(1, len(nums)):
        if nums[i] == nums[i - 1]:
            count += 1
        else:
            frequencies.append(count)
            count = 1

    frequencies.append(count)

    frequencies.sort()

    for i in range(1, len(frequencies)):
        if frequencies[i] == frequencies[i - 1]:
            return False

    return True


# APPROACH 3 — OPTIMAL: HASH MAP + HASH SET
def unique_occurrences_hashing(arr: list[int]) -> bool:
    counts = {}

    for num in arr:
        counts[num] = counts.get(num, 0) + 1

    frequencies = list(counts.values())

    return len(frequencies) == len(set(frequencies))


if __name__ == "__main__":
    test_cases = [
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, -3, 10, 0], False),
        ([5], True),
        ([], True),
        ([1, 2, 3], False),
        ([7, 7, 7], True),
        ([-1, -1, 2, 2, 2], True),
        ([1, 1, 2, 2, 3], False),
    ]

    for arr, expected in test_cases:
        brute = unique_occurrences_brute(arr)
        sorting = unique_occurrences_sorting(arr)
        optimal = unique_occurrences_hashing(arr)

        assert brute == expected
        assert sorting == expected
        assert optimal == expected

        print(f"Input: {arr}")
        print(f"Brute force: {brute}")
        print(f"Sorting:     {sorting}")
        print(f"Hashing:     {optimal}")
        print("All approaches passed.\n")


"""
COMPLEXITY SUMMARY

Let n be the length of arr and k be the number of distinct values.

Approach              Time          Auxiliary Space
Brute force           O(n^2)        O(k)
Sorting               O(n log n)    O(n)
Hash Map + Hash Set   O(n) average  O(k)


INTERVIEW EXPLANATION (SAY THIS OUT LOUD)

"First, I count the frequency of every number using a dictionary.
Then I take all the frequency values and convert them into a set.

A set stores only unique values. So if the set has fewer elements
than the original frequency list, at least two numbers have the
same occurrence count.

Therefore, I return whether both lengths are equal.

The time complexity is O(n) average, and the auxiliary space
complexity is O(k), where k is the number of distinct values."


PATTERN MEMORY

Need occurrence counts
        ↓
Hash Map: value -> frequency
        ↓
Need to detect repeated frequencies
        ↓
Hash Set
        ↓
Compare list length and set length


IMPORTANT DIFFERENCE

Valid Anagram:
    Compare the frequency of every character in two strings.

Ransom Note:
    Check whether one string's required frequencies are available
    in another string.

Unique Number of Occurrences:
    Count each value, then check whether the resulting frequencies
    are all different.


REVISION CHECKLIST

[ ] Explain why a dictionary is needed.
[ ] Explain why a set is needed after counting.
[ ] Write the optimal solution without looking.
[ ] Dry-run [1, 2, 2, 1, 1, 3].
[ ] Dry-run [1, 2].
[ ] Explain the difference between unique values and unique frequencies.
[ ] State time and auxiliary space complexity.
[ ] Explain the solution clearly in under two minutes.
"""
