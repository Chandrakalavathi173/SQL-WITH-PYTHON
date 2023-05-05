import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Chandu(173)',database='chandu')
cur=mydb.cursor()
z='insert into student (emp_id,emp_name,salary) values(%s,%s,%s)'
c=(101,"divya",98)
cur.execute(z,c)
mydb.commit()
print("Inserted successfully") 