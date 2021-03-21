# Python code to demonstrate the working of
# pop() and remove()

import array as arr

# Python code to demonstrate the working of
# pop() and remove()
arr1=arr.array('i',[1,2,3,1,5])

#printing original array
print("The new created array is: ",end=" ")
for i in range(0,5):
  print(arr1[i],end=" ")
print("\r")

# using pop() to remove element at 2nd position
print("The popped elements is: ",end=" ")
print(arr1.pop(2))

# printing array after popping
print("The array after popping is: ",end=" ")
for i in range(0,4):
  print(arr1[i],end=" ")
print("\r")

# using remove() to remove 1st occurrence of 1
arr1.remove(1)
print("After removing elements in the array is: ",end=" ")
for i in range(0,3):
  print(arr1[i],end=" ")
print("\r")
