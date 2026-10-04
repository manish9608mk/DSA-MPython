# 682. Baseball Game

'''
PROBLEM

You are given a list of operations for a baseball game.

Initially, the record is empty.

Each operation is one of four types:

1. Integer x
   → Add score x to the record.

2. "C"
   → Remove the previous score from the record.

3. "D"
   → Add double of the previous score.

4. "+"
   → Add the sum of the previous two scores.

Return the sum of all scores remaining in the record
after processing every operation.


Example:

operations = ["5","2","C","D","+"]


Step by step:

"5"
→ [5]

"2"
→ [5,2]

"C"
→ [5]

"D"
→ [5,10]

"+"
→ [5,10,15]


Final sum:

5 + 10 + 15 = 30


Output:

30


Important:

- "C" removes the previous score completely.
- "D" adds a new score; it does not replace the old one.
- "+" adds a new score using the previous two scores.
- All operations are guaranteed to be valid.
'''


'''
PATTERN

Stack / Simulation


Why?

Every operation depends on the most recent valid scores.

"C"
→ remove the last score

"D"
→ use the last score

"+"
→ use the last two scores


A Stack is perfect because it gives:

append() → add a score
pop()    → remove the last score
[-1]     → last score
[-2]     → second-last score


Recognition:

"Previous score"
"Previous two scores"
"Remove last"
"Undo last"
"Last valid element"

→ Think STACK


Mental Pattern:

Process operations one by one
→ Maintain current valid record
→ Use the latest scores whenever required
'''


'''
APPROACH 1 — BRUTE FORCE

Maintain the complete history of operations and use
backward scanning whenever we need previous valid scores.


For "C":

→ Mark the previous score as invalid.


For "D":

→ Scan backward to find the last valid score.
→ Add double of it.


For "+":

→ Scan backward to find the last two valid scores.
→ Add their sum.


Why does it work?

The record can contain invalidated scores, but scanning
backward allows us to find the latest valid scores.


Why is it inefficient?

Every "D" or "+" may require scanning many previous
operations.

In the worst case, many operations repeatedly scan
almost the entire record.


TIME:

O(n²) worst case


SPACE:

O(n)
'''


# BRUTE FORCE CODE

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record = []

        for op in operations:
            if op == "C":
                for i in range(len(record) - 1, -1, -1):
                    if record[i] is not None:
                        record[i] = None
                        break

            elif op == "D":
                for i in range(len(record) - 1, -1, -1):
                    if record[i] is not None:
                        record.append(2 * record[i])
                        break

            elif op == "+":
                last = None
                second_last = None

                for i in range(len(record) - 1, -1, -1):
                    if record[i] is not None:
                        if last is None:
                            last = record[i]
                        else:
                            second_last = record[i]
                            break

                record.append(last + second_last)

            else:
                record.append(int(op))

        return sum(score for score in record if score is not None)


'''
APPROACH 2 — OPTIMAL / STANDARD

Instead of keeping invalid scores and searching backward,
use a Stack containing only valid scores.


For every operation:


Integer:

→ Convert to int
→ Push into stack


"C":

→ Pop the last score


"D":

→ Take the last score
→ Multiply by 2
→ Push the new score


"+":

→ Take the last two scores
→ Add them
→ Push the new score


At every moment:

stack = current valid record


This is the key simplification.

We never need to search backward because the stack
already contains only valid scores.


Example:

[5,2,4]

"C"

→ pop()

→ [5,2]


No invalid value needs to be stored.
'''


'''
WHY STACK?

The problem has Last-In-First-Out behavior.


"C"

removes the most recent score.

That is exactly:

stack.pop()


"D"

needs the most recent score:

stack[-1]


"+"

needs the most recent two scores:

stack[-1]
stack[-2]


So every required operation maps directly to a
stack operation.


Without a stack, we would repeatedly search for the
latest valid scores.

With a stack:

Last score
→ stack[-1]

Second-last score
→ stack[-2]

Remove last
→ stack.pop()

Add new score
→ stack.append()


That gives O(1) work per operation.
'''


