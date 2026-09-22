from array import *

val = array('i' , [1,2,3,4,5,6,7,8])

# array updation eg: insert, delete, update, append, pop, etc.

val.insert(2, 50) # insert at any position
val.append(100) # append - always goes to last
val[4] = 200 # for replacing existing element or, override the element
for x in val:
  print(x , end=" ") 


