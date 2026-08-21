# 5. Loop Complexity
'''
Loop Complexity
================

The basic rule:

1. One loop running n times
   → O(n)

2. Two sequential loops
   → O(n) + O(n)
   → O(2n)
   → O(n)

3. Nested loops
   → O(n) * O(n)
   → O(n²)

4. Loop where the input is divided/multiplied by a constant
   → O(log n)

5. Outer O(n) loop + inner O(log n) loop
   → O(n log n)

6. Nested loops with different input sizes
   → Multiply the complexities
'''


# ---------------------------------------------------------
# 1. SINGLE LOOP → O(n)
# ---------------------------------------------------------

'''
for i in range(n):
    print(i)

The loop runs n times.

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 2. LOOP WITH CONSTANT WORK → O(n)
# ---------------------------------------------------------

'''
for i in range(n):
    x = i * 2
    print(x)

Each iteration performs constant work O(1).

n iterations × O(1) work

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 3. TWO SEQUENTIAL LOOPS → O(n)
# ---------------------------------------------------------

'''
for i in range(n):
    print(i)

for j in range(n):
    print(j)

First loop  → O(n)
Second loop → O(n)

Total:
O(n) + O(n)
= O(2n)
= O(n)

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 4. THREE SEQUENTIAL LOOPS → O(n)
# ---------------------------------------------------------

'''
for i in range(n):
    print(i)

for j in range(n):
    print(j)

for k in range(n):
    print(k)

O(n) + O(n) + O(n)
= O(3n)
= O(n)

Constants are ignored.

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 5. NESTED LOOP → O(n²)
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(n):
        print(i, j)

Outer loop  → n times
Inner loop  → n times for every outer iteration

Total:
n × n
= n²

Time  → O(n²)
Space → O(1)
'''


# ---------------------------------------------------------
# 6. THREE NESTED LOOPS → O(n³)
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(n):
        for k in range(n):
            print(i, j, k)

n × n × n
= n³

Time  → O(n³)
Space → O(1)
'''


# ---------------------------------------------------------
# 7. NESTED LOOP WITH CONSTANT INNER LOOP → O(n)
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(5):
        print(i, j)

Outer loop → n
Inner loop → 5

n × 5
= 5n
= O(n)

Because 5 is a constant.

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 8. NESTED LOOP WITH DIFFERENT INPUT SIZE → O(n × m)
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(m):
        print(i, j)

Outer loop → n
Inner loop → m

Total:
n × m

Time → O(n × m)
Space → O(1)

Do NOT write O(n²) unless n and m represent the same input size.
'''


# ---------------------------------------------------------
# 9. TRIANGULAR LOOP → O(n²)
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(i):
        print(i, j)

Number of iterations:

0 + 1 + 2 + 3 + ... + (n - 1)

This is:

n(n - 1) / 2

Ignoring constants and lower-order terms:

O(n²)

Time  → O(n²)
Space → O(1)
'''


# ---------------------------------------------------------
# 10. LOOP INCREASING BY 2 → O(n)
# ---------------------------------------------------------

'''
for i in range(0, n, 2):
    print(i)

The loop runs approximately n/2 times.

n/2
= O(n)

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 11. LOOP INCREASING BY CONSTANT k → O(n)
# ---------------------------------------------------------

'''
for i in range(0, n, k):
    print(i)

The loop runs approximately n/k times.

Since k is constant:

O(n/k)
= O(n)

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 12. LOOP DOUBLING EACH TIME → O(log n)
# ---------------------------------------------------------

'''
i = 1

while i < n:
    print(i)
    i *= 2

Values:

1
2
4
8
16
32
...

After k iterations:

2^k = n

Therefore:

k = log₂(n)

Time  → O(log n)
Space → O(1)
'''


# ---------------------------------------------------------
# 13. LOOP HALVING EACH TIME → O(log n)
# ---------------------------------------------------------

