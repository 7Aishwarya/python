def is_prime(num):
    c=0
    for i in range(1,num+1,1):
        if(num%i==0):
            c+=1
    if(c>2):
        print(num, "is not prime")
    else:
        print(num, "is prime")

def is_even(num):
    if(num%2==0):
        print(num, "is even")
    else:
        print(num,"is not even")
