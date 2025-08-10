i=int(input("Enter 3 or more digits number to check Armstrong or Not: "));
j=i
k=i
r=0;
sum=0;
count=0;
while(j>0):
    r=j%10
    count=count+1
    j=j//10
print("Total no. of digits is: ",count)
while(k>0):
    s=k%10
    sum=sum+pow(s,count)
    k=k//10
print(sum)
if(sum==i):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")
