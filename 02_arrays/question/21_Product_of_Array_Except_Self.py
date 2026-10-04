# 238. Product of Array Except Self

'''
PROBLEM

Given an integer array nums, return an array answer such that:

answer[i] = product of every element in nums except nums[i].

Example:

nums = [1,2,3,4]

For index 0:

2 × 3 × 4 = 24

For index 1:

1 × 3 × 4 = 12

For index 2:

1 × 2 × 4 = 8

For index 3:

1 × 2 × 3 = 6

Therefore:

answer = [24,12,8,6]


Important:

- Do not use division.
- Time complexity must be O(n).
- The follow-up asks for O(1) extra space.
- The output array does not count as extra space.
- Zeros can appear in the input.
'''


'''
PATTERN

Prefix Product + Suffix Product


For every index i:

answer[i]
=
product of elements on the left
×
product of elements on the right


Example:

nums = [1,2,3,4]

             i
             ↓
[1,2]      [3,4]

Left product:
1 × 2

Right product:
4

answer[2] = 2 × 4 = 8


Recognition:

"Product except self"
→ Prefix + Suffix


Main idea:

Everything except nums[i]
→ Left side + Right side
→ Prefix product × Suffix product


Mental pattern:

Left product
×
Right product
=
Product except self
'''


'''
APPROACH 1 — BRUTE FORCE

For every index i, multiply every element except nums[i].


Example:

nums = [1,2,3,4]

For i = 0:

2 × 3 × 4 = 24

For i = 1:

1 × 3 × 4 = 12

And so on.


Why does it work?

For each position, we directly calculate exactly
what the problem asks for.


Why is it inefficient?

We repeat almost the same multiplications for every index.

For n elements:

n positions × O(n) work

→ O(n²)


TIME:

O(n²)


SPACE:

O(1) extra space
'''


'''
# BRUTE FORCE CODE
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        for i in range(n):
            product = 1

            for j in range(n):
                if i != j:
                    product *= nums[j]

            answer[i] = product

        return answer


'''
APPROACH 2 — PREFIX + SUFFIX ARRAYS

We can avoid repeated multiplication by precomputing:

1. Product of everything to the left.
2. Product of everything to the right.


Example:

nums = [1,2,3,4]


Prefix products excluding current element:

[1,1,2,6]

Meaning:

index 0 → nothing on left → 1
index 1 → 1
index 2 → 1 × 2 = 2
index 3 → 1 × 2 × 3 = 6


Suffix products excluding current element:

[24,12,4,1]


Then:

answer[i] = prefix[i] × suffix[i]


Therefore:

[1×24, 1×12, 2×4, 6×1]

→ [24,12,8,6]


TIME:

O(n)


SPACE:

O(n)

because we store prefix and suffix arrays.

This satisfies the main O(n) requirement,
but not the O(1) extra-space follow-up.
'''


'''
APPROACH 3 — OPTIMAL / STANDARD

We can reuse the output array for the prefix products.

Then we only need one variable to maintain the suffix product.


PASS 1 — LEFT TO RIGHT

Store the product of all elements before i
in answer[i].


Example:

nums = [1,2,3,4]

Start:

answer = [1,1,1,1]
prefix = 1


i = 0:

answer[0] = prefix = 1
prefix *= nums[0]

prefix = 1


i = 1:

answer[1] = 1
prefix *= 2

prefix = 2


i = 2:

answer[2] = 2
prefix *= 3

prefix = 6


i = 3:

answer[3] = 6
prefix *= 4


Now:

answer = [1,1,2,6]


This array contains the left products.


PASS 2 — RIGHT TO LEFT

Maintain:

suffix = product of elements after i


At each index:

answer[i] *= suffix

Then:

suffix *= nums[i]


For:

answer = [1,1,2,6]


i = 3:

answer[3] = 6 × 1 = 6
suffix = 4


i = 2:

answer[2] = 2 × 4 = 8
suffix = 12


i = 1:

answer[1] = 1 × 12 = 12
suffix = 24


i = 0:

answer[0] = 1 × 24 = 24


Final:

[24,12,8,6]


TIME:

O(n)


SPACE:

O(1) extra space

The output array is not counted.
'''


'''
WHY PREFIX + SUFFIX?

