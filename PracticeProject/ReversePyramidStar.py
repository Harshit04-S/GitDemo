a=int(input("Enter the range: "));
i=1;
while(a>0):
    count=1;
    while(count<i):
        print(' ',end='');
        count=count+1;
    j=1;
    while(j<=(a*2)-1):
        print('*',end='');
        j=j+1;
    print();
    a=a-1;
    i=i+1;