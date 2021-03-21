#A user can treat lists as arrays.
import array as arr
list=[1,2,3,4]
a=arr.array('i',list)
print(a)
print(type(a))