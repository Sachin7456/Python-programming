#adding a key in a given dictionary
a={}
size=int(input("enter the size of dictionary"))
for i in range(0,size):
  key=input("enter key")
  value=input("enter value")
  a[key]=value
print(a)
a.update({2:30})
a