print("//////////////Ludo Game////////////////////")
import random
num=random.randint(1, 6)
a=str(num)
user1=input("User1 choose number in between(1-6): ")
user2=input("User2 choose number in between(1-6): ")
if(user1=="6" or num == "6"):
  user1_1=input("User1 choose number in between(1-6): ")
  if(user1_1==num):
    print("////////////Wow User1 Won! the match/////////////")
elif(user1 !=num or user2==num):
  user2_2=input("User2 choose number in between(1-6): ")
  if(user2_2==num):
    print("////////////Wow User2 Won! the Match/////////////")
else:
  print("Dry the match"
  )