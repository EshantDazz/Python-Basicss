import mysql.connector as sql

my=sql.connect(host="localhost",user="root",passwd="Lolhaha2&",auth_plugin='mysql_native_password')

cur=my.cursor()
cur.execute("create database GeeksforGeeks")

cur.execute("show databases")

for i in cur:
    print(i)
