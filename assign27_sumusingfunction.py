i=0
t=0
def sum(a,b):
    t = t + b
    return(t);

n=int(input("Enter the value of n:"))
for i in range(1, n, 1):
    x=sum(n,i)
print("Sum of n natural numbers:",x)
