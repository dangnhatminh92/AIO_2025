import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

# Insert data into Salesperson table
cursor.execute("""
INSERT INTO Salesperson (SalespersonID, FullName, Email, Phone)
            VALUES
            (1, 'Do Van K', 'k.do@example.com', '0901122334'),
            (2, 'Ngo Thi L', 'l.ngo@example.com', '0912233445'),
            (3, 'Bui Van M', 'm.bui@example.com', '0923344556'),
            (4, 'Tran Thi N', 'n.tran@example.com', '0934455667'),
            (5, 'Nguyen Van O', 'o.nguyen@example.com', '0945566778'),
            (6, 'Le Thi P', 'p.le@example.com', '0956677889'),
            (7, 'Pham Van Q', 'q.pham@example.com', '0967788990'),
            (8, 'Dang Thi R', 'r.dang@example.com', '0978899001'),
            (9, 'Hoang Van S', 's.hoang@example.com', '0989900112'),
            (10, 'Nguyen Thi T', 't.nguyen@example.com', '0990011223');
               
""")

# Insert data into Customers table
cursor.execute("""
INSERT INTO Customers (CustomerID, FullName, Email, Phone)
VALUES 
            (1, 'Do Van K', 'k.do@example.com', '0901122334'),
            (2, 'Ngo Thi L', 'l.ngo@example.com', '0912233445'),
            (3, 'Bui Van M', 'm.bui@example.com', '0923344556'),
            (4, 'Tran Thi N', 'n.tran@example.com', '0934455667'),
            (5, 'Nguyen Van O', 'o.nguyen@example.com', '0945566778'),
            (6, 'Le Thi P', 'p.le@example.com', '0956677889'),
            (7, 'Pham Van Q', 'q.pham@example.com', '0967788990'),
            (8, 'Dang Thi R', 'r.dang@example.com', '0978899001'),
            (9, 'Hoang Van S', 's.hoang@example.com', '0989900112'),
            (10, 'Nguyen Thi T', 't.nguyen@example.com', '0990011223');
""")

# Insert data into Orders table
cursor.execute("""
INSERT INTO Orders (OrderID, CustomerID, SalespersonID, OrderDate, TotalAmount)
VALUES 
            (1, 1, 1, '2024-01-10', 500.00),
            (2, 2, 2, '2024-01-11', 650.50),
            (3, 3, 3, '2024-01-12', 720.75),
            (4, 4, 4, '2024-01-13', 800.00),
            (5, 5, 5, '2024-01-14', 950.25),
            (6, 6, 6, '2024-01-15', 1000.00),
            (7, 7, 7, '2024-01-16', 1100.80),
            (8, 8, 8, '2024-01-17', 1200.00),
            (9, 9, 9, '2024-01-18', 1350.90),
            (10, 10, 10, '2024-01-19', 1500.00);
""")

connection.commit()
cursor.close()
connection.close()
