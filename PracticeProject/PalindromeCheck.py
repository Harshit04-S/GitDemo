a=int(input("Enter the number: "))
b=a
r=0
rev=0
while(a>0):
    r=a%10
    rev=rev*10+r
    a=a//10
print("Reverse of given no. is: ",rev)
if(b==rev):
    print("Palindrome")
else:
    print("Not Palindrome")