'''
STEP-BY-STEP THINKING

1. What is being maintained?

→ The current valid baseball scores.


2. Which operations change the record?

→ All four operations.


3. Does "C" remove the latest score?

→ Yes.


4. Does "D" depend on the latest score?

→ Yes.


5. Does "+" depend on the latest two scores?

→ Yes.


6. What data structure gives direct access to the
   latest elements and can remove the latest element?

→ Stack.


7. What should the stack contain?

→ Only currently valid scores.


8. How do operations map to the stack?

Integer
→ append(int(op))

"C"
→ pop()

"D"
→ append(2 * stack[-1])

"+"
→ append(stack[-1] + stack[-2])


9. What happens after every operation?

→ The stack again represents the current valid record.


10. What do we need at the end?

→ Sum of all values in the stack.


Final Thinking:

Operations
→ Simulate them
→ Maintain valid scores in Stack
→ Sum Stack
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()

            elif op == "D":
                stack.append(2 * stack[-1])

            elif op == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(op))

        return sum(stack)


'''
TEST CASE

operations = ["5","2","C","D","+"]

solution = Solution()

answer = solution.calPoints(operations)

print("Input:", operations)
print("Output:", answer)
'''


'''
OUTPUT

Input: ["5","2","C","D","+"]

Output: 30
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

The stack always contains exactly the valid scores
currently present in the record.


For an integer:

→ We add that score to the record.
→ append() puts it into the stack.


For "C":

→ The latest score is invalidated.
→ pop() removes exactly that score.


For "D":

→ The new score must be twice the latest valid score.
→ stack[-1] gives that score.
→ We append the doubled value.


For "+":

→ The new score must be the sum of the latest two
  valid scores.
→ stack[-1] and stack[-2] give those scores.
→ We append their sum.


Therefore, after every operation:

stack = current valid record


At the end, all remaining scores are exactly the
values inside the stack.

So:

sum(stack)

is the required answer.
'''


'''
DRY RUN

operations = ["5","2","C","D","+"]


Start:

stack = []


Step 1:

Operation = "5"

Integer

→ append(5)

stack = [5]


Step 2:

Operation = "2"

Integer

→ append(2)

stack = [5,2]


Step 3:

Operation = "C"

Remove last score.

→ pop()

stack = [5]


Step 4:

Operation = "D"

Last score:

stack[-1] = 5

Double:

2 × 5 = 10

Append:

stack = [5,10]


Step 5:

Operation = "+"

Last two scores:

5, 10

New score:

5 + 10 = 15

Append:

stack = [5,10,15]


Final:

sum(stack)

= 5 + 10 + 15

= 30


Answer:

30
'''


'''
DRY RUN — IMPORTANT EXAMPLE

operations = ["5","-2","4","C","D","9","+","+"]


Start:

[]


"5"

→ [5]


"-2"

→ [5,-2]


"4"

→ [5,-2,4]


"C"

Remove 4:

→ [5,-2]


"D"

Double the last score:

2 × (-2) = -4

→ [5,-2,-4]


"9"

→ [5,-2,-4,9]


"+"

Last two:

-4, 9

New score:

-4 + 9 = 5

→ [5,-2,-4,9,5]


"+"

Last two:

9, 5

New score:

9 + 5 = 14

→ [5,-2,-4,9,5,14]


Final sum:

5 + (-2) + (-4) + 9 + 5 + 14

= 27


Answer:

27
'''


'''
EDGE CASE 1 — EVERYTHING IS REMOVED

operations = ["1","C"]


"1"

→ [1]


"C"

→ []


Final:

sum([]) = 0


Answer:

0
'''


'''
EDGE CASE 2 — NEGATIVE VALUES

operations = ["5","-2","D"]


"5"

→ [5]


"-2"

→ [5,-2]


"D"

2 × (-2) = -4

→ [5,-2,-4]


The sign must be preserved.

Answer:

5 + (-2) + (-4) = -1
'''


'''
EDGE CASE 3 — "+" AFTER "C"

operations = ["5","2","C","3","+"]


"5"
→ [5]

"2"
→ [5,2]

"C"
→ [5]

"3"
→ [5,3]

"+"
→ 5 + 3 = 8

→ [5,3,8]


The important point:

After "C", the removed score is no longer considered.

The stack automatically handles this.
'''


'''
EDGE CASE 4 — MULTIPLE "D"

operations = ["5","D","D"]


5

