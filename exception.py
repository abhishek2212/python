# print(1/0)
# try:
#   a=1/0
# except ZeroDivisionError as e:
#   print(e)
# finally:
#   a=input("Enter the number: ")
#   print(a)

# for i in range(10):
# print("Hello")

# try:
#   inp=input()
#   print("Press ctrl+C or interrupt the Kernel: ")
# except KeyboardInterrupt:
#   print("Caught KeyboardInterrupt")
# else:
#   print("No execution occured")


# try:
#   import math
#   print(math.exp(1000))
# except OverflowError:
#   print("OverFlow Exception Raised.")
# else:
#   print("Success, no error!")
try:
  print(ans)
except NameError:
  print("NameError: name 'ans is not defined'")
else:
  print("Success, no Error!")