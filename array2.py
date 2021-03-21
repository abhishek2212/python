# importing "array" for array creations
import array as arr
# creating an array with float type
a = arr.array('d', [12.5, 65.9, 85.23, 6.65])
a[0]=45.6
print(a[0])
print(a)
print(type(a))
for i in range(0,4):
  print(a[i])
