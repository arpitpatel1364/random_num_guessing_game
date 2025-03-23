import mysql.connector
from mysql.connector import Error

try:
    # Establishing a connection to the database
    dataBase = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",  # Use your MySQL password here
        database="furniture"
    )

    if dataBase.is_connected():
        print("Successfully connected to the database")

        # Preparing a cursor object
        cursorObject = dataBase.cursor()

        # SQL query to insert data
        sql = "INSERT INTO login(email, password) VALUES (%s, %s)"
        values = ('dax50@gmail.com', '020202020')

        # Executing the SQL command
        cursorObject.execute(sql, values)

        # Committing the transaction
        dataBase.commit()
        print("Record inserted successfully")

except Error as e:
    print(f"Error: {e}")

finally:
    if dataBase.is_connected():
        cursorObject.close()  # Close the cursor
        dataBase.close()      # Close the database connection
        print("Connection closed")   