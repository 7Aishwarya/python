a=input("Enter the string:")
b=""
for i in a:
    c=0
    t=0
    for j in b:
        if i.lower()==j.lower():
            t+=1
    if(t<1):
        b+=i
        for k in a:
            if(i.lower()==k.lower()):
                c+=1
        print(c,i)
