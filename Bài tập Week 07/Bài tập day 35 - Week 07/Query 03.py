#Tính tổng doanh số của từng nhân viên
import pandas as pd
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

query03 = """
SELECT SalespersonID, SUM(TotalAmount) AS TotalSales
FROM Orders
GROUP BY SalespersonID
"""
query03 = pd.read_sql_query(query03, connection)
print(query03)
