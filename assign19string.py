accepted_string=input("enter the string:")
resultant_string=""
count=0
for i in accepted_string:
    if((count==0 or count%2==0) and (i!=" ")):
        resultant_string+=i
    if(i==" "):
        continue
    else:
        count+=1
print("Accepted string:",accepted_string)
print("Resultant string:",resultant_string)
print("Expected string:",resultant_string[::-1])
