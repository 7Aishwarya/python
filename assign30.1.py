l=[]
n=int(input("Enter the number n: "))
def multiple(n):
    if n==1:
        return l.append(3)
    else:
        l.append(n*3)
        n-=1
        return multiple(n)
multiple(n)
print(l[::-1])
