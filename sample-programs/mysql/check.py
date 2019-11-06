import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# $ sudo pip install mysql-connector
# $ sudo pip install mysql-connector-python-rf
# Python Program to Check database connection in MySQL

try:
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='MyNewPass')

    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    if (connection.is_connected()):
        connection.close()
        print("MySQL connection is closed")