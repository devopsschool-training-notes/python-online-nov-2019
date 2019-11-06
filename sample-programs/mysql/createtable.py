import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# $ sudo pip install mysql-connector
# $ sudo pip install mysql-connector-python-rf

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='devopsschool',
                                         user='root',
                                         password='MyNewPass')

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