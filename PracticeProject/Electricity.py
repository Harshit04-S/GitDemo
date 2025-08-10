units=int(input("Enter total units of electricity consumed: "));
totalAmount=5*units;
print("Total amount for",units,"units of electricity is: ",totalAmount);
finalPrice=totalAmount-((totalAmount*10)/100);
print("Final amount after 10% discount is: ",finalPrice)
