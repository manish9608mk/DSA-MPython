from array import *

# Suppose the user wants to create an array,
# but we do not know in advance how many elements
# the user wants to store. so, 

# 1. Create an empty array
arr = array('i', [])

# 2. Ask the user how many elements they want
n = int(input("Enter a number: "))

# 3. Take input for each element
for i in range(0, n):
    arr.append(int(input("Enter next input: ")))

# 4. Print the array elements
for i in range(0, n):
    print(arr[i], end=" ")






print("\n")
# in detail explanation

# 1. Create an empty integer array.
# 'i' means the array will store integers.
# [] means the array is empty initially.
arr = array('i', [])

# 2. Ask the user how many elements
# they want to enter into the array.
n = int(input("Enter a number: "))

# 3. Use a loop to take input one by one.
# The loop runs 'n' times because the user
# wants to enter 'n' elements.
for i in range(0, n):
    arr.append(int(input("Enter next input: ")))

# 4. Now print all the elements of the array.
# The loop visits every index one by one.
for i in range(0, n):
    print(arr[i], end=" ")


'''
IMPORTANT:

n       → tells us how many elements are in the array.

i       → represents the current index while looping.

arr[i]  → gives the element stored at index i.


Example:

arr = [10, 20, 30, 40, 50]

Index:    0   1   2   3   4
          ↓   ↓   ↓   ↓   ↓
Element: 10  20  30  40  50


If:

i = 0
arr[i] = arr[0] = 10

If:

i = 2
arr[i] = arr[2] = 30

If:

i = 4
arr[i] = arr[4] = 50


So remember:

n     → how many elements
i     → current index
arr[i] → element at that index


The main idea to remember -
Think of the flow as:

User tells size
      ↓
     n
      ↓
Run loop n times
      ↓
Take each element
      ↓
arr.append(element)
      ↓
Array is ready
      ↓
Run loop again
      ↓
arr[i] → access each element

One small point: in Python DSA, you'll usually work with list rather than array('i'). The array module is still useful for understanding typed arrays and how arrays work internally, but for most coding-interview problems, list is the standard choice.

'''