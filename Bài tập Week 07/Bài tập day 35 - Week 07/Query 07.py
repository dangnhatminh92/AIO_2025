#Câu 12: Xóa tất cả các đơn hàng của khách hàng có CustomerID = 2
import pandas as pd
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

cursor.execute("""
DELETE FROM Orders
WHERE 1 = 1
AND CustomerID = 2
""")

connection.commit()
cursor.close()
connection.close()

query = """
SELECT * FROM Orders
WHERE 1 = 1
AND CustomerID = 2
"""

query = pd.read_sql_query(query, connection)
print(query)

