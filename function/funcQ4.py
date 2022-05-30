#finding the biggest between 2 numbers
a,b=int(input("enter the first number")),int(input("enter the second number"))
s=lambda a,b:a if a>b else b
print(s(a,b))