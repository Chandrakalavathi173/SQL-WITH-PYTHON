import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Chandu(173)',database='chandu')
cur=mydb.cursor()
z='insert into student(emp_id,emp_name,salary) values(%s,%s,%s)'
a=[(102,'deepthi',100000),(103,'manju',60000),(104,'chandu',29000)]
cur.executemany(z,a)
mydb.commit()
print('Data inserted succesfully')