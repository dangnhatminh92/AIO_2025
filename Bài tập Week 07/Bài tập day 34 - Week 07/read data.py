import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week07"
)
data=pd.read_sql_query("SELECT * FROM STOCK", connection)
print(data)