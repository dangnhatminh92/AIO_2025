import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week07"
)
query_totalbuy = """
SELECT SUM(BUY)  AS Total_buy
FROM STOCK
"""

data_sum_totalbuy = pd.read_sql_query(query_totalbuy, connection)
print(data_sum_totalbuy)