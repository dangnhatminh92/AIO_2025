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
INSERT INTO Orders (OrderID, CustomerID, SalespersonID, OrderDate, TotalAmount)
VALUES
(11, 1, 1, '2024-01-10', 500.00),
(12, 1, 1, '2024-01-11', 650.50),
(13, 2, 2, '2024-01-12', 720.75),
(14, 4, 4, '2024-01-13', 800.00),
(15, 5, 5, '2024-01-14', 950.25);
""")

connection.commit()
cursor.close()
connection.close()
