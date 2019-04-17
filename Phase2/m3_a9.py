import cx_Oracle
try:
    con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')   #2.make some change in username(give wrong username)
    cur =con.cursor()
    cur.execute("delete from Users where User_Id=2")    #1.Run as it is
    con.commit()
    cur.execute("select * from Users")                  #3.give wrong table name and then run
    print(cur.fetchall())
    con.close()
except cx_Oracle.DatabaseError as e:
    print(e)
except cx_Oracle.DatabaseError as e:
    print(e)
except error as e:
    print(e)
    
                                                       #4.Erase all these comments (:-D)
