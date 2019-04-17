class H:
    def select(self,name,about,rooms,transport,price,facilities,book_now,n,l):
        self.name=name
        self.about=about
        self.rooms=rooms
        self.transport=transport
        self.price=price
        self.facilities=facilities
        self.book_now=book_now
        self.l=l
        a=10
        while(a!=0):
            print("----------",self.name,"--------------")
            print("1.About")
            print("2.Rooms")
            print("3.Transport")
            print("4.Facilities")
            print("5.Price")
            print("6.Book now")
            print("7.Student login")
            print("Press 0 to exit")
            
        
            a=int(input("Enter your choice number(options):"))
            print("\n")
            if(a<0 or a>7):
                print("-->>Wrong choice; Enter your choice again\n")
            if(a==1):
                print(self.about)
            if(a==2):
                print(self.rooms)
            if(a==3):
                print(self.transport)
            if(a==4):
                print(self.facilities)
            if(a==5):
                print(self.price)
            if(a==6):
                ocpd=l
                print(self.book_now)
                print("Total vacancy: 50")
                vacant = 50-ocpd
                print("Vacancy left: " ,vacant)
                if(ocpd == 50):
                    print("Sorry!!1 No rooms left")
                else:
                    print("Enter details of the student")
                    name = input("Enter your name:")
                    stuid = int(input("Enter your id:"))
                    pswd = input("Enter password of atleast more than 6 characters")
                    while(len(pswd)<6):
                        print("Invalid password !! try again")
                        pswd=input("Enter password again")
                    npswd=input("Enter password again")
                    if(npswd==pswd):
                        print("Password set successfully!!!")
                        print("Visit www.abc.com for payment options")
                        room_no = str(0)+str(ocpd)
                        import cx_Oracle
                        con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
                        cur=con.cursor()
                        
                        if(n==1):
                            error=1
                            
                            while(error!=0):
                                try:
                                    cur.execute("create table stuid11(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                    cur.execute("insert into stuid11 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.DatabaseError:
                                    cur.execute("insert into stuid11 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.IntegrityError:
                                    print("This password is already taken")
                           
                            con.commit()
                            try:
                                cur.execute('''CREATE TABLE stu_details11(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                                cur.execute("insert into stu_details11 values(:a,:b,:c)",(stuid,name,room_no))
                            except:
                                cur.execute("insert into stu_details11 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        elif(n==2):
                            error=1
                            
                            while(error!=0):
                                try:
                                    cur.execute("create table stuid22(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                    cur.execute("insert into stuid22 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.DatabaseError:
                                    cur.execute("insert into stuid22 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.IntegrityError:
                                    print("This password is already taken")
                           
                            con.commit()
                            try:
                                cur.execute('''CREATE TABLE stu_details22(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid22(stuser_id))''')
                                cur.execute("insert into stu_details22 values(:a,:b,:c)",(stuid,name,room_no))
                            except:
                                cur.execute("insert into stu_details22 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                            
                        
                        elif(n==3):
                            error=1
                            
                            while(error!=0):
                                try:
                                    cur.execute("create table stuid33(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                    cur.execute("insert into stuid33 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.DatabaseError:
                                    cur.execute("insert into stuid33 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.IntegrityError:
                                    print("This password is already taken")
                           
                            con.commit()
                            try:
                                cur.execute('''CREATE TABLE stu_details33(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid33(stuser_id))''')
                                cur.execute("insert into stu_details33 values(:a,:b,:c)",(stuid,name,room_no))
                            except:
                                cur.execute("insert into stu_details33 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1

                        elif(n==4):
                            error=1
                            
                            while(error!=0):
                                try:
                                    cur.execute("create table stuid44(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                    cur.execute("insert into stuid44 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.DatabaseError:
                                    cur.execute("insert into stuid44 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.IntegrityError:
                                    print("This password is already taken")
                            
                            con.commit()
                            try:
                                cur.execute('''CREATE TABLE stu_details44(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid44(stuser_id))''')
                                cur.execute("insert into stu_details44 values(:a,:b,:c)",(stuid,name,room_no))
                            except:
                                cur.execute("insert into stu_details44 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        elif(n==5):
                            error=1
                            
                            while(error!=0):
                                try:
                                    cur.execute("create table stuid55(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                    cur.execute("insert into stuid55 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.DatabaseError:
                                    cur.execute("insert into stuid55 values(:a,:b)",(stuid,pswd))
                                    error=0
                                except cx_Oracle.IntegrityError:
                                    print("This password is already taken")
                            
                            con.commit()
                            try:
                                cur.execute('''CREATE TABLE stu_details55(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid55(stuser_id))''')
                                cur.execute("insert into stu_details55 values(:a,:b,:c)",(stuid,name,room_no))
                            except:
                                cur.execute("insert into stu_details55 values(:a,:b,:c)",(stuid,name,room_no))
                            con.commit()
                            print("Congratulations!!!!! your room has been booked!!")
                            print("Your room number is : " , room_no)
                            ocpd=ocpd+1
                        con.close()    
                    else:
                        while(npswd is not pswd):
                            npswd=input("Password didn't match,enter again")
                            if(npswd==pswd):
                                room_no = str(0)+str(ocpd)
                                import sys
                                con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
                                cur=con.cursor()
                                if(n==1):
                                    error=1
                                    while(error!=0):
                                        try:
                                            cur.execute("create table stuid11(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                            cur.execute("insert into stuid11 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.DatabaseError:
                                            cur.execute("insert into stuid11 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.IntegrityError:
                                            print("This password is already taken")
                                    con.commit()
                                    try:
                                        cur.execute('''CREATE TABLE stu_details11(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid11(stuser_id))''')
                                        cur.execute("insert into stu_details11 values(:a,:b,:c)",(stuid,name,room_no))
                                    except:
                                        cur.execute("insert into stu_details11 values(:a,:b,:c)",(stuid,name,room_no))
                                    con.commit()
                                    print("Congratulations!!!!! your room has been booked!!")
                                    print("Your room number is : " , room_no)
                                    ocpd=ocpd+1
                                    sys.exit()
                                elif(n==2):
                                    error=1
                                    while(error!=0):
                                        try:
                                            cur.execute("create table stuid22(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                            cur.execute("insert into stuid22 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.DatabaseError:
                                            cur.execute("insert into stuid22 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.IntegrityError:
                                            print("This password is already taken")
                                    con.commit()
                                    try:
                                        cur.execute('''CREATE TABLE stu_details22(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid22(stuser_id))''')
                                        cur.execute("insert into stu_details22 values(:a,:b,:c)",(stuid,name,room_no))
                                    except:
                                        cur.execute("insert into stu_details22 values(:a,:b,:c)",(stuid,name,room_no))
                                    con.commit()
                                    print("Congratulations!!!!! your room has been booked!!")
                                    print("Your room number is : " , room_no)
                                    ocpd=ocpd+1
                                    sys.exit()
                                elif(n==3):
                                    error=1
                            
                                    while(error!=0):
                                        try:
                                            cur.execute("create table stuid33(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                            cur.execute("insert into stuid33 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.DatabaseError:
                                            cur.execute("insert into stuid33 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.IntegrityError:
                                            print("This password is already taken")
                                    con.commit()
                                    try:
                                        cur.execute('''CREATE TABLE stu_details33(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid33(stuser_id))''')
                                        cur.execute("insert into stu_details33 values(:a,:b,:c)",(stuid,name,room_no))
                                    except:
                                        cur.execute("insert into stu_details33 values(:a,:b,:c)",(stuid,name,room_no))
                                    con.commit()
                                    print("Congratulations!!!!! your room has been booked!!")
                                    print("Your room number is : " , room_no)
                                    ocpd=ocpd+1
                                    sys.exit()
                                elif(n==4):
                                    error=1
                            
                                    while(error!=0):
                                        try:
                                            cur.execute("create table stuid44(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                            cur.execute("insert into stuid44 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.DatabaseError:
                                            cur.execute("insert into stuid44 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.IntegrityError:
                                            print("This password is already taken")
                                    con.commit()
                                    try:
                                        cur.execute('''CREATE TABLE stu_details44(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid44(stuser_id))''')
                                        cur.execute("insert into stu_details44 values(:a,:b,:c)",(stuid,name,room_no))
                                    except:
                                        cur.execute("insert into stu_details44 values(:a,:b,:c)",(stuid,name,room_no))
                                    con.commit()
                                    print("Congratulations!!!!! your room has been booked!!")
                                    print("Your room number is : " , room_no)
                                    ocpd=ocpd+1
                                    sys.exit()
                                elif(n==5):
                                    error=1
                            
                                    while(error!=0):
                                        try:
                                            cur.execute("create table stuid55(STUSER_ID VARCHAR(30) primary key not null,STU_PSWD VARCHAR(15) not null unique check(length(stu_pswd)>=6))") 
                                            cur.execute("insert into stuid55 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.DatabaseError:
                                            cur.execute("insert into stuid55 values(:a,:b)",(stuid,pswd))
                                            error=0
                                        except cx_Oracle.IntegrityError:
                                            print("This password is already taken")
                                    con.commit()
                                    try:
                                        cur.execute('''CREATE TABLE stu_details55(STUSER_ID VARCHAR(30),STU_NAME VARCHAR(30), STU_ROOMNO INTEGER, foreign key(stuser_id) references stuid55(stuser_id))''')
                                        cur.execute("insert into stu_details55 values(:a,:b,:c)",(stuid,name,room_no))
                                    except:
                                        cur.execute("insert into stu_details55 values(:a,:b,:c)",(stuid,name,room_no))
                                    con.commit()
                                    print("Congratulations!!!!! your room has been booked!!")
                                    print("Your room number is : " , room_no)
                                    ocpd=ocpd+1
                                    sys.exit()
                        con.close()            
            if(a==7):
                import cx_Oracle
                import sys
                con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
                cur=con.cursor()
                user=input("Enter your user id:")
                if(n==1):
                    cur.execute("select STUSER_ID from stuid11")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid11")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute('''select * from stu_details11 where stuser_id = :n''', {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")
                if(n==2):
                    cur.execute("select STUSER_ID from stuid22")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid22")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details22 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        #cur.execute("select days_present from stu_attendance22 where stu_id = :m", {'m':user})
                                        #print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")   
                if(n==3):
                    cur.execute("select STUSER_ID from stuid33")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid33")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details33 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        #cur.execute("select days_present from stu_attendance33 where stu_id = :m", {'m':user})
                                        #print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")    
                if(n==4):
                    cur.execute("select STUSER_ID from stuid44")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid44")
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password):
                                        p=1
                                        cur.execute("select * from stu_details44 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        #cur.execute("select days_present from stu_attendance44 where stu_id = :m", {'m':user})
                                        #print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")
                if(n==5):
                    cur.execute("select STUSER_ID from stuid55")
                    t=cur.fetchall()
                    c=0
                    for i in t:
                        x=i[0]
                        if(x==user):
                            c=1
                            p=0
                            while(p!=1):
                                password=input("Enter password:")
                                cur.execute("select STU_pswd from stuid55 where STUSER_ID= :n", {'n':user})
                                r=cur.fetchall()
                                for j in r:
                                    y=j[0]
                                    
                                    if(y==password ):
                                        p=1
                                        cur.execute("select * from stu_details55 where stuser_id = :n", {'n':user})
                                        print("\n***************DETAILS*****************")
                                        z=('Student id: ', 'Name: ', 'Room no: ')
                                        print(z)
                                        print(cur.fetchall())
                                        #cur.execute("select days_present from stu_attendance55 where stu_id = :m", {'m':user})
                                        #print("No. of days present: ",cur.fetchall() )
                                        print("****************************************\n")
                                if(p!=1):
                                    q=int(input("Wrong password; press 1 to enter again or press 0 to exit "))
                                    if(q==0):
                                        print("-------------------------------------------------------------")
                                        print("You may run the whole program again if you want to know more")
                                        print("                        Thank You                           ")
                                        sys.exit()
                            
                    if(c!=1):
                        print("You are not enrolled or the user id you entered is incorrect. ")    
                con.close()
            
            
class v_g(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=1
        l=0
        import cx_Oracle
        con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
        cur=con.cursor()
        cur.execute("select count(STUSER_ID) from stuid11")
        z1=cur.fetchall()
        for x in z1:
            l=x[0]
        con.close()
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n,l)
        
class v_b(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=2
        l=0
        import cx_Oracle
        con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
        cur=con.cursor()
        cur.execute("select count(STUSER_ID) from stuid22")
        z1=cur.fetchall()
        for x in z1:
            l=x[0]
        con.close()
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n,l)

class a(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=3
        l=0
        import cx_Oracle
        con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
        cur=con.cursor()
        cur.execute("select count(STUSER_ID) from stuid33")
        z1=cur.fetchall()
        for x in z1:
            l=x[0]
        con.close()
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n,l)
class s(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=4
        l=0
        import cx_Oracle
        con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
        cur=con.cursor()
        cur.execute("select count(STUSER_ID) from stuid44")
        z1=cur.fetchall()
        for x in z1:
            l=x[0]
        con.close()
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n,l)
class p(H):
    def select(self,name,about,rooms,transport,price,facilities,book_now):
        n=5
        l=0
        import cx_Oracle
        con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
        cur=con.cursor()
        cur.execute("select count(STUSER_ID) from stuid55")
        z1=cur.fetchall()
        for x in z1:
            l=x[0]
        con.close()
        #Hostel.select(self,name,about,rooms,transport,price,facilities,book_now)
        super().select(name,about,rooms,transport,price,facilities,book_now,n,l)

obj1= v_g()
obj2=v_b()
obj3=a()
obj4=s()
obj5=p()