For index i, nums[i] itself should not be included.

So split the array around i:

[ elements before i ] [ nums[i] ] [ elements after i ]


Everything except nums[i] is exactly:

left product × right product


Instead of recalculating these products for every i,
we calculate them incrementally.

Prefix handles the left side.

Suffix handles the right side.


This also works with zero values without any special case.
'''


'''
WHY USE THE OUTPUT ARRAY?

If we create:

prefix[]
suffix[]

we use O(n) extra space.


But answer[] already has to be returned.

So we can store the prefix product directly in answer.

After that, the suffix product can be maintained with
one variable.


Therefore:

Output array
→ stores prefix product

One variable
→ stores suffix product


Extra space:

O(1)
'''


'''
STEP-BY-STEP THINKING

1. What is answer[i]?

→ Product of every element except nums[i].


2. What makes this difficult?

→ We cannot use division.


3. How can I describe "everything except i"?

→ Everything before i + everything after i.


4. What are those products called?

→ Prefix product and suffix product.


5. Can I calculate prefix products efficiently?

→ Yes, with a left-to-right pass.


6. Can I calculate suffix products efficiently?

→ Yes, with a right-to-left pass.


7. Do I need separate prefix and suffix arrays?

→ No.


8. Where can I store the prefix product?

→ In the output array.


9. How do I store the suffix product?

→ One variable.


10. Final complexity?

→ O(n) time and O(1) extra space.


Final thinking:

Product except self
→ Left product × right product
→ Two passes
→ Reuse answer array
→ O(n), O(1)
'''


'''
# OPTIMAL CODE
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        answer = [1] * n

        prefix = 1

        # Product of all elements to the left.
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]

        suffix = 1

        # Multiply by product of all elements to the right.
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]

        return answer



# TEST CASE

nums = [1,2,3,4]

solution = Solution()

answer = solution.productExceptSelf(nums)

print("Input:", nums)
print("Output:", answer)



'''
OUTPUT

Input: [1,2,3,4]

Output: [24,12,8,6]
'''


'''
WHY DOES THE OPTIMAL APPROACH WORK?

For every index i, we need:

product of all elements except nums[i]


Those elements can be divided into two groups:

1. Elements before i.
2. Elements after i.


Therefore:

answer[i]
=
left_product × right_product


The first pass stores left_product in answer[i].


The second pass maintains right_product and multiplies
it into answer[i].


So after both passes:

answer[i]
=
product of everything before i
×
product of everything after i


nums[i] is never included in either product.

Therefore answer[i] is exactly the required product.


The algorithm is correct for every index,
and it also works when nums contains zeroes.
'''


'''
DRY RUN

nums = [1,2,3,4]


FIRST PASS — PREFIX

Start:

answer = [1,1,1,1]
prefix = 1


Step 1:

i = 0

answer[0] = 1

prefix = 1 × 1
prefix = 1


Step 2:

i = 1

answer[1] = 1

prefix = 1 × 2
prefix = 2


Step 3:

i = 2

answer[2] = 2

prefix = 2 × 3
prefix = 6


Step 4:

i = 3

answer[3] = 6

prefix = 6 × 4
prefix = 24


After first pass:

answer = [1,1,2,6]


SECOND PASS — SUFFIX

Start:

suffix = 1


Step 1:

i = 3

answer[3] = 6 × 1
= 6

suffix = 1 × 4
= 4


Step 2:

i = 2

answer[2] = 2 × 4
= 8

suffix = 4 × 3
= 12


Step 3:

i = 1

answer[1] = 1 × 12
= 12

suffix = 12 × 2
= 24


Step 4:

i = 0

answer[0] = 1 × 24
= 24


Final:

answer = [24,12,8,6]
'''


'''
DRY RUN — ZERO

nums = [-1,1,0,-3,3]


Focus on index 2:

nums[2] = 0


Product on the left:

-1 × 1 = -1


Product on the right:

-3 × 3 = -9


Therefore:

answer[2] = (-1) × (-9)
          = 9


For the other positions,
their left or right side includes the zero.

Therefore their products become 0.


Final:

[0,0,9,0,0]


No special zero handling is required.
'''


