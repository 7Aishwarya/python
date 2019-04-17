k=input("Enter the string: ")
l=len(k)
def reverse(k,l):
    if l==0:
        return
    else:
        print(k[l-1],end="")
        l-=1
        return reverse(k,l)
reverse(k,l)
