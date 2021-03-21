# f=open("abc.txt","r")
# data=f.read()
# data = f.read(20)
# print(data)
# f.close()

# with open("abc.txt") as f:
#   data=f.readline(30) 
#   print(data)

# f=open("new_abc1.txt","a")
# # f.write("Do good for others. it will come back in unexpected ways.")
# f.write("\nLife has no limitations, except the ones you make!")
# f.close()

#///////////
# Python code to illustrate split() function
#//////////
with open("abc.txt","r") as f:
  data=f.readlines()
  for line in data:
    word=line.split()
    print(word)