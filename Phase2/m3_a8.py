import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur =con.cursor()
cur.execute("drop table account")
cur.execute('''create table account(customerid number primary key, accountno varchar2(15),
accounttype varchar2(15) check(accounttype in ('Savings', 'Current', 'Recurring')), balance number)''')
cur.executemany('''insert into account values(:p, :q, :r, :s)''',
                [{'p':101, 'q':str('IBI1001'), 'r':str('Savings'), 's':0},
                 {'p':102, 'q':str('IBI1002'), 'r':str('Current'), 's':1200},
                 {'p':103, 'q':str('IBI1003'), 'r':str('Savings'), 's':6543},
                 {'p':104, 'q':str('IBI1004'), 'r':str('Recurring'), 's':7500},
                 {'p':105, 'q':str('IBI1005'), 'r':str('Current'), 's':0}])
con.commit()
cur.execute("select customerid, balance from account where balance=(select max(balance) from account)")
print("customerid and balance of customer with maximum balance: ", cur.fetchall(), "\n")
cur.execute("select balance from account where customerid=102")
acct_bal=cur.fetchall()
print("balance of customer with customerid=102 is: ",acct_bal)
t=acct_bal[0]
l=t[0]+2000
cur.execute("update account set balance=:a where customerid=102", {'a':l})
con.commit()
cur.execute("select balance from account where customerid=102")
print("updated balance of customer with customerid=102 is: ",cur.fetchall(), "\n")
cur.execute("delete from account where accounttype='Current' and balance=0")
cur.execute("select * from account")
print("Updated account table:\n", cur.fetchall())
con.close()