'''
EDGE CASE 1 — ONE ZERO

nums = [1,2,0,4]

Only the position containing zero can have a non-zero answer.

For zero:

1 × 2 × 4 = 8

For every other position:

product contains zero → 0

Answer:

[0,0,8,0]
'''


'''
EDGE CASE 2 — MULTIPLE ZEROES

nums = [1,0,3,0]

Every answer is 0.

Why?

For every index, at least one zero remains
in the product of the other elements.


Answer:

[0,0,0,0]
'''


'''
EDGE CASE 3 — NEGATIVE VALUES

nums = [-1,1,0,-3,3]

Negative values work normally because multiplication
is handled directly.

No change to the algorithm is required.
'''


'''
EDGE CASE 4 — NO ZEROES

nums = [1,2,3,4]

Normal prefix/suffix multiplication produces:

[24,12,8,6]
'''


'''
TIME & SPACE COMPLEXITY

There are two passes through the array.

First pass:

O(n)


Second pass:

O(n)


Total:

TIME = O(n)


The algorithm uses only:

- answer array
- prefix variable
- suffix variable


The output array does not count as extra space.

Therefore:

SPACE = O(1) extra space
'''


'''
INTERVIEW EXPLANATION

"Each answer[i] is the product of everything to the left
of i multiplied by everything to the right of i.

So I use two passes.

In the first pass, I store the prefix product in the
output array.

In the second pass, I traverse from right to left while
maintaining a suffix product and multiply it into the
output array.

This avoids division, works with zeroes, runs in O(n)
time, and uses O(1) extra space apart from the output."
'''


'''
RECOGNITION TRICKS

1. "Product of everything except current element"

→ Think prefix + suffix.


2. "No division"

→ Do not use total_product / nums[i].


3. Every answer depends on:

→ Left side
→ Right side


4. Need O(1) extra space

→ Reuse the output array.


Quick recognition:

Except self
→ Split around current index
→ Prefix × suffix
'''


'''
REUSABLE TEMPLATE

answer = [1] * n


# Prefix pass
prefix = 1

for i in range(n):
    answer[i] = prefix
    prefix *= nums[i]


# Suffix pass
suffix = 1

for i in range(n - 1, -1, -1):
    answer[i] *= suffix
    suffix *= nums[i]


return answer


Core template:

Left product
→ store in answer

Right product
→ multiply in reverse

'''
 

'''
FAMILY

Prefix / Suffix Problems


Related ideas:

- Prefix sums
- Prefix products
- Suffix products
- Running products
- Running sums
- Range product/sum problems


Important distinction:

Need information from the left
→ Prefix


Need information from the right
→ Suffix


Need both sides excluding current position
→ Prefix + Suffix
'''


'''
COMMON INTERVIEW MISTAKES

1. Using division.

Not allowed.


2. Including nums[i] in the prefix product.

Correct order:

answer[i] = prefix
prefix *= nums[i]


3. Including nums[i] in the suffix product.

Correct order:

answer[i] *= suffix
suffix *= nums[i]


4. Creating unnecessary prefix and suffix arrays.

That uses O(n) extra space.

The optimal solution reuses answer[].


5. Forgetting that the prefix/suffix product at the
   boundary should be 1.

For index 0:

nothing exists on the left
→ product = 1

For the last index:

nothing exists on the right
→ product = 1


6. Handling zeroes with complicated special cases.

The prefix/suffix method handles them naturally.


7. Using nested loops.

That gives O(n²), which is too slow for n = 10^5.
'''


'''
MOST IMPORTANT THING TO REMEMBER

Complete pattern:

Product Except Self
→ Do not use division
→ Split around current index
→ Left product × right product
→ Prefix pass
→ Suffix pass
→ Reuse answer array
→ O(n) time
→ O(1) extra space


One-line rule:

Product Except Self
→ Prefix × Suffix
→ Store Prefix in Answer
→ Multiply Suffix from Right


Formula:

answer[i]
=
(product before i)
×
(product after i)


Final mental model:

        nums[i]
           ↓
[ LEFT ] [ X ] [ RIGHT ]

answer[i]
= LEFT PRODUCT × RIGHT PRODUCT


Implementation:

Left → Right
→ build prefix

Right → Left
→ apply suffix


Most important code pattern:

answer[i] = prefix
prefix *= nums[i]

answer[i] *= suffix
suffix *= nums[i]
'''