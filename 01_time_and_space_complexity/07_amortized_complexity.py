# This is particularly important in Python because you already have:
# arr.append(x)  # O(1) amortized

# 10. Amortized Complexity

'''
Amortized Complexity
====================

Amortized analysis calculates the average cost of a sequence
of operations over time.

IMPORTANT:

Amortized complexity is NOT the same as average-case complexity.

Average-case:
→ Average performance based on a probability/distribution of inputs.

Amortized:
→ Average cost per operation across a sequence of operations,
  even if some individual operations are expensive.


---------------------------------------------------------
1. PYTHON LIST append()
---------------------------------------------------------

arr = []

for i in range(n):
    arr.append(i)

We usually say:

arr.append(i)
→ O(1) amortized

Why?

Python lists are dynamic arrays.

A list has some allocated capacity.

Example conceptually:

Capacity = 4

[1, 2, 3, 4]

When we add another element:

[1, 2, 3, 4, 5]

The existing elements may need to be copied
to a larger memory location.

That particular append can cost:

O(n)


But most append operations are:

O(1)


---------------------------------------------------------
2. EXPENSIVE RESIZE OPERATION
---------------------------------------------------------

Imagine a list has:

Capacity = 4

Current:

[10, 20, 30, 40]

Now:

arr.append(50)

There may not be enough capacity.

Python allocates a larger area and copies elements:

10
20
30
40

Then adds:

50

The resize operation can cost:

O(n)


---------------------------------------------------------
3. WHY append() IS STILL O(1) AMORTIZED
---------------------------------------------------------

Suppose we perform:

n append operations.

Most operations cost:

O(1)

Occasionally, a resize costs:

O(n)

But resizing does not happen on every append.

The total cost of many appends is proportional to n.

Therefore:

n append operations
→ O(n) total time

Average cost per append:

O(n) / n
= O(1)

Therefore:

append()
→ O(1) amortized


---------------------------------------------------------
4. SIMPLE EXAMPLE
---------------------------------------------------------

arr = []

for i in range(n):
    arr.append(i)

Total:

O(n)

because each append is O(1) amortized.

Therefore:

Time  → O(n)
Space → O(n)


---------------------------------------------------------
5. AMORTIZED VS WORST CASE
---------------------------------------------------------

For:

arr.append(x)

Amortized:

O(1)

Worst-case individual operation:

O(n)

Therefore:

Do NOT say:

"Every append is always O(1)."

Better interview answer:

"Python list append is O(1) amortized,
although an individual resize can take O(n)."


---------------------------------------------------------
6. DYNAMIC ARRAY IDEA
---------------------------------------------------------

Conceptually:

Start:

[ ]

Append:

[1]

Append:

[1, 2]

Append:

[1, 2, 3]

Eventually capacity becomes full.

Then:

[1, 2, 3, 4]
        ↓
    RESIZE
        ↓
[1, 2, 3, 4, 5, ...]


The expensive resize happens occasionally.


---------------------------------------------------------
7. TOTAL COST IDEA
---------------------------------------------------------

Suppose resize costs occur approximately at:

1
2
4
8
16
32
...

The total copying work is approximately:

1 + 2 + 4 + 8 + ... + n

This geometric series sums to:

O(n)

Therefore, across n appends:

Total work → O(n)

Amortized cost:

O(n) / n
= O(1)


---------------------------------------------------------
8. WHY THIS MATTERS IN DSA
---------------------------------------------------------

Consider:

arr = []

for i in range(n):
    arr.append(i)

A beginner may think:

"Sometimes append copies the whole array,
so this must be O(n²)."

That is incorrect.

The total cost of all resizing operations
is O(n).

Therefore:

Total Time → O(n)


---------------------------------------------------------
9. append() VS insert(0, x)
---------------------------------------------------------

append:

arr.append(x)

→ O(1) amortized


Insert at beginning:

arr.insert(0, x)

→ O(n)

Why?

Because elements must be shifted.

Example:

[10, 20, 30, 40]

insert 5 at index 0:

[5, 10, 20, 30, 40]

Multiple elements move.


---------------------------------------------------------
10. append() VS pop()
---------------------------------------------------------

arr.append(x)

→ O(1) amortized

arr.pop()

→ O(1)

Removing the last element does not require
shifting all remaining elements.


---------------------------------------------------------
11. append() VS pop(0)
---------------------------------------------------------

arr.pop()

→ O(1)


arr.pop(0)

→ O(n)

Because elements after index 0 must shift left.


---------------------------------------------------------
12. AMORTIZED COMPLEXITY IS ABOUT A SEQUENCE
---------------------------------------------------------

One operation:

arr.append(x)

Could occasionally cost:

O(n)


But:

n append operations

have total cost:

O(n)


Therefore:

Amortized cost per operation:

O(1)


---------------------------------------------------------
13. COMMON EXAMPLE: DYNAMIC ARRAY
---------------------------------------------------------

Dynamic arrays are used by many languages.

Concept:

Fixed-size memory
        ↓
Array becomes full
        ↓
Allocate larger memory
        ↓
Copy elements
        ↓
Continue inserting


This gives:

Access:
O(1)

Append:
O(1) amortized

Resize:
O(n) occasionally


---------------------------------------------------------
14. AMORTIZED COMPLEXITY VS WORST CASE
---------------------------------------------------------

Operation             Amortized       Worst Individual

list.append(x)        O(1)            O(n)

list.pop()            O(1)            O(1)

list.pop(0)           O(n)            O(n)

list[i]               O(1)            O(1)


---------------------------------------------------------
15. AMORTIZED COMPLEXITY VS AVERAGE CASE
---------------------------------------------------------

Average-case analysis:

"What is the expected running time
over a distribution of inputs?"

Amortized analysis:

"What is the average cost per operation
over a sequence of operations?"

They answer different questions.


---------------------------------------------------------
16. IMPORTANT PYTHON INTERVIEW ANSWER
---------------------------------------------------------

Question:

"What is the complexity of Python list append?"

Good answer:

"Python list append is O(1) amortized.
Most appends take constant time, but when the
underlying dynamic array needs to resize, an
individual append can take O(n). Across a
sequence of appends, the amortized cost is O(1)."


---------------------------------------------------------
17. SPACE COMPLEXITY
---------------------------------------------------------

Amortized analysis is mainly discussed for
TIME complexity.

For:

arr.append(x)

The list may need additional capacity internally,
but the asymptotic storage for n elements is:

O(n)


---------------------------------------------------------
18. IMPORTANT RULES
---------------------------------------------------------

RULE 1:

Amortized O(1)
does NOT mean every operation is O(1).


RULE 2:

One operation may occasionally be expensive.


RULE 3:

We analyze the total cost across a sequence
of operations.


RULE 4:

Python list append
→ O(1) amortized.


RULE 5:

Python list insert at beginning
→ O(n).


RULE 6:

Python list pop from end
→ O(1).


RULE 7:

Python list pop from beginning
→ O(n).


FINAL MEMORY TRICK:

Occasionally expensive
        +
Mostly cheap
        +
Analyze the whole sequence
        ↓
Amortized Complexity


For Python list append:

Individual worst case → O(n)
Amortized              → O(1)





The key concep -
Don't think:
append()
    ↓
always O(1)


Think:
Most appends → O(1)
Occasional resize → O(n)
        ↓
Across many operations
        ↓
Amortized → O(1)


'''