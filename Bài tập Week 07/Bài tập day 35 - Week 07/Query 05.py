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
# UPDATE Orders
# SET TotalAmount = 4500000
# WHERE 1 = 1
# AND OrderID = 2;
# """)

# connection.commit()
# cursor.close()
# connection.close()

#Query
query = """
SELECT  * FROM Orders
WHERE 1 = 1
AND OrderID = 2;
"""


query = pd.read_sql_query(query, connection)
print(query)




