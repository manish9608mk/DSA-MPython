# Now we are studying multi dimensional array
from numpy import *


# ex1 
# zero dimensional array
zero_dim = array(10)
print(zero_dim) # 10

# ex2
# one dimensional array or 1D array
one_dim = array([1,2,3,4,5,6,7,8])
print(one_dim) # [1 2 3 4 5 6 7 8]

# ex3 
# two dimensional array or 2D array
# it is a collection of one dimensional array or 1D array
two_dim = array([ [1,2,3], [4,5,6], [7,8,9]]) # its a 3x3 2 dimensional arr
print(two_dim)
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]
'''

# ex4 
# three dimensional array or 3D array
# it is a collection of 2D array 
three_dim = array([ [ [1,2],[3,4]] , [ [5,6],[7,8]] ])
print(three_dim)
'''
[[[1 2]
  [3 4]]

 [[5 6]
  [7 8]]]
'''

# similarly issi tarah ham kisi bhi dimension ka array bana sakte hain
