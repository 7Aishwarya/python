import random
with open("d:\\rhyme.txt","r+") as f1:
    n=0
    line=f1.read()
    a=[line.split()]

print(a)
b=[]
s=""
for i in a:
    n+=1
    s=i
    if(len(s)>3):
        i=random.randint(1,len(s))
        b.append(s)
print(type(b))
print("word count in the file is",len(b))
print(b)
f1.close()
a="abcdefghijk"
for i in a:
    print(i)
x=random.random(a)
print(x)
    
