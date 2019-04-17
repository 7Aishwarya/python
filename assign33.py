f=open("d:\\student_details.txt", "w")
f.write("101 Rahul\n102  Julie\n103 Helena\n104 Kally")
f.close()
f=open("d:\\student_details.txt", "r")
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
    
