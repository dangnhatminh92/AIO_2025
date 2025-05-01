# Liệt kê tất cả các đơn hàng của nhân viên có SalespersonID là 1

import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

query = """
SELECT * FROM Orders
WHERE 1 = 1
AND SalespersonID = 1
"""
query01 = pd.read_sql_query(query, connection)
print(query01)

