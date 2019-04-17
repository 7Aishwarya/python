mylist=[1,2,3,"4",5]
sum=0
try:
    for i in mylist:
        #try:
        sum = sum + i
except TypeError:
    print("Type error occured")
    sum=None
print("sum=",sum)
try:
    print(mylist[5])
except IndexError:
    print("Index out of range")
        
