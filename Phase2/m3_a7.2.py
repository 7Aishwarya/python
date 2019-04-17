import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur =con.cursor()
cur.execute("select * from vehicle")
print(cur.fetchall(),"\n")
uid=input("Enter the vehicleid whoserecord you want to delete:")
cur.execute("delete from vehicle where vehicleid=:a", {'a':uid})
con.commit()
cur.execute("select * from vehicle")
print(cur.fetchall())
con.close()

