from array import *

val = array('i' , [1,2,3,4,5,6,7,8,9])

# slicing rule
# new_array = val[start index : end index]

print()
# suppose we want only 3 4 5
new_array = val[2 : 5]

for i in range(0, len(new_array)):
  print(new_array[i], end=" ") # o/p: 3 4 5 


print()
# suppose we dont want last 3 element
new_array = val[2 : -3]

for i in range(0, len(new_array)):
  print(new_array[i], end=" ") # o/p: 3 4 5 6


print()
# let's say we want to reverse an existing array
new_array = val[ : : -1]

for i in range(0, len(new_array)):
  print(new_array[i], end=" ")