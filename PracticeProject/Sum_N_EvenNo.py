a=int(input("Enter the count: "));
i=2;
sum=0;
count=1;
while(count<=a):
    #print(i);
    if(i%2==0):
        sum=sum+i;
        count = count + 1;
    i=i+1;


print(sum)