'''
i = n

while i > 1:
    print(i)
    i //= 2

Values:

n
n/2
n/4
n/8
n/16
...

The value is divided by 2 each time.

Time  → O(log n)
Space → O(1)
'''


# ---------------------------------------------------------
# 14. OUTER O(n) + INNER O(log n) → O(n log n)
# ---------------------------------------------------------

'''
for i in range(n):
    j = 1

    while j < n:
        print(i, j)
        j *= 2

Outer loop  → O(n)
Inner loop  → O(log n)

Total:

O(n) × O(log n)
= O(n log n)

Time  → O(n log n)
Space → O(1)
'''


# ---------------------------------------------------------
# 15. LOOP INSIDE LOOP WITH DIFFERENT COMPLEXITIES
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(m):
        print(i, j)

Time:

O(n × m)

If n == m:

O(n²)

But if n and m are independent:

O(n × m)
'''


# ---------------------------------------------------------
# 16. SEQUENTIAL DIFFERENT COMPLEXITIES
# ---------------------------------------------------------

'''
for i in range(n):
    print(i)

for j in range(m):
    print(j)

Complexity:

O(n) + O(m)

Therefore:

O(n + m)

NOT O(n × m)
'''


# ---------------------------------------------------------
# 17. NESTED DIFFERENT COMPLEXITIES
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(m):
        print(i, j)

Complexity:

O(n × m)

Nested loops → Multiply
'''


# ---------------------------------------------------------
# 18. LOOP WITH EARLY BREAK
# ---------------------------------------------------------

'''
for x in arr:
    if x == target:
        break

Best case:
Target is first element.

Time → O(1)

Worst case:
Target is last element or doesn't exist.

Time → O(n)

Interview answer:

Time → O(n) worst case
Space → O(1)
'''


# ---------------------------------------------------------
# 19. LOOP WITH CONDITIONAL WORK
# ---------------------------------------------------------

'''
for x in arr:
    if x > 0:
        print(x)

The condition is O(1).
The loop runs n times.

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 20. TWO NESTED LOOPS WITH DIFFERENT RANGES
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(i, n):
        print(i, j)

Number of iterations:

n + (n-1) + (n-2) + ... + 1

= n(n+1)/2

= O(n²)

Time  → O(n²)
Space → O(1)
'''


# ---------------------------------------------------------
# 21. NESTED LOOP THAT DOES NOT ALWAYS RUN n TIMES
# ---------------------------------------------------------

'''
for i in range(n):
    for j in range(10):
        print(i, j)

Inner loop runs only 10 times.

n × 10
= 10n
= O(n)

Time  → O(n)
Space → O(1)
'''


# ---------------------------------------------------------
# 22. IMPORTANT RULES TO REMEMBER
# ---------------------------------------------------------

'''
RULE 1:
Single loop over n
→ O(n)


RULE 2:
Sequential loops
→ ADD

O(n) + O(n)
→ O(n)


RULE 3:
Nested loops
→ MULTIPLY

O(n) × O(n)
→ O(n²)


RULE 4:
Different input sizes

O(n) + O(m)
→ O(n + m)

O(n) × O(m)
→ O(n × m)


RULE 5:
Loop doubles/halves
→ O(log n)


RULE 6:
O(n) loop + O(log n) loop nested
→ O(n log n)


RULE 7:
Constants are ignored

O(5n) → O(n)
O(100n) → O(n)
O(n² + n) → O(n²)


RULE 8:
Keep the dominant term

O(n² + n + 1)
→ O(n²)

O(n + log n)
→ O(n)


RULE 9:
Early break

Best case may be O(1),
but worst case can be O(n).


RULE 10:
Always analyze the actual number of iterations.
Don't decide complexity only by counting the number of "for" loops.





The 5 patterns you absolutely must recognize:

Single loop                  → O(n)

Two sequential loops         → O(n)

Nested loops                 → O(n²)

Doubling / halving           → O(log n)

O(n) loop + O(log n) nested  → O(n log n)
'''