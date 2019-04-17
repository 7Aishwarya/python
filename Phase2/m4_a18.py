from abc import ABC, abstractmethod
class Payment(ABC):
    VAT = 1.15
    @abstractmethod
    def totalAmount(self):
        pass
class CreditCardPayment(Payment):
    processingCharges = 1.02
    def getTotalAmount(self,purchaseAmt):
        amt = purchaseAmt * self.VAT #stmt1
        amt = amt * self.processingCharges
        print("Payment has been made. Your total amount is Rs.", amt)
class cash(Payment):
    def getTotalAmount(self,purchaseAmt):
        print("Payment has been made. Your total amount is Rs.", purchaseAmt * self.VAT) #stmt2
'''class Bill:
    def __init__(self,purchaseAmount):
        self.__purchaseAmount = purchaseAmount
    def makePayment(self,mode):
        #Ensure that it is a valid mode of payment
        if (isinstance(mode, Payment)):
            #actual behavior is selected dynamically
            amount= mode.getTotalAmount(self.__purchaseAmount)
            print("Paid:",amount)
            #create a bill with
            #purchaseAmount=1000
            bill = Bill(1000)
            cc = CreditCardPayment()
            bill.makePayment(cc)
            cash = cashPayment()
            bill.makePayment(cash)'''
while True:
    choice = int(input('''How would you like to pay?
1. Cash
2. Credit Card
'''))
    if(choice == 1):
        obj = cash()
    elif(choice == 2):
        obj = Credit_card()
    amt = int(input("Enter amount:"))
    obj.getTotalAmount(amt)

