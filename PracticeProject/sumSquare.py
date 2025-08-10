i=int(input("Enter the number: "));
sum=0;
r=0;
while(i>0):
    r=i%10
    sum=sum+r*r
    i=i//10
print(sum)