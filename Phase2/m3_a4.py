import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur=con.cursor()
cur.execute('''create table Vehicle(
Vehicleid number(5) primary key, Vehiclename varchar2(10))''')
cur.executemany("insert into vehicle values(:a, :b)",
                [(2001,'Toyota'), (2002,'Maruti'), (2003,'Nissan'), (2004,'Hyundai')])
cur.executemany("insert into vehicle values(:x, :y)",
                [{'x':2006, 'y':str('Honda')}, {'x':2007, 'y':str('Volkswagon')}])
con.commit()
cur.execute("select * from vehicle")
print(cur.fetchall())
con.close()