→ [5]


D:

2 × 5 = 10

→ [5,10]


D:

2 × 10 = 20

→ [5,10,20]


Each "D" uses the current last score.
'''


'''
EDGE CASE 5 — DUPLICATE SCORES

operations = ["5","5","+"]


[5]

→ [5,5]

"+":

5 + 5 = 10

→ [5,5,10]


Duplicate values are completely valid.
'''


'''
TIME & SPACE COMPLEXITY

Let:

n = number of operations


Each operation performs only constant-time work:

Integer
→ append()

"C"
→ pop()

"D"
→ stack[-1] + append()

"+"
→ stack[-1] + stack[-2] + append()


Therefore:

TIME = O(n)


The stack can contain up to n scores.

Therefore:

SPACE = O(n)


Final:

Time  → O(n)
Space → O(n)
'''


'''
INTERVIEW EXPLANATION

"I would use a stack because every operation depends on
the most recent one or two valid scores, and 'C' removes
the most recent score.

For an integer, I push it into the stack.

For 'C', I pop the last score.

For 'D', I push twice the last score.

For '+', I push the sum of the last two scores.

The stack always represents the current valid record,
so after processing all operations I return sum(stack).

The time complexity is O(n) and the space complexity is O(n)."
'''


'''
RECOGNITION TRICKS

1. "Remove the previous score"

→ Stack


2. "Use the previous score"

→ stack[-1]


3. "Use the previous two scores"

→ stack[-1], stack[-2]


4. "Undo the last operation"

→ Stack is a strong candidate.


General pattern:

Last element
→ Stack

Remove last
→ pop()

Add new result
→ append()


For this problem:

Integer
→ Push

C
→ Pop

D
→ Double top and push

+
→ Sum top two and push
'''


'''
REUSABLE TEMPLATE

Stack simulation:

stack = []

for op in operations:

    if op == "C":
        stack.pop()

    elif op == "D":
        stack.append(2 * stack[-1])

    elif op == "+":
        stack.append(stack[-1] + stack[-2])

    else:
        stack.append(int(op))

answer = sum(stack)


Remember:

append → add
pop    → remove last
[-1]   → last
[-2]   → second-last
'''


'''
FAMILY

This belongs to the Stack / Simulation family.


Common ideas:

- Undo operations
- Remove last element
- Previous element
- Previous two elements
- Expression evaluation
- Maintaining recent state
- Browser history
- Backtracking through recent actions


Important recognition:

Need latest element
→ Stack


Need latest two elements
→ Stack


Need remove latest element
→ Stack


Need maintain current state while processing operations
→ Stack / Simulation
'''


'''
COMMON INTERVIEW MISTAKES

1. "D" replaces the previous score.

Wrong:

[5]

D

→ [10]


Correct:

[5]

D

→ [5,10]


2. "+" replaces the previous two scores.

Wrong:

[5,10]

+

→ [15]


Correct:

[5,10]

+

→ [5,10,15]


3. Using the wrong scores for "+"

Correct:

stack[-1] + stack[-2]


4. Forgetting that "C" changes the record.

After:

[5,2,4]

"C"

the record becomes:

[5,2]


Any following operation must use this updated stack.


5. Forgetting to convert integer operations from strings.

Use:

int(op)


6. Overcomplicating the problem.

We do not need:

- Sorting
- Hash Map
- Heap
- Binary Search
- Recursion


The operation rules already match a Stack perfectly.


7. Searching backward for previous scores.

If the data structure contains only valid scores,
the latest valid scores are already at the top.
'''


'''
MOST IMPORTANT THING TO REMEMBER

The complete pattern:

Baseball Game
→ Operation Simulation
→ Need latest scores
→ Use Stack


Operation mapping:

Integer
→ append(int(op))


"C"
→ pop()


"D"
→ append(2 * stack[-1])


"+"
→ append(stack[-1] + stack[-2])


Final:

→ sum(stack)


One-line rule:

Previous / Last / Undo / Remove Last
→ STACK


Final Mental Model:

Integer → PUSH

C → POP

D → 2 × TOP → PUSH

+ → TOP + SECOND TOP → PUSH

Then:

SUM THE STACK


Think:

"Keep only the valid scores,
and let the stack represent the current record."
'''