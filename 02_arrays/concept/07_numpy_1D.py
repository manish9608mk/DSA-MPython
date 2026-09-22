# why numpy
# suppose we want multiple dimensional array like 2D, 3D array 
# then we cannot do that using array import module 
# so, thats why in this case we are using numpy

# and ab ismein typecode bhi batane ki jaurat nhi hai 

from numpy import *

# ex1
val = array([1,2,3,4,5,6,7,8])

for i in range(0, len(val)):
  print(i , end=" ") # 0 1 2 3 4 5 6 7 

# or,
print()

# using enhanced loop
for x in val:
  print(x , end=",") # 1,2,3,4,5,6,7,8,


# ex2
# aise case mein typecode batana parta tha in array module but, in numpy don't
print("\n")
value_int = array([1, 2.6, 3, 4.5, 5])
value_str = array([1, 'b', 3, 'a', 4, 3.9])
value_type_casting = array([2,3,4,5,6] , float)

# iss cose mein 10 se 20 tak ke element 5 part mein divide ho jayega and agar uska ek arr bhi banana chate ho toh iss tarike se kar sakte ho and note: 10 and 20 included hoga 
value_linspace = linspace(10 , 20 , 6) 

value_arange = arange(10 , 20 , 2) # here in third parameter mein common difference denge, or har ek element dusre element se kitne distance pe hoga and note: here 10 is included and 20 is excluded 

value_logspace = logspace(10 , 20 , 2)
value_zero = zeros(10) # zeros ka array bana sakte ho, sare elemrnt 0 ho jayega
value_ones = ones(10) # ismein sare element on ho jayega 

# now suppose agar mujhe zeros and ones ke alawa kisi aur element ka array banana hai then we use - full()
# full(size, values)
value_full = full(10, 7)



for x in value_int:
  print(x , end=" ") # 1.0 2.6 3.0 4.5 5.0

print()
for x in value_str:
  print(x , end=" ") # 1 b 3 a 4 3.9

print()
for x in value_type_casting:
  print(x, end=" ") # 2.0 3.0 4.0 5.0 6.0

print()
for x in value_linspace:
  print(x, end="  ") # 10.0  12.0  14.0  16.0  18.0  20.0

print()
for x in value_arange:
  print(x, end=" ") # 10 12 14 16 18

print()
for x in value_logspace:
  print(x, end=" ") # 10000000000.0 1e+20

print()
for x in value_zero:
  print(x, end=" ") # 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0 0.0

print()
for x in value_ones:
  print(x, end=" ") # 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0 1.0

print()
for x in value_full:
  print(x, end=" ") # 7 7 7 7 7 7 7 7 7 7