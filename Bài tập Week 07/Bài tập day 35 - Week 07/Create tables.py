import pandas as pd
import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123#edc",
    database="aio.week7"
)

cursor = connection.cursor()

# Drop existing tables if they exist
cursor.execute("DROP TABLE IF EXISTS Orders;")
cursor.execute("DROP TABLE IF EXISTS Customers;")
cursor.execute("DROP TABLE IF EXISTS Salesperson;")

cursor.execute("""
CREATE TABLE Salesperson (
               SalespersonID INT PRIMARY KEY,
               FullName VARCHAR(30) NOT NULL,
               Email VARCHAR(255) NOT NULL,
               Phone VARCHAR(15) NOT NULL
               );
""")

cursor.execute("""
CREATE TABLE Customers (
               CustomerID INT PRIMARY KEY,
               FullName VARCHAR(30) NOT NULL,
               Email VARCHAR(255) NOT NULL,
               Phone VARCHAR(15) NOT NULL
               );
""")

cursor.execute("""
CREATE TABLE Orders (
               OrderID INT PRIMARY KEY,
               CustomerID INT,
               SalespersonID INT,
               OrderDate DATE NOT NULL,
               TotalAmount DECIMAL(10,2) NOT NULL,
               FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
               FOREIGN KEY (SalespersonID) REFERENCES Salesperson(SalespersonID)
               );

""")


connection.commit()
cursor.close()
connection.close()



