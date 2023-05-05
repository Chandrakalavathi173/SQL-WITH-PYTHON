import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='Chandu(173)')
print(mydb.connection_id)
cur=mydb.cursor()
cur.execute("create database pythonsql")