qty_prod1=int(input("Enter quantity of 1st product"))
qty_prod2=int(input("Enter quantity of 2nd product"))
price_prod1=int(input("Enter price of 1st product"))
price_prod2=int(input("Enter price of 2nd product"))
cost=((qty_prod1*price_prod1)+(qty_prod2*price_prod2))
#totalcost=((10*cost)/100)+cost
if cost<1000:
    totalcost=cost
elif 1000<cost<2000:
    totalcost=cost-((5/100)*cost)
else:
    totalcost=cost-((10/100)*cost)
print("Total cost is", totalcost)



              
