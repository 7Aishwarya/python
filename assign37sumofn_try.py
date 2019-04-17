sum=0
try:
    n=int(input("Enter the value of n:"))
    for n in range(1,n+1,1):
        sum = sum + n
except ValueError:
    print("Value error occured")
    sum=None
print("Sum of n naturl numbers is:",sum)
