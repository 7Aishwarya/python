customer_details={ 1001 : "John", 1004 : "Jill", 1005: "Joe", 1003 : "Jack" }
for key,value in customer_details.items():
    print("Customer id:",key,"  Customer name:",value)
n=len(customer_details)
print("No. of customers:",n)
print("Customer names in ascending order:")
print(sorted(customer_details.values()))
customer_details.pop(1005)
print("Updated dictionary:",customer_details)
customer_details[1003]="Mary"
print("Updated dictionary:",customer_details)
if(customer_details.get(1002)==None):
    print("ID deos not exist")
else:
    print("Id:",customer_details(1002))


