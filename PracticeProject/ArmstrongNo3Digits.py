i=int(input("Enter the number to check Armstrong or Not: "));
j=i
r=0;
sum=0;
while(j>0):
    r=j%10
    sum=sum+r*r*r
    j=j//10
print(sum)
if(sum==i):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
