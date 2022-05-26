#removing a key from the dictionary
a={}
size=int(input("enter the size of dictionary"))
for i in range(0,size):
  key=int(input("enter key"))
  value=int(input("enter value"))
  a[key]=value
print(a)
a.pop(1)
print("the edited dictionary is",a)