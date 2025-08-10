a=input("Enter a String: ");
b=a.lower()
#print(b)
c=b[-1::-1]
#print(c)
if (c==b):
    print("Palindrome")
else:
    print("Not Palindrome")