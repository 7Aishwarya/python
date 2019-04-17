class Calculator:
    def isPrime(self,number):
        for i in range(2,number):
            if number % i == 0:
                return False
            return True
 
    def getNextPrime(self, number):
        for i in range(number, number+100):
                for p in range(2,i):
                    if i % p == 0:
                            break
                else:
                    return i                
 
    def __init__(self, number):
        bool = self.isPrime(number)
        if bool == True:
            print(self.getNextPrime(number+1))
            self.last_prime = number
 
number = Calculator(13)
