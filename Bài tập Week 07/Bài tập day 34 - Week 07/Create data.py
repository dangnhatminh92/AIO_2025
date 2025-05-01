import mysql.connector
import pandas as pd
# Kết nối tới cơ sở dữ liệu MySQL
connection = mysql.connector.connect(
    host='localhost',        # hoặc IP máy chủ MySQL
    user='root',             # tên người dùng MySQL
    password='123#edc',   # mật khẩu đăng nhập
    database='aio.week07'      # tên cơ sở dữ liệu
)

cursor = connection.cursor()


# Tạo table
cursor.execute("""
CREATE TABLE STOCK (
               ID INT AUTO_INCREMENT PRIMARY KEY,
               NAME VARCHAR(30) NOT NULL,
               BUY DECIMAL(10) NOT NULL,
               INVESTOR VARCHAR(30) NOT NULL
);
               """)


#Insert data
cursor.execute("""
INSERT INTO STOCK (NAME, BUY, INVESTOR)
VALUES 
               ('ACB', '29.45', 'Nguyen'),
               ('VIC', '44.55', 'Nguyen'),
               ('GMD', '74.30', 'Nguyen'),
               ('ACB', '28.45', 'Vinh'),
               ('VIC', '40.55', 'Vinh'),
               ('GMD', '60.30', 'Vinh');
""")


connection.commit()
cursor.close()
connection.close()

