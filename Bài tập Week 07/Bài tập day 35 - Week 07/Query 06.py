# Câu 11: Cập nhật tổng giá trị đơn hàng có OrderID = 2 thành 4.500.000
import pandas as pd
import mysql.connector
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

# cursor.execute("""
# UPDATE Customers
# SET Phone = '09003456789'
# WHERE CustomerID = 3
# """)

# connection.commit()
# cursor.close()
# connection.close()

#Query
query = """
SELECT  * FROM Customers
WHERE 1 = 1
AND CustomerID = 3
"""

query = pd.read_sql_query(query, connection)
print(query)
