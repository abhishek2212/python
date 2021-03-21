# Python code to demonstrate the working of
# index() and reverse()

# importing "array" for array operations
import array as arr

# initializing array with array values
# initializes array with signed integers
arr1 = arr.array('i', [1,2,3,1,2,5])

# printing original array
print("The created new array is: ", end="")
for i in range(0, 6):
    print(arr1[i], end=" ")
print("\r")

# using index() to print index of 1st occurrenece of 2
print("The index of 1st occurance of 2 is: ",end="")
print(arr1.index(2))

#using reverse() to reverse the array
arr1.reverse()


# printing array after reversing
print("The array after reversing is: ",end="")
for i in range(0,6):
  print(arr1[i],end=" ")
print("\r")

txt = "I wonder how this text looks like backwards"
print(txt[::-1])

print(txt)

j=10
print("this is true") if j==10 else print("This is false") 