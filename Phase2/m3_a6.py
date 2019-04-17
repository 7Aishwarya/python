import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur=con.cursor()
cur.execute("select * from vehicle")
print(cur.fetchall())
o=2001
n=1001
for i in range(1,8,1):
    cur.execute("update vehicle set vehicleid=:a where vehicleid=:b", (n, o))
    o+=1
    n+=1
cur.execute("update vehicle set vehiclename='Mahindra' where vehicleid=1003")
con.commit()
cur.execute("select * from vehicle")
print("Table Vehicle after updation:\n", cur.fetchall())
con.close()
