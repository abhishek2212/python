# Python code to demonstrate the working of
# array(), append(), insert()

import array as arr

arr1=arr.array('i',[1,2,3,4])
print("the new created array is: ",end=" ")
for i in range(0,3):
  print(arr1[i],end=" ")
print("\r") 

#usig append() to insert new value at the end 
arr1.append(4)

#printing appended array
print("The appended array is: ",end=" ")
for i in range(0,4):
  print(arr1[i],end=" ")
print("\r")

# using insert() to insert value at specific position
# inserts 5 at 2nd position
arr1.insert(2,5)


#printing array after insertion
print("The array after insertion is: ",end=" ")
for i in range(0,5):
  print(arr1[i],end=" ")
print("\r")