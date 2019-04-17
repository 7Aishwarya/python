def FIBO(number):
    if(number==0):
        return (0)
    elif(number==1):
        return 1
    else :
        return FIBO(number-1)+FIBO(number-2)


a=int(input("enter the no."))
if a<0:
    print("error:the no. entered is -ve")
else:
    print(FIBO(a))
