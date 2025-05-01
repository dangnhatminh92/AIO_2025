#Tìm khách hàng có số lượng đơn hàng nhiều nhất
import pandas as pd
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

query02 = """
SELECT CustomerID, COUNT(OrderID) AS TotalOrders
FROM Orders
GROUP BY CustomerID
ORDER BY TotalOrders DESC
LIMIT 1;
"""
query02 = pd.read_sql_query(query02, connection)
print(query02)


