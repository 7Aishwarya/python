import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur=con.cursor()
#table 1
cur.execute('''create table user1(user_id number primary key not null,
name varchar2(50), email_id varchar2(50) check(email_id like'%@%.%'))''')
cur.execute("insert into user1 values(1, 'Prakhar', 'prakhar@gmail.com')")
cur.execute("insert into user1 values(2, 'Sajal', 'sajal@gmail.com')")
cur.execute("insert into user1 values(3, 'Anand', 'anand@gmail.com')")
cur.execute("insert into user1 values(4, 'Gaurav',  ‘gaurav@gmail.com')")
cur.execute("insert into user1 values(5, 'Raj', 'raj@gmail.com')")
#table 2
cur.execute('''create table pic1(pic_id varchar2(30) primary key not null,
user_id number, path varchar2(50) not null, caption varchar2(80),
date_posted date not null)''')
cur.execute('''insert into pic1 values('p1', '1', '\\users\\a\\pic1',
'smile', '14-June-18')''')
cur.execute("insert into pic1 values('p2', 2, '\\users\\a\\pic2', 'your life your choices', '6-June-18')")
cur.execute("insert into pic1 values('p3', 3, '\\users\\a\\pic3', 'world', '1-December-17')")
cur.execute("insert into pic1 values('p4', 4, '\\users\\a\pic4', 'No caption', '1-December-15')")
cur.execute("insert into pic1 values('p5', 5, '\\users\a\\pic5', 'Friendship', '1-August-16')")
cur.execute("insert into pic1 values('p6', 6, '\\users\\a\\pic6', 'Home ', '1-July-14')")
cur.execute("insert into pic1 values('p7', 7, '\\users\\a\\pic7', 'No caption', '1-June-17')")
cur.execute("insert into pic1 values('p8', 1, '\\users\\a\\pic8', 'Stars', '1-March-17')")
cur.execute("insert into pic1 values('p9', 1, '\\users\\a\\pic9', 'No caption', '13-March-17')")
cur.execute("insert into pic1 values('p10', 1, '\\users\\a\\pic10', 'Life', '07-November-13')")

#table3
cur.execute('''create table user3(pic_id varchar2(20) not null,
user_id number, no_of_likes_on_pic number,
foreign key(user_id) references user1(user_id),
foreign key(pic_id) references pic1(pic_id))''')
cur.execute("insert into user3 values('p1', 5, 5)")
cur.execute("insert into user3 values('p2', 2, 3)")
cur.execute("insert into user3 values('p3', 2, 2)")
cur.execute("insert into user3 values('p4', 3, 3)")
cur.execute("insert into user3 values('p5', 3, 2)")
cur.execute("insert into user3 values('p6', 4, 3)")
cur.execute("insert into user3 values('p7', 4, 2)")
cur.execute("insert into user3 values('p8', 1, 3)")
cur.execute("insert into user3 values('p9', 1, 2)")
cur.execute("insert into user3 values('p10',1, 1)")
#table4
cur.execute('''create table user2(user_id number, liked_no number,
pic_id varchar2(20), foreign key(user_id) references user1(user_id),
foreign key(pic_id) references pic1(pic_id))''')
cur.execute("insert into user2 values(1, 1, 'p1')")
cur.execute("insert into user2 values(2, 1, 'p1')")
cur.execute("insert into user2 values(3, 1, 'p1')")
cur.execute("insert into user2 values(4, 1, 'p1')")
cur.execute("insert into user2 values(5, 1, 'p1')")
cur.execute("insert into user2 values(1, 1, 'p2')")
cur.execute("insert into user2 values(2, 1, 'p2')")
cur.execute("insert into user2 values(3, 1, 'p2')")
cur.execute("insert into user2 values(4, 1, 'p3')")
cur.execute("insert into user2 values(1, 1, 'p3')")
cur.execute("insert into user2 values(1, 1, 'p4')")
cur.execute("insert into user2 values(2, 1, 'p4')")
cur.execute("insert into user2 values(3, 1, 'p4')")
cur.execute("insert into user2 values(4, 1, 'p5')")
cur.execute("insert into user2 values(1, 1, 'p5')")
cur.execute("insert into user2 values(1, 1, 'p6')")
cur.execute("insert into user2 values(2, 1, 'p6')")
cur.execute("insert into user2 values(3, 1, 'p6')")
cur.execute("insert into user2 values(4, 1, 'p7')")
cur.execute("insert into user2 values(1, 1, 'p7')")
cur.execute("insert into user2 values(1, 1, 'p8')")
cur.execute("insert into user2 values(2, 1, 'p8')")
cur.execute("insert into user2 values(3, 1, 'p8')")
cur.execute("insert into user2 values(4, 1, 'p9')")
cur.execute("insert into user2 values(1, 1, 'p9')")
cur.execute("insert into user2 values(1, 1, 'p10')")
#table5
cur.execute('''create table pic2(pic_id varchar2(20) not null,
tags varchar2(30), foreign key(pic_id) references pic1(pic_id))''')
cur.execute("insert into pic2 values('p1', 'Art')")
cur.execute("insert into pic2 values('p2', 'Art')")
cur.execute("insert into pic2 values('p3', 'Music')")
cur.execute("insert into pic2 values('p3', 'Engineering')")
cur.execute("insert into pic2 values('p4', 'Art')")
cur.execute("insert into pic2 values('p5', 'History')")
cur.execute("insert into pic2 values('p6', 'Art')")
cur.execute("insert into pic2 values('p7', 'Art')")
cur.execute("insert into pic2 values('p7', 'Engineering')")
cur.execute("insert into pic2 values('p8', 'Science')")
cur.execute("insert into pic2 values('p9', 'History')")
cur.execute("insert into pic2 values('p10', 'Music')")
con.commit()
con.close()
