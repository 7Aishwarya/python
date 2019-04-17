f=open("d:\\courses.txt", "w")
f.write("Java\nPython\nJavascript\nPHP")
f.close()
f=open("d:\\courses.txt", "r")
lines=f.readlines()
d={}
l=[None] * len(lines)
i=0
for line in lines:
    d[i]=line.strip()
    l[i]=line.strip()
    i = i + 1
print(d)
print(l)
f.close()
    
