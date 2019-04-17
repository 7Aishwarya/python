class Info:
    try:
        @staticmethod
        def Email(email):
            count = 0
            count_2 = 0
            for i in email:
                if i == "@":
                    count += 1
                if i == ".":
                    count_2 += 1
 
            if count == 1 and count_2 > 0:
                pass
            else:
                raise Exception("This is an invalid format")
 
        @staticmethod
        def M_number(number):
            if len(number) == 10:
                pass
            elif len(number) == 11 and number[0] == "+":
                pass
            else:
                raise Exception("Invalid Number")
        @staticmethod
        def Age(age):
            if 0 < age < 101:
                pass
            else:
                raise Exception("Invalid Age")
    except:
        print("Errors have been encountered")
obj = Info()
email = input("Enter your email")
obj.Email(email)
number = input("Enter your Mobile Number")
obj.M_number(number)
age = int(input("Enter your age"))
obj.Age(age)
