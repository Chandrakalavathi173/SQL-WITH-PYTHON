import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Chandu(173)',database='chandu')
cur=mydb.cursor()
f='select * from student where emp_id=101'
cur.execute(f)
display=cur.fetchall()
for x in display:
    print(x)
