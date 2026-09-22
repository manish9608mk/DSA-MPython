# import array
# val = array.array('i' , [1,2,3,4,5,6,7,8,9])

# import array as arr
# val = arr.array('i' , [1,2,3,4,5,6,7,8,9])

from array import *   # better approach
val = array('i' , [1,2,3,4,5,6,7,8,9]) # hre 'i' is type code i means int, d means float, etc.

# 01
print(val) # instead of this we we loop

# 02
for i in range(0,7):
  # print(val[i])
  print(val[i], end=" ")

# 02.1
print()
for i in range(0, len(val)):
  # print(val[i])
  print(val[i], end=" ")

# 03
# using in enhanced for loop: now we dont need index
# val ka jo element ab ek ek karke x name ke variable mein aate jayenga jitna array ka size hai utna bar size mention karne ki jaurat nahi hai
print()
for x in val:
  print(x, end=",")



print("\n-----------------------")
# 04
# more functionalities of array

print(len(val)) # for finding length
print(val.typecode) # for finding typecode

val.reverse() # for reversing
# for i in range(0, len(val)):
#   print(val[i], end=" ")
# or,
for x in val:
  print(x , end=" ")




