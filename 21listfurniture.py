furniture=["sofa set", "dining table", "T.V. stand", "cupboard"]
cost=[20000, 8500, 4599, 13920]
f=input("Enter the furniture you want to buy:")
q=int(input("Enter quantity:"))
c=-1
flag=0
for x in furniture:
    c = c + 1
    if(f==x):
        flag = flag + 1
        if(q>0):
            bill = cost[c] * q
            print("bill:",bill)
        else:
            print("Invalid quantity entered\nBill ammount:0")
if(flag==0):
    print("Furniture not available")
            
