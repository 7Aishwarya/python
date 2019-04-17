import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur =con.cursor()
cur.execute('''create table Users(UserId number(10) primary key check(UserId<10 AND userId>0),
UserName varchar2(30) NOT NULL, Password varchar2(20) NOT NULL,
UserType varchar2(20) check(UserType='Employer' OR UserType='Jobseeker'))''')
cur.execute("insert into Users values(1, 'jobs@infosys.com', 'jobs@infosys', 'Employer')")
cur.execute("insert into Users values(:a, :b, :c, :d)", (2, 'careers@accenture.com', 'Acc1', 'Employer'))
cur.execute("insert into Users values(:p, :q, :r, :s)",
            {'p':3, 'q':str('rahulitsme@gmail.com'), 'r':str('rahulindia93'), 's':str('Jobseeker')})
id=input("Enter userid:")
name=input("Enter username:")
passw=input("Enter password:")
utype=input("Enter user type:")
cur.execute("insert into Users values(:w, :x, :y, :z)",
            {'w':id, 'x':str(name), 'y':str(passw), 'z':str(utype)})
con.commit()
cur.execute("select * from Users")
print(cur.fetchall())
con.close()
