x=int(input("Enter the first number"))
y=int(input("Enter the second number"))
z=int(input("Enter the third number"))
if (x==y==z):
    print(x,y,z,"are equal")
elif (x>y) & (x>z):
    print(x,"is greater than",y,z)    
elif (y>z):
    print(y,"is greater than",z,x)    
else:
    print(z,"is greater than",y,x)
