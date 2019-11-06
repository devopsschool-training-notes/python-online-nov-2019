"""
Referernce
https://pynative.com/python-mysql-database-connection/
https://pynative.com/python-mysql-tutorial/

So our steps will be like this,

- Start your MySQL Server. ( For XAMPP users, start apache and MySQL from XAMPP Control panel )
- Install MySQL Connector in Python, if you don’t have installed.
    $ pip install mysql-connector
- Connect MySQL with Python
- Create a database in MySQL using Python, If you don’t have one or if you wish to create a new one
- Create MySQL table in Python
- Now Insert data in that table using a Python program.
"""
# to Import, we need to install connector by running following script.
# $ sudo pip install mysql-connector
# $ sudo pip install mysql-connector-python-rf
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode


# Python Program to Check database connection in MySQL
try:
    connection = mysql.connector.connect(host='localhost',
                                         user='pynative',
                                         password='pynative@#29')

    if connection.is_connected():
        db_Info = connection.get_server_info()

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")


# Python Program to create database in MySQL
try:
    connection = mysql.connector.connect(host='localhost',
                                         user='pynative',
                                         password='pynative@#29')

    if connection.is_connected():
        my_database = connection.cursor()
        my_database.execute("devops-school")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

# Python Program to create table in MySQL
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_Create_Table_Query = """CREATE TABLE Laptop ( 
                             Id int(11) NOT NULL,
                             Name varchar(250) NOT NULL,
                             Price float NOT NULL,
                             Purchase_date Date NOT NULL,
                             PRIMARY KEY (Id)) """

    cursor = connection.cursor()
    result = cursor.execute(mySql_Create_Table_Query)
    print("Laptop Table created successfully ")

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

# To insert a single row/record into MySQL table
try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='pynative',
                                         password='pynative@#29')

    mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                           VALUES 
                           (1, 'Lenovo ThinkPad P71', 6459, '2019-08-14') """

    cursor = connection.cursor()
    result = cursor.execute(mySql_insert_query)
    connection.commit()
    print("Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

# To insert a using Def and variables MySQL table

def insertVariblesIntoTable(id, name, price, purchase_date):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='Electronics',
                                             user='pynative',
                                             password='pynative@#29')

        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO Laptop (Id, Name, Price, Purchase_date) 
                                VALUES (%s, %s, %s, %s) """

        recordTuple = (id, name, price, purchase_date)
        cursor.execute(mySql_insert_query, recordTuple)
        connection.commit()
        print("Record inserted successfully into Laptop table")

    except mysql.connector.Error as error:
        print("Failed to insert into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertVariblesIntoTable(2, 'Area 51M', 6999, '2019-04-14')
insertVariblesIntoTable(3, 'MacBook Pro', 2499, '2019-06-20')


#  MySQL SELECT Query example to fetch rows from MySQL table.

import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='Electronics',
                                         user='pynative',
                                         password='pynative@#29')

    sql_select_Query = "select * from Laptop"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in Laptop is: ", cursor.rowcount)

    print("\nPrinting each laptop record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Price  = ", row[2])
        print("Purchase date  = ", row[3], "\n")

except Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if (connection.is_connected()):
        connection.close()
        cursor.close()
        print("MySQL connection is closed")


# updating a Laptop table by changing the value of the Price column

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='pynative',
                                         password='pynative@#29')
    cursor = connection.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 1"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update Laptop set Price = 7000 where id = 1"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")

# deleting a single row from the “Laptop” table.

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='electronics',
                                         user='pynative',
                                         password='pynative@#29')

    cursor = connection.cursor()
    print("Displaying laptop record Before Deleting it")
    sql_select_query = """select * from Laptop where id = 7"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_Delete_query = """Delete from Laptop where id = 7"""
    cursor.execute(sql_Delete_query)
    connection.commit()

    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    if len(records) == 0:
        print("\nRecord Deleted successfully ")

except mysql.connector.Error as error:
    print("Failed to delete record from table: {}".format(error))
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")