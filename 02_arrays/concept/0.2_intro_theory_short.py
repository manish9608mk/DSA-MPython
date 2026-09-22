'''
🎯 INTERVIEW THINKING

When you see an array problem, don't code immediately.

Ask:

Know the index?
→ Access / Update → O(1)

Need to visit every element?
→ Traversal → O(n)

Searching an unsorted array?
→ Linear Search → O(n)

Insert/Delete at beginning or middle?
→ Shifting → O(n)

Working from both ends?
→ Two Pointers

Processing right → left?
→ Backward Traversal

Can I modify the same array?
→ Think In-Place → O(1) extra space when possible

Golden habit:
First identify WHAT you need to do with the array,
then choose the technique.
'''


'''
ARRAY BASICS

An array stores multiple values in an ordered sequence.

Python uses lists for most array problems.

Example:

arr = [10, 20, 30, 40, 50]

Index:  0   1   2   3   4
Value: 10  20  30  40  50

Interview definition:

"An array is an ordered collection of elements
that can be accessed using an index."
'''


'''
INDEXING

Python uses zero-based indexing.

arr = [10, 20, 30, 40, 50]

arr[0] → 10
arr[1] → 20
arr[2] → 30

Access by index → O(1)

Negative indexing:

arr[-1] → 50
arr[-2] → 40

Key idea:
If I know the index → O(1) access.
'''


'''
TRAVERSAL

Traversal means visiting array elements.

arr = [10, 20, 30, 40, 50]

for x in arr:
    print(x)

If index is needed:

for i in range(len(arr)):
    print(i, arr[i])

Visiting all n elements → O(n)
'''


'''
ACCESS AND UPDATE

Access = read a value.

arr = [10, 20, 30, 40, 50]

value = arr[2]        # 30

Access → O(1)

Update = change a value.

arr[2] = 100

[10, 20, 30, 40, 50]
          ↓
[10, 20, 100, 40, 50]

Update → O(1)

Key idea:
Known index → Access / Update → O(1)
'''


'''
INSERTION

Adding an element is insertion.

At the end:

arr.append(40)
→ O(1) amortized

At the beginning:

arr.insert(0, 5)
→ O(n)

Why?
Elements must shift right.

In the middle:

arr.insert(2, 99)
→ O(n)

Interview recognition:

Beginning / Middle
        ↓
     SHIFTING
        ↓
       O(n)
'''


'''
DELETION

Removing an element is deletion.

From the end:

arr.pop()
→ O(1)

From the beginning:

arr.pop(0)
→ O(n)

From the middle:

arr.pop(index)
→ O(n)

Why?
Remaining elements may need to shift left.

Remember:

End → O(1)
Beginning → O(n)
Middle → O(n)
'''


'''
SEARCHING

Searching means finding a value or its index.

arr = [10, 20, 30, 40, 50]

Find 40:

for i in range(len(arr)):
    if arr[i] == 40:
        print(i)

Answer → 3

Unsorted array:
Linear Search → O(n)

Why?
We may need to check every element.

Sorted array:
Binary Search can give → O(log n)
'''


'''
FORWARD AND BACKWARD TRAVERSAL

Forward:

10 → 20 → 30 → 40 → 50

for x in arr:
    print(x)

Backward:

50 → 40 → 30 → 20 → 10

for i in range(len(arr) - 1, -1, -1):
    print(arr[i])

Or:

for x in reversed(arr):
    print(x)

Both are O(n) when all elements are visited.

Backward traversal is useful when a problem
requires processing from the right side.
'''


'''
REVERSING AN ARRAY

Example:

[10, 20, 30, 40, 50]
        ↓
[50, 40, 30, 20, 10]

Python:

arr.reverse()
→ modifies the same list

arr = arr[::-1]
→ creates a new list

DSA approach ⭐

Use two pointers:

left = 0
right = len(arr) - 1

while left < right:
    swap arr[left] and arr[right]
    left += 1
    right -= 1

Code:

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

Time → O(n)
Extra Space → O(1)

This is the foundation of TWO POINTERS.
'''


'''
ARRAY OPERATION COMPLEXITY

Operation                    Time

Access arr[i]                O(1)
Update arr[i]                O(1)
len(arr)                     O(1)
Traversal                    O(n)
Search unsorted              O(n)
Append                       O(1) amortized
Insert at beginning          O(n)
Insert in middle             O(n)
Pop from end                 O(1)
Delete beginning             O(n)
Delete middle                O(n)
Reverse in-place             O(n)
'''


'''
🧠 ARRAY MENTAL MODEL

                    ARRAY
                      |
          +-----------+-----------+
          |                       |
      KNOW INDEX?            DON'T KNOW INDEX?
          |                       |
         YES                    SEARCH
          |                       |
        O(1)                    O(n)
          |
     +----+----+
     |         |
   ACCESS    UPDATE
    O(1)      O(1)


INSERT / DELETE
       |
   +---+---+
   |       |
  END    MIDDLE / BEGINNING
   |       |
 O(1)    SHIFT
           |
          O(n)


BOTH ENDS
    ↓
TWO POINTERS


RIGHT → LEFT
    ↓
BACKWARD TRAVERSAL


SAME ARRAY
    ↓
IN-PLACE
    ↓
O(1) EXTRA SPACE
'''


'''
🎯 INTERVIEW EXPLANATION

If asked "What is an array?"

Say:

"An array is an ordered collection of elements
that can be accessed using an index.

In Python, we generally use lists for array problems.

Accessing or updating an element with a known index
takes O(1), while traversal and searching an
unsorted array take O(n).

Insertion or deletion at the beginning or middle
can take O(n) because elements may need to shift."
'''


'''
🔥 FINAL REVISION

1. Array → ordered collection
2. Python → list
3. Index starts at 0
4. Access → O(1)
5. Update → O(1)
6. Traversal → O(n)
7. Unsorted search → O(n)
8. append() → O(1) amortized
9. Insert beginning/middle → O(n)
10. pop() from end → O(1)
11. Delete beginning/middle → O(n)
12. Backward → right to left
13. Reverse → Two Pointers
14. Reverse in-place → O(n) time, O(1) space
15. Both ends → Two Pointers

GOLDEN RULE:

Before coding, ask:

"What do I need to do with this array?"

Access?
Update?
Traverse?
Search?
Insert?
Delete?
Reverse?
Both ends?
Right to left?
In-place?

Identify the operation first.
Then choose the pattern.
'''