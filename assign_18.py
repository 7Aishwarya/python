string=input("Enter string:")
for x in string:
    c=0
    for y in string:
        if((x.upper() or x.lower())==(y.upper() or y.lower())):
            c = c + 1
    for z in string(-1):
        if((z.upper() or z.lower())==(x.upper() or x.lower())):
            print(c)    
        

