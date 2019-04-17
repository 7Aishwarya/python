import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur =con.cursor()
cur.execute("delete from Users where UserId=1")
con.commit()
cur.execute("select * from Users")
print(cur.fetchall())
con.close()
