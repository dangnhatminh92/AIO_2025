import mysql.connector
import pandas as pd
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week07"
)

# Tạo cursor để thực hiện truy vấn
cursor = connection.cursor()

#Tạo bản CUSTOMERS
cursor.execute("""
CREATE TABLE PRODUCT (
    ID INT AUTO_INCREMENT PRIMARY KEY,
    NAME VARCHAR(30) NOT NULL,
    PRICE DECIMAL(10) NOT NULL
);
""")

#INSERT DATA
cursor.execute("""
INSERT INTO PRODUCT (NAME, PRICE)
VALUES
            ('iPhone 15', 18000000),
            ('Galaxy Z-Fold 5', 30000000);
""")

# # UPDATE Price
cursor.execute("""
UPDATE PRODUCT
            SET PRICE = '50000000'
            WHERE 1 = 1
            AND NAME = 'Galaxy Z-Fold 5';
""")
connection.commit()

# DELETE DATA
cursor.execute("""
DELETE FROM PRODUCT
            WHERE 1 = 1
            AND NAME = 'iPhone 15';
""")
connection.commit()



