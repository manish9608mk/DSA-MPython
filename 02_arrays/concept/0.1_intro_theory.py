'''
🎯 Interview thinking -
When you see an array problem, don't immediately code.

First ask yourself:
Do I need to visit every element?
→ Probably O(n).
Do I know the index?
→ Access/update can be O(1).
Am I inserting/deleting in the middle?
→ Think about shifting → O(n).
Am I searching an unsorted array?
→ Usually linear search → O(n).
Do I need to work from both ends?
→ Think two pointers.
Do I need to process from right to left?
→ Backward traversal may be useful.
Can I solve it in-place?
→ Try to avoid unnecessary extra arrays when appropriate.

That last part—recognizing what the problem is asking before writing code—is what will eventually make you much stronger at interview problems.

'''

'''
ARRAY BASICS
An array stores multiple values in an ordered sequence.
Python's list is a dynamic array, not a traditional fixed-size array.

Example:
arr = [10, 20, 30, 40, 50]

Think of it as:
Index:  0   1   2   3   4
Value: 10  20  30  40  50

In Python, we normally use a list for array problems.

Interview definition:
"An array is an ordered collection of elements
that can be accessed using an index."
'''

'''
INDEXING
Python arrays/lists use zero-based indexing.

arr = [10, 20, 30, 40, 50]

arr[0] -> 10
arr[1] -> 20
arr[2] -> 30

Access by index is O(1).

Python also supports negative indexing:

arr[-1] -> 50
arr[-2] -> 40

Interview point:
"If I know the index, I can access the element in O(1) time."
'''

'''
TRAVERSAL
Traversal means visiting every element of an array.
arr = [10, 20, 30, 40, 50]

Traversal:
10 -> 20 -> 30 -> 40 -> 50

When only the value is needed:
for x in arr:
    print(x)

When index is also needed:
for i in range(len(arr)):
    print(i, arr[i])

Visiting all n elements takes O(n) time.
'''

'''
ACCESS AND UPDATE
Access means reading an element.

arr = [10, 20, 30, 40, 50]
value = arr[2]        # 30

Access by index -> O(1)

Update means changing an element.

arr[2] = 100

Before:
[10, 20, 30, 40, 50]

After:
[10, 20, 100, 40, 50]

Update by index -> O(1)

Key idea:
If I know the index, access and update are O(1).
'''

'''
INSERTION
Adding an element is called insertion.

1. Insert at the end:
arr.append(40)
Usually O(1) amortized.

2. Insert at beginning:
arr.insert(0, 5)
Elements must shift right.
Time -> O(n)

3. Insert in middle:
arr.insert(2, 99)
Elements after the position may need to shift.
Time -> O(n)

Interview recognition:
Insertion at beginning/middle -> think SHIFTING -> O(n).
'''

'''
DELETION
Deleting an element means removing it from the array.

Delete from end:
arr.pop()
Usually -> O(1)

Delete from beginning:
arr.pop(0)
Remaining elements shift left.
Time -> O(n)

Delete from middle:
arr.pop(index)
Elements after the index may shift left.
Time -> O(n)

Interview recognition:
End       -> usually O(1)
Beginning -> O(n)
Middle    -> O(n)

Reason:
Elements have to shift.
'''

'''
SEARCHING
Searching means finding whether a value exists
and/or finding its index.

Example:
arr = [10, 20, 30, 40, 50]

Find 40:

for i in range(len(arr)):
    if arr[i] == 40:
        print(i)

Answer -> 3

For an unsorted array, linear search is used.
Worst-case time -> O(n)

Why?
We may have to check every element.

Later:
Binary Search can reduce searching to O(log n)
when the array is sorted.
'''

'''
FORWARD AND BACKWARD TRAVERSAL
Useful when a problem asks you to process
elements from the right side.

Both take O(n) time if all elements are visited.

Forward -
Normal direction:
10 → 20 → 30 → 40 → 50

Python:
for x in arr:
    print(x)

Or:

for i in range(len(arr)):
    print(arr[i])

Backward -
Reverse direction:
50 → 40 → 30 → 20 → 10

Using range:

for i in range(len(arr) - 1, -1, -1):
    print(arr[i])

Or Python slicing:

for x in reversed(arr):
    print(x)

Why do interviews care?
Many problems ask you to process an array:
from right to left
from the end
compare current element with previous element
maintain information about elements on the right

So you should be comfortable with both directions.
'''

