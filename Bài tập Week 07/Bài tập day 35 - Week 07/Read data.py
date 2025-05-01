import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)
data=pd.read_sql_query("SELECT * FROM Salesperson", connection)
data2=pd.read_sql_query("SELECT * FROM Customers", connection)
data3=pd.read_sql_query("SELECT * FROM Orders", connection)
print(data)
print(data2)
print(data3)