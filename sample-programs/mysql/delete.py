import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

# $ sudo pip install mysql-connector
# $ sudo pip install mysql-connector-python-rf

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='devopsschool1',
                                         user='root',
                                         password='MyNewPass')

    cursor = connection.cursor()
    print("Displaying laptop record Before Deleting it")
    sql_select_query = """select * from Laptop where id = 2"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    sql_Delete_query = """Delete from Laptop where id = 2"""
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