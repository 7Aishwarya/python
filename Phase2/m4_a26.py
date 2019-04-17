class InvalidString(Exception):
    def __init__(self):
        Exception.__init__(self,"Found Asterisk")
    def asteriskChecker(myString):
        for i in myString:
            if(i=="*"):
                raise InvalidString() #statement1
