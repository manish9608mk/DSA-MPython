# Note: DON'T REMEMBER

#1 Big-O
'''
Big-O describes the growth rate of an algorithm.
Big-O describes how the resource usage grows as input size n grows.

The most important complexities for interviews:

O(1)          Constant
O(log n)      Logarithmic
O(n)          Linear
O(n log n)    Linearithmic
O(n²)         Quadratic
O(n³)         Cubic
O(2ⁿ)         Exponential
O(n!)         Factorial

Generally:
Better
  ↑
O(1)
O(log n)
O(n)
O(n log n)
O(n²)
O(n³)
O(2ⁿ)
O(n!)
  ↓
Worse

'''

#2 Python-specific complexity or omplexity of Python's built-ins.
#  - List
'''
arr[i]              → O(1)
arr.append(x)       → O(1) amortized
arr.pop()            → O(1)
arr.pop(i)           → O(n)
arr.insert(i, x)     → O(n)
x in arr             → O(n)
arr.remove(x)        → O(n)
arr.reverse()        → O(n)
arr.sort()           → O(n log n)
arr.copy()           → O(n)
'''
# Python Dictionary & Set Complexity.
'''
Dictionary

d[key]           # O(1) average
d[key] = value   # O(1) average
d.get(key)       # O(1) average
d.pop(key)       # O(1) average
key in d         # O(1) average

Set

s.add(x)         # O(1) average
s.remove(x)      # O(1) average
s.discard(x)     # O(1) average
x in s           # O(1) average
s.pop()          # O(1) average
'''

# 3. Python String Complexity

'''
s[i]                 → O(1)
len(s)               → O(1)
x in s               → O(n)
s + t                → O(n + m)
s.lower()             → O(n)
s.upper()             → O(n)
s.strip()             → O(n)
s.split()             → O(n)
s.replace(a, b)       → O(n)
s[::-1]               → O(n)
s.count(x)            → O(n)
'''

