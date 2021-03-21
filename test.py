# count=0
# while count<3:
#   count += 1
#   print(f"hello + {count}")
# else:
#   print("Invalid!")


# /////////////////////////////////
# while loop in single line
# ////////////////////////////////
# count=0
# while(count==0): print("Hello Rahul")


# /////////////////////////////////
# for loop in single line
# ////////////////////////////////

# for i in range(0,5):
#   print("Hello Anuj "+str(i))

# n=input("Enter the name: ")
# for i in range(1,11):
#   print("Hello "+ str(n)+" "+str(i))

# 0 to n-1 
# n=int(input("Enter the number: "))
# for i in range(1,n):
#   print(i, end=" ")
# print("\r")
'''
# ///////////////////////////////////////////
#List iteration
# ///////////////////////////////////////////
# print("List Iteration")
# l=["Mango","Grapes","Lichy","black-berry"]
# for i in l:
#   print(i,end=" ")
# print("\r")
'''



# ///////////////////////////////////////////
#List iteration
# ///////////////////////////////////////////
# print("Tuple Iteration")
# tup = ("Mango", "Grapes", "Lichy", "black-berry")
# for i in tup:
#   print(i, end=" ")
# print("\r")

# ///////////////////////////////////////////
#List iteration
# ///////////////////////////////////////////
# print("String Iteration")
# str1 = "Mango"
# for i in str1:
#   print(i, end=" ")
# print("\r")


# ///////////////////////////////////////////
#Dic iteration
# ///////////////////////////////////////////
# print("List Iteration")
# d = dict()
# d["xyz"]=123
# d["abc"]=345
# for i in d:
#   print("%s %d" %(i, d[i]))
# print("\r")



# //////////////////////////
#  Python program to illustrate
# Iterating by index
# /////////////////////////

# list=["Akash",12,98.5,True]
# for i in range(len(list)):
#   print(list[i])


# i=1
# while i<5:
#   print("Rahul")
#   i += 1 #i = i+1

# list =[11,12,13]
# for i in list:
#   print(i,end=" ")
# print("\r")

# for i in range(3,20,1):
#   print(i)

# ///////////////////////////
# Continue
# ///////////////////////////

# for letter in "intelligencetechnologies":
#   if letter =="i" or letter=="e":
#     continue
#   print("Current Letter: ",letter)


# ///////////////////////////
# break
# ///////////////////////////

# for letter in "intelligencetechnologies":
#   if letter =="l" or letter=="s":
#     break
# print("Current Letter: ",letter)

# ///////////////////////////
# pass
# ///////////////////////////

# for letter in "intelligencetechnologiex":
#   pass
# print("Last letter of words: ",letter)


# for i in range(10):
#   pass
# print("Last digit is: ",i)

# range(n,n-1)
# for digits in range(1,50):
#   break
# print("The current digit is: ",digits)

# for digit2 in range(50):
#   pass
# print("the last digit of: ",digit2)

# ///////////////////////////////////////
# break statement
#///////////////////////////////////// 
# for i in range(1,80):
#   print(i)
#   if(i==3):
#     break

#/////////////////////////////////////
#  continue statement
#////////////////////////////////// 

# for i in range(4):
#   print("printing")
#   if i==2:
#     continue
#   print(i)

#/////////////////////////////////////
#  pass statement
#//////////////////////////////////

# list1=[12,15,17]
# for i in list1:
#   pass
# print("hi")

# def greet(name="Stark"):
#   gr="Hello "+name
#   return gr
# a=greet()
# b=greet("Alok")
# # print(a)
# print(b)
# print(a)

dic1={"name":"Atul","College_name":"arsd","roll_number":93,"marks":(98,86,95)}
# print(type(dic1))
# print(dic1)

# print(dic1["marks"])
# print(dic1.items())

# print(dic1.keys())
# dic1.update({"roll_number":99})
# print(dic1)

# print(dic1.get("name"))
# print(dic1["name"])

# del dic1
# print(dic1)

# //////////////////////////////////////
# set
# /////////////////////////////////////
# set1=set()
# print(set1)
# set1.add(1)
# set1.add(2)
# set1.add(2)
# print(len(set1))

# set2={1,3,4,7,(2,5,8,7)}
# set2.remove(3)
# print(set2.pop())
# set2.clear()
# print(set2)

# set3={1,2,3}
# set4={4,2,5,3}

# print(set3.union(set4))
# print(set3 | set4)

# print(set3.intersection(set4))
# print(set3 & set4)


'''
#///////////////////////////////////////
# Number guessing -Project
#///////////////////////////////////////
print("//////////////Number guessing Game Project///////////////")

import random
user_number=int(input("Enter the number: "))
ran_num=random.randint(0,9)
if(user_number == ran_num):
  print("User won the match",user_number)
elif(user_number != ran_num):
  print("Computer won the Match",ran_num)
else:
  print("Invalid!")

'''



# ////////////////////////////////////////
# function
# ////////////////////////////////////////

# def oddEven(x):
#   if x%2==0:
#     print("even")
#   else:
#     print("Odd")
# x=int(input("Enter the number: "))
# oddEven(x)

# ////////////////////////////////////////
# function Docstring (__doc__)
# ////////////////////////////////////////

# def sayHi():
#   "Hello Rahul!"
# print(sayHi.__doc__)



import sys

for line in sys.stdin:
  if 'q'==line.rstrip():
    break
  print(f'Input:{line}')
print("Exit")
