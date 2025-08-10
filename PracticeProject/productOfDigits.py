a=int(input("Enter the number: "))
prod=1
r=0
while(a>0):
    r=a%10
    prod=prod*r
    a=a//10
print("Product of didgits of given no. is: ",prod)


