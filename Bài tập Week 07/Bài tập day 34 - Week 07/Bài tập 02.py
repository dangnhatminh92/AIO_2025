import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week07"
)

query_maxbuy = """
SELECT INVESTOR, MAX(BUY) AS Max_buy
FROM STOCK
GROUP BY INVESTOR;
"""

data_maxbuy = pd.read_sql_query(query_maxbuy, connection)
print(data_maxbuy)