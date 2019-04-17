import cx_Oracle
con=cx_Oracle.connect('SYSTEM/1234@localhost/xe')
cur=con.cursor()
"""n=int(input('''What do you want to know? Enter your choice no:\n
1.Max Likes\n
2.Min Likes\n
3.Who liked most\n
4.Music pictures\n
5.Popular Tag\n
6.Most liked User\n
7.Old Tagging\n
8.Delete Inactive Users\n'''))"""
cur.execute("drop table user_pic_posted")
cur.execute("drop table user_pic_like")
cur.execute("drop table pic_tags")
cur.execute("drop table user_details")
cur.execute("drop table pic_details")
cur.execute('''create table user_details(user_id varchar2(20) primary key not null,
name varchar2(50), email_id varchar2(50) check(email_id like'%@%.%'))''')
cur.execute("insert into user_details values('u1', 'Aishwarya', 'aish@gmail.com')")
cur.execute("insert into user_details values('u2', 'Bhavya', 'bhavya@gmail.com')")
cur.execute("insert into user_details values('u3', 'Lavisha', 'lavisha@gmail.com')")
cur.execute("insert into user_details values('u4', 'Divyanshi', 'divyanshi@gmail.com')")
cur.execute("insert into user_details values('u5', 'Abhay Raj Sharma', 'abhay@gmail.com')")
cur.execute("insert into user_details values('u6', 'Aashi', 'aashi@gmail.com')")
cur.execute("insert into user_details values('u7', 'Geetu', 'geetu@gmail.com')")
cur.execute('''create table pic_details(pic_id varchar2(20) primary key not null,
path varchar2(50) not null, caption varchar2(50),date_posted date not null)''')
cur.execute('''insert into pic_details values('p1', '\\users\\a\\pic1',
'your smile chases the sunshine of someones life', '14-June-2018')''')
cur.execute("insert into pic_details values('p2', '\\users\\a\\pic2', 'your life your choices', '5-July-2018')")
cur.execute("insert into pic_details values('p3', '\\users\\a\\pic3', 'Happiness', '1-December-2017')")
cur.execute("insert into pic_details values('p4', '\\users\\a\pic4', 'No caption', '1-December-2017')")
cur.execute("insert into pic_details values('p5', '\\users\a\\pic5', 'Friend', '1-August-2017')")
cur.execute("insert into pic_details values('p6', '\\users\\a\\pic6', 'Home sweet home', '1-July-2017')")
cur.execute("insert into pic_details values('p7', '\\users\\a\\pic7', 'No caption', '1-June-2017')")
cur.execute("insert into pic_details values('p8', '\\users\\a\\pic8', 'Smile', '1-March-2017')")
cur.execute("insert into pic_details values('p9', '\\users\\a\\pic9', 'No caption', '13-March-2017')")
cur.execute("insert into pic_details values('p10', '\\users\\a\\pic10', 'Happy Birthday', '07-November-2017')")
cur.execute('''create table user_pic_posted(pic_id varchar2(20) not null,
user_id varchar2(20), no_of_likes_on_pic number,
foreign key(user_id) references user_details(user_id),
foreign key(pic_id) references pic_details(pic_id))''')
cur.execute("insert into user_pic_posted values('p1', 'u5', 5)")
cur.execute("insert into user_pic_posted values('p2', 'u2', 3)")
cur.execute("insert into user_pic_posted values('p3', 'u2', 2)")
cur.execute("insert into user_pic_posted values('p4', 'u3', 3)")
cur.execute("insert into user_pic_posted values('p5', 'u3', 2)")
cur.execute("insert into user_pic_posted values('p6', 'u4', 3)")
cur.execute("insert into user_pic_posted values('p7', 'u4', 2)")
cur.execute("insert into user_pic_posted values('p8', 'u1', 3)")
cur.execute("insert into user_pic_posted values('p9', 'u1', 2)")
cur.execute("insert into user_pic_posted values('p10','u1', 1)")
cur.execute('''create table user_pic_like(user_id varchar2(20), liked_picid varchar2(20),
foreign key(user_id) references user_details(user_id),
foreign key(liked_picid) references pic_details(pic_id))''')
cur.execute("insert into user_pic_like values('u1', 'p1')")
cur.execute("insert into user_pic_like values('u2', 'p1')")
cur.execute("insert into user_pic_like values('u3', 'p1')")
cur.execute("insert into user_pic_like values('u4', 'p1')")
cur.execute("insert into user_pic_like values('u5', 'p1')")
cur.execute("insert into user_pic_like values('u1', 'p2')")
cur.execute("insert into user_pic_like values('u2', 'p2')")
cur.execute("insert into user_pic_like values('u3', 'p2')")
cur.execute("insert into user_pic_like values('u4', 'p3')")
cur.execute("insert into user_pic_like values('u1', 'p3')")
cur.execute("insert into user_pic_like values('u1', 'p4')")
cur.execute("insert into user_pic_like values('u2', 'p4')")
cur.execute("insert into user_pic_like values('u3', 'p4')")
cur.execute("insert into user_pic_like values('u4', 'p5')")
cur.execute("insert into user_pic_like values('u1', 'p5')")
cur.execute("insert into user_pic_like values('u1', 'p6')")
cur.execute("insert into user_pic_like values('u2', 'p6')")
cur.execute("insert into user_pic_like values('u3', 'p6')")
cur.execute("insert into user_pic_like values('u4', 'p7')")
cur.execute("insert into user_pic_like values('u1', 'p7')")
cur.execute("insert into user_pic_like values('u1', 'p8')")
cur.execute("insert into user_pic_like values('u2', 'p8')")
cur.execute("insert into user_pic_like values('u3', 'p8')")
cur.execute("insert into user_pic_like values('u4', 'p9')")
cur.execute("insert into user_pic_like values('u1', 'p9')")
cur.execute("insert into user_pic_like values('u1', 'p10')")
cur.execute('''create table pic_tags(pic_id varchar2(20) not null, tags varchar2(30),
foreign key(pic_id) references pic_details(pic_id))''')
cur.execute("insert into pic_tags values('p1', 'Art')")
cur.execute("insert into pic_tags values('p2', 'Art')")
cur.execute("insert into pic_tags values('p3', 'Music')")
cur.execute("insert into pic_tags values('p3', 'Engineering')")
cur.execute("insert into pic_tags values('p4', 'Art')")
cur.execute("insert into pic_tags values('p5', 'History')")
cur.execute("insert into pic_tags values('p6', 'Art')")
cur.execute("insert into pic_tags values('p7', 'Art')")
cur.execute("insert into pic_tags values('p7', 'Engineering')")
cur.execute("insert into pic_tags values('p8', 'Science')")
cur.execute("insert into pic_tags values('p9', 'History')")
cur.execute("insert into pic_tags values('p10', 'Music')")
con.commit()
cur.execute("select pic_id, tags from pic_tags where tags='Music'")
print(cur.fetchall())
con.close()