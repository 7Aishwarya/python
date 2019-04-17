import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur=con.cursor()
cur.execute("SELECT * FROM Employer")
print(cur.fetchall())
print("Description for SELECT:\n", cur.description)
print("no. of rows=",cur.rowcount)
con.close()

