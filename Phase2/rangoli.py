n=int(input("Enter a no 1 to 26:"))
c=96
dash=n
alpha=n
t=[]
q=0
for i in range(1,n+1):
    for j in range(1,(2*dash)-1):
        print("-",end='')
    for k in range(i):
        print(chr(c+alpha),end='')
        if(q==1):
            print("-",end="")
        if(i>1):
            t.append(chr(c+alpha))
        alpha=alpha-1
    t.reverse()
    L=len(t)
    count=1
    for j in range(1,L):
        print(t[count],end='')
        if(j!=L-1):
            print("-",end="")
        count+=1
    for j in range(((2*dash)-2)):
        print("-",end='')
    print()
    c=96
    dash=dash-1
    alpha=n
    t=[]
    q=1

c2=96
dash2=2
alpha2=n
t2=[]
for i in range(n,0,-1):
    if(i<n):
        print('-',end='')
        for j in range(1,(2*dash2)-2):
            print("-",end='')
        for k in range(i):
            print(chr(c2+alpha2),end='')
            if(k!=i):
                print("-",end='')
            t2.append(chr(c2+alpha2))
            alpha2=alpha2-1
        t2.reverse()
        L=len(t2)
        count=1
        for j in range(1,L):
            print(t2[count],end='-')
            count+=1
        for j in range(1,(2*dash2)-2):
            print("-",end='')
        print()
        c2=96
        dash2=dash2+1
        alpha2=n
        t2=[]
    
