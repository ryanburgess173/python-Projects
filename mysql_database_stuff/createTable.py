from createConnection import MySQLConnection


def main():
    connection = MySQLConnection("learnPythonSQL")
    connection.get_mycursor().execute(
        "CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
