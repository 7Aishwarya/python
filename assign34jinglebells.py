import random
with open("d:\\rhyme.txt","r+") as f1:
    n=0
    line=f1.read()
    a=[line.split()]
b={}
c=""
for i in a:
    n+=1
    c=i
    x=random.randrange(c[1:len(c):1])
    print(x)
        
#print("word count in the file is",len(b))
#print(b)
f1.close()
