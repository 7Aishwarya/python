n=int(input("Enter a number:"))
a=0
b=1
print("Fibonacci series:")
for x in range(0,n,1):
    if(x==0):
        print(b, end=" ")
    sum=a+b
    print(sum, end=" ")
    a=b
    b=sum
