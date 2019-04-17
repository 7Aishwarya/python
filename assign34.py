f1=open("d:\\rhyme.txt","r+")
line=f1.read()
a=(line.lower().split())
b={}
n=0
for i in a:
    b[n]=i
    n+=1
print(b)
print(type(b))
print ("word count in the file is",len(a))
item=0
c={}
for items in a:
    if items not in c:
        c[items]=1
    else:
        c[items]+=1
print(c)
f1.close()
