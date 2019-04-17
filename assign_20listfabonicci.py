def f(n):
    a=0
    b=1
    for x in range(0,n+1,1):
        if(x==0):
            list=[b]
        sum=a+b
        list.append(sum)
        a=b
        b=sum
    return list
    
n=int(input("Enter a number:"))
print("Fibonacci series:",f(n))

