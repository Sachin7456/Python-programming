#maping two lists into dictionary without zip function 
a=[1,2,3,4,5]
b=[6,7,8,9,10]
d=dict(map(lambda a,b:{a,b},a,b))
d