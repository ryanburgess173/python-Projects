from createConnection import MySQLConnection


def main():
    connection = MySQLConnection()
    connection.mycursor.execute(
        "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
