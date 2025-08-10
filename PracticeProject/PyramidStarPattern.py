a=int(input("Enter the range: "));
i=1;
k=1;
while(i<=a):
    count=1;
    while(count<=(a-i)):
        print(' ',end='');
        count=count+1;
    j=1;
    while(j<=k):
        print('*',end='');
        j=j+1;
    print();
    k=k+2;
    i=i+1;




