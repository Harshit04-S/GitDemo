a=int(input("Enter the number: "))
r=0
rev=0
while(a>0):
    r=a%10
    rev=rev*10+r
    a=a//10
print(rev)