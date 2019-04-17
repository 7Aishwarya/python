c_id=int(input("Enter the customer id:"))
if(c_id>=101 and c_id<=1000):
    p1=int(input("Enter price of product1:"))
    p2=int(input("Enter price of product2:"))
    p3=int(input("Enter price of product3:"))
    total = p1 + p2 + p3
    if(total>1000):
        d=0.05*total
    elif(total>=500 and total<1000):
        d=0.02*total
    else:
        d=0.01*total
    bill_amount=total-d
    print("Total bill:",bill_amount)
else:
    print("Invalid customer id")
