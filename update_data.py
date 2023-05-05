import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Chandu(173)',database='chandu')
cur=mydb.cursor()
x='update student set salary=salary+10000 where emp_id=103'
cur.execute(x)
mydb.commit()