'''
REVERSING AN ARRAY
This is an important interview concept.

Suppose:
arr = [10, 20, 30, 40, 50]
We want:
[50, 40, 30, 20, 10]

There are several ways.

Method 1 — Python built-in
arr.reverse()
This modifies the original array.

Method 2 — Slicing
arr = arr[::-1]
This creates a new list.

Method 3 — Two pointers ⭐
Best DSA approach:
Use two pointers.

left = 0
right = len(arr) - 1

While left < right:
    swap arr[left] and arr[right]
    move left forward
    move right backward

Example:

10  20  30  40  50
L                   R

50  20  30  40  10

50  40  30  20  10
    L       R

Stop when left >= right.

Time  -> O(n)
Space -> O(1)

code:
def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]

        left += 1
        right -= 1

    return arr

This is an important foundation for the
Two Pointers pattern.because you'll see two pointers again later
'''

'''
ARRAY OPERATION COMPLEXITY:

Operation                         Time

Access arr[i]                     O(1)

Update arr[i]                     O(1)

len(arr)                          O(1)

Traverse                          O(n)

Search unsorted array             O(n)

Append at end                     O(1) amortized

Insert at beginning               O(n)

Insert in middle                  O(n)

Pop from end                      O(1)

Delete from beginning             O(n)

Delete from middle                O(n)

Reverse in-place                  O(n)


INTERVIEW THINKING:
When you see an ARRAY problem:
DO NOT immediately start coding.

First ask:

QUESTION 1:

Do I know the index?

YES
 ↓
Access / Update
 ↓
O(1)


QUESTION 2:

Do I need to visit every element?

YES
 ↓
Traversal
 ↓
Usually O(n)


QUESTION 3:

Am I searching an unsorted array?

YES
 ↓
Linear Search
 ↓
O(n)


QUESTION 4:

Am I inserting/deleting at the beginning
or middle?

YES
 ↓
Elements may SHIFT
 ↓
O(n)


QUESTION 5:

Am I working from BOTH ENDS?

YES
 ↓
Think TWO POINTERS


QUESTION 6:

Do I need to process from RIGHT TO LEFT?

YES
 ↓
Think BACKWARD TRAVERSAL


QUESTION 7:

Can I modify the same array
instead of creating another one?

YES
 ↓
Consider an IN-PLACE solution
 ↓
Potentially O(1) extra space



MOST IMPORTANT MENTAL MODEL:

                    ARRAY
                      |
          +-----------+-----------+
          |                       |
      KNOW INDEX?            DON'T KNOW INDEX?
          |                       |
         YES                      |
          |                       |
       O(1)                   SEARCH
          |                       |
     +----+----+                 O(n)
     |         |
   ACCESS    UPDATE
    O(1)      O(1)


          INSERTION / DELETION
                    |
          +---------+---------+
          |                   |
         END             BEGINNING/MIDDLE
          |                   |
       O(1) usually         SHIFT
                            |
                           O(n)


          PROCESS BOTH ENDS?
                    |
                   YES
                    |
              TWO POINTERS


          PROCESS RIGHT → LEFT?
                    |
                   YES
                    |
          BACKWARD TRAVERSAL



INTERVIEW EXPLANATION:

If an interviewer asks:

"What is an array?"

You can say:

"An array is an ordered collection of elements
that can be accessed using an index.

In Python, we generally use lists to solve
array-based problems.

Accessing or updating an element when its index
is known takes O(1) time, while traversing or
searching an unsorted array takes O(n) time.

Insertion or deletion at the beginning or middle
can take O(n) because elements may need to shift."


FINAL REVISION
Remember these:
1. Array -> ordered collection
2. Python -> use list for array problems
3. Indexing starts at 0
4. arr[i] -> access -> O(1)
5. arr[i] = value -> update -> O(1)
6. Traversal -> visit elements -> O(n)
7. Unsorted search -> linear search -> O(n)
8. append() -> O(1) amortized
9. Insert beginning/middle -> shifting -> O(n)
10. pop() from end -> O(1)
11. Delete beginning/middle -> shifting -> O(n)
12. Backward traversal -> right to left
13. Reverse -> two pointers -> O(n) time, O(1) space
14. Both ends -> think TWO POINTERS
15. Avoid unnecessary extra arrays when an in-place
    solution is possible


GOLDEN RULE:
Before coding an array problem, ask:
"WHAT DO I NEED TO DO WITH THE ARRAY?"
Then identify:

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

Once you identify the operation/pattern,
the implementation becomes much easier.
'''

