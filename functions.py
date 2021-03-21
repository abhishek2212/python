# def evenOdd(x):
#   if(x%2==0):
#     print(f"The number {x} is : even")
#   else:
#     print(f"The number {x} is : odd")
# # x=int(input("enter a number: "))
# evenOdd(45)
# evenOdd(4)


# //////////////////////////////////////////////////////////
# Docstring
# ////////////////////////////////
# def sayHi():
#   "hello world!"
# print(sayHi.__doc__)

# //////////////////////////////////////////////////////////
# The return statement
# ////////////////////////////////

# def square_value(num):
#   return num**2
# print(f"the square is: {square_value(4)}")

# print(f"the square is: {square_value(6)}")


# def fName():
#   gr="hello"
#   return gr

# name=fName()
# print(type(name))

# def my_function(x):
#   return 5*x
# print(my_function(5))
# print(my_function(6))
# print(my_function(4))

#////////////////////////////////////////////////
#calculator design using python
#////////////////////////////////////////////////

# def userInput():
#   pass
# def add(a,b):
#   # for addtion logic is here....
#   return a+b


# def sub(a,b):
#   # for subtraction logic is here....
#   return a-b


# def mul(a,b):
#   # for multiplication logic is here....
#   return a*b


# def div(a,b):
#   # for division logic is here....
#   return a/b
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))

# def display(a,b):
#   print(f"The addtion of number {a} and {b} is: ",add(a,b))
#   print(f"The subtraction of number {a} and {b} is: ", sub(a, b))
#   print(f"The multiplication of number {a} and {b} is: ", mul(a, b))
#   print(f"The division of number {a} and {b} is: ", div(a, b))

# display(a,b)


# ///////////////////////////////////////////////////////////////////////////////////////////////////
# return 5


#//////////////////////////////////////////////////////////////////////
#funnction recursion

#Advantage of recursion function
# Recursive functions make the code look clean and elegant.
# A complex task can be broken down into simpler sub-problems using recursion.
# Sequence generation is easier with recursion than using some nested iteration.


#Disadvantage of recursion function
# A lot of memory and time is taken through recursive calls which makes it expensive for use.
# Recursive functions are challenging hard to debug.
# The reasoning behind recursion can sometimes be tough to think through.
# /////////////////////////

# def factorail(x):
#   if x==1 or x==0:
#     return 1
#   else:
#     return (x*factorail(x-1))
# num=int(input("Enter the number to check the factorial of a number: "))
# print("The factorail of ",num," is ",factorail(num))


# def factoril(n):
#   if n==0 or n==1:
#     return 1
#   else:
#     return n*factoril(n-1)
# num=int(input("Enter a number to check factorial of number: "))
# print(f"The number {num} factorial is: {factoril(num)}")


#/////////////////////////////////////////
# Program to print factorial of a number  
# recursively.


# def recursive_functorial(n):
#   if n==1:
#     return n
#   else:
#     return n*recursive_functorial(n-1)

# #user input
# num=int(input("Enter a number to check the factorail factorail of number: "))

# # check if the input is valid or not
# if num<0:
#   print("Invalid input! Please enter a positive number.")
# elif num==0:
#   print("Factorial of number 0 is 1")
# else:
#   print("Factorial of number: ",num," is ",recursive_functorial(num))

#//////////////////////////////////////
#Python Arbitrary Arguments
# def greet(*names):
#   for name in names:
#     print("Hello ",name)
# greet("Rahul","Rohit","Monika","Anamika")



#Arguments
#default arguments
def greet(*names,msg="Good-Morning"):
  for name in names:
    print("Hello ",name +", "+ msg)
greet("Rahul","Rohit","Krishna","Ramu")



























