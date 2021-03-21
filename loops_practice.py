'''Exercise 1: Print First 10 natural numbers using while loop'''
'''
i=0
while(i<=10):
  print(i, end=" ")
  i=i+1
'''

# /////////////////////////////////////////////////////////////
'''
Exercise 2: Print the following pattern
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
'''
print("Second number pattern")
for row in range(1,6):
  for column in range(1,row+1):
    print(column, end=" ")
  print(" ")
'''
# ///////////////////////////////////////////////////////////////////////////////////
''' 
Exercise 3: Accept number from user and calculate the sum of all number from 1 to a given number
For example, if user entered 10 the output should be 55.

'''
'''
sum=0
num=int(input("Enter the number: "))
for i in range(1,num+1):
  sum +=i
print(f"the sum of first {num} number is: = {sum}")
'''
# //////////////////////////////////////////////////////////////////////////////////

'''
Exercise 4: Print multiplication table of a given number
For example, num = 2 so the output should be 2 4 6 8 10 12 14 16 18 20
'''
'''
num_table=int(input("Enter the number: "))
print(f"the number {num_table} table of : ")
for i in range(1,11):
  print(f"{num_table} x {i} = {num_table*i}")
'''
# ///////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 5: Given a list, iterate it, and display numbers divisible by five, and if you find a number greater than 150, stop the loop iteration.
list1 = [12, 15, 32, 42, 55, 75, 122, 132, 150, 180, 200]
'''
'''
list1=[12,15,32,42,55,75,122,150,180,200]
for i in list1:
  if(i > 150):
    break
  if(i%5==0):
    print(i)
'''
# ///////////////////////////////////////////////////////////////////////////////////////////////

'''
Exercise 7: Print the following pattern using for loop
5 4 3 2 1 
4 3 2 1 
3 2 1 
2 1 
1
'''
'''
for i in range(5):
  for j in range(5-i,0,-1):
    print(j, end=" ")
  print(" ")
'''
# //////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 8: Reverse the following list using for loop
list1 = [10, 20, 30, 40, 50]
'''
'''
list1=[10,20,30,40,50]
# start=len(list1)-1
# stop=-1
# step=-1
for i in range(len(list1)-1,-1,-1):
  print(list1[i],end=" ")
'''
# /////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 9: Display numbers from -10 to -1 using for loop
Expected output: -10, -9, -8, -7, -6, -5, -4, -3, -2, -1
'''
'''
for i in range(-10,0,1):
  print(f"{i}")
'''
# ////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 10: Display a message “Done” after successful execution of for loop
Expected output:
0
1
2
3
4
Done!
'''
'''
for i in range(5):
  print(i)
else:
  print("Done!")
'''
# ////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 11: Write a program to display all prime numbers within a range
Note: A Prime Number is a whole number that cannot be made by multiplying other whole numbers
Examples:
6 is not a Prime Number because it can be made by 2×3 = 6
37 is a Prime Number because no other whole numbers multiply together to make it.
Expected output is-:
Prime numbers between 25 and 50 are:
29
31
37
41
43
47

'''
'''
start=1
end=100
print(f"The prime number in between({start}-{end}): ")
for num in range(start,end+1):
  if(num > 1):
    for i in range(2,num):
      if(num%i==0):
        break
    else:
      print(num)
'''
# ////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 12: Display fibonacci series up to 10 terms.
Expected output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
'''
'''
terms=10
num1,num2=0,1
count=0
print("Fibonacci Sequence: ")
while count<terms:
  print(num1,end=" ")
  temp=num1+num2
  # update_value
  num1=num2
  num2=temp
  count +=1
'''
# ////////////////////////////////////////////////////////////////////////////////////////////
'''
Exercise 13: Write a loop to find the factorial of any number
For example: calculate the factorial of 5
5! = 5 × 4 × 3 × 2 × 1 = 120
Expected output: 120
'''
num = 5
factorial = 1
if (num < 0):
  print("Factorial doesn't exist.....")
elif num == 0:
  print("The factorail of 0 is 1")
else:
  for i in range(1, num + 1):
    factorial = factorial * i
  print("the factorail of ", num, " is ", factorial)
