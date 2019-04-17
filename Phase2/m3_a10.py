import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur=con.cursor()
try:
    cur.execute("insert into product values('P106', 'Jams', 150)")
except cx_Oracle.DatabaseError as e:
    print(e)
finally:
    con.close()
