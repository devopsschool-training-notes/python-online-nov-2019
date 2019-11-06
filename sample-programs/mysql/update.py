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

    print("Before updating a record ")
    sql_select_query = """select * from Laptop where id = 2"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update Laptop set Name = 'Lenvo' where id = 3"""
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