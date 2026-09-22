from array import *

# let say we want new array of of existing array also called as copy then,

val = array('i' , [1,2,3,4,5,6,7,8])

copy_array = array(val.typecode , (x for x in val))

# ex1
# using enhanced loop
for x in val:
  print(x, end=" ") # o/p: 1 2 3 4 5 6 7 8 

print() # or,

# ex2
# using normal loop
for i in range(0, len(val)):
  print(copy_array[i] , end=",") # o/p: 1,2,3,4,5,6,7,8,


print()
# ex3
# copy karke ab ham koi bhi operation kar sakte hain ispe 
# eg: multiply by 2 in whole existing array
copy_array_operation = array(val.typecode , ( (x*2) for x in val))

for i in range(0, len(val)):
  print(copy_array_operation[i], end="  ") # o/p: 2  4  6  8  10  12  14  16 


'''
issi tarike se ham log old array se new array bana sakte hain
'''


print()
# ex4
# pop function use when we know the position of index
# now let's say we have to delete any element 
copy_array_operation.pop(3) # with index

for i in range(0, len(copy_array_operation)):
  print(copy_array_operation[i], end=" ") # o/p: 2 4 6 10 12 14 16

print()
# now its beahving like a stack
copy_array_operation.pop() # without index

for i in range(0, len(copy_array_operation)):
  print(copy_array_operation[i], end=" ") # o/p: 2 4 6 10 12 14


print()
# ex5
# remove function is use when we the exact element to remove 
copy_array_operation.remove(10)

for i in range(0, len(copy_array_operation)):
  print(copy_array_operation[i], end=" ") # o/p: 2 4 6 12 14
