#Tìm nhân viên có doanh số cao nhất
import pandas as pd
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

query04 = """
SELECT SalespersonID , SUM(TotalAmount) AS TotalSales
FROM Orders
GROUP BY SalespersonID
ORDER BY TotalSales DESC
LIMIT 1;
"""
query04 = pd.read_sql_query(query04, connection)
print(query04)
