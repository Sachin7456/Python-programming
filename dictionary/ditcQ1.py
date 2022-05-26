#checking whether a dictionary is empty or not
a={}
size=int(input("enter the size of dictionary"))
for i in range(0,size):
  key=input("enter key")
  value=input("enter value")
  a[key]=value
if(len(a)==0):
  print("empty")
else:
  
  print("not")