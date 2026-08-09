
import mysql.connector
conn=mysql.connector.connect (
    host='localhost',
    user='root',
    password='Kumar',
    database='expense_db')
cursor=conn.cursor()