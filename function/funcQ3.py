from lib2to3.pgen2.literals import evalString


# printing the fruits name 

def my_function(food):
  for x in food:
    print(x)

fruits = eval(input("enter the name for fruits"))

my_function(fruits)