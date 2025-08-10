a=input("Enter a String: ");
output=''
for i in range((len(a)-1),-1,-1):
    if(a[i]!=' '):

#    print(a[i],end='');
        output=output+a[i];
    else:
        continue;
#print(output)
if (output==a):
    print("Palindrome")
else:
    print("Not Palindrome")