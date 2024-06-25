import mysql.connector
from mysql.connector import Error

class MySQLConnection:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection.is_connected():
            self.connection.close()
            print("MySQL connection is closed")


class MySQLCursor:
    def __init__(self, connection):
        self.connection = connection
        self.cursor = None

    def __enter__(self):
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()


# Usage example
try:
    with MySQLConnection(host='localhost', database='golanders', user='root', password='') as connection:
        with MySQLCursor(connection) as cursor:
            cursor.execute("SELECT * FROM employee")
            records = cursor.fetchall()

            for row in records:
                print(row)

except Error as e:
    print(f"Error: {e}")
