import mysql.connector
from mysql.connector import Error
from pprint import pprint


def main():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            database='golanders',
            user='root',
            password=''
        )

        if connection.is_connected():
            print('Successful connection')
    except Error as e:
        print(f"Error in connection: {e}")
    except Exception as e:
        print(f"Unknown error: {e}")

    cursor = connection.cursor()
    cursor.execute("SHOW TABLES")
    pprint(cursor.fetchall())

    print("done")

    cursor.close()
    connection.close()


if __name__ == '__main__':
    main()
