string1=input("Enter string1:")
string2=input("Enter string2:")
l1=len(string1)
l2=len(string2)
print(l1)
print(l2)
c=""
for x in string1:
    if (x.isupper()==True):
        c = c + x
for x in string2:
    if (x.isupper()==True):
        c = c + x
print(c)

