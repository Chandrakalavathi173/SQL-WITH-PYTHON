import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Chandu(173)',database='chandu')
cur=mydb.cursor()
t= 'create table student(emp_id integer(4),emp_name varchar(30),salary integer(10))'
cur.execute(t)