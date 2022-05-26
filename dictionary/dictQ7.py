#merging two dictionaries
a={}
size=int(input("enter the size of first dictionary"))
for i in range(0,size):
  key=input("enter key")
  value=input("enter value")
  a[key]=value
b={}
size=int(input("enter the size of second array"))
for j in range(0,size):
  key=input("enter key")
  value=input("enter value")
  b[key]=value
a.update(b)
